# แบบฝึกหัด 2.1
# 2.1 Figure 1
((3/4)+(1/4)+(7/4))
# 2.1 Figure 2
(1+6*8-7)
# 2.1 Figure 3
(5*6+7*8-(2/5))
# 2.1 Figure 4
(7*3+8*4-(3/7))
# 2.1 Figure 5
(9*4+6*12-(4/3))

# แบบฝึกหัด 2.2
# 2.2 Figure 1
(3*(4+1-2*5))
# 2.2 Figure 2
((1+2+3)/(4+5+6))
# 2.2 Figure 3
(7* ((5+6) / (7+(7/8))))

# แบบฝึกหัด 2.3
# 2.3 Figure 1
3**(5+3/4)
# 2.3 Figure 2
(7+3*4)**(1/2)
# 2.3 Figure 3
((5+6**2.5)/((3.5)**(1/2)))+3**2


# แบบฝึกหัด 2.4

3+97//2**3%8
# ** คือเครื่องหมายยกกำลัง
# // คือหารโดยปัดเศษลงเป็นจำนวนเต็มที่ใกล้ที่สุด
# เอา 3 บวกกับ 97
# นำ  2 ยกกำลัง3 และหารเอาเศษ 8
# นำ ทั้งสองค่ามา หารปัดเศษ

12//3/2+2**3**2
# นำ 12 หารปัดเศษกับ 3 ส่วน 2
# นำ มาบวกกับ 2 กำลัง 3 กำลัง 2

3+97//8%8
# Note: % is Modulus (return the remainder of dividing)
# นำ  97 หารปัดเศษ กับ 8
# และมาหารหาเศษ กับ 8
# บวก 3

12//3/2+2**9
# 12 divided by 3 and rounding down to the nearly number then dividing with 2
# Raising 2 to the power of 9

12//3/2+512
# 12 dividing by 3 and rounding down.
# Dividing by 2 then plus 512

3+12%8
# 12 Divided by 8 and find the remainder of its result
# And Plus 3

8//3/3%5
# 8 divided by 3 and rounding to the nearest whole number
# Divided by 3
# And Get Remainder of dividing by 5 (Modulus)

2*10//256%4
# 2 times 10
# Dividing 256 and rounding down to the nearest whole number
# Dividing by 4 and get remainder

1.23*10**59
# 10 raise to the power of 59
# multiply by 1.23

7+53//18%6
# 53 divided by 18 and rounding down
# Divided by 6 and return remainder value
# Plus 7

# Test2(10 คะแนน)

# กำหนดจำนวนเงิน
cash = 512
num1 = cash

# คำนวณจำนวนเหรียญ
coin_20 = num1 // 20
num1 = num1 % 20

coin_10 = num1 // 10
num1 = num1 % 10

coin_5 = num1 // 5
num1 = num1 % 5

coin_1 = num1 // 1

# แสดงจำนวนเหรียญแต่ละชนิด
print(f"สำหรับจำนวนเงิน {cash} บาท:")
print("เหรียญ 20 บาท:", coin_20, "เหรียญ")
print("เหรียญ 10 บาท:", coin_10, "เหรียญ")
print("เหรียญ 5 บาท:", coin_5, "เหรียญ")
print("เหรียญ 1 บาท:", coin_1, "เหรียญ")

print()

# กำหนดจำนวนเงิน
cash = 1024
num1 = cash

# คำนวณจำนวนเหรียญ
coin_20 = num1 // 20
num1 = num1 % 20

coin_10 = num1 // 10
num1 = num1 % 10

coin_5 = num1 // 5
num1 = num1 % 5

coin_1 = num1 // 1

# แสดงจำนวนเหรียญแต่ละชนิด
print(f"สำหรับจำนวนเงิน {cash} บาท:")
print("เหรียญ 20 บาท:", coin_20, "เหรียญ")
print("เหรียญ 10 บาท:", coin_10, "เหรียญ")
print("เหรียญ 5 บาท:", coin_5, "เหรียญ")
print("เหรียญ 1 บาท:", coin_1, "เหรียญ")

print()

# กำหนดจำนวนเงิน
cash = 4096
num1 = cash

# คำนวณจำนวนเหรียญ
coin_20 = num1 // 20
num1 = num1 % 20

coin_10 = num1 // 10
num1 = num1 % 10

coin_5 = num1 // 5
num1 = num1 % 5

coin_1 = num1 // 1

# แสดงจำนวนเหรียญแต่ละชนิด
print(f"สำหรับจำนวนเงิน {cash} บาท:")
print("เหรียญ 20 บาท:", coin_20, "เหรียญ")
print("เหรียญ 10 บาท:", coin_10, "เหรียญ")
print("เหรียญ 5 บาท:", coin_5, "เหรียญ")
print("เหรียญ 1 บาท:", coin_1, "เหรียญ")

print()

# กำหนดจำนวนเงิน
cash = 5709
num1 = cash

# คำนวณจำนวนเหรียญ
coin_20 = num1 // 20
num1 = num1 % 20

coin_10 = num1 // 10
num1 = num1 % 10

coin_5 = num1 // 5
num1 = num1 % 5

coin_1 = num1 // 1

# แสดงจำนวนเหรียญแต่ละชนิด
print(f"สำหรับจำนวนเงิน {cash} บาท:")
print("เหรียญ 20 บาท:", coin_20, "เหรียญ")
print("เหรียญ 10 บาท:", coin_10, "เหรียญ")
print("เหรียญ 5 บาท:", coin_5, "เหรียญ")
print("เหรียญ 1 บาท:", coin_1, "เหรียญ")

