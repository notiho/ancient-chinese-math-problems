"""
今有溝上廣一丈五尺，下廣一丈，深五尺，袤七丈。問︰積幾何？
荅曰：四千三百七十五尺。
春程人功七百六十六尺，并出土功五分之一，定功六百一十二尺、五分尺之四。問︰用徒幾何？
荅曰： a人 。
"""

"""
### Problem Explanation:

1. **First Part**: Calculate the volume of the ditch.
   - The ditch has a trapezoidal cross-section:
     - Top width: 1丈5尺 = 15尺
     - Bottom width: 1丈 = 10尺
     - Depth: 5尺
   - Length of the ditch: 7丈 = 70尺
   - The formula for the volume of a trapezoidal prism is:
     \[
     V = \frac{(上廣 + 下廣) \times 深}{2} \times 袤
     \]

2. **Second Part**: Determine the number of workers needed.
   - Total volume of the ditch: 4375尺³.
   - Each worker can dig **612尺³ and 4/5尺³** (including the extra 1/5 for moving soil).
   - To calculate the number of workers:
     \[
     人數 = \frac{\text{總土方量}}{\text{每人挖掘量}}
     \]

---

### Python Code:


"""


from fractions import Fraction

# Dimensions of the ditch
上廣 = 15  # Top width in 尺
下廣 = 10  # Bottom width in 尺
深 = 5     # Depth in 尺
袤 = 70    # Length in 尺

# Calculate the volume of the ditch
積 = Fraction((上廣 + 下廣) * 深, 2) * 袤

# Verify the calculated volume matches the given answer
assert 積 == 4375, "Calculated volume does not match the given answer!"

# Worker capacity
每人挖掘量 = 612 + Fraction(4, 5)  # Each worker can dig this much 尺³

# Calculate the number of workers needed
用徒 = 積 / 每人挖掘量

# Simplify the result
a = 用徒.limit_denominator()

# Output the result
a


"""


---

### Explanation of Results:
- The calculated volume of the ditch is **4375尺³**, which matches the given answer.
- The number of workers needed is calculated as **a**, expressed as a fraction or a mixed number.
"""


"""
"""
