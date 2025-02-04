"""
今有負他錢轉利償之初去轉利得二倍還錢一百第二轉利得三倍還錢二百第三轉利得四倍還錢三百第四轉利得五倍還錢四百得畢凡轉利倍數皆通本錢今除初本有錢五千九百五十問初本幾何
術曰置初利還錢以三乘之併第二還錢又以四乘之併第三還錢又以五乘之併第四還錢訖併餘錢為實以四轉得利倍數相乘得一百二十減一餘為法實如法得一
答曰本錢 a
"""

"""
Suppose someone owes money and repays it with compounded interest. 
Initially, the compounded interest doubles, and they repay 100. 
In the second round, the compounded interest triples, and they repay 200. 
In the third round, the compounded interest quadruples, and they repay 300. 
In the fourth round, the compounded interest quintuples, and they repay 400. 
After all repayments, the total compounded interest equals the principal.

Now, the remaining money after all repayments is 5950. 
Question: What was the initial principal?

The procedure says: Place the initial repayment with interest and multiply it by 3. Add the second repayment. 
Then multiply by 4 and add the third repayment. 
Then multiply by 5 and add the fourth repayment. 
Finally, add the remaining money, obtaining the dividend. 
Multiply the four compounded interest multipliers (2, 3, 4, 5) together, obtaining 120. Subtract 1, giving the divisor. 
Divide the dividend by the divisor to obtain the principal.

Answer: The principal is *a*.
"""

# 初去轉利得二倍還錢一百
初還錢 = 100
初倍數 = 2

# 第二轉利得三倍還錢二百
第二還錢 = 200
第二倍數 = 3

# 第三轉利得四倍還錢三百
第三還錢 = 300
第三倍數 = 4

# 第四轉利得五倍還錢四百
第四還錢 = 400
第四倍數 = 5

# 餘錢
餘錢 = 5950

# 置初利還錢以三乘之併第二還錢
實 = 3 * 初還錢 + 第二還錢

# 又以四乘之併第三還錢
實 = 4 * 實 + 第三還錢

# 又以五乘之併第四還錢
實 = 5 * 實 + 第四還錢

# 訖併餘錢為實
實 += 餘錢

# 以四轉得利倍數相乘得一百二十
法 = 初倍數 * 第二倍數 * 第三倍數 * 第四倍數

# 減一餘為法
法 -= 1

# 實如法得一
a = Fraction(實, 法)
"""
"""
