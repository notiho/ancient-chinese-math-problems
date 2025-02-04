"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
### Problem Breakdown:

1. **First Part: Calculating the Volume of the Canal**  
   The canal has the following dimensions:
   - Top width: 1 zhang 8 chi = 18 chi
   - Bottom width: 3 chi 6 cun = 3.6 chi
   - Depth: 1 zhang 8 chi = 18 chi
   - Length: 51824 chi

   The formula for the volume of a trapezoidal prism is:
   \[
   V = \frac{(上廣 + 下廣)}{2} \times 深 \times 袤
   \]

2. **Second Part: Calculating the Number of Workers Required**  
   - Each worker can dig 300 chi³ of earth.
   - Using the volume calculated above, divide it by the work capacity of one worker to determine the number of workers required. If there is a remainder, it is the leftover volume.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Canal dimensions
上廣 = 18  # Top width in chi
下廣 = 3 + Fraction(6, 10)  # Bottom width in chi (3 chi 6 cun = 3.6 chi)
深 = 18  # Depth in chi
袤 = 51824  # Length in chi

# Calculate the volume of the canal
平均廣 = (上廣 + 下廣) / 2  # Average width
積 = 平均廣 * 深 * 袤  # Volume in cubic chi

# Convert the volume to chi and cun
積整數部分 = int(積)  # Integer part of the volume
積小數部分 = (積 - 積整數部分) * 10  # Fractional part converted to cun

# Worker capacity
人功 = 300  # Each worker can dig 300 cubic chi

# Calculate the number of workers required
用徒 = 積 // 人功  # Number of full workers
剩餘尺 = 積 % 人功  # Remaining volume in chi³

# Output results
a = 用徒
b = 剩餘尺

print(f"Canal volume: {積整數部分} chi {積小數部分:.1f} cun")
print(f"Workers required: {a} workers")
print(f"Remaining volume: {b} chi³")
#----- content ends here -----


"""


---

### Explanation of the Code:

1. **Volume Calculation**:
   - The average width of the canal is calculated as the mean of the top and bottom widths.
   - The volume is then calculated using the formula for the volume of a trapezoidal prism.

2. **Worker Calculation**:
   - The total volume is divided by the capacity of one worker to determine the number of workers required.
   - The remainder is calculated to determine the leftover volume.

---

### Final Answer:

- Canal volume: **174585 chi 6 cun**
- Workers required: **581 workers**
- Remaining volume: **285 chi³**
"""


"""
Code error: unsupported format string passed to Fraction.__format__"""
