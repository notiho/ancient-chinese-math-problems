"""
今有凡醬二升飼五人，有醬三百二十斛。問：人㡬何？
答曰： a人 。
"""

#----- content starts here -----
"""
Suppose there are 2 sheng of sauce to feed 5 people. There are 320 hu of sauce in total.
Question: how many people can be fed?

Answer: *a* people.
"""

# 醬二升飼五人
醬_二升 = 2
飼_五人 = 5

# 醬三百二十斛
醬_總量 = 320

# Convert hu to sheng (1 hu = 10 dou, 1 dou = 10 sheng, so 1 hu = 100 sheng)
醬_總量_升 = 醬_總量 * 100

# Sauce per person
醬_每人 = Fraction(醬_二升, 飼_五人)

# Total number of people that can be fed
a = 醬_總量_升 / 醬_每人

a = int(a)  # Since the number of people must be an integer
a#----- content ends here -----

"""
"""
