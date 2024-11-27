l=['heep','he','heeeep','hp','hep']
s='hai python'
import re
match_obj=re.match('h',s)#returns matchobj if pattern present in starting of string else none.
print(match_obj)
search=re.search('h',s)#returns matchobj search the pattern throughout the string else none.
print(search)
find_all=re.findall('h',s)#returns list of matched content if present in the string, else empty list.
print(find_all)
split=re.split('r',s)#it returns the list and split the string if any match is found.
print(split)
sub=re.sub('h','w',s,2)#it will replace the search_char with new_char in the string.
print(sub)
subn=re.subn('h','w',s,4)#it will replace the search_char with new_char and returns as tuple.
print(subn)
print(subn[1])#to print how many times the char is present in the given string.
finditer=re.finditer('h',s)#returns the iterable object which consist of match object of matched content, else None.
print(finditer)
patternobj=re.compile('ha')#it convert regular expression pattern into pattern object.
text=patternobj.findall(s)#now we can use the pattern object for searching.
print(text)