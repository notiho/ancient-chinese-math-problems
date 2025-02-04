"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This is a classic ancient Chinese math problem involving a shared well and the lengths of ropes used by five families. Let's solve it step by step.

### Problem Breakdown:
- Five families (甲, 乙, 丙, 丁, 戊) share a well.
- Each family has a rope of a certain length, but their rope is insufficient by a certain amount:
  - 甲's rope is 2 *綆* shorter than 乙's rope.
  - 乙's rope is 3 *綆* shorter than 丙's rope.
  - 丙's rope is 4 *綆* shorter than 丁's rope.
  - 丁's rope is 5 *綆* shorter than 戊's rope.
  - 戊's rope is 6 *綆* shorter than 甲's rope.
- If each family adds the amount they are short (1 *綆*), all the ropes will reach the bottom of the well.

### Goal:
Find:
1. The depth of the well (`井深`).
2. The length of each family's rope (`綆長`).

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Let the depth of the well be `a` (in 丈), and each family's rope length be variables:
# 甲 = b, 乙 = c, 丙 = d, 丁 = e, 戊 = f (all in 丈).

# Equations based on the problem:
# 1. b + 2 = c
# 2. c + 3 = d
# 3. d + 4 = e
# 4. e + 5 = f
# 5. f + 6 = b
# 6. Each family's rope + 1 = depth of the well: b + 1 = c + 1 = d + 1 = e + 1 = f + 1 = a

# Solve step by step:
# From equation (1): c = b + 2
# From equation (2): d = c + 3 = (b + 2) + 3 = b + 5
# From equation (3): e = d + 4 = (b + 5) + 4 = b + 9
# From equation (4): f = e + 5 = (b + 9) + 5 = b + 14
# From equation (5): b = f + 6 = (b + 14) + 6 = b + 20
# This implies b = b + 20, which is a contradiction unless we consider modular arithmetic.

# To simplify, we solve for the depth of the well:
井深 = Fraction(井深)
#----- content ends here -----


"""



"""


"""
Code error: name '井深' is not defined"""
