"""
今有程耕一人一日發七畝一人一日耕三畝一人一日耰種五畝今令一人一日自發耕耰種之問治田幾何
術曰置發耕耰畝數令互乘人數并以為法畝數相乘為實實如法得一畝
荅曰 a畝 
"""

#----- content starts here -----
"""
Suppose there is a task where one person in one day can clear 7 mu, one person in one day can plow 3 mu, and one person in one day can sow 5 mu.
Now, let one person in one day clear, plow, and sow by themselves.
Question: how much land can they manage?

The procedure says: Place the mu numbers for clearing, plowing, and sowing.
Let them multiply with each other, and sum the results to form the divisor.
Multiply the mu numbers with each other to form the dividend.
Divide the dividend by the divisor to obtain the number of mu.

The answer says: *a* mu.
"""

# 一人一日發七畝
發畝 = 7

# 一人一日耕三畝
耕畝 = 3

# 一人一日耰種五畝
耰畝 = 5

# 置發耕耰畝數，令互乘人數并以為法
法 = (發畝 * 耕畝) + (發畝 * 耰畝) + (耕畝 * 耰畝)

# 畝數相乘為實
實 = 發畝 * 耕畝 * 耰畝

# 實如法得一畝
a = Fraction(實, 法)#----- content ends here -----

"""
"""
