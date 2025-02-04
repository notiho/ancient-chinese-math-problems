"""
假令有粟五千一百四十石，欲作方窖、圓窖各一，令口小底大，方面於圓徑等，兩深亦同，其深少於下方七尺，多於上方一丈四尺，盛各滿中而粟適盡。問：方、徑、深各多少？
術曰：以四十二乘斛法，以乘粟，七十五而一，為方亭積。令方差自乘，三而一，為隅陽冪，以截多乘之，減積，余為實。以多乘差，加冪，為方法。多加差，為廉法，從。開立方除之，即上方。加差，即合所問。
答曰：上方徑各 a尺 ，下方徑各 b丈 ，深各 c丈 。
"""

"""
This problem is quite complex and involves ancient Chinese mathematical techniques for solving cubic equations. The problem describes a scenario where grain is stored in two types of pits (square and circular), and the dimensions of these pits are related. The solution involves calculating the dimensions of the pits based on the given constraints.

Let's break this down step by step and translate the procedure into Python code:

---

### Problem Description:
- There are **5140 shi** of grain.
- Two pits are to be constructed: one square and one circular.
- The pits have:
  - A smaller opening at the top and a larger base at the bottom.
  - The square side length of the opening is equal to the diameter of the circular opening.
  - The depths of the pits are the same.
  - The depth is **7 chi less than the bottom side length** and **1 zhang 4 chi more than the top side length**.
- Both pits are filled to capacity, and the grain is exactly used up.

### Procedure:
1. Multiply **42 by the volume conversion factor** (斛法).
2. Multiply the result by the total grain (粟).
3. Divide by 75 to get the **square pit's volume** (方亭積).
4. Use the square difference method to calculate the dimensions:
   - Compute the **difference of the sides** (差).
   - Square the difference and divide by 3 to get the **corner surplus** (隅陽冪).
   - Multiply the surplus by the larger side and subtract from the volume to get the **actual volume** (實).
   - Use the larger side and the difference to calculate the **method for the square side** (方法) and the **method for the edge** (廉法).
5. Solve the cubic equation to find the **top side length** (上方).
6. Add the difference to get the **bottom side length** (下方).
7. Use the relationship between depth and side lengths to find the **depth** (深).

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction
from math import isclose

# 粟五千一百四十石
粟 = 5140

# 斛法
斛法 = 42

# Multiply 斛法 by 粟 and divide by 75 to get 方亭積
方亭積 = Fraction(斛法 * 粟, 75)

# 差 (difference between bottom and top side lengths)
差 = Fraction(7 + 14, 10)  # 7 chi + 1 zhang 4 chi = 7 + 14 chi = 21 chi = 2.1 zhang

# 隅陽冪: 差自乘，三而一
隅陽冪 = Fraction(差**2, 3)

# 實: 方亭積減隅陽冪乘多 (多 = bottom side length)
# We need to solve for 多 (bottom side length)
# 方方法: 多乘差，加冪
# 廉法: 多加差

# Iterative solution to find 多 (bottom side length)
for 多 in range(1, 100):  # Test integer values for 多 in zhang
    多 = Fraction(多)
    方法 = 多 * 差 + 隅陽冪
    廉法 = 多 + 差
    上方 = 方亭積 / 方法  # Solve for top side length
    if isclose(float(上方), float(多 - 差), rel_tol=1e-9):  # Check if solution satisfies the equation
        break

# 上方 (top side length)
上方 = 多 - 差

# 下方 (bottom side length)
下方 = 多

# 深 (depth): 下方 - 7 chi = 上方 + 1 zhang 4 chi
深 = 下方 - Fraction(7, 10)

# Final answers
a = 上方  # Top side length (in zhang)
b = 下方  # Bottom side length (in zhang)
c = 深    # Depth (in zhang)

print(f"上方徑各 {a} 尺")
print(f"下方徑各 {b} 丈")
print(f"深各 {c} 丈")
#----- content ends here -----


"""


---

### Explanation of Variables:
- `粟`: Total grain in shi.
- `斛法`: Conversion factor for volume.
- `方亭積`: Volume of the square pit.
- `差`: Difference between the bottom and top side lengths.
- `隅陽冪`: Corner surplus, calculated using the square of the difference.
- `多`: Bottom side length (to be solved iteratively).
- `方法`: Method for the square side.
- `廉法`: Method for the edge.
- `上方`: Top side length.
- `下方`: Bottom side length.
- `深`: Depth of the pit.

This code follows the ancient procedure step by step and solves for the dimensions of the pits.
"""


"""
Variable 'a' has wrong value. Expected: 7, Actual: 969/10
Variable 'b' has wrong value. Expected: 14/5, Actual: 99
Variable 'c' has wrong value. Expected: 21/10, Actual: 983/10"""
