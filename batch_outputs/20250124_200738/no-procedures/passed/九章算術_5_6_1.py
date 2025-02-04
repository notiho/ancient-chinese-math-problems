"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
荅曰： a人 。
"""

"""
Let's break this problem into two parts:

1. **Calculate the volume of the ditch (溝)**:
   The ditch has a trapezoidal cross-section, with the top width, bottom width, and depth provided. The length (袤) is also given. The formula for the volume of a trapezoidal prism is:

   \[
   V = \frac{(上廣 + 下廣) \times 深}{2} \times 袤
   \]

2. **Calculate the number of workers (徒)**:
   The total work required is the volume divided by the work rate per person. The work rate includes an adjustment for the additional effort of removing the soil.

---

### Step 1: Calculate the volume of the ditch



---

### Step 2: Calculate the number of workers

The problem states that:
- The total work per person is 766 尺³, including an additional 1/5 for removing soil.
- The adjusted work per person is \( 766 + \frac{766}{5} = 612 \frac{4}{5} \) 尺³.

The number of workers is the total volume divided by the adjusted work per person.


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
上廣 = Fraction(1, 1) + Fraction(5, 10)  # 1丈5尺 = 1.5丈
下廣 = Fraction(1, 1)                   # 1丈
深 = Fraction(5, 10)                    # 5尺 = 0.5丈
袤 = Fraction(7, 1)                     # 7丈

# Volume formula: V = ((上廣 + 下廣) * 深 / 2) * 袤
V = ((上廣 + 下廣) * 深 / 2) * 袤
print(f"Volume of the ditch (積): {V} 丈³")

# Convert volume to 尺³ (1丈³ = 1000尺³)
V_in_尺 = V * 1000
print(f"Volume of the ditch (積): {V_in_尺} 尺³")

# Work rate per person
individual_work = Fraction(612, 1) + Fraction(4, 5)  # 612 4/5 尺³

# Number of workers
a = V_in_尺 / individual_work
print(f"Number of workers (用徒): {a} 人")
#----- content ends here -----


"""


---

### Final Answer:
The number of workers \( a \) is calculated as a fraction or mixed number.
"""


"""
"""
