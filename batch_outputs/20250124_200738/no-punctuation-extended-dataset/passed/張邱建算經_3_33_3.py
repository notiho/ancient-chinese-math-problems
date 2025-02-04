"""
今有負他錢轉利償之初去轉利得二倍還錢一百第二轉利得三倍還錢二百第三轉利得四倍還錢三百第四轉利得五倍還錢四百得畢凡轉利倍數皆通本錢今除初本有錢五千九百五十問初本幾何
術曰置初利還錢以三乘之併第二還錢又以四乘之併第三還錢又以五乘之併第四還錢訖併餘錢為實以四轉得利倍數相乘得一百二十減一餘為法實如法得一
答曰本錢 a
"""

#----- content starts here -----
"""
Suppose someone owes money and repays it with compounded interest. Initially, the compounded interest doubles, and they repay 100. In the second period, the compounded interest triples, and they repay 200. In the third period, the compounded interest quadruples, and they repay 300. In the fourth period, the compounded interest quintuples, and they repay 400. After all repayments, the total compounded interest equals the principal.

Now, suppose the remaining money after all repayments is 5950. Question: What is the initial principal?

The procedure says: Place the first repayment and multiply it by 3. Add the second repayment. Then multiply it by 4. Add the third repayment. Then multiply it by 5. Add the fourth repayment. Finally, add the remaining money, obtaining the dividend. Multiply the four compounded interest multipliers (2, 3, 4, 5) together, obtaining 120. Subtract 1, leaving 119 as the divisor. Divide the dividend by the divisor to obtain the principal.

Answer: The principal is *a*.
"""

# 初去轉利得二倍還錢一百
第一還錢 = 100

# 第二轉利得三倍還錢二百
第二還錢 = 200

# 第三轉利得四倍還錢三百
第三還錢 = 300

# 第四轉利得五倍還錢四百
第四還錢 = 400

# 餘錢
餘錢 = 5950

# 置初利還錢以三乘之，併第二還錢
實 = 3 * 第一還錢 + 第二還錢

# 又以四乘之，併第三還錢
實 = 4 * 實 + 第三還錢

# 又以五乘之，併第四還錢
實 = 5 * 實 + 第四還錢

# 訖併餘錢為實
實 += 餘錢

# 以四轉得利倍數相乘得一百二十，減一餘為法
法 = (2 * 3 * 4 * 5) - 1

# 實如法得一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
