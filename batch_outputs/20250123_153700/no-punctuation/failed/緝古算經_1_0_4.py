"""
假令天正十一月朔夜半日在斗十度七百分度之四百八十一章嵗為母朔月行定分九千朔日定小餘一萬日法二萬章嵗七百亦名行分也今不取加時度問天正朔夜半之時月在何處
術曰以章歲減朔月行定分余以乘朔日定小余滿日法而一為先行分不盡者半法已上收成一已下者棄之若先行分滿日行分而一為度分以減朔日夜半日所在度分若度分不足減加往宿度其分不足減者退一度為行分而減之余即朔日夜半月行所在度及分也
答曰在鬥 a度 
"""

"""
This problem involves calculating the position of the moon at midnight on the first day of the eleventh month of a specific year, based on ancient Chinese calendrical methods. Let's translate the procedure into Python step by step.

### Problem Breakdown:
- The sun's position at midnight on the first day of the eleventh month is given as 10 degrees and 481/700 degrees in the Dipper (斗).
- The moon's motion is governed by specific constants:
  - **朔月行定分 (Monthly motion constant)** = 9000
  - **朔日定小余 (Daily motion constant)** = 10000
  - **日法 (Full day divisor)** = 20000
  - **章嵗 (Cycle constant)** = 700
- The goal is to calculate the moon's position at midnight on the first day of the eleventh month.

### Procedure:
1. Subtract the monthly motion constant (朔月行定分) from the cycle constant (章嵗).
2. Multiply the remainder by the daily motion constant (朔日定小余).
3. Divide the result by the full day divisor (日法), obtaining the quotient (先行分) and the remainder.
4. If the remainder is greater than or equal to half the divisor, round up the quotient; otherwise, discard the remainder.
5. Convert the quotient into degrees and fractions of a degree.
6. Subtract this value from the sun's position at midnight to find the moon's position.
7. If the subtraction results in a negative value, adjust by borrowing from the next degree.

### Python Code:


"""


from fractions import Fraction

# Constants
章嵗 = 700  # Cycle constant
朔月行定分 = 9000  # Monthly motion constant
朔日定小余 = 10000  # Daily motion constant
日法 = 20000  # Full day divisor
日所在度分 = Fraction(10) + Fraction(481, 700)  # Sun's position at midnight

# Step 1: Subtract the monthly motion constant from the cycle constant
余 = 章嵗 - 朔月行定分

# Step 2: Multiply the remainder by the daily motion constant
實 = 余 * 朔日定小余

# Step 3: Divide the result by the full day divisor
先行分 = 實 // 日法  # Quotient
餘數 = 實 % 日法  # Remainder

# Step 4: Round the quotient based on the remainder
if 餘數 >= 日法 / 2:
    先行分 += 1

# Step 5: Convert the quotient into degrees and fractions of a degree
度分 = Fraction(先行分, 10000)  # Convert to degrees

# Step 6: Subtract this value from the sun's position at midnight
月所在度分 = 日所在度分 - 度分

# Step 7: Adjust if the result is negative
if 月所在度分 < 0:
    月所在度分 += 360  # Add 360 degrees to normalize

# Final Answer
a = 月所在度分


"""


### Explanation of Variables:
- `章嵗` (Cycle constant): Represents the cycle of the year.
- `朔月行定分` (Monthly motion constant): Governs the moon's motion over a month.
- `朔日定小余` (Daily motion constant): Governs the moon's motion over a day.
- `日法` (Full day divisor): Used to normalize the calculations.
- `日所在度分` (Sun's position): The sun's position at midnight on the first day of the eleventh month.
- `先行分` (Initial motion): The moon's motion calculated in fractions of a degree.
- `度分` (Degrees and fractions): The moon's motion converted to degrees.
- `月所在度分` (Moon's position): The final position of the moon at midnight.

### Final Answer:
The moon is located at **a** degrees in the Dipper (斗).
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 15543/1400"""
