import random
scores = [0,0] # scores[0]-player, scores[1]-computer
while True:
    buffer=[random.randint(1,6),random.randint(1,6)] # buffer for int 1 and 2
    scores[0]+=sum(buffer)
    print("Lietotajs: "+(str)(buffer[0])+" "+(str)(buffer[1])+" | "+(str)(scores[0]))
    buffer.clear() # nav obligati
    if scores[0]>100: break
    buffer = [random.randint(1, 6), random.randint(1, 6)]  # buffer for int 1 and 2
    scores[1]+= sum(buffer)
    print("Dators   : " + (str)(buffer[0]) + " " + (str)(buffer[1]) + " | " + (str)(scores[1]))
    if scores[1]>100: break

if scores[0]>scores[1]:
    print("Uzvar lietotajs")
else:
    print("Uzvar dators")
print("Lietotaja punkti: "+(str)(scores[0]))
print("Datora punkti   : "+(str)(scores[1]))