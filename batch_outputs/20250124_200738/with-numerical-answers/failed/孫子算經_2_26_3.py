"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a(=13)人 ，絹 b(=84)匹 。
"""

#----- content starts here -----
"""
Suppose someone stole silk from the treasury, but the exact amount lost is unknown.
It is only known that when the silk was divided among people in the grass, each person received 6 bolts, with 6 bolts left over.
If each person were to receive 7 bolts, there would not be enough silk by 7 bolts.
Question: how many people and how much silk are there?

The procedure says: First, place the number of people receiving 6 bolts in the top-right corner, and the surplus of 6 bolts in the bottom-right corner.
Then, place the number of people receiving 7 bolts in the top-left corner, and the deficit of 7 bolts in the bottom-left corner.
Multiply these diagonally, and add the results to obtain the total amount of silk.
Add the surplus and deficit to obtain the total number of people.

Answer: there are *a*(=13) people, and *b*(=84) bolts of silk.
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
右積 = 右上 * 右下
左積 = 左上 * 左下

# 并之為絹
b = 右積 + 左積 # 84

# 并盈不足為人
a = 右下 + 左下 # 13#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 84, Actual: 85"""
