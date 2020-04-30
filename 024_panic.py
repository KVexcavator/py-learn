phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
# my solution destructive , change list 
#plist = plist[1:8:1]
#plist[2] = ' '
#plist[4] = plist.pop()
#new_phrase = ''.join(plist)

# book solution, not xhange list
new_phrase = ''.join(plist[1:3])
new_phrase = new_phrase + ''.join([plist[5],plist[4], plist[7], plist[6]])
print(plist)
print(new_phrase)
