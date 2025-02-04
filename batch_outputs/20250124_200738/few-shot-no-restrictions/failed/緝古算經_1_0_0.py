"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This is a classical Chinese calendrical problem involving the calculation of the moon's position at midnight on the first day of the eleventh month. The solution involves modular arithmetic and approximations based on ancient Chinese astronomical methods. Let's translate the procedure into Python code step by step.

---

### Problem Breakdown:
1. **Given Data:**
   - The sun is at **斗 (Dipper) 10度7分480秒** at midnight on the first day of the eleventh month.
   - Constants:
     - **章歲 (Zhang Sui)** = 700 (also called 行分法, the cycle divisor).
     - **朔月行定分 (Shuo Month Fixed Movement)** = 9000.
     - **朔日定小余 (Shuo Day Fixed Remainder)** = 10000.
     - **日法 (Day Divisor)** = 20000.

2. **Procedure:**
   - Subtract **朔月行定分** from **章歲**.
   - Multiply the remainder by **朔日定小余**.
   - Divide the result by **日法** to get the **先行分 (First Movement Remainder)**.
   - Round the remainder:
     - If ≥ half of **日法**, round up.
     - Otherwise, discard the remainder.
   - Convert the **先行分** into degrees and fractions of a degree.
   - Subtract this from the sun's position at midnight to find the moon's position.
   - Handle cases where the subtraction results in negative values by adjusting with the zodiac cycle.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given constants
章歲 = 700  # Zhang Sui
朔月行定分 = 9000  # Shuo Month Fixed Movement
朔日定小余 = 10000  # Shuo Day Fixed Remainder
日法 = 20000  # Day Divisor

# Sun's position at midnight (斗 10度7分480秒)
日所在度 = 10  # Degrees
日所在分 = Fraction(7, 100)  # Fractions of a degree (7/100)
日所在秒 = Fraction(480, 10000)  # Fractions of a degree (480/10000)
日所在度分 = 日所在度 + 日所在分 + 日所在秒  # Total position in degrees

# Step 1: Subtract 朔月行定分 from 章歲
余 = 章歲 - 朔月行定分

# Step 2: Multiply the remainder by 朔日定小余
先行分 = 余 * 朔日定小余

# Step 3: Divide by 日法 to get the remainder
先行分 = Fraction(先行分, 日法)

# Step 4: Round the remainder
if 先行分 >= Fraction(1, 2):  # If ≥ half of 日法, round up
    先行分 = 1
else:  # Otherwise, discard the remainder
    先行分 = 0

# Step 5: Convert 先行分 into degrees and fractions of a degree
度分 = Fraction(先行分, 1)  # Convert to degrees (先行分 is already in degrees)

# Step 6: Subtract from the sun's position
月所在度分 = 日所在度分 - 度分

# Step 7: Handle negative values (adjust with zodiac cycle)
if 月所在度分 < 0:
    月所在度分 += 360  # Add 360 degrees to adjust

# Extract the final position in degrees
a = 月所在度分

# Output the result
print(f"答曰：在鬥 {a}度。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Constants:** The constants are directly translated from the problem statement.
2. **Fractions:** The `fractions.Fraction` class is used to handle non-integer values precisely.
3. **Rounding:** The rounding logic follows the ancient method described in the problem.
4. **Adjustments:** If the subtraction results in a negative position, the zodiac cycle (360 degrees) is added to ensure the position is within the valid range.

---

### Example Output:
If you run the code, it will calculate the moon's position at midnight on the first day of the eleventh month based on the given data and procedure. The result will be in degrees, as required by the problem.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 5059/500"""
