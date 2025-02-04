"""
今有人盜庫絹，不知所失幾何？但聞草中分絹，人得六匹，盈六匹；人得七匹，不足七匹。問人、絹各幾何？
術曰：先置人得六匹于右上，盈六匹于右下，後置人得七匹于左上，不足七匹于左下，維乘之所得，并之為絹，并盈不足為人。
答曰：賊 a人 ，絹 b匹 。
"""

#----- content starts here -----
"""
Suppose someone has stolen silk from the storehouse, but the exact amount of silk lost is unknown.
It is only known that when the silk is divided among people such that each person gets 6 bolts of silk, there is a remainder of 6 bolts.
However, when the silk is divided such that each person gets 7 bolts, there are not enough bolts to give each person 7.

Question: How many people and how many bolts of silk are there?

The procedure says: 
- First, place the number of bolts per person (6) in the top right, and the remainder (6) in the bottom right.
- Then, place the number of bolts per person (7) in the top left, and the shortage (7) in the bottom left.
- Multiply diagonally and sum the results to find the total number of bolts of silk.
- Add the remainder and shortage to find the number of people.

Answer: The thief group consists of *a* people, and the stolen silk is *b* bolts.
"""

# Known values
右上 = 6  # Each person gets 6 bolts
右下 = 6  # Remainder is 6 bolts
左上 = 7  # Each person gets 7 bolts
左下 = 7  # Shortage is 7 bolts

# Compute the total number of bolts of silk (絹)
絹 = (右上 * 左下) + (左上 * 右下)

# Compute the total number of people (人)
人 = 右下 + 左下

# Final results
a = 人  # Number of people
b = 絹  # Number of bolts of silk

a, b  # Output the results#----- content ends here -----

"""
"""
