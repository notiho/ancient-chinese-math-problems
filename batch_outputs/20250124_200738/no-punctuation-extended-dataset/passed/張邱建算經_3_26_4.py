"""
今有廩人人日食米六升今三十五日食米七千四百九十二斛八㪷問人幾何
術曰置米數為實以六升乘三十五日為法實如法得一
答曰 a人
"""

#----- content starts here -----
"""
Suppose there is a granary, and each person eats 6 sheng of rice per day.
Now, in 35 days, 7492 hu and 8 dou of rice are consumed.
Question: how many people are there?

The procedure says: Place the amount of rice as the dividend.
Multiply 6 sheng by 35 days to get the divisor.
Divide the dividend by the divisor to obtain the number of people.

Answer: *a* people.
"""

# 每人每天食米六升
每日每人食米 = 6  # 升

# 三十五日
日數 = 35

# 七千四百九十二斛八㪷
# Convert the total rice into sheng
# 1 斛 = 10 斗, 1 斗 = 10 升
總米 = (7492 * 10 * 10) + (8 * 10)  # Convert to 升

# 置米數為實
實 = 總米

# 以六升乘三十五日為法
法 = 每日每人食米 * 日數

# 實如法得一
a = Fraction(實, 法)  # 人數#----- content ends here -----

"""
"""
