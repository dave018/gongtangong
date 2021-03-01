prompt = """
1. Add
2. Del
3. List
4. Quit

Enter number: """

number = 0
while 1:
    print(prompt)
    number = int(input("숫자를 입력하세요 : "))
    if number==4:
        break
    
    if (number == 1):
        continue
    print(number)