#!usr/bin/python3

import requests, json, os
# kode warna
p='\033[37;1m'
h='\033[32;1m'
b='\033[34;1m'
n='\033[00;1m'
m='\033[31;1m'
m_='\033[41;1m'

logo="""
{} ╰╮╰╮╰╮
╭━━━━━━━╮      ╭━━━━━━━━━━━━━━╮
╰━━━━━━━╯      │ {}Api WhatsApp {}│
┃{}╭╭╮┏┏┏┏{}┣━╮    ╰━━━━━━━━━━━━━━╯
┃{}┃┃┃┣┣┣┣{}┃ ┃   / {}Coder {}: {}Tegar Dev
{}┃{}╰╰╯┃┃┗┗{}┣━╯
╰━━━━━━━╯        [{} Dunia Kode {}]
""".format(p,h,p,b,p,b,p,b,p,m,p,b,p,m_,n)
url='https://wa-apiz.herokuapp.com/'

def biasa():
    pesan=input('{}【{}✪{}】{}pesan {}: {}'.format(p,b,p,h,m,p))
    rep=pesan.replace(' ', '%20')
    try:
        req=requests.get(url+'send?number='+nomor+'&msg='+rep)
        print('{}({}✔{}){}terkirim'.format(p,h,p,h))
    except requests.exceptions.HTTPError:
        print('{}({}✖{}){}tidak terkirim'.format(p,m,p,m))

def file():
    pesan=input('{}【{}✪{}】{}file pesan {}: {}'.format(p,b,p,h,m,p))
    file=open(pesan, 'r').read()
    rep=file.replace(' ', '%20')
    cek=rep.replace('\n', '%0A')
    try:
        req=requests.get(url+'send?number='+nomor+'&msg='+cek)
        print('{}({}✔{}){}terkirim'.format(p,h,p,h))
    except requests.exceptions.HTTPError:
        print('{}({}✖{}){}tidak terkirim'.format(p,m,p,m))

if __name__=="__main__":
    os.system('clear')
    print(logo)
    nomor=input('{}【{}✪{}】{}nomor {}: {}'.format(p,b,p,h,m,p))
    print('{}pilih metode pesan'.format(h))
    print('{}({}1{}){}Biasa {}({}2{}){}File'.format(p,b,p,h,p,b,p,h))
    pil=input('{}【{}✪{}】{}pilih {}: {}'.format(p,b,p,h,m,p))
    if pil == "1":
        biasa()
    elif pil == "2":
        file()
    else:
        print('pilihan tidak ada')
