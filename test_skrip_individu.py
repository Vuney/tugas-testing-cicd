import pytest
import requests

# --- FUNGSI 1: MATEMATIKA (Penjumlahan) ---
def tambah(a, b):
    return a + b

def test_fungsi_penjumlahan():
    assert tambah(3, 5) == 8
    assert tambah(-1, 1) == 0
    assert tambah(100, 200) == 300

# --- FUNGSI 2: LOGIKA LOGIN (Sederhana) ---
def cek_login(username, password):
    # Simulasi logika backend sederhana
    if username == "admin" and password == "1234":
        return True
    return False

def test_login_sukses():
    assert cek_login("admin", "1234") == True

def test_login_gagal():
    assert cek_login("user_salah", "1234") == False
    assert cek_login("admin", "salah_pass") == False

# --- FUNGSI 3: API TESTING (Mengambil Data dari Internet) ---
def test_api_get_user():
    # Mengambil data dummy dari reqres.in
    response = requests.get("https://reqres.in/api/users/2")
    
    # 1. Cek Status Code harus 200 (OK)
    assert response.status_code == 200
    
    # 2. Cek apakah datanya benar
    data = response.json()
    assert data['data']['first_name'] == "Janet"