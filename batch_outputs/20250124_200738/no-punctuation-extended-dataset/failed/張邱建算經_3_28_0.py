"""
今有二人三日錮銅得一斤九兩五銖今一月日錮銅得九千八百七十六斤五兩四銖少半銖問人功幾何
術曰置二人三日所得錮銅斤兩銖通之作銖以二人三日相乘除之為一人一日之銖二十四而一還以一人一日所得兩銖通分内子復以一月三日乘一人積分所得復以銖分母三通之為法又以今錮銅斤兩通為銖以少半銖者三分之一以三通内一以六乘之為實實如法而一得人數不盡約之為分
答曰 a人
"""

#----- content starts here -----
"""
Suppose two people over three days smelt copper and obtain 1 jin, 9 liang, and 5 zhu. 
Now, in one month (30 days), the total smelted copper is 9876 jin, 5 liang, and 4 zhu, minus half a zhu.
Question: how many people worked?

The procedure says: Place the copper smelted by two people over three days, converting jin, liang, and zhu into zhu. 
Divide it by the product of two people and three days to find the zhu smelted by one person in one day.
Convert this back into liang and zhu for clarity.
Then, multiply the one-person one-day zhu by 30 days to find the total zhu smelted by one person in one month.
Convert the divisor (法) by multiplying the denominator of zhu by 3.
Now, convert the total copper smelted in one month into zhu, including the adjustment for "minus half a zhu" (subtracting 1/2 zhu).
Multiply this by 6 to form the dividend (實).
Divide the dividend by the divisor (法) to find the number of people.
If the result is not exact, simplify it into a fraction.

Answer: *a* people.
"""

from fractions import Fraction

# Conversion factors
jin_to_liang = 16  # 1 jin = 16 liang
liang_to_zhu = 24  # 1 liang = 24 zhu

# Data for two people over three days
jin_2_people_3_days = 1
liang_2_people_3_days = 9
zhu_2_people_3_days = 5

# Convert to zhu
total_zhu_2_people_3_days = (
    jin_2_people_3_days * jin_to_liang * liang_to_zhu +
    liang_2_people_3_days * liang_to_zhu +
    zhu_2_people_3_days
)

# Divide by (2 people * 3 days) to find one person one day zhu
one_person_one_day_zhu = Fraction(total_zhu_2_people_3_days, 2 * 3)

# Data for total copper smelted in one month (30 days)
jin_total = 9876
liang_total = 5
zhu_total = 4
half_zhu_adjustment = Fraction(1, 2)  # Subtract half a zhu

# Convert total copper smelted to zhu, including adjustment
total_zhu_one_month = (
    jin_total * jin_to_liang * liang_to_zhu +
    liang_total * liang_to_zhu +
    zhu_total
) - half_zhu_adjustment

# Calculate the divisor (法)
法 = Fraction(one_person_one_day_zhu * 30, 1)

# Calculate the dividend (實)
實 = total_zhu_one_month * 6

# Calculate the number of people
a = 實 / 法

# Simplify the result
a = a.limit_denominator()

a  # Number of people#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 455101/363, Actual: 4551009/605"""
