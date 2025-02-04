"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
答曰： a丈 。
"""

"""
This is a classic problem involving geometry and similar triangles. Let's break it down and solve it step by step.

### Problem Breakdown:
1. A right triangle is formed by a measuring tool (偃矩) placed on the edge of a cliff.
2. The height of the vertical leg (句) of the first triangle is 6 chi (尺).
3. From the top of the vertical leg, the line of sight to the bottom of the valley intersects the horizontal leg (股) at 9 chi 1 cun (9.1 chi).
4. A second measuring tool is placed 3 zhang (丈) away horizontally from the first one.
5. From the top of the vertical leg of the second tool, the line of sight intersects the horizontal leg at 8 chi 5 cun (8.5 chi).
6. We are tasked with finding the depth of the valley (谷深).

---

### Solution:
We will use the concept of similar triangles to solve this problem.

---

### Variables:
- First triangle:
  - Vertical leg (句1): 6 chi
  - Horizontal leg (股1): 9.1 chi
- Second triangle:
  - Vertical leg (句2): 6 chi
  - Horizontal leg (股2): 8.5 chi
- Distance between the two tools: 3 zhang = 30 chi
- Depth of the valley: `a` zhang

---

### Steps:
1. Let the depth of the valley be `h` (in chi).
2. Using similar triangles, the ratio of the depth of the valley to the horizontal leg is the same for both triangles.

For the first triangle:
\[
\frac{h}{9.1} = \frac{6}{9.1}
\]

For the second triangle:
\[
\frac{h}{30 + 8.5} = \frac{6}{8.5}
\]

3. Solve these equations to find `h`.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# First triangle
句1 = 6  # Vertical leg (chi)
股1 = Fraction(91, 10)  # Horizontal leg (chi)

# Second triangle
句2 = 6  # Vertical leg (chi)
股2 = Fraction(85, 10)  # Horizontal leg (chi)

# Distance between the two tools
distance_between_tools = 30  # chi

# Depth of the valley (h)
# Using similar triangles:
# h / 股1 = 句1 / 股1
h1 = 句1 * 股1 / 句1

# h / (distance_between_tools + 股2) = 句2 / 股2
h2 = 句2 * (distance_between_tools + 股2) / 句2

# Final depth of the valley (h)
h = h1  # Both equations should yield the same result

# Convert depth to zhang (1 zhang = 10 chi)
a = Fraction(h, 10)

# Output
a
#----- content ends here -----


"""


---

### Explanation of the Code:
1. We use the `Fraction` class to ensure precise calculations with fractions.
2. The depth of the valley is calculated using the ratios derived from similar triangles.
3. The final depth is converted from chi to zhang by dividing by 10.

---

### Final Answer:
The depth of the valley is `a` zhang.
"""


"""
Variable 'a' has wrong value. Expected: 419/10, Actual: 91/100"""
