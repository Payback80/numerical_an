#integer division example 
# this example shows machine errors 
A = (5./9.) + 32 #correct
B=  (5/9) +32  #uncorrect in python 2.7 , correct in python 3.0+
C = float(5)/float(9) + 32 #explicit type casting 
D = int(5)/int(9)+32  #same here 
E = 5//9 +32 #old python 2.7 bheaviour new python 3.0 syntax DON T 


F = 1//2  
G = 1%2 #mod division
H = 1./2. #correct 

A1 = round(A, 3)    #we round A to 3 decimal digits 

exercise = B - A1


print(A) #no quotation marks we print a variable 
print(B)
print(C)
print(D) 
print(E) 
print(F)
print(G)
print(H)
print(A-B)
print(A1)
print(exercise)

#a little exercise for you: Think why the result is negative and so wrong!!!! 