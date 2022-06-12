import re, requests, os, sys
from time import time as timer	
from multiprocessing.dummy import Pool
from colorama import Fore								
from colorama import Style
####### Colors	 ######	
fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT
										
#######################
# proxies = {
    # 'http': 'socks5://localhost:9050',
    # 'https': 'socks5://localhost:9050'
# }

def banners():
    try:
        os.mkdir('result')
    except:
        pass
        
    banner = """{}

                   ...          
                 ;::::;           ::
               ;::::; :;        :::::: 
              ;::::;  :;   Dir/File Scanner
             ;:::::'   :;     By RaiC0d3r
            ;:::::;     ;.
           ,:::::'       ;           OOO\
           ::::::;       ;          OOOOO\{}
           ;:::::;       ;         OOOOOOOO
          ,;::::::;     ;'         / OOOOOOO
        ;:::::::::`. ,,,;.        /  / DOOOOOO
      .';:::::::::::::::::;,     /  /     DOOOO
     ,::::::;::::::;;;;::::;,   /  /        DOOO
    ;`::::::`'::::::;;;::::: ,#/  /          DOOO
    :`:::::::`;::::::;;::: ;::#  /            DOOO  {}
    ::`:::::::`;:::::::: ;::::# /              DOO
    `:`:::::::`;:::::: ;::::::#/               DOO
     :::`:::::::`;; ;:::::::::##                OO
     ::::`:::::::`;::::::::;:::#                OO
     `:::::`::::::::::::;'`:;::#                O
      `:::::`::::::::;' /  / `:#
       ::::::`:::::;'  /  /   `#                                                                                            

		\n""".format(fg, fr, fg, sn)
		
    print(banner)


def getoption():
    print("{}[1]{} Single Site".format(fg, fw))
    print("{}[2]{} Multiple Site".format(fg, fw))
    choiceoption=input('Put Number => ')
    if choiceoption=='1':
        url = input("\n\033[92m[!]\033[91m ENTER WEBSITE : ")
        singlescanner(url)
        
    elif choiceoption=='2':
        start_raw = input("\n\033[92m[!]\033[91m ENTER LIST OF WEBSITES : ")
        try:
            with open(start_raw, 'r') as f:
                url = f.read().splitlines()
        except IOError:
            pass
        start = timer()
        ThreadPool = Pool(100)
        Threads = ThreadPool.map(multiscanner, url)
        print('PrivateBot Finished in : ' + str(timer() - start) + ' seconds')

def singlescanner(url):
    director = open(input("\n\033[92m[!]\033[91m ENTER LIST OF DIRECTORY : "), 'r').read().splitlines()
    for director in director:
        #print(director)
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        request = requests.get(url+"/"+director, headers=Headers ,timeout=10)
        kode = request.status_code
        if(kode == 200) or (kode == 301) or (kode == 302) or (kode == 403):
            print('[Site]: {}'.format(url+"/"+director))
            open('result/found.txt', 'a').write(url+"/"+director+ '\n')
##################end reverse############

def multiscanner(url):
    director = open("dir.txt", 'r').read().splitlines()
    for director in director:
        #print(director)
        Headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        request = requests.get(url+"/"+director, headers=Headers ,timeout=10)
        kode = request.status_code
        if(kode == 200) or (kode == 301) or (kode == 302) or (kode == 403):
            print('[Site]: {}'.format(url+director))
            open('result/found.txt', 'a').write(url+director+ '\n')
##################end reverse############
banners()
getoption()


