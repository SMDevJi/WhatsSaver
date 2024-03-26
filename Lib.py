import os
import shutil

def clear():
	os.system("clear")

def jpg_rnm():
	a=os.listdir("Statuses/Images")
	w=1
	os.chdir("Statuses/Images")
	for each in a:
		b=f"Status_Image_{w}.jpg"
		os.rename(each,b)
		w=w+1

def png_rnm():
	c=os.listdir()
	x=2
	for each in c:
		d=f"Status_Image_{x}.png"
		if each.endswith(".png"):
			os.rename(each,d)
		else:
			pass
		x=x+1


def mp_rnm():
	e=os.listdir("Statuses/Videos")
	y=1
	os.chdir("Statuses/Videos")
	for each in e:
		f=f"Status_Video_{y}.mp4"
		os.rename(each,f)
		y=y+1

def gp_rnm():
	g=os.listdir("Statuses/Videos")
	z=2
	os.chdir("Statuses/Videos")
	for each in g:
		h=f"Status_Video_{z}.3gp"
		if each.endswith(".3gp"):
			os.rename(each,h)
		else:
			pass
		z=z+1