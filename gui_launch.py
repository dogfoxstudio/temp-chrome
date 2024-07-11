import tkinter as tk
import tkinter.font as tkFont

import string
import random
import os
import subprocess
from string import Template

import shutil

WIN_PLATFORM = True
CHROME_DIR = '.\\chrome-win\\chrome.exe'

DELETE_USED_PROXIES = False
DELETE_USED_UA = False

class App:
    def __init__(self, root):
        self.root = root
        #setting title
        self.root.title("Chrome temp-profile creator")
        #setting window size
        width=800
        height=525
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)
        
        self.names = self.getNames()
        self.profiles = self.getProfiles()
        
        listbox=tk.Listbox(self.root, listvariable=tk.StringVar(value=self.names))
        listbox["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=16)
        listbox["font"] = ft
        listbox["fg"] = "#333333"
        listbox["justify"] = "left"
        listbox.place(x=90,y=20,width=400,height=300)
        listbox["selectmode"] = "single"
        listbox.bind("<<ListboxSelect>>", self.listbox_update)
        self.listbox = listbox

        profileButton=tk.Button(self.root)
        profileButton["bg"] = "#e9e9ed"
        ft = tkFont.Font(size=8)
        profileButton["font"] = ft
        profileButton["fg"] = "#000000"
        profileButton["justify"] = "center"
        profileButton["text"] = "Новый профиль"
        profileButton.place(x=520,y=20,width=180,height=35)
        profileButton["command"] = self.profileButton_command

        launchButton=tk.Button(self.root)
        launchButton["bg"] = "#e9e9ed"
        ft = tkFont.Font(size=8)
        launchButton["font"] = ft
        launchButton["fg"] = "#000000"
        launchButton["justify"] = "center"
        launchButton["text"] = "Запустить профиль"
        launchButton.place(x=520,y=80,width=180,height=35)
        launchButton["command"] = self.launchButton_command

        changeButton=tk.Button(self.root)
        changeButton["bg"] = "#e9e9ed"
        ft = tkFont.Font(size=8)
        changeButton["font"] = ft
        changeButton["fg"] = "#000000"
        changeButton["justify"] = "center"
        changeButton["text"] = "Изменить профиль"
        changeButton.place(x=520,y=140,width=180,height=35)
        changeButton["command"] = self.changeButton_command
        
        deleteButton=tk.Button(self.root)
        deleteButton["bg"] = "#e9e9ed"
        ft = tkFont.Font(size=8)
        deleteButton["font"] = ft
        deleteButton["fg"] = "#000000"
        deleteButton["justify"] = "center"
        deleteButton["text"] = "Удалить профиль"
        deleteButton.place(x=520,y=200,width=180,height=25)
        deleteButton["command"] = self.deleteButton_command

        proxyValue=tk.Label(self.root, justify="left")
        proxyValue["bg"] = "#e5e5e5"
        ft = tkFont.Font(size=8)
        proxyValue["font"] = ft
        proxyValue["fg"] = "#333333"
        proxyValue["justify"] = "left"
        proxyValue["text"] = "proxy"
        proxyValue.place(x=180,y=340,width=560,height=30)
        self.proxyValue = proxyValue

        UAValue=tk.Label(self.root, justify="left")
        UAValue["bg"] = "#e5e5e5"
        ft = tkFont.Font(size=8)
        UAValue["font"] = ft
        UAValue["fg"] = "#333333"
        UAValue["justify"] = "left"
        UAValue["text"] = "useragent"
        UAValue.place(x=180,y=400,width=560,height=30)
        self.UAValue = UAValue

        proxyLabel=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=18)
        proxyLabel["font"] = ft
        proxyLabel["fg"] = "#333333"
        proxyLabel["justify"] = "left"
        proxyLabel["text"] = "Прокси:"
        proxyLabel.place(x=60,y=340,width=120,height=30)

        UALabel=tk.Label(self.root)
        ft = tkFont.Font(family='Times',size=18)
        UALabel["font"] = ft
        UALabel["fg"] = "#333333"
        UALabel["justify"] = "left"
        UALabel["text"] = "UserAgent:"
        UALabel.place(x=60,y=400,width=120,height=30)

        proxyList=tk.Button(self.root)
        proxyList["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=12)
        proxyList["font"] = ft
        proxyList["fg"] = "#000000"
        proxyList["justify"] = "center"
        proxyList["text"] = "Список прокси"
        proxyList.place(x=530,y=250,width=160,height=30)
        proxyList["command"] = self.proxyList_command

        UAList=tk.Button(self.root)
        UAList["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=12)
        UAList["font"] = ft
        UAList["fg"] = "#000000"
        UAList["justify"] = "center"
        UAList["text"] = "Список UserAgent"
        UAList.place(x=530,y=290,width=160,height=30)
        UAList["command"] = self.UAList_command

        self.URLEntry=tk.Entry(self.root)
        self.URLEntry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=18)
        self.URLEntry["font"] = ft
        self.URLEntry["fg"] = "#333333"
        self.URLEntry["justify"] = "left"
        self.URLEntry["text"] = "URL"
        self.URLEntry.place(x=60,y=460,width=560,height=40)

        openButton=tk.Button(self.root)
        openButton["bg"] = "#e9e9ed"
        ft = tkFont.Font(family='Times',size=18)
        openButton["font"] = ft
        openButton["fg"] = "#000000"
        openButton["justify"] = "center"
        openButton["text"] = "Открыть"
        openButton.place(x=640,y=460,width=100,height=40)
        openButton["command"] = self.openButton_command

    def refresh(self):
        self.root.update()
        self.root.update_idletasks()
    
    def launch(self, name, site="google.com"):
        settings = open('./profiles/'+name+'/settings.txt', "r")
        settings.readline()
        useragent = settings.readline()
        useragent = useragent.replace('\n','')
        proxy = settings.readline()
        proxy = proxy.replace('\n','')
        settings.close()
        print("UserAgent:"+useragent)
        print("proxy: "+proxy)
        if WIN_PLATFORM:
            subprocess.run([
        CHROME_DIR, \
        "--user-data-dir="+'./profiles/'+name,\
        "--load-extension=../extensions/ext1,../extensions/ext2,../extensions/ext3,../extensions/ext4",\
        "--proxy-server="+proxy,\
        "--user-agent="+useragent, \
        site
        ])
        else:
            subprocess.run([
            "chromium", \
            "--user-data-dir="+'./profiles/'+name,\
            "--load-extension=./extensions/ext1,./extensions/ext2,./extensions/ext3,./extensions/ext4",\
            "--proxy-server="+proxy,\
            "--user-agent="+useragent
            ])
        self.refresh()
    
    def createprofile(self, name):
        #создание каталога профиля
        if not os.path.exists('./profiles/'+name):
            os.makedirs('./profiles/'+name)
        #создание файла настроек
        settings = open('./profiles/'+name+'/settings.txt', "w")
        settings.write(name+"\n")
        #выбор UserAgent
        try:
            useragent = random.choice(open('useragents.txt').readlines())
        except:
            useragent = ''
        with open("useragents.txt", "r") as uas:
            lines = uas.readlines()
        with open("useragents.txt", "w") as uas:
            for line in lines:
                if useragent in line:
                    if not DELETE_USED_UA: uas.write(line)
                else:
                    uas.write(line)
            
        settings.write(useragent)
        #выбор прокси
        try:
            proxy = random.choice(open('proxies.txt').readlines())
        except:
            proxy = ''
        settings.write(proxy)
        with open("proxies.txt", "r") as prx:
            lines = prx.readlines()
        with open("proxies.txt", "w") as prx:
            for line in lines:
                if proxy in line:
                    if not DELETE_USED_PROXIES: prx.write(line)
                else:
                    prx.write(line)
        #выбор часового пояса
            #потом доделаю
        settings.close()
        self.refresh()
        #создание файла запуска
        #launcher = open("./launchers/profile_"+name+".bat", "w")
        #launcher.write("cd .. \n")
        #launcher.write("python ./launch.py "+name)
        #launcher.close()
        #создание окна
        #greet = open('./profiles/'+name+'/greetings.html', "w")
        #greet.write(greetings_template.safe_substitute( prx=proxy,profilename=name,UA=useragent))
    
    def getNames(self):
        profiles = os.listdir('./profiles/')
        names = []
        for profile in profiles:
            with open('./profiles/'+profile+'/settings.txt', "r") as f:
                names.append(f.readline()[:-1])
        return names
    
    def getProfiles(self):
        profiles = os.listdir('./profiles/')
        self.refresh()
        return profiles
    
    def listbox_update(self, event):
        try:
            sel = self.listbox.curselection()
            with open('./profiles/'+self.profiles[sel[0]]+'/settings.txt', "r") as f:
                f.readline()
                UA = f.readline()
                prx = f.readline()
                UA = UA.replace('\n','')
                prx = prx.replace('\n','')
            self.proxyValue["text"] = prx
            self.UAValue["text"]    = UA
            #print(UA)
            #print(prx)
        except:
            self.proxyValue["text"] = "None"
            self.UAValue["text"] = "None"
        self.refresh()
        
    def profileButton_command(self):
        profilename = "".join(random.choice(string.ascii_letters) for x in range(6))
        print("Creating new profile: "+profilename)
        self.createprofile(profilename)
        print("Launching ...")
        self.refresh()
        self.launch(profilename)
        self.refresh()


    def launchButton_command(self):
        selection = self.listbox.curselection()
        print("Selected profile "+self.names[selection[0]])
        print("Launching ...")
        self.launch(self.profiles[selection[0]])
        self.refresh()

    def changeButton_command(self):
        print("to do")
        
    def deleteButton_command(self):
        try:
            selection = self.listbox.curselection()
            shutil.rmtree('./profiles/'+self.profiles[selection[0]])
        except: pass
        self.refresh()

    def proxyList_command(self):
        print("to do")


    def UAList_command(self):
        print("to do")


    def openButton_command(self):
        try:
            selection = self.listbox.curselection()
            prf = self.names[selection[0]]
            print("Selected profile "+prf)
            if prf == None or prf == '':
                raise Exception('Profile not found')
            print("Launching ...")
        except:
            prf = "".join(random.choice(string.ascii_letters) for x in range(6))
            print("Creating new profile: "+prf)
            self.createprofile(prf)
            print("Launching ...")
        self.launch(prf, self.URLEntry.get())
        self.refresh()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    
    root.mainloop()
