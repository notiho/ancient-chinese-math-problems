"""
今有二人三日錮銅得一斤九兩五銖今一月日錮銅得九千八百七十六斤五兩四銖少半銖問人功幾何
術曰置二人三日所得錮銅斤兩銖通之作銖以二人三日相乘除之為一人一日之銖二十四而一還以一人一日所得兩銖通分内子復以一月三日乘一人積分所得復以銖分母三通之為法又以今錮銅斤兩通為銖以少半銖者三分之一以三通内一以六乘之為實實如法而一得人數不盡約之為分
答曰 a人
"""

"""
Suppose there are two people working for three days, smelting copper, and they obtain 1 jin, 9 liang, and 5 zhu.
Now, in one month and three days (33 days total), they smelt 9876 jin, 5 liang, and 4 zhu, minus half a zhu.
Question: how many people were working?

The procedure says:
1. Combine the jin, liang, and zhu obtained by two people in three days into zhu.
2. Divide this total zhu by the product of two people and three days to find the zhu produced by one person in one day.
3. Convert one person's daily production back into liang and zhu.
4. Multiply one person's daily production by the total number of days (33 days) to find the total production by one person.
5. Convert the total production by one person into a fraction of zhu.
6. Use the total copper smelted (9876 jin, 5 liang, 4 zhu minus half a zhu) and convert it into zhu.
7. Subtract half a zhu (1/2 zhu) from the total.
8. Multiply the remaining total by 6 to get the dividend.
9. Divide the dividend by the divisor (from step 5) to find the number of people.
10. If the result is not exact, simplify it into a fraction.

Answer: *a* people.
"""

# Constants for unit conversions
jin_to_liang = 16  # 1 jin = 16 liang
liang_to_zhu = 24  # 1 liang = 24 zhu

# Step 1: Combine 2 people, 3 days' production into zhu
jin = 1
liang = 9
zhu = 5
total_zhu_2_people_3_days = (jin * jin_to_liang * liang_to_zhu) + (liang * liang_to_zhu) + zhu

# Step 2: Divide by 2 people * 3 days to get 1 person's daily production in zhu
one_person_one_day_zhu = Fraction(total_zhu_2_people_3_days, 2 * 3)

# Step 3: Convert one person's daily production back into liang and zhu
# (not needed for further calculations, but shown for clarity)
one_person_one_day_liang = one_person_one_day_zhu // liang_to_zhu
one_person_one_day_remaining_zhu = one_person_one_day_zhu % liang_to_zhu

# Step 4: Multiply by 33 days to get total production by one person in zhu
total_days = 33
one_person_total_zhu = one_person_one_day_zhu * total_days

# Step 5: Convert total production by one person into a fraction of zhu
divisor = one_person_total_zhu

# Step 6: Convert total copper smelted (9876 jin, 5 liang, 4 zhu minus half a zhu) into zhu
jin = 9876
liang = 5
zhu = 4
total_zhu_smelted = (jin * jin_to_liang * liang_to_zhu) + (liang * liang_to_zhu) + zhu

# Step 7: Subtract half a zhu (1/2 zhu) from the total
total_zhu_smelted -= Fraction(1, 2)

# Step 8: Multiply the remaining total by 6 to get the dividend
dividend = total_zhu_smelted * 6

# Step 9: Divide the dividend by the divisor to find the number of people
a = Fraction(dividend, divisor)

# Final answer
a
"""
Variable 'a' has wrong value. Expected: 455101/363, Actual: 9102018/1331"""
