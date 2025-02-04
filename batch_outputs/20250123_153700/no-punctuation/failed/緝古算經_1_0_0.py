"""
假令天正十一月朔夜半日在斗十度七百分度之四百八十一章嵗為母朔月行定分九千朔日定小餘一萬日法二萬章嵗七百亦名行分也今不取加時度問天正朔夜半之時月在何處
術曰以章歲減朔月行定分余以乘朔日定小余滿日法而一為先行分不盡者半法已上收成一已下者棄之若先行分滿日行分而一為度分以減朔日夜半日所在度分若度分不足減加往宿度其分不足減者退一度為行分而減之余即朔日夜半月行所在度及分也
答曰在鬥 a度 
"""

"""
This is a complex ancient Chinese calendrical problem involving astronomical calculations. The problem asks for the position of the moon at midnight on the first day of the eleventh month of a specific year, given various constants and rules for calculation. Below is the Python implementation of the procedure described in the problem:


"""


from fractions import Fraction

# Constants provided in the problem
章嵗 = 481  # 章嵗 (481 in the problem)
朔月行定分 = 9000  # 朔月行定分
朔日定小餘 = 10000  # 朔日定小餘
滿日法 = 20000  # 滿日法
行分 = 700  # 行分

# Step 1: 以章嵗減朔月行定分余
余 = 章嵗 % 朔月行定分

# Step 2: 以乘朔日定小餘
先行分 = 余 * 朔日定小餘

# Step 3: 滿日法而一為先行分
先行分 = Fraction(先行分, 滿日法)

# Step 4: 不盡者半法已上收成一已下者棄之
if 先行分 - int(先行分) >= Fraction(1, 2):
    先行分 = int(先行分) + 1
else:
    先行分 = int(先行分)

# Step 5: 若先行分滿日行分而一為度分
度分 = Fraction(先行分, 行分)

# Step 6: 以減朔日夜半日所在度分
夜半日所在度分 = 10 + Fraction(7, 100)  # Initial position of the sun at midnight
度分 = 夜半日所在度分 - 度分

# Step 7: 若度分不足減加往宿度
if 度分 < 0:
    度分 += 30  # Add 30 degrees (a full zodiac sign)

# Step 8: 其分不足減者退一度為行分而減之
度 = int(度分)  # Integer part of the degree
分 = (度分 - 度) * 100  # Fractional part of the degree converted to 分

if 分 < 0:
    度 -= 1
    分 += 100

# Final result
a = 度 + 分 / 100  # The moon's position in degrees
print(f"在鬥 {a} 度")


"""


### Explanation of the Code:
1. **Constants**: The constants provided in the problem are used directly in the calculations.
2. **Modulo Operation**: The remainder of `章嵗` divided by `朔月行定分` is calculated.
3. **Multiplication and Division**: The remainder is multiplied by `朔日定小餘` and divided by `滿日法` to get the initial fractional value of `先行分`.
4. **Rounding**: If the fractional part of `先行分` is greater than or equal to 0.5, it is rounded up; otherwise, it is truncated.
5. **Degree Conversion**: The `先行分` is converted into degrees (`度分`) by dividing by `行分`.
6. **Adjustment**: If the resulting degrees are negative, 30 degrees are added to adjust for the zodiac cycle.
7. **Fractional Degrees**: The fractional part of the degrees is converted into "分" (hundredths of a degree).
8. **Final Adjustment**: If the fractional part is negative, 1 degree is subtracted, and 100 "分" are added to adjust.

### Answer:
The moon's position at midnight on the first day of the eleventh month is `a` degrees in the zodiac sign of "斗".
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 1702/175"""
