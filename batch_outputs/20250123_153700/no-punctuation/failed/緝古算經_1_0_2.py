"""
假令天正十一月朔夜半日在斗十度七百分度之四百八十一章嵗為母朔月行定分九千朔日定小餘一萬日法二萬章嵗七百亦名行分也今不取加時度問天正朔夜半之時月在何處
術曰以章歲減朔月行定分余以乘朔日定小余滿日法而一為先行分不盡者半法已上收成一已下者棄之若先行分滿日行分而一為度分以減朔日夜半日所在度分若度分不足減加往宿度其分不足減者退一度為行分而減之余即朔日夜半月行所在度及分也
答曰在鬥 a度 
"""

"""
This is a complex ancient Chinese astronomical problem involving calculations of the moon's position at midnight on the first day of the eleventh month. Let's translate the procedure into Python step by step.

### Problem Breakdown:
- The problem provides various constants and asks for the moon's position at midnight on the first day of the eleventh month.
- The procedure involves modular arithmetic and rounding rules.

### Procedure:
1. Subtract the "定分" (fixed motion of the moon per month) from the "章歲" (total motion of the year).
2. Multiply the remainder by the "定小餘" (fixed small remainder of the moon's motion per day).
3. Divide the result by the "日法" (day divisor), and the quotient is the "先行分" (initial motion fraction).
4. If the remainder is greater than or equal to half the divisor, round up; otherwise, discard it.
5. If the "先行分" exceeds the "日行分" (daily motion fraction), convert it into degrees and fractions.
6. Subtract this from the sun's position at midnight to find the moon's position.

### Constants:
- `章歲 = 481` (motion of the year)
- `朔月行定分 = 9000` (fixed motion of the moon per month)
- `朔日定小餘 = 10000` (fixed small remainder of the moon's motion per day)
- `日法 = 20000` (day divisor)
- `日行分 = 700` (daily motion fraction)
- `朔日夜半日所在 = 10度7分` (sun's position at midnight)

### Python Code:


"""


from fractions import Fraction

# Constants
章歲 = 481
朔月行定分 = 9000
朔日定小餘 = 10000
日法 = 20000
日行分 = 700
朔日夜半日所在度 = 10
朔日夜半日所在分 = Fraction(7, 100)

# Step 1: Subtract the fixed motion of the moon per month from the motion of the year
余 = 章歲 - 朔月行定分

# Step 2: Multiply the remainder by the fixed small remainder of the moon's motion per day
實 = 余 * 朔日定小餘

# Step 3: Divide the result by the day divisor to get the initial motion fraction
先行分 = 實 // 日法
餘數 = 實 % 日法

# Step 4: Round the remainder
if 餘數 >= 日法 / 2:
    先行分 += 1

# Step 5: Convert the initial motion fraction into degrees and fractions
度分 = Fraction(先行分, 日行分)

# Step 6: Subtract from the sun's position at midnight
月所在度 = 朔日夜半日所在度 - int(度分)
月所在分 = 朔日夜半日所在分 - (度分 - int(度分))

# Adjust if the fractions go negative
if 月所在分 < 0:
    月所在度 -= 1
    月所在分 += 1

# Answer
a = 月所在度 + 月所在分
print(f"答曰：在鬥 {a} 度")


"""


### Explanation of the Code:
1. **Constants**: The constants are directly taken from the problem statement.
2. **Step-by-Step Procedure**: Each step of the procedure is implemented in Python, following the ancient algorithm.
3. **Fractions**: The `Fraction` class is used to handle fractional degrees and ensure precision.
4. **Adjustments**: If the fractional part becomes negative, adjustments are made to ensure the result is correct.

### Final Answer:
The moon's position at midnight on the first day of the eleventh month is `a` degrees in the constellation "斗" (Dipper).
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 2827/175"""
