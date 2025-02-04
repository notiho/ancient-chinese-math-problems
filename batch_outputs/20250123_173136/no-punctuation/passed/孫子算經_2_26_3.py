"""
今有人盜庫絹不知所失幾何但聞草中分絹人得六匹盈六匹人得七匹不足七匹問人絹各幾何
術曰先置人得六匹于右上盈六匹于右下後置人得七匹于左上不足七匹于左下維乘之所得并之為絹并盈不足為人
答曰賊 a人 絹 b匹 
"""

"""
Suppose someone stole silk from the storehouse, but the exact amount lost is unknown.
It is only heard that when dividing the silk among people, each person gets 6 pi, with 6 pi left over.
If each person gets 7 pi, then 7 pi are insufficient.
Question: how many people and how much silk are there?

The procedure says: First, place the number of people getting 6 pi in the top-right, and the 6 pi left over in the bottom-right.
Then, place the number of people getting 7 pi in the top-left, and the 7 pi insufficient in the bottom-left.
Cross-multiply the values, sum them to get the total silk.
Sum the surplus and deficit to get the total number of people.

Answer: the thief is *a* people, and the silk is *b* pi.
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
絹 = (右上 * 左下) + (左上 * 右下)

# 并盈不足為人
人 = 右下 + 左下

# 答案
a = 人
b = 絹
"""
"""
