"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
答曰： a丈 。
"""

"""
This is a classic ancient Chinese geometry problem involving similar triangles. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
1. A carpenter's square (right triangle) is placed on the edge of a cliff. The vertical leg (the "upright") is 6 chi (尺) tall.
2. From the top of the vertical leg, the line of sight to the bottom of the valley intersects the horizontal leg (the "base") at a distance of 9 chi 1 cun (9.1 chi).
3. Another carpenter's square is placed 3 zhang (丈) away horizontally from the first one.
4. From the top of the second vertical leg, the line of sight to the bottom of the valley intersects the horizontal leg at a distance of 8 chi 5 cun (8.5 chi).
5. The question asks for the depth of the valley (谷深), denoted as `a` zhang.

### Solution:
This problem involves similar triangles. Using the properties of similar triangles, we can set up equations to solve for the depth of the valley.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
句高 = 6  # Height of the vertical leg in chi
下股 = Fraction(91, 10)  # Horizontal distance for the first square (9 chi 1 cun = 9.1 chi)
矩間 = 30  # Distance between the two carpenter's squares in chi (3 zhang = 30 chi)
上股 = Fraction(85, 10)  # Horizontal distance for the second square (8 chi 5 cun = 8.5 chi)

# Let the depth of the valley be `a` (in chi)
# Using similar triangles, we know:
# Depth of valley = (句高 * 矩間) / (下股 - 上股)

a = (句高 * 矩間) / (下股 - 上股)

# Convert depth from chi to zhang (1 zhang = 10 chi)
a_in_zhang = a / 10

# Output the result
a_in_zhang
#----- content ends here -----


"""


---

### Explanation of the Formula:
1. The depth of the valley is proportional to the height of the vertical leg (句高) and the distance between the two carpenter's squares (矩間).
2. The difference in the horizontal distances (下股 - 上股) determines the slope of the line of sight.
3. Using the formula for similar triangles, the depth of the valley is calculated as:

   \[
   a = \frac{\text{句高} \times \text{矩間}}{\text{下股} - \text{上股}}
   \]

4. Finally, the result is converted from chi to zhang.

---

### Final Answer:
The depth of the valley, `a`, will be calculated in zhang using the above Python code.
"""


"""
Variable 'a' has wrong value. Expected: 419/10, Actual: 300"""
