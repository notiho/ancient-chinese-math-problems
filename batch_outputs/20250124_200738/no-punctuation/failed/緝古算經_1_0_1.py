"""
假令天正十一月朔夜半日在斗十度七百分度之四百八十一章嵗為母朔月行定分九千朔日定小餘一萬日法二萬章嵗七百亦名行分也今不取加時度問天正朔夜半之時月在何處
術曰以章歲減朔月行定分余以乘朔日定小余滿日法而一為先行分不盡者半法已上收成一已下者棄之若先行分滿日行分而一為度分以減朔日夜半日所在度分若度分不足減加往宿度其分不足減者退一度為行分而減之余即朔日夜半月行所在度及分也
答曰在鬥 a度 
"""

"""
This is a complex ancient Chinese astronomical problem involving the calculation of the moon's position at midnight on the first day of the eleventh month. Let's translate the procedure into Python step by step.

### Problem Breakdown:
- **Given Data:**
  - At midnight on the first day of the eleventh month, the sun is at 10 degrees and 481/700 degrees in the constellation Dou.
  - The year is a "mother year" (母朔), and the moon's fixed motion is 9000 "定分".
  - The moon's small remainder is 10,000 "小餘".
  - The divisor for days is 20,000 "日法".
  - The year's divisor is 700, also called the "motion divisor" (行分).

- **Question:**
  - At midnight on the first day of the eleventh month, where is the moon located?

- **Procedure:**
  1. Subtract the moon's fixed motion (朔月行定分) from the year's divisor (章嵗).
  2. Multiply the remainder by the moon's small remainder (朔日定小餘).
  3. Divide the result by the day divisor (日法). The quotient is the "initial motion divisor" (先行分).
  4. If the remainder is greater than or equal to half the divisor, round up; otherwise, discard it.
  5. If the initial motion divisor exceeds the year's divisor, divide it by the year's divisor to get degrees and fractions.
  6. Subtract the result from the sun's position at midnight to find the moon's position.
  7. If the degrees are insufficient for subtraction, adjust by borrowing from the next degree.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
章嵗 = 700  # Year's divisor
朔月行定分 = 9000  # Moon's fixed motion
朔日定小餘 = 10000  # Moon's small remainder
日法 = 20000  # Day divisor
日所在度分 = Fraction(10, 1) + Fraction(481, 700)  # Sun's position at midnight

# Step 1: Subtract the moon's fixed motion from the year's divisor
余 = 章嵗 - 朔月行定分

# Step 2: Multiply the remainder by the moon's small remainder
實 = 余 *朔日定小餘

# Step 3: Divide the result by the day divisor to get the initial motion divisor
先行分 = 實 // 日法
餘數 = 實 % 日法

# Step 4: Round the remainder
if 餘數 >= 日法 / 2:
    先行分 += 1

# Step 5: If the initial motion divisor exceeds the year's divisor, divide it
度分 = Fraction(先行分, 章嵗)

# Step 6: Subtract the result from the sun's position at midnight
月所在度分 = 日所在度分 - 度分

# Step 7: Adjust if the degrees are insufficient for subtraction
if 月所在度分 < 0:
    月所在度分 += 1  # Borrow 1 degree
    月所在度分 -= Fraction(1, 章嵗)

# Final result
a = 月所在度分
#----- content ends here -----


"""


### Explanation of the Code:
1. **Subtract the moon's fixed motion from the year's divisor:** This gives the remainder of the year's motion after accounting for the moon's fixed motion.
2. **Multiply by the moon's small remainder:** This scales the remainder to account for the moon's small remainder.
3. **Divide by the day divisor:** This calculates the initial motion divisor and its remainder.
4. **Round the remainder:** If the remainder is greater than or equal to half the divisor, round up; otherwise, discard it.
5. **Convert to degrees and fractions:** If the initial motion divisor exceeds the year's divisor, divide it to get degrees and fractions.
6. **Subtract from the sun's position:** This gives the moon's position relative to the sun's position at midnight.
7. **Adjust for negative values:** If the result is negative, adjust by borrowing from the next degree.

### Final Answer:
The moon's position at midnight on the first day of the eleventh month is in Dou at `a` degrees.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 11631/700"""
