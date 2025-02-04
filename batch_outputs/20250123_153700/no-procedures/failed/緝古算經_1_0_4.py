"""
假今天正十一月朔夜半，日在鬥十度七百分度之四百八十。以章歲為母，朔月行定分九千，朔日定小余一萬，日法二萬，章歲七百，亦名行分法。今不取加時日度。問：天正朔夜半之時月在何處？
答曰：在鬥 a度 。
"""

"""
This is a classical Chinese calendrical problem involving the calculation of the moon's position at a specific time, based on ancient astronomical systems. Let's break it down step by step and solve it using Python.

---

### Problem Breakdown:
1. **Given Data:**
   - **Sun's position at midnight on the first day of the 11th month:** 斗 (Dipper) 10 degrees + \( \frac{480}{7000} \) degrees.
   - **Lunar month movement (定分):** 9000.
   - **Lunar day remainder (定小余):** 10000.
   - **Solar cycle (日法):** 20000.
   - **Zhang Sui (章歲):** 700 (also called 行分法).

2. **Goal:**
   - Calculate the moon's position at midnight on the first day of the 11th month.

3. **Method:**
   - The moon's position is determined by the difference between the sun's position and the moon's position, calculated using the given constants.

---

### Python Code Solution:


"""


from fractions import Fraction

# Given data
sun_position = 10 + Fraction(480, 7000)  # Sun's position in degrees
lunar_month_movement = 9000             # 定分
lunar_day_remainder = 10000             # 定小余
solar_cycle = 20000                     # 日法
zhang_sui = 700                         # 章歲

# Step 1: Calculate the moon's position
# Formula: 月在 = 日在 - (定小余 / 日法) * 定分
moon_position = sun_position - Fraction(lunar_day_remainder, solar_cycle) * Fraction(lunar_month_movement, zhang_sui)

# Step 2: Convert the moon's position to degrees in the Dipper (斗)
a = moon_position

# Output the result
print(f"The moon is at {a} degrees in the Dipper.")


"""


---

### Explanation of the Formula:
1. The moon's position is calculated by subtracting the moon's movement (based on 定小余 and 定分) from the sun's position.
2. The fraction \( \frac{\text{定小余}}{\text{日法}} \) represents the proportion of the lunar day relative to the solar cycle.
3. Multiplying this fraction by \( \text{定分} \) gives the moon's movement relative to the sun.
4. Subtracting this from the sun's position gives the moon's position.

---

### Final Answer:
The moon's position is \( a \) degrees in the Dipper (斗).
"""


"""
Variable 'a' has wrong value. Expected: 333/70, Actual: 91/25"""
