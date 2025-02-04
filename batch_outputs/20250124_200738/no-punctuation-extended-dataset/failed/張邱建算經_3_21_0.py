"""
今有雀一隻重一兩九銖燕一隻重一兩五銖有雀燕二十五隻併重二斤一十三銖問燕雀各幾何
術曰置假令雀一十五隻燕十隻盈四銖於右行又置假令雀十二隻燕十三隻不足八銖於左行以盈不足維乘之併以為實併盈不足為法實如法得一
答曰雀 a隻 燕 b隻
"""

#----- content starts here -----
"""
Suppose there is one sparrow weighing 1 liang and 9 zhu, and one swallow weighing 1 liang and 5 zhu.
There are 25 sparrows and swallows in total, and their combined weight is 2 jin and 13 zhu.
Question: how many sparrows and swallows are there respectively?

The procedure says: 
1. Assume (假令) there are 15 sparrows and 10 swallows. Calculate the excess (盈) of 4 zhu on the right side.
2. Assume (假令) there are 12 sparrows and 13 swallows. Calculate the deficiency (不足) of 8 zhu on the left side.
3. Multiply the excess and deficiency with each other, and add them together to form the dividend (實).
4. Add the excess and deficiency together to form the divisor (法).
5. Divide the dividend by the divisor to obtain the number of sparrows (雀).
6. Subtract the number of sparrows from the total to obtain the number of swallows (燕).

Answer: there are *a* sparrows and *b* swallows.
"""

# 雀一隻重一兩九銖
雀重 = 1 * 16 + 9  # Convert to zhu (1 liang = 16 zhu)

# 燕一隻重一兩五銖
燕重 = 1 * 16 + 5  # Convert to zhu

# 雀燕二十五隻
總隻數 = 25

# 併重二斤一十三銖
總重 = 2 * 16 * 16 + 13  # Convert to zhu (1 jin = 16 liang, 1 liang = 16 zhu)

# 假令雀十五隻燕十隻
假雀1 = 15
假燕1 = 10
假重1 = 假雀1 * 雀重 + 假燕1 * 燕重
盈 = 假重1 - 総重  # 盈 (excess) = calculated weight - total weight

# 假令雀十二隻燕十三隻
假雀2 = 12
假燕2 = 13
假重2 = 假雀2 * 雀重 + 假燕2 * 燕重
不足 = 總重 - 假重2  # 不足 (deficiency) = total weight - calculated weight

# 以盈不足維乘之併以為實
實 = 盈 * 不足

# 併盈不足為法
法 = 盈 + 不足

# 實如法得一 (雀的數量)
a = Fraction(實, 法)

# 燕的數量
b = 總隻數 - a#----- content ends here -----

"""
Code error: name '総重' is not defined"""
