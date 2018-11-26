m = 640.                         #meters
#convert to centimeters
cm = m * 10 ** 2               #due ordini di grandezza ergo 1cm * 10^2 
#conversions 
inch = cm * 0.39370
feet = cm * 0.032808
yards = cm * 0.010936
miles = cm * 0.0000062137      #veramente bruttissimo da vedere, riscrivilo in notazione scientifica 


print("sono " ,cm , "cm")
print("corrisponde a pollici", inch)
print("corrisponde a", feet, "piedi")                           #corretto
print("corrisponde a yarde", yards )
print("corrisponde a miglia", miles)

# c è un non errore di decimali  nella semplicità andrebbe un po' deciso come troncarli se su o giù vabbè 

