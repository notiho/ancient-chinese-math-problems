"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

#----- content starts here -----
"""
Suppose someone stole silk from the storehouse, but the exact amount of silk lost is unknown.
It is only known that when dividing the silk among people in the grass, each person gets 6 bolts, with 6 bolts left over.
If each person gets 7 bolts, there are not enough bolts for 7 bolts per person.
Question: how many people and how many bolts of silk are there?

The procedure says: First, place the number of bolts per person (6) in the top right, and the remainder (6) in the bottom right.
Then, place the number of bolts per person (7) in the top left, and the shortage (7) in the bottom left.
Multiply these pairs diagonally, add the results to get the total number of bolts of silk.
Add the remainder and shortage to get the total number of people.

Answer: there are *a* people, and *b* bolts of silk.
"""

# 人得六匹于右上，盈六匹于右下
右上 = 6
右下 = 6

# 人得七匹于左上，不足七匹于左下
左上 = 7
左下 = 7

# 維乘之所得
右積 = 右上 * 右下
左積 = 左上 * 左下

# 并之為絹
絹 = 右積 + 左積

# 并盈不足為人
人 = 右下 + 左下

# 答案
a = 人
b = 絹#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 84, Actual: 85"""
