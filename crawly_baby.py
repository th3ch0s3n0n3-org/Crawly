#!/usr/bin/python3
# discover hidden directory by bruteforceing common directory name
# if we get a respond then their is a directory then we also get the recursive of the directory.

import requests
import optparse


result = pyfiglet.figlet_format("CRAWLY")
print("----------------------------------------------------------------")
print(" ")
print("         (                          (          )         ")
print("   (     )\ )     (       (  (      )\ )    ( /(         ")
print("   )\   (()/(     )\      )\))(   '(()/(    )\())        ")
print(" (((_)   /(_)) ((((_)(   ((_)()\ )  /(_))  ((_)\         ")
print(" \___  (_))    )\ _ )\  _(())\_)()(_))   __ ((_)          ")
print("((/ __| | _ \   (_)_\(_) \ \((_)/ /| |    \ \ / /        ")
print(" | (__  |   /    / _ \    \ \/\/ / | |__   \ V /         ")
print("  \___| |_|_\   /_/ \_\    \_/\_/  |____|   |_|          ")
print(" ")
print("----------------------------------------------------------------")                                          
print("                         created by-- Rishabh,Vinayak&Rinal")
print("----------------------------------------------------------------")


parser = optparse.OptionParser()

parser.add_option("--url", "-u", dest="url", help="Enter the url, you want to bruteforce (--url http://URL)")
parser.add_option("--wordlist", "-w", dest="wordlist", help="Enter the path fo the worlist (--wordlist /PATH)" )
(options, arguments) = parser.parse_args()


url = options.url
wordlist = options.wordlist
def request(url):
    try:
        return requests.get(url)
    except requests.exceptions.ConnectionError:
        pass


path = []


def dirdiscover(url):
    
    with open(wordlist, "r") as wordlist_file:
        for line in wordlist_file:
            word = line.strip()
            test_url = url + "/" + word
            response = request(test_url)
            if response:
                print("[+] Discovered URL ----> " + test_url)
                path.append(word)



# edit the url you want to scan
dirdiscover(url)

# recursively gothrough each and every path
for paths in path:
    dirdiscover(url + "/" + paths)

