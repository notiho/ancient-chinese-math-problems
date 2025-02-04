"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
答曰： a人 。
"""

#----- content starts here -----
"""
Suppose there are 2 sheng of sauce to feed 5 people. Now there are 320 hu of sauce.
Question: how many people can be fed?

Answer: *a* people.
"""

# 醬二升飼五人
醬_per_person = Fraction(2, 5)  # 2 sheng feeds 5 people, so each person gets 2/5 sheng

# 醬三百二十斛
醬_total = 320  # 320 hu

# Convert hu to sheng (1 hu = 10 dou, 1 dou = 10 sheng, so 1 hu = 100 sheng)
醬_total_in_sheng = 320 * 100

# Calculate the number of people that can be fed
a = 醬_total_in_sheng / 醬_per_person

# Simplify the result
a = Fraction(a)

a#----- content ends here -----

"""
"""
