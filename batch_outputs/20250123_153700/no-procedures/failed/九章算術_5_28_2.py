"""
今有冥谷上廣二丈，袤七丈，下廣八尺，袤四丈，深六丈五尺。問︰積幾何？
荅曰：五萬二千尺。
荅曰：人到二百一尺、五十分尺之十三。用徒二百五十八人、一萬六十三分人之三千七百四十六。
荅曰：人到 a尺 。用徒 b人 。
"""

"""
To solve this problem, we calculate the volume of the irregularly shaped valley (冥谷) and then determine how much work is required to excavate it. Here's the breakdown:

### Problem:
1. The valley has:
   - Top width: 2 zhang (20 chi)
   - Top length: 7 zhang (70 chi)
   - Bottom width: 8 chi
   - Bottom length: 4 zhang (40 chi)
   - Depth: 6 zhang 5 chi (65 chi)

2. The volume is calculated using the formula for a truncated prism:
   \[
   V = \frac{1}{2} \times (上廣 \times 上袤 + 下廣 \times 下袤) \times 深
   \]

3. The work required is calculated based on the volume:
   - Each person can excavate **201 chi** of earth.
   - Each person requires **258 people** to complete the task.

---

### Python Code:


"""


from fractions import Fraction

# Dimensions of the valley
上廣 = 20  # Top width in chi
上袤 = 70  # Top length in chi
下廣 = 8   # Bottom width in chi
下袤 = 40  # Bottom length in chi
深 = 65    # Depth in chi

# Calculate the volume of the valley
積 = Fraction(1, 2) * (上廣 * 上袤 + 下廣 * 下袤) * 深

# Each person can excavate 201 chi of earth
人到 = Fraction(積, 201)

# Total number of workers needed
用徒 = Fraction(積, 201 * 258)

# Results
a = 人到  # Earth excavated per person
b = 用徒  # Total workers required

# Output the results
a, b


"""


---

### Explanation of Results:
1. **a (人到)**: The amount of earth each person excavates, expressed in chi.
2. **b (用徒)**: The total number of workers required to excavate the valley, expressed as a fraction of people.


"""


"""
Variable 'a' has wrong value. Expected: 10063/50, Actual: 55900/201
Variable 'b' has wrong value. Expected: 2600000/10063, Actual: 650/603"""
