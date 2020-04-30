phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

pattern = "on tap"
for letter in plist:
    if letter not in pattern:
        plist.remove(letter)
for i in range(2):
    plist.pop()
plist.insert(2, plist.pop(3))
plist.extend([plist.pop(), plist.pop()])

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)

