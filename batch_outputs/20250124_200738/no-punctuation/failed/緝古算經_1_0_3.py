"""
假令天正十一月朔夜半日在斗十度七百分度之四百八十一章嵗為母朔月行定分九千朔日定小餘一萬日法二萬章嵗七百亦名行分也今不取加時度問天正朔夜半之時月在何處
術曰以章歲減朔月行定分余以乘朔日定小余滿日法而一為先行分不盡者半法已上收成一已下者棄之若先行分滿日行分而一為度分以減朔日夜半日所在度分若度分不足減加往宿度其分不足減者退一度為行分而減之余即朔日夜半月行所在度及分也
答曰在鬥 a度 
"""

"""
This is a complex ancient Chinese astronomical problem involving the calculation of the moon's position at midnight on a specific day. Below is the Python implementation of the procedure ("術") described in the problem:


"""

#----- content starts here -----

"""
Suppose it is the 11th month of the Tianzheng calendar, on the first day of the month, at midnight. The sun is at 10 degrees and 481/700 of a degree in the Dipper (斗) constellation.
The year is a "mother year" (母朔), and the moon's fixed movement per month is 9000 units. The moon's fixed remainder per day is 10,000 units. The divisor for days is 20,000 units. The year's divisor is 700, also called the "movement divisor" (行分).

Now, without adding the adjustment for time, the question is: at midnight on the first day of the month, where is the moon located?

The procedure says:
1. Subtract the moon's fixed movement per month (朔月行定分) from the year's divisor (章嵗).
2. Multiply the remainder by the moon's fixed remainder per day (朔日定小余).
3. Divide the result by the day divisor (滿日法), and take the integer part as the "initial movement divisor" (先行分).
4. If there is a remainder, check:
   - If it is greater than or equal to half the divisor, round up by adding 1.
   - Otherwise, discard it.
5. If the initial movement divisor exceeds the year's divisor, subtract the year's divisor to get the degree and fraction of movement.
6. Subtract this from the sun's position at midnight to find the moon's position.
7. If the degree is insufficient to subtract, adjust by borrowing from the next degree.

Answer: The moon is at *a* degrees in the Dipper (斗) constellation.
"""

from fractions import Fraction

# Initial values
章嵗 = 700  # Year's divisor
朔月行定分 = 9000  # Moon's fixed movement per month
朔日定小余 = 10000  # Moon's fixed remainder per day
滿日法 = 20000  # Day divisor
朔日夜半日所在度分 = Fraction(10, 1) + Fraction(481, 700)  # Sun's position at midnight in degrees

# Step 1: Subtract the moon's fixed movement per month from the year's divisor
余 = 章嵗 - 朔月行定分

# Step 2: Multiply the remainder by the moon's fixed remainder per day
實 = 余 *朔日定小余

# Step 3: Divide by the day divisor to get the initial movement divisor
先行分 = 實 // 滿日法
餘數 = 實 % 滿日法

# Step 4: Handle the remainder
if 餘數 >= 滿日法 / 2:
    先行分 += 1

# Step 5: If the initial movement divisor exceeds the year's divisor, adjust
度分 = 先行分 % 章嵗

# Step 6: Subtract from the sun's position at midnight
月所在度分 = 朔日夜半日所在度分 - Fraction(度分, 1)

# Step 7: Handle insufficient degrees
if 月所在度分 < 0:
    月所在度分 += 10  # Borrow 1 degree (10 degrees in this case)

# Final answer
a = 月所在度分
#----- content ends here -----


"""


### Explanation of the Code:
1. **Initial Values**: The problem provides constants such as `章嵗` (year's divisor), `朔月行定分` (moon’s fixed movement per month), and `朔日定小余` (moon’s fixed remainder per day).
2. **Subtraction**: The moon's fixed movement per month is subtracted from the year's divisor.
3. **Multiplication and Division**: The remainder is multiplied by the moon's fixed remainder per day and divided by the day divisor to get the initial movement divisor.
4. **Rounding**: If the remainder is greater than or equal to half the divisor, it is rounded up; otherwise, it is discarded.
5. **Adjustment**: If the initial movement divisor exceeds the year's divisor, it is adjusted to fit within the range.
6. **Subtraction from Sun's Position**: The calculated movement is subtracted from the sun's position at midnight to find the moon's position.
7. **Handling Negative Values**: If the result is negative, it is adjusted by borrowing from the next degree.

### Final Output:
The variable `a` represents the moon's position in degrees in the Dipper (斗) constellation at midnight on the first day of the 11th month.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: -20519/700"""
