"""
今有穿渠上廣一丈八尺，下廣三尺六寸，深一丈八尺，袤五萬一千八百二十四尺。問︰積幾何？
荅曰：一千七萬四千五百八十五尺六寸。
秋程人功三百尺，問︰用徒幾何？
術曰：以一人功尺數，乘先到人數為實。并渠上下廣而半之，以深乘之為法。實如法得袤尺。
荅曰： a人 功。內少 b尺 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves calculating the volume of a trapezoidal prism (the canal) and determining the number of workers required to complete the work.

### Problem Breakdown:
1. **Volume Calculation**:
   - Top width: 1丈8尺 = 18尺
   - Bottom width: 3尺6寸 = 3.6尺
   - Depth: 1丈8尺 = 18尺
   - Length: 51824尺
   - Formula for the volume of a trapezoidal prism:  
     \( V = \frac{(上廣 + 下廣)}{2} \times 深 \times 袤 \)

2. **Workers Calculation**:
   - Each worker can complete 300尺 of work.
   - Determine the number of workers required to complete the canal.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions of the canal
top_width = Fraction(18)  # 1丈8尺 = 18尺
bottom_width = Fraction(3.6)  # 3尺6寸 = 3.6尺
depth = Fraction(18)  # 1丈8尺 = 18尺
length = Fraction(51824)  # 袤 = 51824尺

# Calculate the volume of the canal
average_width = (top_width + bottom_width) / 2  # Average width
volume = average_width * depth * length  # Volume in cubic 尺

# Convert volume to 尺 and 寸 (1尺 = 10寸)
volume_寸 = volume * 10  # Convert to 寸 for precision
volume_尺 = volume_寸 // 10  # Integer part in 尺
remaining_寸 = volume_寸 % 10  # Remaining part in 寸

# Assign the answer for volume
a = volume_尺
b = remaining_寸

# Worker calculation
worker_capacity = Fraction(300)  # Each worker can complete 300尺
workers = volume // worker_capacity  # Number of full workers
remaining_work = volume % worker_capacity  # Remaining work in 尺

# Assign the answer for workers
a = workers
b = remaining_work

# Results
print(f"Volume: {volume_尺}尺 {remaining_寸}寸")
print(f"Workers required: {workers}人, Remaining work: {remaining_work}尺")
#----- content ends here -----


"""


### Explanation of Variables:
- `a`: Number of workers required.
- `b`: Remaining work in 尺 after assigning full workers.

### Outputs:
- Volume of the canal in 尺 and 寸.
- Number of workers required and the remaining work in 尺.
"""


"""
Variable 'a' has wrong value. Expected: 33582, Actual: 33581
Variable 'b' has wrong value. Expected: 72/5, Actual: 40194626674287507/140737488355328"""
