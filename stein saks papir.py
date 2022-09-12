import random 

valg  = ["stein", "saks", "papir"]

spillPaaNytt = True

while spillPaaNytt == True:
    
    maskinValg = random.choice(valg)

    brukerValg = input("Velg stein, saks eller papir:")

    if maskinValg == "stein":
        if brukerValg == "stein":
            print("maskinen valgte stein, det ble uavgjort")
        elif brukerValg == "saks":
            print("maskinen valgte stein, du tapte ")
        elif brukerValg == "papir":
            print("maskinen valgte stein, du vant ")

    if maskinValg == "saks":
        if brukerValg == "stein":
            print("maskinen valgte saks, du vant ")
        elif brukerValg == "saks":
            print("maskinen valgte saks, det ble uavgjort") 
        elif brukerValg == "papir":
            print("maskinen valgte saks, du tapte ")

    if maskinValg == "papir":
        if brukerValg == "stein":
            print("maskinen valgte papir, du tapte ")
        elif brukerValg == "saks":
            print("maskinen valgte papir, du vant ") 
        elif brukerValg == "papir":
            print("maskinen valgte papir, det ble uavgjort")

spillPaaNyttinput = input("Vil du spille igjen? j/n :")
if spillPaaNyttinput == "n":
   spillPaaNytt = False

print("takk for att du spillte! ha det bra")