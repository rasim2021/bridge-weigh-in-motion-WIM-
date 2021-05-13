#forward problem 

import numpy

L = [20,20, 20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20]
L = numpy.array(L)

#delta is the step along the beam 
delta = [0.5, 0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
delta = numpy.array(delta)

#a is the distance along the beam measured from the left 
a =[0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5,13,13.5,14,14.5,15,15.5,16,16.5,17,17.5,18,18.5,19,19.5,20]
a = numpy.array(a) 

#Force
F = 100 #kN

#calc sigma
y = 250 #mm
E = 32800 #MPa
I =1.837E9 #mm4
sig = y/(E*I)


kappa = []

b = []
y = 20
while y >= 0.0: 
   b.append(y)
   y = y-0.5
b = numpy.array(b)

#similar triangles 
kappa = b/L * a

#adding 4 0's to ensure BM can be calculated with an axle spacing of 3m
N = 4
Length = len(kappa)
pad_kappa = numpy.pad(kappa,(0,N),'constant', constant_values = 0)

#Calc bending moment list
BM = []
for k in range (0,Length):
    bendingMoment = (pad_kappa[k]*F) + (pad_kappa[k+2]*F)
    BM.append(bendingMoment)
"""print(BM)"""

#strain calculation 
Strain =[]
for j in range(0,len(BM)):
    strain = (BM[j] * sig) * 10E6
    Strain.append(strain)

#making all elements in kappa_inv negative 
kappa_inv = [ -x for x in kappa]
BM_calculated = []


#backward problem 
for s in Strain:
    stress = s * E
    bendingMomentCurrent = stress * (I/y)
    BM_calculated.append(bendingMomentCurrent)

#plot of forward problem 

import matplotlib.pyplot as plt
plot1 = plt.figure("Truck + IL = Load Effect (Strain)")
plt.plot(a,kappa_inv)
plt.ylabel('KAPPA')
plt.xlabel('LENGTH ALONG BEAM')


#plot of backward problem 

plot2 = plt.figure("Truck+Load Effect = IL")
plt.plot(a,BM_calculated)
plt.ylabel('BENDING MOMENT')
plt.xlabel('LENGTH ALONG BEAM')
plt.show()

"""
print('strain is', Strain)

print(BM_calculated)"""



