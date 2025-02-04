"""
今有差丁夫五百人合共重車一百一十三乘問各共重幾何
術曰置人數為實車數為法而一得四人共重又置一於上方命之實餘返減法訖以四加十一方一得五人共重法餘即四人共重車數實餘即五人共重車數
答曰 a乘 乘各 b人 共重 c乘 乘各 d人 共重
"""

"""
Suppose there are 500 laborers, divided into groups of 4 and 5 people, who together load 113 carts.
Question: how many carts are loaded by each group, and how many people are in each cart?

The procedure says: Place the number of people as the dividend and the number of carts as the divisor.
Divide, obtaining the number of carts loaded by 4 people.
Then, place 1 at the top and assign it as the dividend.
Subtract the remainder from the divisor until finished.
Add 4 to 11, and divide, obtaining the number of carts loaded by 5 people.
The divisor remainder corresponds to the carts loaded by 4 people, and the dividend remainder corresponds to the carts loaded by 5 people.

Answer: *a* carts, each with *b* people, loaded by 4-person groups; *c* carts, each with *d* people, loaded by 5-person groups.
"""

# 丁夫五百人
總人數 = 500

# 重車一百一十三乘
總車數 = 113

# 置人數為實，車數為法
實 = 總人數
法 = 總車數

# 一得四人共重
四人共重車數 = Fraction(實, 法)

# 置一於上方命之實
實餘 = 總人數 % 總車數

# 餘返減法訖
法餘 = 總車數 - 實餘

# 以四加十一方一得五人共重
五人共重車數 = Fraction(法餘 + 4 + 11, 1)

# 法餘即四人共重車數
a = 四人共重車數
b = 4

# 實餘即五人共重車數
c = 五人共重車數
d = 5
"""
Variable 'a' has wrong value. Expected: 65, Actual: 500/113
Variable 'c' has wrong value. Expected: 48, Actual: 80"""
