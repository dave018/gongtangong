f = open("04-3_file_IO.txt", 'w')

for i in range(1,11):
    data = "%dth line.\n" % i #if not \n, there is only 1 line.
    f.write(data)
f.close()

#readline
f = open("04-3_file_IO.txt", 'r')
while True:
    line = f.readline() 
    if not line : break # if EOF, readline return "" and this is False.
    print(line, end='') #line has already \n. if no end='', 2 new lines
f.close()

'''
while 1:
    data = input()
    if not data: break #enter is break;
    print(data)
'''

#readlines
f = open("04-3_file_IO.txt", 'r')
lines = f.readlines()
print(len(lines))
for line in lines:
    print(line,end='')
f.close()

#read
f = open("04-3_file_IO.txt", 'r')
data = f.read()
print(data)
f.close()

#append mode
f = open("04-3_file_IO.txt", 'a')
for i in range(11,20):
    data = "%dth line.\n" % i
    f.write(data)
f.close

#with close file automatically
with open("04-3_file_IO.txt", 'r') as f:
    print(f.readline())