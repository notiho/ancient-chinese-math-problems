"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
答曰： a丈 。
"""

"""
This is a classic ancient Chinese mathematics problem involving geometry and similar triangles. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
1. A carpenter's square (a right triangle) is placed on the edge of a cliff.
2. The vertical leg (the "upright") of the square is 6 chi (尺) tall.
3. From the top of the vertical leg, the bottom of the valley is observed, and the horizontal leg (the "base") extends 9 chi and 1 cun (寸) into the valley.
4. Another carpenter's square is placed 3 zhang (丈) away horizontally from the first square.
5. From the top of the second square's vertical leg, the bottom of the valley is observed again, and the horizontal leg extends 8 chi and 5 cun into the valley.
6. The task is to calculate the depth of the valley.

---

### Conversion:
1 zhang = 10 chi  
1 chi = 10 cun  

---

### Solution:
We use the concept of similar triangles to solve this problem. The depth of the valley is the unknown variable.


"""


from fractions import Fraction

# Given values
句高 = 6  # The height of the vertical leg (in chi)
第一次入下股 = 9 + Fraction(1, 10)  # 9 chi 1 cun = 9.1 chi
矩間相去 = 3 * 10  # 3 zhang = 30 chi
第二次入上股 = 8 + Fraction(5, 10)  # 8 chi 5 cun = 8.5 chi

# Let the depth of the valley be "谷深" (in chi)
# Using similar triangles:
# For the first observation: 谷深 / 第一次入下股 = 句高 / (谷深 - 句高)
# For the second observation: 谷深 / 第二次入上股 = 句高 / (谷深 - 句高 - 矩間相去)

# Solve the equations:
# 1. 谷深 / 第一次入下股 = 句高 / (谷深 - 句高)
# Cross-multiply:
# 谷深 * (谷深 - 句高) = 第一次入下股 * 句高
# 谷深^2 - 谷深 * 句高 = 第一次入下股 * 句高

# 2. 谷深 / 第二次入上股 = 句高 / (谷深 - 句高 - 矩間相去)
# Cross-multiply:
# 谷深 * (谷深 - 句高 - 矩間相去) = 第二次入上股 * 句高
# 谷深^2 - 谷深 * (句高 + 矩間相去) = 第二次入上股 * 句高

# Define the two equations:
def equation1(谷深):
    return 谷深**2 - 谷深 * 句高 - 第一次入下股 * 句高

def equation2(谷深):
    return 谷深**2 - 谷深 * (句高 + 矩間相去) - 第二次入上股 * 句高

# Solve the equations numerically (trial and error or approximation)
谷深 = Fraction(60, 1)  # Initial guess (in chi)

# Iterate to refine the solution
for _ in range(100):
    if abs(equation1(谷深)) < Fraction(1, 1000) and abs(equation2(谷深)) < Fraction(1, 1000):
        break
    谷深 -= Fraction(equation1(谷深) + equation2(谷深), 2 * 谷深)  # Adjust using a simple numerical method

# Convert the depth to zhang
a = 谷深 / 10  # 1 zhang = 10 chi

# Output the result
a


"""


### Explanation of the Code:
1. The problem is solved using the concept of similar triangles and two equations derived from the observations.
2. The equations are solved numerically using an iterative method to approximate the depth of the valley.
3. The final result is converted from chi to zhang for the answer.

### Final Answer:
The depth of the valley is approximately `a` zhang.
"""


"""
Variable 'a' has wrong value. Expected: 419/10, Actual: 16719919234950967935900479960403681233096969111714787211572596313071213439324490173550013729335083203362239749369586562472073360351363406355599302357/7185459187521228373567744962895106462878289978886797448990283124265478785278426123855679760725066684710240947640394785535365602050909191313978349562"""
