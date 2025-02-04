"""
今有共買犬人出五不足九十人出五十適足問人數犬價各幾何
盈適足不足適足術曰以盈及不足之數為實置所出率以少減多餘為法實如法得一人其求物價者以適足乘人數得物價
荅曰 a人 犬價 b 
"""

#----- content starts here -----
"""
Suppose there is a group of people buying a dog. 
When each person contributes 5, they are short by 90. 
When each person contributes 50, they have exactly enough.
Question: how many people are there, and what is the price of the dog?

The procedure for "excess and exact, deficit and exact" says:
Take the numbers of excess and deficit as the dividend.
Place the contribution rates, subtracting the smaller from the larger, and take the remainder as the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the dog, multiply the exact contribution by the number of people.

Answer: *a* people, and the price of the dog is *b*.
"""

# 盈及不足之數為實
盈 = 0  # Excess amount when contributing 50 (exactly enough)
不足 = 90  # Deficit amount when contributing 5
實 = 盈 + 不足

# 置所出率，以少減多餘為法
少 = 5  # Contribution rate when short
多 = 50  # Contribution rate when exact
法 = 多 - 少

# 實如法得一人
a = Fraction(實, 法)

# 其求物價者，以適足乘人數得物價
適足 = 多  # Exact contribution rate
b = 適足 * a#----- content ends here -----

"""
"""
