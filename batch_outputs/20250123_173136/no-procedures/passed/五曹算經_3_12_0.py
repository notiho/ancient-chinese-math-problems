"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
答曰： a人 。
"""

"""
Suppose there are 2 sheng of sauce to feed 5 people. There are 320 hu of sauce available.
Question: how many people can be fed?

Answer: *a* people.
"""

# 醬二升飼五人
醬_per_人 = Fraction(2, 5)  # 2 sheng feeds 5 people, so each person gets 2/5 sheng

# 醬三百二十斛
醬_total = 320  # in hu

# Convert hu to sheng (1 hu = 10 dou, 1 dou = 10 sheng, so 1 hu = 100 sheng)
醬_total_in_sheng = 醬_total * 100

# Calculate the total number of people that can be fed
a = 醬_total_in_sheng / 醬_per_人

# Simplify the result using Fraction
a = Fraction(a)

a  # Output the result
"""
"""
