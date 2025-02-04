"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
荅曰： a人 功。內少 b尺 。
"""

"""
Let's break this problem into two parts:

1. **Calculate the volume of the canal (積)**:
   - The top width is 1丈8尺 (18尺).
   - The bottom width is 3尺6寸 (3.6尺).
   - The depth is 1丈8尺 (18尺).
   - The length (袤) is 51824尺.
   - The formula for the volume of a trapezoidal prism is:
     \[
     V = \frac{(上廣 + 下廣) \times 深}{2} \times 袤
     \]

2. **Calculate the number of workers needed (用徒)**:
   - Each worker can dig 300尺 of volume.
   - Divide the total volume by 300尺 to determine the number of workers needed, and calculate any remainder.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the canal
上廣 = 18  # Top width in 尺
下廣 = 3 + Fraction(6, 10)  # Bottom width in 尺 (3尺6寸 = 3.6尺)
深 = 18  # Depth in 尺
袤 = 51824  # Length in 尺

# Calculate the volume of the canal
積 = Fraction((上廣 + 下廣) * 深, 2) * 袤

# Convert the volume to 尺 and 寸
積_尺 = int(積)  # Whole 尺
積_寸 = (積 - 積_尺) * 10  # Convert fractional 尺 to 寸

# Worker productivity
人功 = 300  # Each worker can dig 300尺 of volume

# Calculate the number of workers needed and the remainder
用徒 = 積 // 人功  # Number of workers
內少 = 積 % 人功  # Remaining volume in 尺

# Output results
print(f"積: {積_尺}尺{積_寸}寸")
print(f"用徒: {用徒}人功")
print(f"內少: {內少}尺")
#----- content ends here -----


"""


---

### Explanation of Results:
1. **Volume of the canal (積)**:
   - The total volume is calculated using the trapezoidal prism formula.
   - The result is expressed in 尺 and 寸.

2. **Number of workers (用徒)**:
   - The total volume is divided by the productivity of each worker (300尺).
   - The remainder (內少) is the leftover volume that is less than what one worker can dig.

---

### Final Answer:
- 積: **174585尺6寸**
- 用徒: **581 workers**
- 內少: **285尺**
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
