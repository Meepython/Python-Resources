# Test 3-1
=============== Figure 3.1 ===============

# Epik Software EIEI
h = int(input("Input Hours: "))
m = int(input("Input Minutes: "))
s = int(input("Input Seconds: "))

# Convert into Second
h_sec = int(h * 3600)
m_sec = int(m * 60)

# Calculate all second
total_second = h_sec + m_sec + s

print("----------------------------")

print(f"Total Second = {total_second}")

print("----------------------------")

=============== Figure 3.2 ===============

x = int(input("Input some integer here "))
y = 2-x+(3/(7**(x**3)))-(5/11**(x**3))
print(f"Y = {y}")

=============== Figure 3.3 ===============

a = int(input("Input some int here "))
x = 1
X = (x+(a/x) / 2)
print(X)

=============== Figure 3.4 ===============

v1,v2,v3 = (int(e) for e in input().split())
#v1,v2,v3 = int(input().split())
v = (v1,v2,v3)
u1,u2,u3 = (int(e) for e in input().split())
u = (u1,u2,u3)

V = v1 * v2 * v3
U = u1 * u2 * u3

Total_Vector = V * U
print(Total_Vector)

=============== Figure 3.5 ===============

#Epic Program here
import math
x1,y1,x2,y2 =(int(e) for e in input("Type number : X1 Y1 X2 Y2 ").split())

C1 = x1,y1
C2 = x2,y2

Distance_2P = math.sqrt((x1 - x2) ** 2 - (y1-y2) ** 2)
print("Distance: ", Distance_2P)

=============== Figure 3.6 ===============

weight = int(input("Input ur weight: "))
height = int(input("Input ur height: "))
real_height = height * (10 ** -2)
bmi = weight / ( real_height * real_height)

print("Your BMI is: ", round(bmi, 1))
#Alternate Solution
# math.floor(number*10)/10

=============== Figure 3.7 ===============

product = str(input("Enter your Product: "))
price_before_tax = float(input("Enter your Price: "))

vat = price_before_tax * 0.07 # Calculate VAT
price_with_tax = vat + price_before_tax  # Adding VAT and price

discount = (price_with_tax >= 500) * (price_with_tax * 0.03) # Calculate Sales price
total_price = price_with_tax - discount # Subtracting price and discount

print(f"Product name {product} Total {round(total_price, 1)} Baht")

=============== Figure 3.8 ===============

import math

H = int(input("Enter H: ")) # Height
C = int(input("Enter C: ")) # Step up
S = int(input("Enter S: ")) # Step down

days = ((H - C) / (C - S)) + 1
print(f"Total {int(math.ceil(days))} days")


=============== Figure 3.9 ===============

import math

width = float(input("Width: "))
length = float(input("Length: "))

area = width * length
rai = math.ceil(area / 1600)

rai_money = rai * 1000

print("Area:", format(rai, ".1f"), "Rai")
print("Money:", format(rai_money, ".1f"), "Baht")


=============== Figure 3.10 ===============

station = int(input("Get off from station "))
pay_money = int(input("Money spent "))
# Check the select station and its price
s_price = ((station == 1) * 27) + ((station == 2) * 35) + ((station == 3) * 42)
print(f"station {station} : Price: {s_price}")

change = pay_money - s_price

coin10 = change // 10
change = change % 10

coin5 = change // 5
change = change % 5

coin2 = change // 2
change = change % 2

coin1 = change // 1
change = change % 1

print("Currency Change")
print("coin 10: ",coin10, "baht")
print("coin 5: ",coin5, "baht")
print("coin 2: ",coin2, "baht")
print("coin 1: ",coin1, "baht")

===============================================
