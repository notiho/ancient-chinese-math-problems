"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This is a classic ancient Chinese math problem involving a shared well and the lengths of ropes (綆) used by five families. Each family has a rope that is shorter than the required depth of the well, and the relationships between their rope lengths are described. The goal is to find the depth of the well and the length of each family's rope.

---

### Problem Breakdown:
1. Let the depth of the well be `a` (in 丈, where 1 丈 = 10 尺).
2. Let the rope lengths of the five families (甲, 乙, 丙, 丁, 戊) be `b`, `c`, `d`, `e`, and `f` respectively (in 丈).
3. The relationships are:
   - 甲's rope is 2 丈 too short, so `b + 2 = a`.
   - 乙's rope is 3 丈 too short, so `c + 3 = a`.
   - 丙's rope is 4 丈 too short, so `d + 4 = a`.
   - 丁's rope is 5 丈 too short, so `e + 5 = a`.
   - 戊's rope is 6 丈 too short, so `f + 6 = a`.
4. If each family receives an additional 1 丈 of rope, all ropes will be sufficient to reach the bottom of the well.

---

### Solution in Python:


"""

#----- content starts here -----

from fractions import Fraction

# Let the depth of the well be 'a' (in 丈)
# Let the rope lengths of 甲, 乙, 丙, 丁, 戊 be 'b', 'c', 'd', 'e', 'f' respectively (in 丈)

# Relationships:
# b + 2 = a
# c + 3 = a
# d + 4 = a
# e + 5 = a
# f + 6 = a

# If each family gets an additional 1 丈 of rope, all ropes will be sufficient:
# b + 1 = c + 1 = d + 1 = e + 1 = f + 1 = a

# Solve for a (depth of the well):
a = Fraction(2 + 3 + 4 + 5 + 6 + 5, 5)  # Average depth considering all relationships

# Solve for each rope length:
b = a - 2
c = a - 3
d = a - 4
e = a - 5
f = a - 6

# Output results:
井深 = a
甲綆長 = b
乙綆長 = c
丙綆長 = d
丁綆長 = e
戊綆長 = f

井深, 甲綆長, 乙綆長, 丙綆長, 丁綆長, 戊綆長
#----- content ends here -----


"""


---

### Explanation of the Code:
1. The depth of the well `a` is calculated as the average of the relationships described.
2. Each family's rope length is then calculated by subtracting their respective "shortfall" from the depth of the well.
3. The results are expressed as fractions to ensure precision.

---

### Final Answer:
- 井深 `a` 丈
- 甲綆長 `b` 丈
- 乙綆長 `c` 丈
- 丙綆長 `d` 丈
- 丁綆長 `e` 丈
- 戊綆長 `f` 丈
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 5
Variable 'b' has wrong value. Expected: 53/20, Actual: 3
Variable 'c' has wrong value. Expected: 191/100, Actual: 2
Variable 'd' has wrong value. Expected: 37/25, Actual: 1
Variable 'e' has wrong value. Expected: 129/100, Actual: 0
Variable 'f' has wrong value. Expected: 38/5, Actual: -1"""
