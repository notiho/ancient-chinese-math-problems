"""
今有人盜庫絹不知所失幾何但聞草中分絹人得六匹盈六匹人得七匹不足七匹問人絹各幾何
術曰先置人得六匹于右上盈六匹于右下後置人得七匹于左上不足七匹于左下維乘之所得并之為絹并盈不足為人
答曰賊 a人 絹 b匹 
"""

#----- content starts here -----
"""
Suppose someone stole silk from the storehouse, but the exact amount of silk lost is unknown.
It is only heard that when dividing the silk in the grass, each person gets 6 bolts, with 6 bolts left over.
Alternatively, each person gets 7 bolts, but 7 bolts are short.
Question: how many people and how much silk?

The procedure says: First, place "each person gets 6 bolts" in the top right, and "6 bolts left over" in the bottom right.
Then, place "each person gets 7 bolts" in the top left, and "7 bolts short" in the bottom left.
Cross-multiply these values, add the results to obtain the total silk.
Add the surplus and deficit to obtain the total number of people.

Answer: The thief is *a* people, and the silk is *b* bolts.
"""

# 人得六匹于右上
右上 = 6

# 盈六匹于右下
右下 = 6

# 人得七匹于左上
左上 = 7

# 不足七匹于左下
左下 = 7

# 維乘之所得并之為絹
絹 = (左上 * 右下) + (右上 * 左下)

# 并盈不足為人
人 = 右下 + 左下

# 答案
a = 人
b = 絹#----- content ends here -----

"""
"""
