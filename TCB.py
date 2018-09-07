##DESCRIPTION
#Check Folder Path for .txt files
#set count variable to corresponding integer
#delete file
#call function
#reset count 	

import os, time, subprocess, sys, collections, webbrowser, logging
import twilio.rest import Client

#Twilio Acct Info
account_sid = 'AC1b989f45df7bf74e78e3513828405a29'
auth_token = 'dc5d8be9e7f2d4a60f4398c6eb6449e3'

client = Client(account_sid, auth_token)
myTwilioNumber = '+12568040303'
myCellPhone = '+12566565759'

##FUNCTIONS##

def shutdown():
	os.system('shutdown -s')

def restart():
	os.system('shutdown -r')

def wakeup():
	subprocess.Popen('C:/Users/Thermaltake/AppData/Roaming/Spotify/Spotify.exe')
	webbrowswer.open('https://us-mg6.mail.yahoo.com/neo/launch')
	webbrowswer.open('https://www.rescuetime.com/dashboard')

def code():
	webbrowser.open('https://somafm.com/player/@/now-playing/groovesalad')
	subprocess.Popen('C:/Windows/system32/cmd.exe')
	subprocees.Popen('C:/Python_Files/Sublime Text 3/sublime_text.exe')

def login():
	subbprocess.Popen('C:/Program Files (x86)/TeamViewer/TeamViewer.exe')

##MAIN##
def main():
	x=0

	if os.path.infile('C:/Programs Files x86/Python/dropbox/shutdown.txt') exists:
		x=1
	if os.path.infile('C:/Programs Files x86/Python/dropbox/restart.txt')
		x=2
	if os.path.infile('C:/Programs Files x86/Python/dropbox/wakeup.txt')
		x=3
	if os.path.infile('C:/Program Files x86/Python/dropbox/code.txt')
		x=4
	if os.path.infile('C:/Program Files x86/Python/dropbox/login.txt')
		x=5
	else:	
		print('No File Found')


	if x=1
		shutdown()	
	if x=2
		restart()	
	if x=3
		wakeup()	
	if x=4
		code()	
	if x=5
		login()	


main()


