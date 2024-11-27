#extract all indian mobile numbers in given string.
s='+91-8594749532  +12-88483037594  +91-8446797978'
import re
n=re.findall('[+]91-[6-9]\d{9}',s)
print(n)

#extract valid gmail ids
s1='abidjdsfj8438@gmail.com  hfjfkdiej88@gmailcom kfufkdkd@gamil.com'
m=re.findall('[a-z0-9A-Z]\w*[.]?\w+@gmail[.]com',s1)
print(m)