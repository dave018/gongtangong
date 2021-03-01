print("Hellow World")
print('Python is fun')
print("""Life is too short, You need python""")
print('''Life is too short, You need python''')

print("Python's favorite food is perl")
print('"Python is very easy." he says.')
print("\"Python is very easy.\" he says.")

print("123\n   456")
print('''123
   456''')
print('''
123
   456''')
multilines = '''
123
   456'''
print(multilines)

head = "Python"
tail = " is fun!"
a = head+tail #len is 14. There is no \0 character
print(a*2 + "| length is " + str(len(a*2)))
print(a[13]) #print '!'. This means that string index is with 0 like C/C++
print(a[-1]) #print '!'. if i < 0, a[i] means a[(len(a) + i)%len(a)].
#print(a[-15]) #this is out of range. [14] is P
print(a[10:13]) #print 'fun'. [13] which is '!' is not printed
print(a[10:-5]) #print nothing.
print(a[:6]) #print 'Python'
print(a[10:]) #print 'fun!'
print(a[:9] + " really" + a[9:])

#format code
print("I eat %d %s" % (3, "apples"))
print("I eat %s %s" % (3, "apples"))
print("upside 5%")
print("downside %3d%%" % 3) # if string has '%' with other format, need '%%'

#format function
print("I eat {0} {1}".format(3, "apples"))
print("I eat {number} {fruit}".format(fruit="apples", number=3))
#print("I eat {0} {fruit}".format(fruit="apples", 3)) #error
print("I eat {0} {fruit} {1}".format(3, "much", fruit="apples"))
print("downside {0:>3}%".format(3)) #:>3 == :3
print("downside {0:^10}%".format(3)) #align center
print("downside {0:=<10}%".format(3)) #fill space to character('=')
print("{0:10.4f}".format(3.141592623)) #print '3.1415' aligned right.
print("{0} calculation string".format(head*2))

#f string formatting
print(f'{head*2} asdfasdf {tail+"!"}')
print(f'"hi":=^10')

print(a.find('P')) #return index = 0
print(a.find('n')) #return index first found
print(a.find('S')) #return error = -1
#print(a.index('S')) #error
print(a.index('n')) #return index first found

print(",".join('abcd'))
print(",".join(['a', 'b', 'c', 'd']))
print(a.replace("Python", "JAVA")) #protect original. return value is changed
print(a)
print(a.split('n'))
print("n".join(a.split('n'))) #join <-> split. opposite feature
print(a.upper())
print(a.lower())
myStr = "Hello World"
print(myStr.replace("Hell", "Heaven") + " | " + myStr)