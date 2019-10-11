#!/usr/bin/env python
#-*- coding: utf-8 -*-

# coded by : w0n63d4n
# awx tool 
# recode ? sertakan nick saya !
g = '\033[92m'
w = '\033[97m'
r = '\033[91m'
y = '\033[93m'
b = '\033[94m'
u = '\033[95m'
bm= '\033[96m'
n = '\033[0m'

import requests
import urllib, urllib.error
import time
import os

os.system("clear")
print(y+"\t\tcoded by  :  w0n63d4n")
print("\t\tname tool : AWX")
print("\t\thave fun with me :)\n\n"+n)
print(w+" 1. cari website")
print(" 2. ceck website")
print(" 3. lihat list web")
print(" 4. web found dir")
print(" 5. masukan dork")
print(" 6. exit tool\n")
inp = int(input(" pilih bos : "))
if inp == 1:
    f = open("dork.txt", "r").read().split("\n")
    page = 1
    PageDepth = int(input(g+' butuh berapah web : '+w))
    print(bm+'\n wait process finder new website..')
    for dork in f:
        if dork == "":
            continue
        for k in range(0, PageDepth):
            bingurl = "https://www.bing.com/search?q="+dork+"&first="+str(page)+"&FORM=PORE"
            page += 10
            headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
            try:
                pageSource = requests.get(bingurl, headers=headers).text
            except requests.exceptions.HTTPError:
                continue
            except requests.exceptions.ConnectionError:
                continue
            except requests.exceptions.Timeout:
                continue
            da = pageSource.split('<li class="b_algo"><h2><a href="')
            domains = []
            for i in range(0, 10):
                try:
                    domains.append(da[i+1].split('"')[0])
                except:
                    pass
            for l in domains:
                open('web.txt', 'a+').close()
                l = l.split('/')
                l = l[0] + '//' + l[1] + l[2]
                if l not in open('web.txt', 'r').read():
                    open('web.txt', 'a+').write(l + '\n')
                    print(' '+w+l)
    print(g+" SELESAI !!")
    
if inp == 2:
    msk = input("masukan dir web : ")
    daftar = open('web.txt','r').read().split('\n')
    print ("cek in URL..")
    for i in daftar:
        target = i+msk
        sip = open('web.txt','r').read()
        if i in sip:
            try:
                bau = urllib.request.Request(target)
                bob = urllib.request.urlopen(bau)
                open('FOUND.txt', 'a').write(target+'\n')
                print(w+target+g+'  FOUND'+w)
            except urllib.error.HTTPError:
                print(w+target+r+' NOT FOUND'+w)
                continue
            except ConnectionResetError:
                continue
            except ValueError:
                continue
            except urllib.error.URLError:
                continue
            except KeyboardInterrupt:
                break
            
    time.sleep(2)
    print(g+' cecking finished'+w)

if inp == 3:
    os.system("micro web.txt")
if inp == 4:
    os.system("micro FOUND.txt")
if inp == 5:
    os.system("micro dork.txt")
if inp == 6:
    raise SystemExit(" jangan lupa balik lagi :V")
