"""
今有二人三日錮銅得一斤九兩五銖今一月日錮銅得九千八百七十六斤五兩四銖少半銖問人功幾何
術曰置二人三日所得錮銅斤兩銖通之作銖以二人三日相乘除之為一人一日之銖二十四而一還以一人一日所得兩銖通分内子復以一月三日乘一人積分所得復以銖分母三通之為法又以今錮銅斤兩通為銖以少半銖者三分之一以三通内一以六乘之為實實如法而一得人數不盡約之為分
答曰 a人
"""

#----- content starts here -----
"""
Suppose there are two people working for three days, smelting copper and obtaining 1 jin, 9 liang, and 5 zhu. 
Now, in one month and three days (33 days total), they smelt 9876 jin, 5 liang, and 4 zhu, minus half a zhu. 
Question: how many people worked?

The procedure says: Place the amount of copper smelted by two people in three days (in jin, liang, and zhu), convert it all into zhu, and divide it by the product of two people and three days. 
This gives the amount of zhu smelted by one person in one day. 
Convert this back into liang and zhu for clarity. 
Then, multiply the one-person-one-day amount by 33 days to get the total amount smelted by one person in 33 days. 
Convert this into zhu and use it as the divisor. 

Next, convert the total amount of copper smelted in 33 days (9876 jin, 5 liang, 4 zhu minus half a zhu) into zhu. 
For the "minus half a zhu," subtract 1/2 zhu. 
Multiply this by 6 to get the dividend. 
Divide the dividend by the divisor to get the number of people. 
If the result is not exact, simplify it into a fraction.

Answer: *a* people.
"""

# Constants for unit conversions
jin_to_liang = 16  # 1 jin = 16 liang
liang_to_zhu = 24  # 1 liang = 24 zhu

# Data for two people in three days
jin_3days = 1
liang_3days = 9
zhu_3days = 5

# Convert the amount smelted in three days to zhu
total_zhu_3days = jin_3days * jin_to_liang * liang_to_zhu + liang_3days * liang_to_zhu + zhu_3days

# Divide by the product of two people and three days to get one person's one-day output in zhu
one_person_one_day_zhu = Fraction(total_zhu_3days, 2 * 3)

# Total days worked in one month and three days
total_days = 33

# Multiply one person's one-day output by total days to get one person's total output in zhu for 33 days
one_person_total_zhu = one_person_one_day_zhu * total_days

# Data for total copper smelted in 33 days
jin_total = 9876
liang_total = 5
zhu_total = 4
half_zhu = Fraction(1, 2)

# Convert the total amount smelted to zhu, accounting for the "minus half a zhu"
total_zhu = jin_total * jin_to_liang * liang_to_zhu + liang_total * liang_to_zhu + zhu_total - half_zhu

# Multiply by 6 to get the dividend
dividend = total_zhu * 6

# Use one person's total output in zhu as the divisor
divisor = one_person_total_zhu

# Divide to find the number of people
a = Fraction(dividend, divisor)  # Simplify the result into a fraction if necessary#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 455101/363, Actual: 9102018/1331"""
