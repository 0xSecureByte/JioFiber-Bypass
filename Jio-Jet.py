import random
import os
import requests
import getpass
import pyfiglet
from bs4 import BeautifulSoup as bs
from lxml import etree

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

print(f"{color}{fig}{end}")
print(f"""
                    THIS TOOL GETS DATA FROM {green}JIOFIBER ROUTER{end}  
                    MAKE SURE YOU HAVE SETUP THE ROUTER.              
                    CREDITS:- {cyan}@{end}{green}0xchirantan{end}
""")
jio_lan_ip = input(f"{cyan}Enter your Jio-Router IP {end}{yellow}(Press enter for default: 192.168.29.1):{end} {green}")
username = input(f"{end}{cyan}Enter your Username: {end}{green}")
password = getpass.getpass(f"{end}{cyan}Enter your Password: {end}")

if(jio_lan_ip == ""):
    jio_lan_ip = '192.168.29.1'

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

response = requests.post(f'http://{jio_lan_ip}/platform.cgi', headers=headers, cookies=cookies, data=data, verify=False)
soup0 = bs(response.content, "html.parser")
dom = etree.HTML(str(soup0))

access_denied = dom.xpath('/html/body/div[1]/div/div/div[1]/p')[0].text
access_denied = access_denied.strip()
if(access_denied==''):
    ip = dom.xpath('/html/body/div[1]/div[2]/div[6]/div[2]/div[4]/div[3]/div[5]/p')[0].text
    conn_clients = dom.xpath('/html/body/div[1]/div[2]/div[6]/div[2]/div[4]/div[1]/div[9]/p')[0].text
    conn_clients = conn_clients.strip()
    mac_addr = dom.xpath('/html/body/div[1]/div[2]/div[6]/div[2]/div[4]/div[3]/div[10]/p')[0].text
    serial = dom.xpath('/html/body/div[1]/div[1]/div[2]/p[2]/span')[0].text
    version = dom.xpath('/html/body/div[1]/div[2]/div[6]/div[2]/div[4]/div[1]/div[3]/p')[0].text
    model = dom.xpath('/html/body/div[1]/div[2]/div[6]/div[2]/div[4]/div[1]/div[5]/p')[0].text
    print(f'{access_denied}')
    print(f'{cyan}WAN-IP: {end}',f'{green}[ {end}{red}', ip,f'{end}{green} ]{end}')
    print(f'{cyan}CONNECTED-CLIENTS: {end}',f'{green}[ {end}{red}', conn_clients,f'{end}{green} ]{end}')
    print(f'{cyan}MAC-ADDR: {end}',f'{green}[ {end}{red}', mac_addr,f'{end}{green} ]{end}')
    print(f'{cyan}SERIAL-NO: {end}',f'{green}[ {end}{red}', serial,f'{end}{green} ]{end}')
    print(f'{cyan}VERSION-NO: {end}',f'{green}[ {end}{red}', version,f'{end}{green} ]{end}')
    print(f'{cyan}MODEL-NO: {end}',f'{green}[ {end}{red}', model,f'{end}{green} ]{end}')
else:
    print(f'{red}{access_denied}{end}')

response.close()