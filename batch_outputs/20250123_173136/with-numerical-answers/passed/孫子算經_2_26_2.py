"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a(=13)人 ，絹 b(=84)匹 。
"""

"""
Suppose someone has stolen silk from the storehouse, but the amount lost is unknown.
It is only heard that when dividing the silk among people in the grass, each person gets 6 bolts, with 6 bolts left over.
If each person gets 7 bolts, there are not enough bolts by 7.
Question: how many people and how many bolts of silk are there?

The procedure says: First, place the number of people getting 6 bolts in the upper right, and the surplus of 6 bolts in the lower right.
Then, place the number of people getting 7 bolts in the upper left, and the deficit of 7 bolts in the lower left.
Multiply these diagonally, and add the results to obtain the total number of bolts.
Add the surplus and deficit to obtain the total number of people.

Answer: the thieves are *a*(=13) people, and the silk is *b*(=84) bolts.
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
b = 右乘 + 左乘 # 84

# 并盈不足為人
a = 右下 + 左下 # 13
"""
"""
