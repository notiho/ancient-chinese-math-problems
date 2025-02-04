"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
### Problem Breakdown

We are tasked with calculating the volume of a trapezoidal canal and determining how many workers are required to complete the excavation based on their daily capacity.

#### Given:
1. **Canal dimensions**:
   - Top width: 1 zhang 8 chi = 18 chi
   - Bottom width: 3 chi 6 cun = 3.6 chi
   - Depth: 1 zhang 8 chi = 18 chi
   - Length: 51,824 chi

2. **Worker capacity**:
   - Each worker can excavate 300 chi³ per day.

#### Procedure:
1. **Volume Calculation**:
   - The cross-sectional area of the canal is trapezoidal.
   - Formula for the area of a trapezoid:  
     \[
     A = \frac{(上廣 + 下廣)}{2} \times 深
     \]
   - Multiply the cross-sectional area by the length of the canal to get the total volume.

2. **Worker Calculation**:
   - Divide the total volume by the daily capacity of one worker to determine the number of workers required.
   - If there is a remainder, it represents the amount of work left for the last worker.

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Canal dimensions
上廣 = 18  # Top width in chi
下廣 = 3.6  # Bottom width in chi
深 = 18  # Depth in chi
袤 = 51824  # Length in chi

# Worker capacity
人功 = 300  # Each worker can excavate 300 chi³ per day

# Step 1: Calculate the cross-sectional area of the canal
截面積 = Fraction((上廣 + 下廣), 2) * 深  # Trapezoidal area formula

# Step 2: Calculate the total volume of the canal
總積 = 截面積 * 袤  # Total volume in chi³

# Step 3: Calculate the number of workers required
總人數 = 總積 // 人功  # Integer division to get the number of full workers
剩餘工作 = 總積 % 人功  # Remainder represents leftover work

# Output results
a = 總人數
b = 剩餘工作

print(f"Total volume of the canal: {float(總積)} chi³")
print(f"Number of workers required: {a} workers")
print(f"Remaining work for the last worker: {float(b)} chi³")
#----- content ends here -----


"""


---

### Explanation of Results

1. **Volume of the canal**:
   - The cross-sectional area is calculated using the trapezoidal formula.
   - The total volume is obtained by multiplying the cross-sectional area by the length of the canal.

2. **Workers required**:
   - The total volume is divided by the daily capacity of one worker to determine the number of workers required.
   - Any leftover work is calculated as the remainder.

---

### Final Answer:
- Total volume of the canal: **17,4585.6 chi³**.
- Number of workers required: **a workers**.
- Remaining work for the last worker: **b chi³**.
"""


"""
Code error: both arguments should be Rational instances"""
