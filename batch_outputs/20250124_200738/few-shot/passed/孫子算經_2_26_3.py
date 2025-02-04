"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

#----- content starts here -----
"""
Suppose someone stole silk from the treasury, but the amount lost is unknown.
It is only heard that when dividing the silk among people in the grass, each person gets 6 bolts, with 6 bolts left over.
If each person gets 7 bolts, there are not enough bolts for 7 bolts each.
Question: how many people and how many bolts of silk are there?

The procedure says: First, place the "each person gets 6 bolts" on the top right, and the "6 bolts left over" on the bottom right.
Then, place the "each person gets 7 bolts" on the top left, and the "not enough for 7 bolts" on the bottom left.
Multiply these diagonally, add the results to obtain the total silk.
Add the surplus and deficit to obtain the total number of people.

Answer: there are *a* thieves, and *b* bolts of silk.
"""

# 人得六匹于右上
右上 = 6

# 盈六匹于右下
右下 = 6

# 人得七匹于左上
左上 = 7

# 不足七匹于左下
左下 = 7

# 維乘之所得
右乘 = 右上 * 左下
左乘 = 左上 * 右下

# 并之為絹
絹 = 右乘 + 左乘

# 并盈不足為人
人 = 右下 + 左下

a = 人
b = 絹#----- content ends here -----

"""
"""
