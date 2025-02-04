"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This is a complex ancient Chinese astronomical calculation involving the position of the moon at a specific time. Let's translate the procedure into Python step by step.

### Problem Setup:
- The sun is at **斗 (Dipper)**, 10 degrees and 480/700 of a degree.
- **章岁 (Zhang Sui)** is the base unit, with a value of 700.
- **朔月行定分 (Shuo Yue Xing Ding Fen)** is 9000.
- **朔日定小余 (Shuo Ri Ding Xiao Yu)** is 10000.
- **日法 (Ri Fa)** is 20000.
- **章岁** is also called **行分法 (Xing Fen Fa)**.

The goal is to calculate the moon's position at **天正十一月朔夜半 (midnight of the first day of the eleventh month)**.

---

### Procedure:
1. Subtract **朔月行定分** from **章岁**.
2. Multiply the remainder by **朔日定小余**.
3. Divide the product by **日法**, and take the integer part as **先行分 (Xian Xing Fen)**.
   - If there is a remainder, round up if it is greater than or equal to half of **日法**, otherwise discard it.
4. If **先行分** exceeds **日行分**, convert it into degrees and fractions.
5. Subtract this value from the sun's position at midnight.
   - If the result is negative, add the total degrees of the previous constellation.
   - If the fractions are insufficient, borrow 1 degree and convert it into fractions.
6. The result is the moon's position at midnight.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
章歲 = 700
朔月行定分 = 9000
朔日定小余 = 10000
日法 = 20000
日所在度 = 10
日所在分 = Fraction(480, 700)

# Step 1: Subtract 朔月行定分 from 章歲
余 = 章歲 - 朔月行定分

# Step 2: Multiply the remainder by 朔日定小余
積 = 余 * 朔日定小余

# Step 3: Divide the product by 日法
先行分 = 積 // 日法
餘數 = 積 % 日法

# Round up if the remainder is greater than or equal to half of 日法
if 餘數 >= 日法 / 2:
    先行分 += 1

# Step 4: Convert 先行分 into degrees and fractions
度分 = Fraction(先行分, 1)

# Step 5: Subtract from the sun's position
月所在度 = 日所在度 - int(度分)
月所在分 = 日所在分 - (度分 - int(度分))

# Handle negative results
if 月所在分 < 0:
    月所在度 -= 1
    月所在分 += 1  # Convert 1 degree into fractions (1 degree = 1 in this system)

if 月所在度 < 0:
    月所在度 += 28  # Add the total degrees of the previous constellation (28 constellations in total)

# Final result
a = 月所在度 + 月所在分
#----- content ends here -----


"""


### Explanation of the Code:
1. **Subtraction and Multiplication**: The first part of the procedure calculates the remainder after subtracting **朔月行定分** from **章岁**, then multiplies it by **朔日定小余**.
2. **Division and Rounding**: The result is divided by **日法**, and the remainder determines whether to round up or not.
3. **Degree Conversion**: The integer part of the division is converted into degrees and fractions.
4. **Position Adjustment**: The moon's position is calculated by subtracting the derived value from the sun's position. Negative results are adjusted by borrowing or adding degrees.

### Final Answer:
The moon is at **a** degrees in the constellation **斗 (Dipper)**.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 145624/35"""
