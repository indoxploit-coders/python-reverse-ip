import urllib2
import re
import random


#Decoded by DayWalker
#Concat : rafsanzani.suhada99[at]gmail[dot]com
#Caranye
# Target : facebook.com <– Target 



class reverse(object):
 def run(self, target):
  print “”
  if target.startswith(“http://&#8221;):
   target = target.replace(“http://&#8221;, “”)
  elif target.startswith(“https://&#8221;): 
   target = target.replace(“https://&#8221;, “”)
  else:
   pass

  url = “http://viewdns.info/reverseip/?host=%s&t=1&#8221; % (target)

  try:
   opener = urllib2.build_opener()
   opener.addheaders = [(‘User-agent’,’Mozilla/5.0 (Mobile; rv:14.0) Gecko/14.0 Firefox/14.0′)]
   response = opener.open(url)
   data = response.read()
   comp = re.compile(“
\S+
<td")
   baglantilar = comp.findall(data)

   for i in baglantilar:
    i = i.replace(“

“, “”).replace(“
<td", "")

    if i.startswith(“http://&#8221;):
     pass
    else:
     i = “http://”+i 

    if “Domain” not in i:
     print i     

  except:
   print “Something’s went wrong ..”
   pass


if __name__ == ‘__main__’:
 a = raw_input(“\n\t Target : “)
 reverse().run(a)

print “\n IndoXploit Coders Team”
# Indoxploit Coders Team
