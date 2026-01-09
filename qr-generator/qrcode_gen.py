import qrcode
import time
import sys

link = input("Link: ")

def www_adder(link):
    if link.startswith("http://"):
        link = link.replace("http://", "http://www.")
    elif link.startswith("https://"):
        link = link.replace("https://", "https://www.")

    return link

def http_adder(link):
    question_http_https = input("Please add http:// or https://: ")
    if question_http_https == "http://":
        link = question_http_https + link
    elif question_http_https == "https://":
        link = question_http_https + link

    return link

def tld_adder(link):
    question_tld = input("Please add TLD: ")
    link = link + question_tld

    return link

if link.lower() == "q":
    sys.exit()

else:


    link_lenght = len(link) 

    if link_lenght < 4:
        print("Please enter a valid link")
        sys.exit()

    if "http" not in link:
        print("Link must start with http:// or https://")

        question_http = input("Do you want to continue? (y/n): ")

        if question_http == "y":
            link = http_adder(link)
        else:
            sys.exit()

    if "www." not in link:
        print("Link must contain www.")

        question_www = input("Do you want to continue? (y/n): ")

        if question_www == "y":
            link = www_adder(link)
        else:
            sys.exit()

    if "." not in link[-4:]:
        print("Link must end with .com, .net, .org, .edu, .gov, .io, .me, .co, .in")
        question_com = input("Do you want to continue? (y/n): ")
        if question_com == "y":
            link = tld_adder(link)
        else:
            sys.exit()
    try:
        img = qrcode.make(link)
        
        a = int(time.time())
        
        img.save(f"qrcode_{a}.png")

        img.show()

        print(f"QRCode saved as qrcode_{a}.png and opened for preview")
    except Exception as e:
        print(f"Error: {e}")
