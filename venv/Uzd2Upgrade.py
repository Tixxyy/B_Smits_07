import random
import time

def getRandValue():
    return[random.randint(1,6),random.randint(1,6)] # buffer for int 1 and 2
def printValue(user,randVal1, randVal2, score): # izprinte ara lietotaja/datora "uzmesto" vertibu un kopejo rezultatu
    return ((user)+(str)(randVal1)+" "+(str)(randVal2)+" | "+(str)(score))
def gameLogic(val1, val2,currentScore):
    if  (val1== 1) and (val2 == 1): # tiek uzmests 1-1, rezultatam tiek pieskirta vertiba 0
        currentScore=0
    elif (val1==1) or (val2==1): # tiek uzmests 1 vieninieks, tiek atgriests jau esosais rezultats
        return currentScore
    elif (val1==val2): # tiek uzmestas 2 vienadas vertibas (iznemot 1-1) rezultatam pieskaita kaulinu summu*2
        currentScore+=(val1+val2)*2
    else:
        currentScore+=val1+val2 # parastais gadijums, rezultatam pieskaita kaulinu summu

    return currentScore

#programmas galvena dala
userinput = (str)(input("Speles uzsaceja noteiksanai ludzu izvelaties opeciju 'moneta' vai 'gerbonis': "))

if (not userinput == "moneta") and (not userinput == "gerbonis"): #checks for bad input
    print("Bad input")
else:
    lietotajsVaiDators = ["Lietotajs: ", "Dators   : "] # saraksts ar lietotajiem
    izvele = random.choice(["moneta", "gerbonis"])
    reversedd = False #parbaude prieks izvades
    if  userinput!=izvele: # ja zaude, uzsak 'dators'
        print("Jus zaudejat, speli uzsak dators")
        lietotajsVaiDators=list(reversed(lietotajsVaiDators)) # speles lietotaja uzsaksanas seciba tiek "mainita"
        reversedd = True # parbaude prieks izvades
    else:
        print("Jus uzvarejat, speli uzsaciet jus")

    time.sleep(2)

    scores = [0, 0]  # scores[0]-player/computer, scores[1]-computer/player  # lietotajs uzvar monetas uzminesana/lietotajs zaude
    gajienuskaits=1
    while True:
        buffer=getRandValue() #iegust randomizetas vertibas
        scores[0]=gameLogic(buffer[0],buffer[1],scores[0]) # speles logika, tiek atgriests attiecigais rezultats
        print(printValue(lietotajsVaiDators[0],buffer[0],buffer[1],scores[0]))
        buffer.clear()
        if scores[0]>=100: break
        buffer = getRandValue()
        scores[1] = gameLogic(buffer[0], buffer[1], scores[1])
        print(printValue(lietotajsVaiDators[1], buffer[0], buffer[1], scores[1]))
        if scores[1]>=100: break
        time.sleep(1)
        gajienuskaits+=1

    if  reversedd==False: # tas ir - lietotaju seciba nav mainijusies (lietotajs 1, dators 2)
        if scores[0]>scores[1]:
            print("Uzvar lietotajs ")
        else:
            print("Uzvar dators")
    else: # lietotaju seciba ir mainijusies (dators 1, lietotajs 2)
        if scores[0]>scores[1]:
            print("Uzvar dators ")
        else:
            print("Uzvar Lietotajs")

    print("Lietotaja punkti: "+(str)(scores[0]))
    print("Datora punkti   : "+(str)(scores[1]))
    print("Kopejais gajienu skaits: "+(str)(gajienuskaits))

