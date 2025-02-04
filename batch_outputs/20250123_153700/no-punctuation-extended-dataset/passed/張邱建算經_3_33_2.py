"""
今有負他錢轉利償之初去轉利得二倍還錢一百第二轉利得三倍還錢二百第三轉利得四倍還錢三百第四轉利得五倍還錢四百得畢凡轉利倍數皆通本錢今除初本有錢五千九百五十問初本幾何
術曰置初利還錢以三乘之併第二還錢又以四乘之併第三還錢又以五乘之併第四還錢訖併餘錢為實以四轉得利倍數相乘得一百二十減一餘為法實如法得一
答曰本錢 a
"""

"""
Suppose someone owes money and repays it with compounded interest. 
Initially, after the first interest accrual, the debt doubles, and they repay 100. 
After the second interest accrual, the debt triples, and they repay 200. 
After the third interest accrual, the debt quadruples, and they repay 300. 
After the fourth interest accrual, the debt quintuples, and they repay 400. 
After all repayments, the debt is cleared. 
The total compounded interest multiplier includes the principal.

Now, suppose the total repayments amount to 5950. 
Question: What was the initial principal?

The procedure says: Place the first repayment and multiply it by 3. Add the second repayment. Then multiply the result by 4. Add the third repayment. Then multiply the result by 5. Add the fourth repayment. Finally, add the remaining money to form the dividend. 
Take the product of the four compounded interest multipliers (2, 3, 4, 5), which is 120. Subtract 1 to form the divisor. 
Divide the dividend by the divisor to obtain the initial principal.

Answer: The initial principal is *a*.
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

# 置初利還錢，以三乘之
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

# 訖併餘錢，為實
實 += 餘錢

# 以四轉得利倍數相乘，得一百二十
法 = 2 * 3 * 4 * 5

# 減一餘，為法
法 -= 1

# 實如法得一
a = Fraction(實, 法)
"""
"""
