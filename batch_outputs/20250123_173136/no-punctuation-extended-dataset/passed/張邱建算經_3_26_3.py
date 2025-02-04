"""
今有廩人人日食米六升今三十五日食米七千四百九十二斛八㪷問人幾何
術曰置米數為實以六升乘三十五日為法實如法得一
答曰 a人
"""

"""
Suppose there is a granary where each person consumes 6 sheng of rice per day.
Now, in 35 days, 7492 hu and 8 dou of rice are consumed.
Question: how many people are there?

The procedure says: Place the amount of rice as the dividend.
Multiply 6 sheng by 35 days to obtain the divisor.
Divide the dividend by the divisor to obtain the number of people.

Answer: *a* people.
"""

# 每人每日食米六升
每日食米 = 6  # 升

# 三十五日
日數 = 35

# 35日食米七千四百九十二斛八㪷
# Convert 7492 hu and 8 dou to sheng
# 1 hu = 10 dou, 1 dou = 10 sheng
總米數 = (7492 * 10 * 10) + (8 * 10)  # Convert to 升

# 置米數為實
實 = 總米數

# 以六升乘三十五日為法
法 = 每日食米 * 日數

# 實如法得一
a = Fraction(實, 法)  # 人數
"""
"""
