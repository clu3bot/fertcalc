import os
import subprocess as sp 
import math
import time as t 

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

p1 = "Typically Fertilizer is Measured by Nitrogen, Phosphorus, Potassium"
p2 = "NPK is represented by %"
p3 = "lbs of solluable fertilizer"


def calculate():
    clear()
    print (p1)
    sol = input("\nElement To Measure: ")
    clear()
    print(p2)
    per = input("\nPercent of "+sol+" in fertilizer: ")
    clear()
    print(p3)
    lbs = input("\nlbs: ")
    clear()
    gal = input ("Gallons of water in stock tank: ")
    clear()

    y = (round(int(per)/100, 2))
    x = y*int(lbs)
    egrams = (round(x*453.54, 2))
    lit = (round (int(gal)*3.79, 2))
    sppm1 = (round ((int(egrams)/lit)*10**6, 2))
    sppm2 = (round (sppm1/10**3, 1))
    
    output_ppm = input ("Disired output ppm of " + sol+": ")
    inj = (round (sppm2/int(output_ppm)))

    clear()
    print ("PPM of "+sol+" in Stock Tank = "+str(sppm2))
    print ("Set injector to 1:"+str(inj)+" to achieve "+output_ppm+" ppm of "+sol+" in output solution.")


calculate()
