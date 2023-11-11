import storage
import os, sys, requests, re, random, time
import requests 
import datetime
import getpass
from os import system as psl
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as bsn

psl('rm -rf filer.txt')
idd = []

def logo():
	
    
    print("\033[1;32m    ██╗  ██╗██████╗ ")
    print("\033[1;32m    ╚██╗██╔╝██╔══██╗")
    print("\033[1;32m     ╚███╔╝ ██║  ██║")
    print("\033[1;32m     ██╔██╗ ██║  ██║")
    print("\033[1;32m    ██╔╝ ██╗██████╔╝")
    print("\033[1;32m   ╚═╝  ╚═╝╚═════╝ ")
    print("\n\033[1;39m━▷MADE BY :-: Wali Charsi")
    print("\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑")
    print("\n\033[1;39m━▷FACEBOOK :-:  Wali x'Cot")
    print("\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑")
    print("\n\033[1;39m━▷The Tool Pool Ka Real Bap Wali Here")
    print("\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑")

psl('rm -rf filer.txt')
idd = []

def main():
    psl('clear')
    logo()
    print('\n\033[1;39mPut >> Cookies, Delay Time, Chat/Inbox Link id, File Reapet, Haters Name, Abouse File ')
    print("\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑\033[1;30m◑\033[1;31m◑\033[1;32m◑\033[1;33m◑\033[1;34m◑\033[1;35m◑\033[1;36m◑\033[1;37m◑◑\033[1;33m◑\033[1;34m◑\033[1;35m◑")
    coki = input('[+] Cookies : ')
    cookies={'cookie': coki}
    ch = requests.get('https://mbasic.facebook.com/', cookies=cookies)
    if 'mbasic_logout_button' in ch.text:
        pass
    else:
        print(' \x1b[1;91mYour Account is on Checkpoint !!! \x1b[1;97m')
        os.sys.exit()
    print(' \x1b[1;92m Account Logged in Successfully\x1b[1;97m ')
    print('')
    delay = int(input('[+] Delay Seconds : '))
    print('─────────────────')
    lnk = input('[+] Chat/Inbox Link id : ')
    print('─────────────────')
    lim = int(input('[+] File Repeat : '))
    print('─────────────────')
    hater = input('[+] Haters Name : ')
    print('─────────────────')
    filee = input('[+] File : ')
    fileee = open(filee,'r').read()
    cpy(fileee,lim)
    file = open('filer.txt','r').readlines()
    idd.append(file)
    with bsn(max_workers=30) as crack:
        psl('clear')
        logo()
        print('')
        print('Total messages : %s' %(len(file)))
        print('Process starting.........')
        print('────────────────────')
        for mess in idd:
            sm = '1'
            if sm == '1':
                crack.submit(msg,mess,coki,lnk,delay,hater)
        os.sys.exit()

def msg(mess,coki,lnk,delay,hater):
    ses = requests.Session()
    try:
        for msgs in mess:
            try:
                time.sleep(delay)
                timm = datetime.datetime.now()
                nm,ti = str(timm).split(' ')
                tim,hff = ti.split('.')
                today = datetime.date.today()
                year,month,day = str(today).split('-')
                cookies={'cookie': coki}
                g_url = 'https://d.facebook.com/messages/read/?tid='+lnk
                g_headers = {
                    'authority': 'd.facebook.com',
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-language': 'en-US,en;q=0.9',
                    'cache-control': 'max-age=0',
                    'referer': 'https://d.facebook.com/messages/read/?tid='+lnk,
                    'sec-ch-prefers-color-scheme': 'light',
                    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
                    'sec-ch-ua-full-version-list': '" Not A;Brand";v="99.0.0.0", "Chromium";v="101.0.4951.40"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-ch-ua-platform-version': '"11.0.0"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 11; TECNO CE7j) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
                }
                res1 = requests.get(url=g_url, cookies=cookies, headers=g_headers).text
                j2 = re.search(
                    r'name="jazoest" value="([^"]+)"',
                    res1
                ).group(1)
        
                fb_dtsg = re.search(
                    r'name="fb_dtsg" value="([^"]+)"',
                    res1
                ).group(1)
        
                csid = re.search(
                    r'name="csid" value="([^"]+)"',
                    res1
                ).group(1)
        
                tids = re.search(
                    r'name="tids" value="([^"]+)"',
                    res1
                ).group(1)
            
                ses.headers.update({
                    'content-type': 'application/x-www-form-urlencoded',
                })
            
                rose1 = sop(res1, 'html.parser')
                rose = rose1.find('form',method='post')['action']
                payload = {
                    'fb_dtsg': fb_dtsg,
                    'jazoest': j2,
                    'body': hater+' '+str(msgs),
                    'send': 'Send',
                    'tids': tids,
                    'wwwupp': 'C3',
                    'platform_xmd': '',
                    'referrer': '',
                    'ctype': '',
                    'cver': 'legacy',
                    'csid': csid
                }
                host = 'https://d.facebook.com'
                post = ses.post(url=host+rose, data=payload, cookies=cookies).text
                print('\x1b[1;31m[+] Han Sahii Hai [+] Time :\x1b[1;92m ' +str(tim))
                print('\x1b[1;31m[+] Date :\x1b[1;92m ' +day+'/'+month+'/'+year)
                print('\x1b[1;31m[+] Haters : \x1b[1;92m' +hater)
                print('\x1b[1;31m[1;39m[+] Han Chla Gya Tera [+] Message :\x1b[1;92m ' +hater+msgs+'\x1b[1;31m')
                print('─────────────────────')
            except requests.exceptions.ConnectionError:
                time.sleep(10)
                pass
            except Exception as e:
                pass
        loop+=1
    except requests.exceptions.ConnectionError:
        time.sleep(10)
        pass
    except Exception as e:
        print(e) 
        
   
def cpy(fileee,lim):
    for i in range(lim):
        open('filer.txt','a').write(fileee+'\n')

main()
