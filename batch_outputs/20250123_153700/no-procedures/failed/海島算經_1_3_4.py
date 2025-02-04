"""
今有望深谷，偃矩岸上，令句高六尺。從句端望谷底，入下股九尺一寸。又設重矩于上，其矩間相去三丈。更從句端望谷底，入上股八尺五寸。問谷深幾何？
答曰： a丈 。
"""

"""
This is a classic problem involving geometry and similar triangles. Let's break it down step by step and translate it into Python code.

### Problem Explanation:
1. A carpenter's square (right triangle) is placed on the edge of a cliff.
2. The vertical leg (句) of the square is 6 chi (尺) tall.
3. From the top of the vertical leg, the bottom of the valley is observed, and the horizontal leg (股) extends 9 chi 1 cun (9.1 chi) into the valley.
4. Another carpenter's square is placed 3 zhang (丈) away horizontally from the first one.
5. From the top of the second vertical leg, the bottom of the valley is observed again, and the horizontal leg extends 8 chi 5 cun (8.5 chi) into the valley.
6. The goal is to calculate the depth of the valley (谷深).

---

### Python Code:


"""


from fractions import Fraction

# Known values
句高 = 6  # The height of the vertical leg (句) in chi
第一次股 = Fraction(91, 10)  # The horizontal leg (股) for the first observation in chi (9 chi 1 cun = 9.1 chi)
矩間距離 = 30  # The distance between the two carpenter's squares in chi (3 zhang = 30 chi)
第二次股 = Fraction(85, 10)  # The horizontal leg (股) for the second observation in chi (8 chi 5 cun = 8.5 chi)

# Let the depth of the valley be "谷深" (h), and the horizontal distance from the first square to the valley bottom be "x".

# Using similar triangles for the first observation:
# h / 第一次股 = 句高 / x
# h = (句高 / x) * 第一次股
# => x = (句高 * 第一次股) / h

# Using similar triangles for the second observation:
# h / (第二次股 + 矩間距離) = 句高 / x
# h = (句高 / x) * (第二次股 + 矩間距離)

# Solving for h:
# From the first equation: x = (句高 * 第一次股) / h
# Substitute x into the second equation:
# h = (句高 / ((句高 * 第一次股) / h)) * (第二次股 + 矩間距離)
# Simplify:
# h = (h / 第一次股) * (第二次股 + 矩間距離)
# h * 第一次股 = h * (第二次股 + 矩間距離)
# h = (句高 * (第二次股 + 矩間距離)) / (第一次股 - 第二次股)

# Calculate h:
谷深 = (句高 * (第二次股 + 矩間距離)) / (第一次股 - 第二次股)

# Convert chi to zhang (1 zhang = 10 chi)
谷深_丈 = 谷深 / 10

# Output the result
谷深_丈


"""


---

### Explanation of the Formula:
1. We use the property of similar triangles to relate the depth of the valley (h) to the horizontal distances (股) and the height of the vertical leg (句).
2. By setting up two equations for the two observations and solving for `h`, we derive the formula:
   \[
   h = \frac{\text{句高} \times (\text{第二次股} + \text{矩間距離})}{\text{第一次股} - \text{第二次股}}
   \]
3. Finally, we convert the depth from chi to zhang for the final answer.

---

### Final Answer:
The depth of the valley (谷深) in zhang is stored in the variable `谷深_丈`.
"""


"""
Missing variable in output: 'a'"""
