import random

print("Ievadiet 'end', lai beigtu")

while True:
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
        if   userinput=="end":
            break
        elif  (int)(userinput)==result:
            print("Pareizi")
        elif (int)(userinput)!=result:
            print("Nepareizi, pareiza atbilde ir "+(str)(result))
    except:
        print("Bad input, only int or (str)'end' is allowed. If you want to end the program enter 'end' ")



    # #alternativa "primitiva" versija ar if-iem, beigs darbibu tiklidz ko bus slikta ievade
    #
    # userinput=(input((str)(values[0])+" "+choice+" "+(str)(values[1])+" = "))
    # if   (not((userinput.startswith('-') and userinput[1:].isdigit()) or userinput.isdigit())):
    #     break # ja str sakas ar simbolu '-' un viss neieskaitot pirmo simbolu ('-') ir digit or str ir digit
    # else:
    #         if (int)(userinput)==result:
    #             print("Pareizi")
    #         else:
    #             print("Nepareizi")
