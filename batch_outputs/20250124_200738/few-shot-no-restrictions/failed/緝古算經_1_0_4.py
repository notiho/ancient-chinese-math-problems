"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
術曰：以章歲減朔月行定分，余以乘朔日定小余，滿日法而一，為先行分。不盡者，半法已上收成一，已下者棄之。若先行分滿日行分而一，為度分，以減朔日夜半日所在度分，若度分不足減，加往宿度；其分不足減者，退一度為行分而減之，余即朔日夜半月行所在度及分也。
答曰：在鬥 a度 。
"""

"""
This is a fascinating ancient Chinese astronomical problem involving the calculation of the moon's position at midnight on the first day of the eleventh lunar month. Let's translate the procedure into Python code step by step.

---

### Problem Breakdown:
1. **Given Data:**
   - The sun is at **斗 (Dipper) 10 degrees and 480/10000 of a degree** at midnight on the first day of the eleventh lunar month.
   - **章歲 (Zhang Sui)** = 700 (also called 行分法, the divisor for calculations).
   - **朔月行定分 (Fixed motion of the moon per month)** = 9000.
   - **朔日定小余 (Fixed small remainder per day)** = 10000.
   - **日法 (Divisor for days)** = 20000.

2. **Procedure:**
   - Subtract **朔月行定分** from **章歲** to get the remainder.
   - Multiply the remainder by **朔日定小余**.
   - Divide the product by **日法** to get the **先行分 (preliminary motion)**.
   - If there is a remainder:
     - If the remainder is greater than or equal to half of **日法**, round up.
     - Otherwise, discard it.
   - Convert **先行分** into degrees and fractions of a degree.
   - Subtract this value from the sun's position at midnight.
   - If the result is negative, adjust by adding the degrees of the previous constellation.
   - The final result is the moon's position at midnight.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
章歲 = 700  # Zhang Sui
朔月行定分 = 9000  # Fixed motion of the moon per month
朔日定小余 = 10000  # Fixed small remainder per day
日法 = 20000  # Divisor for days
朔日夜半日所在度分 = Fraction(10, 1) + Fraction(480, 10000)  # Sun's position at midnight (斗 10 degrees and 480/10000)

# Step 1: Subtract 朔月行定分 from 章歲
余 = 章歲 - 朔月行定分

# Step 2: Multiply the remainder by 朔日定小余
實 = 余 * 朔日定小余

# Step 3: Divide the product by 日法 to get 先行分
先行分 = Fraction(實, 日法)

# Step 4: Handle the remainder
if 先行分.denominator > 1:  # If there's a remainder
    remainder = 先行分 - int(先行分)  # Get the fractional part
    if remainder >= Fraction(1, 2):  # If remainder >= 0.5, round up
        先行分 = int(先行分) + 1
    else:  # Otherwise, discard the remainder
        先行分 = int(先行分)

# Step 5: Convert 先行分 into degrees and fractions of a degree
度分 = Fraction(先行分, 1)  # Convert to degrees (since 1 unit = 1 degree)

# Step 6: Subtract from the sun's position at midnight
月所在度分 = 朔日夜半日所在度分 - 度分

# Step 7: Adjust if the result is negative
if 月所在度分 < 0:
    月所在度分 += 30  # Add 30 degrees (the degrees of the previous constellation)

# Final result
a = 月所在度分
print(f"答曰：在鬥 {a} 度。")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Fractions:** The `Fraction` class is used to handle precise calculations involving fractions, as ancient Chinese calculations often involve fractional values.
2. **Rounding:** The rounding rule (round up if ≥ 0.5, discard otherwise) is implemented using conditional logic.
3. **Adjusting for Negative Values:** If the calculated position is negative, we add 30 degrees to adjust for the previous constellation.

---

### Example Output:
If you run the code with the given data, it will calculate the moon's position at midnight on the first day of the eleventh lunar month. The result will be in degrees within the **斗 (Dipper)** constellation.


"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 520006/125"""
