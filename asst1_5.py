# -*- coding: utf-8 -*-
"""ASST1-5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wrMR5LmC4GQXWmDs9TXhRwM9NqD-Abfh

ASSIGNMENT 1

QN 1
"""

# To find the downstream depth of open channel
# Given Data
Q= float(input("Enter the value of Discharge:"))
T= int(input("Enter the value of top width:"))
g= float(input("Enter the value of acceleration due to Gravity:"))
y1= float(input("Enter the value of upstream depth:"))
Z= float(input("Enter the Value of hump:"))
#Dicharge per meter width
q=Q/T
print("The value of discharge per meter width is:", q)
#Area Calculation
A1= T*y1
print("The value of upstream area is:", A1)
# Calculation of Froude Number
Fr1 = ((Q*Q*T)/(g*A1* A1 *A1))**0.5
print("The value of Froude number is:", Fr1)
if Fr1>1:
 print("The flow is Super Critical Flow")
else:
 print("The flow is Sub Critical Flow")
#Upstream Energy
E1=(y1+(Q*Q)/(2 *g*A1 *A1))
print("The value of Energy at initial Section is:", E1)
#Downstream Energy
E2=E1-Z
print("The value of downstream Energy E2 is:", E2)
#Critical Depth
yc=(q*q/g)**0.3333
print("The Value of critical depth is:", yc)
Ec=1.5*yc
print("The value of critical Energy is:", Ec)
if Ec>E2:
 print("Chocking Conditlon")
else:
 print("SAFE")
#Calculation of Zmax
Zmax=E1-Ec
print("The value of maxinmum hump is:", Zmax)

"""QN 2"""

# To find the doawnstream depth of open channel
# Given Data
Q= float(input("Enter the value of Discharge:"))
T= int(input("Enter the value of top width:"))
g= float(input("Enter the value of acceleration due to Gravity:"))
y1= float(input("Enter the value of upstream depth:"))
Z= float(input("Enter the Value of hump:"))
#Dicharge per meter width
q=Q/T
print("The value of discharge per meter width is:", q)
#Area Calculation
A1= T*y1
print("The value of upstream area is:", A1)
# Calculation of Froude Number
Fr1 = ((Q*Q*T)/(g*A1* A1 *A1))**0.5
print("The value of Froude number is:", Fr1)
if Fr1>1:
 print("The flow is Super Critical Flow")
else:
 print("The flow is Sub Critical Flow")
#Upstream Energy
E1=(y1+(Q*Q)/(2 *g*A1 *A1))
print("The value of Energy at initial Section is:", E1)
#Downstream Energy
E2=E1-Z
print("The value of downstream Energy E2 is:", E2)
#Critical Depth
yc=(q*q/g)**0.3333
print("The Value of critical depth is:", yc)
Ec=1.5*yc
print("The value of critical Energy is:", Ec)
if Ec>E2:
 print("Chocking Conditlon")
else:
 print("SAFE")
#Calculation of Zmax
 Zmax=E1-Ec
 print("The value of maxinmum hump is:", Zmax)

"""QN 3"""

#To find the downstream depth of open channel
#Given Data
Q= int(input("Enter the value of Discharge:"))
B1 = float(input("Enter the value of width at upstream: "))
B2 = float(input("Enter the value of width at downstream: "))
g= float(input("Enter the value of acceleration due to Gravity:"))
yl= int(input("enter the value of upstream depth:"))
#Dicharge per meter width
q1=Q/B1
q2=Q/B2
print("The value of discharge per meter width is:'", q1)
print("The value of discharge per meter width is:", q2)
#Area Calculation
A1=B1*y1
print("The value of upstream area is:", A1)
#Calculation of Froude Number
Fr1=((Q*Q*B1)/(g*A1*A1*A1)) **0.5
print("The value of Froude number is:", Fr1)
if Fr1>1:
 print("The flow is Super Critical Flow")
else:
 print("The flow is Sub Critical Flow")
#Upstream Energy
E1=y1+((Q*Q)/(2*g*A1*A1))
print("The value of Energy at initial Section is:",E1)
#B2min: Any dition
B2min = (27*Q*Q/(8*g*E1*E1*E1))**0.5
print("The value of minimum width to be kept to avoid Chocking is:", B2min)
if B2min > B2:
 print("Chocking Condition")
else:
 print("SAFE")
#Critical Depth
yc=((Q*Q)/(B2*B2*g))**0.3333
print ("The Value of critical depth is: ", yc)
Ec=1.5*yc
print("The value of critical Energy is", Ec)

"""QN 4"""

#Design of Efficient Channel Section
Q= int(input("Enter the value of Discharge:"))
n= float(input("Enter the value of Rugosity coefficient:"))
So= float(input("Enter the value of bed slope:"))
g= float(input("Enter the value of acceleration due to Gravity:"))
#Manning's Formula
#Q=(AR^2/3S^1/2)/n
yn=((Q*n*50*1.591)/(1.732))**(3/8)
print("The Value of yn is", yn)
#To encounter the effect of free board
yn1=1.1*yn
print("The Value of ynl is", yn1)
#Cross Sectional Area
A=1.732*yn*yn1
print("The cross sectional Area is:", A)
#Top Width
T=4*yn/1.732
print("The value of top Width is:", T)
#Bottom Width
B=2*yn/1.732
print("The value of Bottom Width is'", B)
Fr=((Q*Q*T)/(g*A*A*A))*0.5
print("The value of Froude number is:", Fr)
if Fr>1:
 print("The flow is Super Critical Flow")
else:
  print("The flow is Sub Critical Flow")

"""ASSIGNMENT 2

QN 1
"""

# Calculation of total Infiltration by Horton's Equation
fo = int(input("Enter the value of initial Infiltration Rate:"))
fc= float (input("Enter the value of Final infiltration Rate:"))
t= int(input("Enter the value of Time:"))
kh= float(input("Enter the value of Decay Coefficient:"))
# The total Infiltration is given by:
Fp= fc*t+(fo-fc)/kh
print ("The value of Total Infiltration is:", Fp)

"""QN 2"""

#Calculation of Mean precipitation by theissen's polygon Method
#The value of precipitation at Each station is
p1=int(input("Enter the value of rainfall at Station 1:"))
p2= int(input("Enter the value of rainfall at Station 2:"))
p3 =int(input("Enter the value of rainfall at Station 3:"))
p4 =int(input("Enter the value of rainfall at Station 4:"))
p5 =int(input("Enter the value of rainfall at Station 5:"))
#Area for each station
A1= int(input("Enter the value of Catchment Area for raingauge station 1:"))
A2= int(input("Enter the value of Catchment Area for raingauge station 2:"))
A3 =int(input("Enter the value of Catchment Area for raingauge station 3:"))
A4=int(input("Enter the value of Catchment Area for raingauge station 4:"))
A5= int(input("Enter the value of Catchment Area for raingauge station 5:"))
#The total catchment area is
A=A1+A2+A3+A4+A5
print("The value of Total Catchment area is:", A)
#Runoff Volume
V=(p1*A1+p2*A2+p3*A3+p4*A4+p5*A5)*2500
print("The runoff volume from the given catchment is:", V)
# Mean Precipitation
p=(p1*A1+p2*A2+p3*A3+p4*A4+p5*A5)/A
print("The value of Mean Precipitalon is:", p)

"""QN 3"""

#Calculation of Mean precipitation by Isohytel Method
#The value of precipitation at Each station i
p1= int(input("Enter the value of rainfall at Station 1:"))
p2= int(input("Enter the value of rainfall at Station 2:"))
p3= int(input("Enter the value of rainfall at Station 3:"))
p4= int(input("Enter the value of rainfall at Station 4:"))
p5= int(input("Enter the value of rainfall at Station 5:"))
p6= int(input("Enter the value of rainfall at Station 6:"))
p7= int(input("Enter the value of rainfall at Station 7:"))
p8= int(input("Enter the value of rainfall at Station 8:"))
# Area for each station
A1= int(input("Enter the value of Catchment Area for raingage station 1:"))
A2= int(input("Enter the value of Catchment Area for raingauge station 2:"))
A3= int(input("Enter the value of Catchment Area for raingauge station 3:"))
A4= int(input("Enter the value of Catchnent Area for reingauge station 4:"))
A5= int(input(" Enter the value of Catchment Ares for raingauge station 5:"))
A6= int(input("Enter the value of Catchment Area for raingeuge station 6:"))
A7= int (input("Enter the value of Catchment Area for reingauge station 7:"))
# The total catchment area is
A=A1+A2+A3+A4+A5+A6+A7
print("The value of Total Catchment ar ea is :", A)
#Mean Precipitation
p=((p1+p2)*A1/2+(p2+p3)*A2/2+(p3+p4)*A3/2+(p4+p5)*A4/2+(p5+p6)*A5/2+(p6+p7)*A6/2+(p7+p8)*A7/2)/A
print("the value of Mean Precipitalon is:", p)

"""ASSIGNMENT 3

QN 1
"""

#To Calculate the length of transition curve
V= int(input("Enter the value of design speed:"))
R= int(input("Enter the value of Radius of curvature:"))
N= int(input("Enter the value of slope:"))
W= float(input("Enter the value of width of road including extra widening:"))
emax= float(input("enter the value for plain terain:"))
ecal=(V*V/(225*R))
print("The value of Super elevation:",ecal)
if ecal<emax:
 print(ecal)
else:
 print(emax)
Ls=(emax*N*W/2)
print("The length of transition curve:", Ls)

"""QN 2"""

R = int(input("Constant R:"))
C = int(input("Constant C:"))
import numpy as geek
A = int(input("Total Data Values for EWL Constant:"))
B = int(input("Total Data Values for AADT: "))
EWL_Constant =[]
AADT =[]
for i in range(1,A+1):
  print("Enter EWL Constant:")
  A = float(input())
  EWL_Constant.append(A)
for j in range(1,B+1):
  print("Enter AADT:")
  B = float(input())
  AADT. append (B)
product=geek.dot(EWL_Constant,AADT)
print("Dot Product:\n", product)
Total_EWL = product
print("Total EWL:", Total_EWL)
print("EWL after 60 years:",Total_EWL*1.6)
TI = 1.35*(((1.6*Total_EWL)+((product)/2))**0.11)
print("Traffic Index : ", TI)
Thickness = 0.166*TI*(99-R)/(C**0.2)
print ("Pavement Thickness: ", Thickness, "cm")

"""QN 3"""

P =float (input(" Load in kg: "))
p =float (input(" Tyre pressure kg/cm^2: "))
M = int (input("Total Number of layers in a given Pavement : "))
pi = 3.14159
CBR = []
for i in range (1, M+1):
  print("California Bearing Ratio of Material in %")
CBR_value = float(input())
CBR.append(CBR_value)
T = ((1.75*P)/(CBR_value)-(P/(p*pi)))**0.5
print("Thickness Above this layer: ", T, "cm")
print("Given that bitumen layer of 4 cm")

"""ASSIGNMENT 4

QN 1
"""

fck = float(input(" Enter the value of characteristic compressive strength:"))
# Experimental Determinations
Gca = float(input ("Enter the value of specific gravity of CA:"))
Gfa = float(input("Enter the value of specific gravity of FA:"))
Gc = float(input("Enter the value of specific gravity of Cement:"))
Water_Density = float(input("Enter the value of Water Density:"))
AGG_Size = float(input("Enter the nominal Size of Aggregate:"))
Nature_of_AGG = input("Nature of Aggregates:")
Slump = float(input("Enter the value of workability of concrete:"))
Admixture = input("Type of Admixture:")
Exposure_Condition = input("Exposure Condition:")
Concreting = input("Type of Concreting:")
Zone = int(input("Zone:"))
# Target Mean Strength
sigma = {10:3.5,15:3.5,20: 4,25:4,30: 5,35: 5,40: 5,45: 5,50: 5,55: 5}
ft=fck+sigma[fck]*1.65
print("Target Mean Strength:",ft,"MPa")
# Maximum free Water Cement Ratio
# Reference IS 456: 2000 Table 5
if(Concreting == "Plain"):
 WC_ratio = {"Mild" : 0.6,"Moderate" :0.6,"Severe" :0.5,"Very Severe" :0.45,
             "Extreme":0.4}
else:
 WC_ratio ={"Mild": 0.55,"Moderate":0.5,"Severe" :0.45,"Very Severe" :0.45,
            "Extreme":0.4}
print("W/C Ratio:",WC_ratio[Exposure_Condition] )
WC_ratio = WC_ratio[Exposure_Condition]
# Minimum Cement Content
if(Concreting == "plain"):
 Min_Cement_Content = {"Mild":220,"Moderate": 240,"Severe": 250,
                       "Very Severe": 260,"Extreme": 280}
else:
  Min_Cement_Content = {"Mild":300,"Moderate": 300,"Severe": 320,
                       "Very Severe": 340,"Extreme": 360}

print("Minmum Cement Content:", Min_Cement_Content[Exposure_Condition],"kg/m^3")

# Water Content
Water_Content={10:208,20:186,40:165}
Water_Content = Water_Content[AGG_Size]
if (Slump == 75):
 Water_Content = Water_Content + Water_Content*0.03
elif (Slump == 100):
 Water_Content = Water_Content + Water_Content*0.06
elif (Slump == 125):
 Water_Content = Water_Content + Water_Content*0.09
elif (Slump == 150):
 Water_Content = Water_Content + Water_Content*0.12
elif (Slump == 175):
 Water_Content = Water_Content + Water_Content*0.15
elif (Slump == 200):
 Water_Content = Water_Content + Water_Content*0.18
if (Nature_of_AGG == "Sub-Angular"):
 Water_Content = Water_Content - 10
elif (Nature_of_AGG == "Gravel"):
 Water_Content = Water_Content - 20
elif (Nature_of_AGG == "Round"):
 Water_Content = Water_Content - 25
if (Admixture == "Plastisizer"):
 Water_Content = Water_Content-(0.1*Water_Content)
elif (Admixture=="Super-plastisizer"):
 Water_Content = Water_Content-(0.2*Water_Content)
print("Water Content:", Water_Content, "kg/m^3")
# Cement Content
Cement_Content = Water_Content/WC_ratio
print("CementContent:", Cement_Content, "kg/m^3")
print("As Per IS 456:2000, Maximum allowed Cement Content is 450 kg/m^3")

if (Cement_Content< 450):
  Cement_Content = Cement_Content
else:
  Cement_Content = 450

if Cement_Content< 450:
  print("Safe")

# Volume Calculations
Vol_Cement = Cement_Content/(Gc*Water_Density)
print("Volume of Cemnet:",Vol_Cement,"m^3")
Vol_Water = Water_Content/Water_Density
print("Volume of Water:",Vol_Water,"m^3")
Vol_AGG= 1-Vol_Water-Vol_Cement
print("Volume of Course Aggregates and Fine Aggregates: ",Vol_AGG, "m^3")
Zone_ID ={}
Zone_ID[1]= {10:0.44, 20:0.60, 40:0.69}
Zone_ID[2]={10:0.46, 20:0.62, 40:0.71}
Zone_ID[3]={10:0.48, 20:0.64, 40:0.73}
Zone_ID[4]={10:0.5, 20:0.66, 40:0.75}
Fraction = Zone_ID[Zone] [AGG_Size]
if (WC_ratio==0.5) :
  Fraction=Fraction
elif (WC_ratio==0.45):
  Fraction=Fraction+(0.01*Fraction)
elif (WC_ratio==0.4):
  Fraction=Fraction+(0.02 * Fraction)
elif (WC_ratio==0.55):
  Fraction=Fraction-(0.01*Fraction)
elif (WC_ratio==0.60):
  Fraction=Fraction-(0.02*Fraction)

print("Course Aggregate fraction:", Fraction)
Vol_CA = Vol_AGG*Fraction
print ("Volume of Course Aggregate:", Vol_CA,"m^3")

Vol_FA = Vol_AGG-Vol_CA
print ("Volume of Fine Aggregate: ", Vol_FA,"m^3")

Mass_CA= Vol_CA*Gca* Water_Density
print ("Mass of Course Aggregates: ", Mass_CA, "Kg/m^3")

Mass_FA = Vol_FA*Gfa*Water_Density
print ("Mass of Fine Aggregates:", Mass_FA, "kg/m^3")

# Ratios
print("Weight Batching")
print(Cement_Content/Cement_Content,":", Mass_FA/Cement_Content,":",
      Mass_CA/Cement_Content,":",Water_Content/Cement_Content)
print("Volume Batching:")
print(Vol_Cement/Vol_Cement,":",Vol_FA/Vol_Cement,":",Vol_CA/Vol_Cement,":",Vol_Water/Vol_Cement)

"""ASSIGNMENT 5

QN 1
"""

#To find the ultimate moment carring capacity of singly r/f beam
fck = float(input("Enter the value of charateristics compressive strength:"))
fy = float(input("Enter the grade of steel:"))
Es = float(input("Enter the value of Modulus of Elasticity of steel:"))
b = float(input("Enter the value of Width:"))
d = float(input("Enter the value of effective depth:"))
d1 = float(input("Enter the value of bar diameter (d1):"))
d2 = float(input("Enter the value of bar diameter (d2):"))
n=int(input("Enter the number of bars"))
Ast1=(n*0.7854*d1*d1)
Ast2=(n*0.7854*d2*d2)
print("The value of area of steel (Ast1):", Ast1)
print("The vaiue of area of steel (Ast2):", Ast2)
#Total area of steel
Ast=Ast1+Ast2
print("The value of area of steel (Ast):", Ast)
#Neutral Axis Factor
ku = 0.0035/(0.0055+(fy/(1.15*Es)))
print("The value of Neutral axis factor (ku):", ku)
#Momenent of Resistance factor
Ru=0.36*fck*ku*(1-(0.42*ku))
print("The value of Moment of Resistance factor (Ru):", Ru)
#Maximum Neutral Axis:
xumax = ku*d
print("The value of maximum neutral axis (xumax):", xumax)
xu = (0.87*fy*Ast)/(0.36*fck*b)
print ("The value of Actual Neutral Axis (xu):", xu)
if xumax>xu:
 print("UNDER REINFORCED")
else:
 print("OVER REINFORCED")
#By Comparing
X = float(input("Enter the value of Neutral Axis:"))
#Moment of Resistance
Mu=0.36*fck*xu*b*(d-(0.42*xu))*10*-6
print("The value of Moment of Resistance is:", Mu)

"""ASSIGNMENT 5.1

QN 1
"""

#Design of Slab
#Given Data
#Effective span is already given in question
span= float(input("Enter the value of effective span in meters:"))
b= float(input("Enter the value of width of slab in mm:"))
bs= float(input("Entert the value of Support Width in meters:"))
fck = float(input(" Enter the value of Characteristics Compressive Strength:"))
fy = float(input("Enter the value of grade of steel:"))
Es = float(input("Enter the value of Modulus of Elasticity is:"))
LL = float(input("Enter the value of Live Load:"))
FF = float(input("Enter the value of Floor Finish:"))
Density = float(input("Enter the value of Density of RCC:"))
# Design Constants
# Neutral Axis Factor
ku=0.0035/((0.0055)+(fy/(1.15*Es)))
print("The value of Neutral Axis Factor (ku) is:", ku)
# Moment of Resistan ce Facor
Ru= 0.36*fck*ku*(1-(0.42*ku))
print("The value of Moment Resisteance factor (Ru) is:", Ru)
#Assurming pt 0.5 from fig.4 from IS 456:2007 page no.38
fs=float(input("Ent er the value of Steel Stress of Service:"))
#From Graph find out the Modification Factor
MF=float(input("Enter the value of Modification Factor:"))
#From Clause 23.2.1 Select span/d Ratio
S=float(input("Enter the value of span/d ratio:"))
#Correction Factors
k1=float(input("Enter the value of Correction factor if sapn> 10m (k1):"))
k2= float(input(" Enter the value of Tension r/f correction factor (k2):"))
k3= float(input ("enter the value of Compression r/f correction factor (k3):"))
k4= float (input(" Enter the value of correction factor in case of flanged section (k4):"))
# Effective depth
d1=(span*1000)/(S*MF*k1*k2*k3*k4)
print("The value of effective depth as per deflection criteria is:", d1)
# Define Effective depth and overall depth Assuming value of cover
d = float(input("Enter the value of Effective depth in mm (d):"))
D= float(input("Enter the value of Overall depth in mm (D):"))
# Load Calculations
# Self Weight of slab
DL=D*Density/1000
print("The Dead load is:", DL)
# Total Load is
Factor=float(input("Enter the value of partial Safety Factor is: "))
TL=DL+LL+FF
print("The value of total load is:", TL)
Wu=Factor*TL
print("Wu=", Wu)
# Bendingf Moment Calculations (Mu)
Mu= Wu*span*span/8
print("The Value of Bending Moment (Mu) is:", Mu)
# Check for effective depth
d2=(Mu*1000000/(Ru*b))**0.5
print("The value of Effective depth as per Mornent criteria:", d2)
if d2>d:
 print ("Revise the Depth:")
else:
 print ("'SAFE")
d = float(input("Enter the value of Effective depth in mm (d):"))
print("Minimum Steel Calculations")
Astmin = 0.12*b*D/100
print("The value of Minimum steel is:", Astmin)
print("Main Steel calculations'")
Ast=((0.5*fck*b*d)/(fy))*(1-((1-((4.6*Mu*1000000)/(fck*b*d*d)))**0.5))
print("Ast:", Ast)
print("Check for Ast")
if Ast<Astmin:
 print("Take Ast=Astmin")
else:
 print("Ast>Astmin, Hence SAFE")
dia1 = float(input("Enter the value of bar diameter for main steel:"))
dia2 = float(input(" Enter the value of bar diameter for Distribution steel:"))
#Area of bar
ao1 = 0.7854*dia1*dia1
print("The Value of Area of main steel bar (ao1):", ao1)
ao2= 0.7854* dia2*dia2
print("The Value of Area of main steel bar (ao2):", ao2)
# Sapcing Calculations
Spacing1 = ao1*b/Ast
print("The sapcing for main steel bars is;", Spacing1)
Spacing2=ao2*b/Astmin
print("The sapcing for distribution steel bars is;", Spacing2)
print("Check 1 for main steel")
if Spacing1>300:
 print("UNSAFE")
else:
 print("SAFE")
print("'Check 2 for main steel")
if Spacing1 > 3*d:
 print("UNSAFE")
else:
 print("SAFE")
print("Check 1 fon Distribution steel")
if Spacing1>300:
 print("UNSAFE")
else:
 print("SAFE")
print("Check 2 for Distribution steel")
if Spacing1>5*d:
 print("UNSAFE")
else:
 print("SAFE")
print("Approximated values of Sapcing:")
S1= float(input("Enter the value of spacing of main bars:"))
S2=float(input("Enter the value of spacing of distribution bars:"))
Astprovided=ao1*b/S1
print("The provided steel area for main bars at section in mm^2 is:", Astprovided)
Astprodist=ao2*b/S2
print("The provided steel area for distribution bars at section in mm^2 is: ", Astprodist)
# Check for Shear
Vu=(Wu*span/2)-(Wu*((bs/2)-(d/1000)))
print("The value of SF at a Section is:", Vu)
Stress=(Vu*1000)/(b*d)
print("The vaiue of shear stress is:", Stress)
# From table 20 IS 456:2007 page 73
Stressmax = float(input("Enter the value of maximum Shear stress:"))
if Stress>Stressmax:
 print("Crushing will happen")
else:
 print("SAFE")
pt=(100*Ast)/(b*d)*120
print("Enter the value of percentage steel is:", pt)
#From table 19 IS 456:2007 page 73
SS=float(input("Enter the value of Shear Stress is:"))
k=float(input("Enter the value of depth factor:"))
Shear=k*SS
print("The value of shear at section is, Shear")
if Stress>Shear:
 print("Shear Reinforcement Required")
else:
 print("Shear Reinforcement not Required, SAFE")
# Check for Deflection
ActDEF=span*1000/d
print("The value od span/d is:", ActDEF)
# Actual Deflection
MaxDEF=S*MF*k1*k2*k3*k4
print("The permissible deflection is:", MaxDEF)
if MaxDEF>S/d:
 print("SAFE")
else:
 print("UNSAFE")
# Check for Anchorage Length
M1=0.87*fy*Ast*(d*(fy*Ast)/(fck*b))
print("The value of Moment (M1)'", M1)
lo = 8*dia1
La = 1.3*(M1/Vu)+10
print ("The value of Anchorage length is:", La)
# Development Length
bonds = float(input("Enter the value of Bond Stress:"))
Ld = 0.87*fy*dia1/4*bonds*1.6
print("The value of Development length is:", Ld)
if La>Ld:
 print("'SAFE")
else:
 print("increase anchorage")

# Stress When depth is constant
Q = float(input("Enter the value of Load in kN:"))
N= int(input("Number of data values of radial distance:"))
pi = 3.14159265359
Z = float(input("Depth:"))
r = []
for i in range (1, N+1):
  print("Enter radial distance in m".format (i))
  Value_r = float(input())
  r.append(Value_r)
  Stress =((3*Q)/(2*pi*Z*Z))*(((1/(1+((Value_r/Z)**2))))**2.5)
  print("Stress:",Stress,"kN/m^2")