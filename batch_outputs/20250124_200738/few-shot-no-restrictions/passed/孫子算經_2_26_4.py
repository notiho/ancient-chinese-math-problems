"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

#----- content starts here -----
"""
Suppose someone has stolen silk from a storehouse, but the exact amount of silk lost is unknown.
It is only known that when the silk was divided among people in the grass, each person received 6 bolts of silk, with 6 bolts left over.
However, when each person received 7 bolts, there were not enough silk bolts to give everyone 7 bolts.
Question: how many people and how many bolts of silk are there?

The procedure says: First, place the number of bolts per person (6) in the top right, and the remainder (6) in the bottom right.
Then, place the number of bolts per person (7) in the top left, and the deficit (7) in the bottom left.
Multiply diagonally, add the results to get the total number of silk bolts.
Add the remainder and deficit to get the total number of people.

Answer: there are *a* people, and *b* bolts of silk.
"""

# Define the known values
右上 = 6  # Each person gets 6 bolts
右下 = 6  # 6 bolts left over
左上 = 7  # Each person gets 7 bolts
左下 = 7  # 7 bolts deficit

# Multiply diagonally and sum to get the total number of silk bolts
絹 = (右上 * 左下) + (左上 * 右下)

# Add the remainder and deficit to get the total number of people
人 = 右下 + 左下

# Assign the results
a = 人
b = 絹#----- content ends here -----

"""
"""
