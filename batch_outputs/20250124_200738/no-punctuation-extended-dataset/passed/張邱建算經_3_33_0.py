"""
今有負他錢轉利償之初去轉利得二倍還錢一百第二轉利得三倍還錢二百第三轉利得四倍還錢三百第四轉利得五倍還錢四百得畢凡轉利倍數皆通本錢今除初本有錢五千九百五十問初本幾何
術曰置初利還錢以三乘之併第二還錢又以四乘之併第三還錢又以五乘之併第四還錢訖併餘錢為實以四轉得利倍數相乘得一百二十減一餘為法實如法得一
答曰本錢 a
"""

#----- content starts here -----
"""
Suppose someone borrowed money and repaid it with compounded interest. 
Initially, the compounded interest doubled the principal, and they repaid 100. 
In the second round, the compounded interest tripled the principal, and they repaid 200. 
In the third round, the compounded interest quadrupled the principal, and they repaid 300. 
In the fourth round, the compounded interest quintupled the principal, and they repaid 400. 
After all repayments, the total compounded interest equals the original principal. 
Now, the total repayments amount to 5950. 
Question: What was the original principal?

The procedure says: Place the first repayment and multiply it by 3. Add the second repayment. Then multiply the sum by 4. Add the third repayment. Then multiply the sum by 5. Add the fourth repayment. Finally, add the remaining money to form the dividend. 
Take the product of the compounded interest multipliers (2, 3, 4, 5), subtract 1, and subtract the remainder to form the divisor. 
Divide the dividend by the divisor to obtain the original principal.

Answer: The original principal is *a*.
"""

# 初還錢
初還錢 = 100

# 第二還錢
第二還錢 = 200

# 第三還錢
第三還錢 = 300

# 第四還錢
第四還錢 = 400

# 餘錢
餘錢 = 5950

# 置初利還錢以三乘之
實 = 3 * 初還錢

# 併第二還錢
實 += 第二還錢

# 又以四乘之
實 *= 4

# 併第三還錢
實 += 第三還錢

# 又以五乘之
實 *= 5

# 併第四還錢
實 += 第四還錢

# 訖併餘錢為實
實 += 餘錢

# 以四轉得利倍數相乘得一百二十
法 = 2 * 3 * 4 * 5

# 減一餘為法
法 -= 1

# 實如法得一
a = Fraction(實, 法)#----- content ends here -----

"""
"""
