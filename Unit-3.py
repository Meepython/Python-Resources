# Test 3-1
#=============== Figure 3.1 ===============

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

#=============== Figure 3.2 ===============

x = int(input("Input some integer here "))
y = 2-x+(3/(7**(x**3)))-(5/11**(x**3))
print(f"Y = {y}")

#=============== Figure 3.3 ===============

a = int(input("Input some int here "))
x = 1
X = (x+(a/x) / 2)
print(X)

#=============== Figure 3.4 ===============

v1,v2,v3 = (int(e) for e in input().split())
#v1,v2,v3 = int(input().split())
v = (v1,v2,v3)
u1,u2,u3 = (int(e) for e in input().split())
u = (u1,u2,u3)

V = v1 * v2 * v3
U = u1 * u2 * u3

Total_Vector = V * U
print(Total_Vector)

#=============== Figure 3.5 ===============

#Epic Program here
import math
x1,y1,x2,y2 =(int(e) for e in input("Type number : X1 Y1 X2 Y2 ").split())

C1 = x1,y1
C2 = x2,y2

Distance_2P = math.sqrt((x1 - x2) ** 2 - (y1-y2) ** 2)
print("Distance: ", Distance_2P)

#=============== Figure 3.6 ===============

weight = int(input("Input ur weight: "))
height = int(input("Input ur height: "))
real_height = height * (10 ** -2)
bmi = weight / ( real_height * real_height)

print("Your BMI is: ", round(bmi, 1))
#Alternate Solution
# math.floor(number*10)/10

#=============== Figure 3.7 ===============

product = str(input("Enter your Product: "))
price_before_tax = float(input("Enter your Price: "))

vat = price_before_tax * 0.07 # Calculate VAT
price_with_tax = vat + price_before_tax  # Adding VAT and price

discount = (price_with_tax >= 500) * (price_with_tax * 0.03) # Calculate Sales price
total_price = price_with_tax - discount # Subtracting price and discount

print(f"Product name {product} Total {round(total_price, 1)} Baht")

#=============== Figure 3.8 ===============

import math

H = int(input("Enter H: ")) # Height
C = int(input("Enter C: ")) # Step up
S = int(input("Enter S: ")) # Step down

days = ((H - C) / (C - S)) + 1
print(f"Total {int(math.ceil(days))} days")


#=============== Figure 3.9 ===============

import math

width = float(input("Width: "))
length = float(input("Length: "))

area = width * length
rai = math.ceil(area / 1600)

rai_money = rai * 1000

print("Area:", format(rai, ".1f"), "Rai")
print("Money:", format(rai_money, ".1f"), "Baht")


#=============== Figure 3.10 ===============

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

#===============================================

# Test 3-2

# Figure 1
ตอบ .split() เป็นคำสั่งที่ใช้แยกค่า str ให้อยู่ในรูปแบบ List คำสั่งนี้ใช้ได้ทั้งกับตัวแปรที่มีค่า str และ ใช้กับ input() ในเวลาที่อยากใส่ค่า input มากกว่า 1 ค่าในบรรทัดเดียว เช่น a,b,c = input().split() จะรับค่า str สามค่า(ดับเบิลคลิกเพื่อตอบ)

# Figure 2
v1,v2,v3,v4,v5 = (int(e) for e in input().split())
V = (v1,v2,v3,v4,v5)
u1,u2,u3,u4,u5 = (int(e) for e in input().split())
U = (u1,u2,u3,u4,u5)

TotalVector = ((v1+u1),(v2+u2),(v3+u3),(v4+u4),(v5+u5))
print("เวกเตอร์ V+U = ",(TotalVector))

# Figure 3
x1,x2,x3,x4,x5,x6,x7,x8,x9,x10 = (int(e) for e in input().split())
mean = (x1+x2+x3+x4+x5+x6+x7+x8+x9+x10)/10
print("Mean: ", mean)

# Figure 4
a,b,c = input("Input A,B as char and C as Int: ").split()
c = int(c)

test = a+b
print(test * c)

# Figure 5
name1,name2,name3,name4,name5,name6,name7,name8,name9,name10 = input("Input your name").split()
lname1,lname2,lname3,lname4,lname5,lname6,lname7,lname8,lname9,lname10 = input("Inout your surname").split()
score1,score2,score3,score4,score5,score6,score7,score8,score9,score10 = (int(e) for e in input("Input your score").split())

score_mean = (score1 + score2 + score3 + score4 + score5 + score6 + score7 + score8 + score9 + score10) / 10

print(f"""

Average score of ... Students

||========================================================||
||   Name               Surname              Score        ||
||========================================================||

  {name1:<15}       {lname1:<15}        {score1:<3}
  {name2:<15}       {lname2:<15}        {score2:<3}
  {name3:<15}       {lname3:<15}        {score3:<3}
  {name4:<15}       {lname4:<15}        {score4:<3}
  {name5:<15}       {lname5:<15}        {score5:<3}
  {name6:<15}       {lname6:<15}        {score6:<3}
  {name7:<15}       {lname7:<15}        {score7:<3}
  {name8:<15}       {lname8:<15}        {score8:<3}
  {name9:<15}       {lname9:<15}        {score9:<3}
  {name10:<15}      {lname10:<15}       {score10:<3}

===========================================================

  Score Average                         {score_mean:<5}

===========================================================

 """)
