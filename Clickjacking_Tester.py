#Author:D4Vinci
import urllib2 ,sys

def check(url):
    try:
        if "http" not in url:
            url = "http://" + url
        data = urllib2.urlopen(url)
        headers = data.info()

        if not "X-Frame-Options" in headers:
            return True
    except:
        return False

def Create_Poc(url):
    code = """<html>
   <head>
     <title>Clickjack test page</title>
   </head>
   <body>
     <p>Website is vulnerable to clickjacking!</p>
     <iframe src="{}" width="500" height="500"></iframe>
   </body>
</html>
    """.format(url)
    f = open(url+".html","w")
    f.write(code)
    f.close()

def main():
    try:
	f = open('sites.txt', 'r')
	z = f.readlines()
       
    except:
        print "[!] Error"
        print "[!] Usage: "+ sys.argv[0].split("\\")[-1]+" <URL>"
        sys.exit(0)
    for x in z[0:]:
   	 print " [>] Clickjacking Vulnerability Tester By D4Vinci"
    	 print " \n[#] Checking "+x
    	 if check(x):
        	 print " [X]** The website is VULNERABLE! **"
        	 Create_Poc(x)
        	 print " [#] Created a poc and saved to Clickjacking.html"
    	 elif not check(x):
        	 print " [!] The website is not vulnerable.!"

if __name__ == '__main__':
    main()
