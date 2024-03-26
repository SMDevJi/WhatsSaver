import os
from Lib import*
print("Installing requirements...")
os.system("pip3 install pyfiglet")
clear()
from pyfiglet import Figlet
k = Figlet(font='standard')
print (k.renderText('WhatsSaver'))
print("                                 ---by DarkGuySM")
import shutil
import glob

mp4s=glob.glob("/storage/emulated/0/WhatsApp/Media/.Statuses/*.mp4")
gps=glob.glob("/storage/emulated/0/WhatsApp/Media/.Statuses/*.3gp")
jpgs=glob.glob("/storage/emulated/0/WhatsApp/Media/.Statuses/*.jpg")
pngs=glob.glob("/storage/emulated/0/WhatsApp/Media/.Statuses/*.png")


ver=("Enter 1 to save images.\nEnter 2 to save videos")
print("-"*67)
print("   ")
print(ver)
print("   ")
print("Warning! All statuses previously saved using this tool will be deleted!!")
print("   ")

wd=os.getcwd()
def wa():
	chk=input("Enter choice>> ")
	if chk=='1':
		lst=os.listdir("Statuses/Images")
		wrk=os.getcwd()
		for i in lst:
			os.remove(wrk+"/Statuses/Images/"+i)
		for jpg in jpgs:
			shutil.copy(jpg,"Statuses/Images")
		jpg_rnm()
		for png in pngs:
			shutil.copy(png,wd+"/Statuses/Images")
		png_rnm()
	elif chk=='2':
		lst=os.listdir("Statuses/Videos/")
		wrk=os.getcwd()
		for i in lst:
			os.remove(wrk+"/Statuses/Videos/"+i)
		for mp4 in mp4s:
			shutil.copy(mp4,"Statuses/Videos")
		mp_rnm()
		os.chdir(wd)
		for gp in gps:
			shutil.copy(gp,"Statuses/Videos")
		gp_rnm()
	else:
		clear()
		print(k.renderText('WhatsSaver'))
		print("                                 ---by DarkGuySM")
		print("-"*67)
		print("   ")
		print(ver)
		print("   ")
		print("Warning! All statuses previously saved using this tool will be deleted!!")
		print("   ")
		print("Please enter correct option..")
		wa()
wa()
print("   ")
print("Done! ")