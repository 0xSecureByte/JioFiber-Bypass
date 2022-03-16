import requests

jio_lan_ip = input('Enter your Jio-IP: ')
username = 'admin'
password = '12345678'
cookie = 'b5080ad6185a72e3681f100aab8a428'
cookies = {
    'TeamF1Login': cookie,
}

headers = {
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Origin': f'http://{jio_lan_ip}',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Referer': f'http://{jio_lan_ip}/',
    'Accept-Language': 'en-US,en;q=0.9',
}

data = {
    'thispage': 'index.html',
    'users.username': username,
    'users.password': password,
    'button.login.users.dashboard': 'Login'
}

for i in range(1,30):
    response = requests.post(f'http://{jio_lan_ip}/platform.cgi', headers=headers, cookies=cookies, data=data, verify=False)
    response.close()
