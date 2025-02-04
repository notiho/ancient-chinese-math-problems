"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To solve this problem, we need to calculate the volume of the irregularly shaped valley (冥谷) and then determine how much work is required to excavate it. The valley has different dimensions at the top and bottom, and we are given its depth. Let's break this down step by step.

---

### Problem Breakdown:

1. **Dimensions of the valley:**
   - Top width: 2 丈 = 20 尺
   - Top length: 7 丈 = 70 尺
   - Bottom width: 8 尺
   - Bottom length: 4 丈 = 40 尺
   - Depth: 6 丈 5 尺 = 65 尺

2. **Volume of the valley:**
   The valley is shaped like a truncated prism. The formula for the volume of a truncated prism is:
   \[
   V = \frac{1}{2} \cdot h \cdot (A_{\text{top}} + A_{\text{bottom}})
   \]
   where:
   - \( h \) is the depth,
   - \( A_{\text{top}} \) is the area of the top face,
   - \( A_{\text{bottom}} \) is the area of the bottom face.

3. **Work required:**
   - It is stated that 201 尺 of volume corresponds to 1 person’s work.
   - We need to calculate the total number of workers required to excavate the valley.

---

### Python Code:


"""


from fractions import Fraction

# Dimensions of the valley
top_width = 20  # in 尺
top_length = 70  # in 尺
bottom_width = 8  # in 尺
bottom_length = 40  # in 尺
depth = 65  # in 尺

# Calculate the areas of the top and bottom faces
area_top = top_width * top_length
area_bottom = bottom_width * bottom_length

# Calculate the volume of the valley
volume = Fraction(1, 2) * depth * (area_top + area_bottom)

# Work required: 201 尺 of volume corresponds to 1 person
work_per_person = Fraction(201)  # in 尺
workers = volume / work_per_person

# Output results
a = work_per_person  # Volume per person
b = workers  # Total workers required

# Print results
print(f"人到 {a} 尺。")
print(f"用徒 {b} 人。")


"""


---

### Explanation of Results:

1. **Volume Calculation:**
   - Top area: \( 20 \times 70 = 1400 \, \text{尺}^2 \)
   - Bottom area: \( 8 \times 40 = 320 \, \text{尺}^2 \)
   - Volume: \( \frac{1}{2} \cdot 65 \cdot (1400 + 320) = 55,900 \, \text{尺}^3 \)

2. **Work Calculation:**
   - Volume per person: \( 201 \, \text{尺}^3 \)
   - Total workers: \( \frac{55,900}{201} = 278 \, \text{people (approximately)} \)

---

### Final Answer:

- 人到 \( 201 \, \text{尺} \)。
- 用徒 \( 278 \, \text{人} \)。
"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 201
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 55900/201"""
