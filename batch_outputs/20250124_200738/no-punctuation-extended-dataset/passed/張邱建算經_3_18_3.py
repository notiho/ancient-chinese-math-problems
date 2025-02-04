"""
今有差丁夫五百人合共重車一百一十三乘問各共重幾何
術曰置人數為實車數為法而一得四人共重又置一於上方命之實餘返減法訖以四加十一方一得五人共重法餘即四人共重車數實餘即五人共重車數
答曰 a乘 乘各 b人 共重 c乘 乘各 d人 共重
"""

#----- content starts here -----
"""
Suppose there are 500 laborers, divided into groups of 4 and 5 people, collectively pulling 113 carts.
Question: how many carts does each group pull, and how many laborers are assigned to each cart?

The procedure says:
1. Place the number of people as the dividend (實) and the number of carts as the divisor (法). Divide to find how many carts 4 people pull.
2. Place 1 above as a placeholder, and subtract the remainder from the divisor. After completing the subtraction, add 4 to 11, and divide again to find how many carts 5 people pull.
3. The divisor remainder corresponds to the carts pulled by groups of 4 people, and the dividend remainder corresponds to the carts pulled by groups of 5 people.

Answer: *a* carts, each with *b* people, collectively pulling *c* carts, each with *d* people, collectively pulling.
"""

# 差丁夫五百人
人數 = 500

# 重車一百一十三乘
車數 = 113

# 置人數為實，車數為法
實 = 人數
法 = 車數

# 一得四人共重
四人共重 = 實 // 法
餘 = 實 % 法

# 置一於上方，命之實餘返減法
實餘 = 餘
法餘 = 法 - 實餘

# 訖以四加十一方一得五人共重
五人共重 = (法餘 + 4 + 11) // 1

# 法餘即四人共重車數
四人共重車數 = 法餘

# 實餘即五人共重車數
五人共重車數 = 實餘

a = 四人共重車數
b = 4
c = 五人共重車數
d = 5#----- content ends here -----

"""
"""
