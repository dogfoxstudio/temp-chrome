import string
import random
import os
import subprocess
from sys import argv
import time

def getProfiles():
    profiles = os.listdir('./profiles/')
    return profiles
    
def launch(name, url=""):
    settings = open('./profiles/'+name+'/settings.txt', "r")
    settings.readline()
    useragent = settings.readline()
    useragent = useragent.replace('\n','')
    proxy = settings.readline()
    proxy = proxy.replace('\n','')
    settings.close()
    print("UserAgent:"+useragent)
    print("proxy: "+proxy)
    subprocess.Popen([
        "chrome-win/chrome", \
        "--user-data-dir="+'./profiles/'+name,\
        "--load-extension=../extensions/ext1,../extensions/ext2,../extensions/ext3,../extensions/ext4",\
        "--proxy-server="+proxy,\
        "--user-agent="+useragent,\
        url
    ],shell=True)
    #subprocess.Popen([
    #    "chromium", \
    #    "--user-data-dir="+'./profiles/'+name,\
    #    "--load-extension=./extensions/ext1,./extensions/ext2,./extensions/ext3,./extensions/ext4",\
    #    "--proxy-server="+proxy,\
    #    "--user-agent="+useragent,\
    #    url
    #],shell=True)
    
def createprofile(name, url=""):
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
    settings.write(proxy+"\n")
    with open("proxies.txt", "r") as prx:
        lines = prx.readlines()
    with open("proxies.txt", "w") as prx:
        for line in lines:
            if proxy not in line:
                prx.write(line)
    #сохранение ссылки по умолчанию
    #settings.write(url+"\n")
    settings.close()
    
def main():
    profiles = getProfiles()
    urls = ""
    for a in argv[1:]:
        urls = urls + a
    #urls = "google.com"
    for prf in profiles:
        print("Launching "+prf+"...")
        launch(prf, urls)
        #Установка интервала случайной задержки
        delay = random.randint(10,15)
        print("Waiting "+str(delay)+" seconds")
        time.sleep(delay)
    
if __name__ == "__main__":
    main()
