"""
今有差丁夫五百人合共重車一百一十三乘問各共重幾何
術曰置人數為實車數為法而一得四人共重又置一於上方命之實餘返減法訖以四加十一方一得五人共重法餘即四人共重車數實餘即五人共重車數
答曰 a乘 乘各 b人 共重 c乘 乘各 d人 共重
"""

"""
Suppose there are 500 laborers of varying strength, collectively responsible for 113 carts.
Question: how many carts are shared by each group of laborers?

The procedure says:
- Place the number of people as the dividend and the number of carts as the divisor. Divide, obtaining the number of carts shared by 4 people.
- Then place 1 at the top, and assign it as the dividend. Subtract the remainder from the divisor repeatedly until finished.
- Add 4 to 11, and divide again, obtaining the number of carts shared by 5 people.
- The remainder from the divisor corresponds to the carts shared by 4 people.
- The remainder from the dividend corresponds to the carts shared by 5 people.

Answer: *a* carts, with *b* people per cart, shared by 4-person groups.
*c* carts, with *d* people per cart, shared by 5-person groups.
"""

# 丁夫五百人
人數 = 500

# 重車一百一十三乘
車數 = 113

# 置人數為實，車數為法，而一得四人共重
實 = 人數
法 = 車數
四人共重 = 实 // 法
餘 = 实 % 法

# 置一於上方，命之實，餘返減法訖
實 = 1
法 = 餘
while 實 >= 法:
    實 -= 法

# 以四加十一，方一得五人共重
法 += 4 + 11
五人共重 = 实 // 法
餘 = 实 % 法

# 法餘即四人共重車數
a = 四人共重
b = 4

# 車數實餘即五人共重車數
c = 五人共重
d = 5
"""
Code error: name '实' is not defined"""
