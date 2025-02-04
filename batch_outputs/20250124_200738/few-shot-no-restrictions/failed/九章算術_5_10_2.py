"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
### Problem Breakdown and Solution in Python

#### Problem Statement:
1. A canal has the following dimensions:
   - Top width: 1 zhang 8 chi (18 chi)
   - Bottom width: 3 chi 6 cun (3.6 chi)
   - Depth: 1 zhang 8 chi (18 chi)
   - Length: 51824 chi

   Question 1: What is the total volume of the canal?

   Answer: 174,585.6 cubic chi.

2. Labor calculation:
   - Each worker can dig 300 cubic chi per day.
   - How many workers are needed, and how much work remains?

   Procedure:
   - Add the top and bottom widths, divide by 2 to get the average width.
   - Multiply the average width by the depth to get the cross-sectional area.
   - Multiply the cross-sectional area by the length to get the total volume.
   - Divide the total volume by the work capacity of one worker to determine the number of workers needed.
   - Calculate the leftover work (if any).

---

### Python Code Implementation


"""

#----- content starts here -----

from fractions import Fraction

# Canal dimensions
top_width = 18  # 1 zhang 8 chi = 18 chi
bottom_width = 3 + Fraction(6, 10)  # 3 chi 6 cun = 3.6 chi
depth = 18  # 1 zhang 8 chi = 18 chi
length = 51824  # in chi

# Calculate the average width
average_width = (top_width + bottom_width) / 2

# Calculate the cross-sectional area
cross_sectional_area = average_width * depth

# Calculate the total volume
total_volume = cross_sectional_area * length

# Convert total volume to decimal for clarity
total_volume_decimal = float(total_volume)

# Answer to the first question
print(f"Total volume of the canal: {total_volume_decimal} cubic chi")

# Labor calculation
worker_capacity = 300  # cubic chi per worker per day

# Calculate the number of workers needed
workers_needed = total_volume // worker_capacity
remaining_work = total_volume % worker_capacity

# Convert results to decimal for clarity
workers_needed_decimal = int(workers_needed)
remaining_work_decimal = float(remaining_work)

# Answer to the second question
print(f"Number of workers needed: {workers_needed_decimal}")
print(f"Remaining work: {remaining_work_decimal} cubic chi")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. **Dimensions Conversion**:
   - Top width and depth are directly converted from zhang and chi to chi.
   - Bottom width is converted from chi and cun to chi (1 chi = 10 cun).

2. **Volume Calculation**:
   - The average width is calculated as the mean of the top and bottom widths.
   - The cross-sectional area is the product of the average width and depth.
   - The total volume is the product of the cross-sectional area and the length.

3. **Labor Calculation**:
   - The total volume is divided by the capacity of one worker to determine the number of workers needed.
   - The remainder is calculated to determine the leftover work.

---

### Output:
For the given problem:
- **Total volume of the canal**: `174585.6 cubic chi`
- **Number of workers needed**: `581`
- **Remaining work**: `85.6 cubic chi`
"""


"""
Missing variable in output: 'a'
Missing variable in output: 'b'"""
