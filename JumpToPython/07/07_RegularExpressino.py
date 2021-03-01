import re

data = """
park 800905-1049118
kim  700905-1059119
"""

pat = re.compile("(\d{6})[-]\d{7}")
print(pat.sub("\g<1>-*******", data))

#meta character : . ^ $ * + ? { } [ ] \ | ( )
'''
[0-9]     : \d
[^0-9]    : \D
[ \t\n\r\f\v] : \s
[^ \t\n\r\f\v] : \S
[a-zA-Z0-9_] : /w
[^a-zA-Z0-9_] : /W

a.b : without \n, any character can locate at '.'
a[.]b : only match "a.b". not match "a0b"

#repeat {m,n}
ab?c = ab{0,1}c
ab*c = ab{0,}c
ab+c = ab{1,}c
'''
import re

p = re.compile('[a-z]+')
print(p.match("python")) #<re.Match object; span=(0, 6), match='python'>
print(p.match('3 python')) #None
print(p.match('py 3 thon')) #<re.Match object; span=(0, 2), match='py'>
# findall return list
print(p.findall('py 3 thon')) #['py', 'thon']
print(p.findall('3 python')) #['python']

# finditer return match object
for i in p.finditer('py 3 thon'):
    print(i)
#<re.Match object; span=(0, 2), match='py'>
#<re.Match object; span=(5, 9), match='thon'>
    print("matched string : ", i.group(), i.span()) #span() return tuple

m = re.compile('a.b')
print(m.match('a\nb')) #None
m = re.compile('a.b', re.S)
print(m.match('a\nb')) #Match

print(p.match("Python")) #None
p = re.compile('[a-z]+', re.IGNORECASE) #re.I == re.IGNORECASE
print(p.match("Python")) #Match

#MultiLIne
p = re.compile("^python\s\w+")

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data)) #['python one']

p = re.compile("^python\s\w+", re.MULTILINE)
print(p.findall(data))