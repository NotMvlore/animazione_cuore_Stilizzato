import os
import time


colonne = 7
righe = 6

r = 0
c = 0

"""
## Fase 1 e 7
for r in range(6):
    for c in range(7):
        if ((r == 0 and c % 3 != 0) or 
            (r == 1 and c %3 == 0) or
            (r - c == 2) or
            (r + c == 8)):
            print("*", end=" ")
        else:
            print(" ", end =" ")
    print("")

print("\n")

## Fase 2 e 6

for r in range(6):
    for c in range(7):
        if (
            (((c == 1) or (c==5)) and ((r==1) or (r == 2))) or
            (((c==2) or (c==4)) and ((r==0) or (r == 3) or (r == 4))) or
            ((c==3) and ((r==1) or (r == 5)))
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

## fase 3 e 5

for r in range(6):
    for c in range(7):
        if (
            (((c==2) or (c==4)) and ((r==0) or (r == 3) or (r == 4) or (r==1) or (r == 2))) or
            ((c==3) and ((r==1) or (r == 5)))
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

## fase 4

for r in range(6):
    for c in range(7):
        if (
            (c==3)
        ):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

"""
try:

    
    pos = 0
    giro = 1

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        if (pos == 0):
            giro = 1
        if (pos == 3):
            giro = -1 

        if (pos == 0) : 
            for r in range(6):
                for c in range(7):
                    if ((r == 0 and c % 3 != 0) or 
                        (r == 1 and c %3 == 0) or
                        (r - c == 2) or
                        (r + c == 8)):
                        print("*", end=" ")
                    else:
                        print(" ", end =" ")
                print()


        elif (pos == 1):
            for r in range(6):
                for c in range(7):
                    if (
                        (((c == 1) or (c==5)) and ((r==1) or (r == 2))) or
                        (((c==2) or (c==4)) and ((r==0) or (r == 3) or (r == 4))) or
                        ((c==3) and ((r==1) or (r == 5)))
                    ):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                print()


        elif (pos == 2):
            for r in range(6):
                for c in range(7):
                    if (
                        (((c==2) or (c==4)) and ((r==0) or (r == 3) or (r == 4) or (r==1) or (r == 2))) or
                        ((c==3) and ((r==1) or (r == 5)))
                    ):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                print()
  

        elif (pos == 3):
            for r in range(6):
                for c in range(7):
                    if (
                        (c==3)
                    ):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                print()
        pos += giro
        
        # Velocità dell'animazione (più basso = più veloce)
        time.sleep(0.08)

except KeyboardInterrupt:
    # Permette di uscire pulitamente premendo Ctrl+C
    print("\nAnimazione terminata!")
