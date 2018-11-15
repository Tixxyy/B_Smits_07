import random

i = 0
correct = 0
while i < 10:
    choice = random.choice(['+', '-', '*', '/', '**'])
    if choice != '**' and  choice != '/':
        values = [random.randint(1,10),random.randint(1,10)] # values = 2 skaitlu vertibas (sija gadijuma ranzomizetas)
        if choice=='+':
            result = values[0] + values[1]
        if choice=='-':
            result = values[0] - values[1]
        if choice=='*':
            result = values[0] * values[1]
    elif choice == '**':
            values = [random.randint(1,10),2] # kapinatajs 2 ari tiek pievienots masivam lai atvieglotu izvadi
            result= values[0]**values[1]
    elif choice == '/':
        values = [random.randint(1,100),random.randint(1,10)]
        result = (int)(values[0]/values[1])

    # main program
    userinput=(input((str)(values[0])+" "+choice+" "+(str)(values[1])+" = "))
    try:
        if  (int)(userinput)==result:
            print("Pareizi")
            correct +=1
        elif (int)(userinput)!=result:
            print("Nepareizi, pareiza atbilde ir "+(str)(result))
        i+=1
    except:
        print("Bad input, only int is allowed ")

print("Pareizo atbilzu skaits: "+(str)(correct))