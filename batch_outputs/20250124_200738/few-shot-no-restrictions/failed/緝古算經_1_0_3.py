"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This is a complex ancient Chinese astronomical calculation involving the position of the moon at a specific time. Let's break it down step by step and translate it into Python code.

### Problem Breakdown:
- **Given:**
  - The sun is at **斗** (Dipper) 10 degrees and 7/100 of a degree, plus 480/10000 of a degree.
  - **章歲** (Zhang Sui) is the base unit, with a value of 700 (also referred to as the "行分法").
  - **朔月行定分** (fixed movement of the moon per month) is 9000.
  - **朔日定小余** (fixed remainder per day) is 10000.
  - **日法** (day divisor) is 20000.
  - The calculation does not consider additional time or daily movement of the sun.

- **Question:**
  - Where is the moon located (in degrees and fractions of a degree) at **天正十一月朔夜半** (midnight of the first day of the 11th month)?

- **Procedure:**
  1. Subtract **朔月行定分** from **章歲**.
  2. Multiply the remainder by **朔日定小余**.
  3. Divide the product by **日法** to get the "先行分" (initial movement fraction).
     - If there is a remainder, round it:
       - If the remainder is greater than or equal to half of **日法**, round up.
       - Otherwise, discard it.
  4. If the "先行分" exceeds **日行分** (daily movement fraction), convert it into degrees and fractions of a degree.
  5. Subtract the sun's position at midnight from the calculated position of the moon.
     - If the degrees are insufficient for subtraction, borrow from the next degree.
  6. The result is the moon's position at midnight.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given constants
章歲 = 700  # Zhang Sui
朔月行定分 = 9000  # Fixed movement of the moon per month
朔日定小余 = 10000  # Fixed remainder per day
日法 = 20000  # Day divisor
日所在度分 = Fraction(10) + Fraction(7, 100) + Fraction(480, 10000)  # Sun's position at midnight

# Step 1: Subtract 朔月行定分 from 章歲
余 = 章歲 - 朔月行定分

# Step 2: Multiply the remainder by 朔日定小余
實 = 余 * 朔日定小余

# Step 3: Divide the product by 日法 to get 先行分
先行分 = Fraction(實, 日法)

# Step 3.1: Round the remainder
if 先行分.denominator > 1:
    remainder = 先行分 - int(先行分)
    if remainder >= Fraction(1, 2):
        先行分 = int(先行分) + 1
    else:
        先行分 = int(先行分)

# Step 4: Convert 先行分 into degrees and fractions of a degree
度分 = Fraction(先行分, 1)  # Convert to degrees

# Step 5: Subtract the sun's position from the moon's position
if 度分 < 日所在度分:
    # Borrow 1 degree if necessary
    度分 += 1
    度分 -= 日所在度分
else:
    度分 -= 日所在度分

# Final result
a = 度分
print(f"答曰：在鬥 {a} 度。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Constants:** The given values for **章歲**, **朔月行定分**, **朔日定小余**, and **日法** are directly translated into variables.
2. **Sun's Position:** The sun's position is represented as a fraction for precise calculations.
3. **Step-by-Step Calculation:** Each step of the procedure is implemented in Python, including subtraction, multiplication, division, and rounding.
4. **Borrowing Logic:** If the moon's position is less than the sun's position, we borrow 1 degree to ensure proper subtraction.
5. **Final Output:** The result is printed as the moon's position in degrees.

---

### Example Output:
If you run the code with the given values, it will calculate the moon's position at midnight of the first day of the 11th month. The result will be displayed as `在鬥 a 度`, where `a` is the calculated position.
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: -2079559/500"""
