import string
import random
import os
import subprocess

from sys import argv

def launch(name):
    settings = open('./profiles/'+name+'/settings.txt', "r")
    settings.readline()
    useragent = settings.readline()[:-2]
    proxy = settings.readline()
    settings.close()
    print("UserAgent:"+useragent)
    print("proxy: "+proxy)
    subprocess.run([
        "chromium", \
        "--user-data-dir="+'./profiles/'+name,\
        "--load-extension=./extensions/ext1,./extensions/ext2,./extensions/ext3,./extensions/ext4",\
        "--proxy-server="+proxy,\
        "--proxy-bypass-list=192.168.1.1/24",\
        "--user-agent="+useragent
    ])
    

def createprofile(name):
    #создание каталога профиля
    if not os.path.exists('./profiles/'+name):
        os.makedirs('./profiles/'+name)
    #создание файла настроек
    settings = open('./profiles/'+name+'/settings.txt', "w")
    settings.write(name+"\n")
    #выбор UserAgent
    useragent = random.choice(open('useragents.txt').readlines())
    settings.write(useragent)
    #выбор прокси
    proxy = random.choice(open('proxies.txt').readlines())
    settings.write(proxy)
    with open("proxies.txt", "r") as prx:
        lines = prx.readlines()
    with open("proxies.txt", "w") as prx:
        for line in lines:
            if proxy not in line:
                prx.write(line)
    #выбор часового пояса
        #потом доделаю
    settings.close()

if len(argv) >1:
    profilename = argv[1]
else:
    profilename = "".join(random.choice(string.ascii_letters) for x in range(6))

profiles = os.listdir('./profiles/')

if profilename in profiles:
    print("Profile " + profilename + " exists")
    print("Launching ...")
    launch(profilename)
else:
    print("Creating new profile: "+profilename)
    createprofile(profilename)
    print("Launching ...")
    launch(profilename)
    