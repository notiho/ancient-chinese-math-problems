"""
今有邱田周六百四十步徑三百八十步。問：為田㡬何？
術曰：列周六百四十步半之得三百二十步又列徑三百八十步半之得一百九十步二位相乘得六萬八百步以畝法除之即得。
答曰： a頃 奇 b步 。
"""

"""
To solve this problem, we need to compute the area of the field (田) based on the given dimensions. The problem describes a rectangular field where the 周 (perimeter) is 640 steps, and the 徑 (diagonal) is 380 steps. The solution involves calculating the area of the field and converting it into the appropriate units (頃 and 步).

Here is the Python code to compute the solution:


"""


from fractions import Fraction

# Given values
周 = 640  # Perimeter in steps
徑 = 380  # Diagonal in steps

# Step 1: Compute half of the 周 (perimeter) and half of the 徑 (diagonal)
半周 = Fraction(周, 2)  # Half of the perimeter
半徑 = Fraction(徑, 2)  # Half of the diagonal

# Step 2: Multiply the two halves to get the area in square steps
面積 = 半周 * 半徑  # Area in square steps

# Step 3: Convert the area into 頃 and 步
# 1 頃 = 10000 square steps
a = 面積 // 10000  # Number of 頃
b = 面積 % 10000  # Remaining 步

# Results
a = int(a)  # Convert to integer for 頃
b = int(b)  # Convert to integer for 步

# The answer is stored in variables a (頃) and b (步)


"""


### Explanation of the Code:
1. **Step 1**: Compute half of the 周 (perimeter) and half of the 徑 (diagonal). These are given as 640 steps and 380 steps, respectively.
2. **Step 2**: Multiply the two halves to calculate the area in square steps.
3. **Step 3**: Convert the area into 頃 and 步. Since 1 頃 equals 10,000 square steps, we use integer division (`//`) to find the number of 頃 and the remainder (`%`) to find the remaining 步.

### Final Answer:
The variables `a` and `b` will contain the number of 頃 and 步, respectively.
"""


"""
Variable 'a' has wrong value. Expected: 253/100, Actual: 6
Variable 'b' has wrong value. Expected: 80, Actual: 800"""
