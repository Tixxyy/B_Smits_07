import random
import time

def getRandValue():
    return[random.randint(1,6),random.randint(1,6)]

def printValue(user,randVal1, randVal2, score):
    if  user == "Dators": # parbaude, lai varetu izprintet visu 1 rinda (Vards 'Dators' ir isaks par 'Lietotajs')
        return ((user.ljust(len(user)+3))+": "+(str)(randVal1)+" "+(str)(randVal2)+" | "+(str)(score))
    #ljust izmantots, lai izvaditu visu viena rinda ar Lietotaju (ljust(varda garums + cik atstarpes-(garakais vards - isakais)))
    elif user == "Lietotajs":
        return ((user)+": "+(str)(randVal1)+" "+(str)(randVal2)+" | "+(str)(score))

def gameLogic(val1, val2,currentScore):
    if  (val1== 1) and (val2 == 1):
        currentScore=0
    elif (val1==1) or (val2==1):
        return currentScore # sort of an empty statement // could be improved
    elif (val1==val2):
        currentScore+=(val1+val2)*2
    else:
        currentScore+=val1+val2

    return currentScore

#programmas galvena dala
userinput = (str)(input("Speles uzsaceja noteiksanai ludzu izvelaties opeciju 'moneta' vai 'gerbonis': "))

if (userinput != "moneta") and (userinput != "gerbonis"): #checks for bad input
    print("Bad input")
else:
    lietotajsVaiDators = ["Lietotajs", "Dators"] # saraksts ar lietotajiem
    izvele = random.choice(["moneta", "gerbonis"])
    if  userinput!=izvele: # ja zaude, uzsak 'dators'
        print("Jus zaudejat, speli uzsak dators")
        lietotajsVaiDators=list(reversed(lietotajsVaiDators)) # speles lietotaja uzsaksanas seciba tiek "mainita"
    else:
        print("Jus uzvarejat, speli uzsaciet jus")
    time.sleep(2) # pauze paredzamibai

    scores = [0, 0]  # scores[0]-player/computer, scores[1]-computer/player
    gajienuskaits = 1 # 1 jo pedejais gajiens netiks ieskatitits (while cikls beigsies uzreiz)
    while True:
        buffer=getRandValue()
        scores[0]=gameLogic(buffer[0],buffer[1],scores[0])
        print(printValue(lietotajsVaiDators[0],buffer[0],buffer[1],scores[0]))
        buffer.clear() # nav obligati
        if scores[0]>=100: break
        buffer = getRandValue()
        scores[1] = gameLogic(buffer[0], buffer[1], scores[1])
        print(printValue(lietotajsVaiDators[1], buffer[0], buffer[1], scores[1]))
        if scores[1]>=100: break
        time.sleep(1) # pauze paredzamibai
        gajienuskaits+=1

    if scores[0]>scores[1]:
        print("Uzvareja "+lietotajsVaiDators[0].lower())
    else:
        print("Uzvareja "+lietotajsVaiDators[1].lower())

    def replaceLastLetterWithA(stringA): # nomaina pedejo burtu uz a. Piemeram, 'Lietotajs'-->'Lietotaja'
        a = list(stringA)
        a[len(a)-1]='a'
        return "".join(a)

    print("\n"+replaceLastLetterWithA(lietotajsVaiDators[0])+" punktu skaits: "+(str)(scores[0]))
    print(replaceLastLetterWithA(lietotajsVaiDators[1])+" punktu skaits: "+(str)(scores[1]))
    print("Kopejais gajienu skaits: "+(str)(gajienuskaits)) # pasa interesei

