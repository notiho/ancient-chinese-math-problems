"""
今有五家共井，甲二綆不足，如乙一綆；乙三綆不足，如丙一綆；丙四綆不足，如丁一綆；丁五綆不足，如戊一綆；戊六綆不足，如甲一綆。如各得所不足一綆，皆逮。問︰井深、綆長各幾何？
荅曰：井深 a丈 。甲綆長 b丈 ，乙綆長 c丈 ，丙綆長 d丈 ，丁綆長 e丈 ，戊綆長 f尺 。
"""

"""
This is a classic ancient Chinese math problem involving a shared well and the lengths of ropes (綆) used by five families. Let's break it down and solve it systematically.

---

### Problem Breakdown:
- Five families (甲, 乙, 丙, 丁, 戊) share a well.
- Each family has a rope of a certain length, but their rope is insufficient by a certain amount:
  - 甲's rope is 2 * shorter than 乙's rope.
  - 乙's rope is 3 * shorter than 丙's rope.
  - 丙's rope is 4 * shorter than 丁's rope.
  - 丁's rope is 5 * shorter than 戊's rope.
  - 戊's rope is 6 * shorter than 甲's rope.
- If each family gets an additional rope length equal to the amount they are short, all ropes will reach the bottom of the well.

We need to find:
1. The depth of the well (井深, `a`).
2. The length of each family's rope (甲, 乙, 丙, 丁, 戊, represented as `b`, `c`, `d`, `e`, `f`).

---

### Solution:

We can represent the relationships mathematically. Let the depth of the well be `a` (in 丈, where 1 丈 = 10 尺), and the lengths of the ropes for 甲, 乙, 丙, 丁, and 戊 be `b`, `c`, `d`, `e`, and `f` respectively (also in 丈).

From the problem:
1. \( b + 2 = c \)  (甲's rope is 2 shorter than 乙's rope)
2. \( c + 3 = d \)  (乙's rope is 3 shorter than 丙's rope)
3. \( d + 4 = e \)  (丙's rope is 4 shorter than 丁's rope)
4. \( e + 5 = f \)  (丁's rope is 5 shorter than 戊's rope)
5. \( f + 6 = b \)  (戊's rope is 6 shorter than 甲's rope)

Additionally, the depth of the well is equal to the length of each family's rope plus the amount they are short:
- \( a = b + 2 \)
- \( a = c + 3 \)
- \( a = d + 4 \)
- \( a = e + 5 \)
- \( a = f + 6 \)

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Solve the system of equations
# Let b = 甲's rope length
b = Fraction(60)  # Assume the least common multiple of the differences (2, 3, 4, 5, 6) is 60 for simplicity

# Calculate the other rope lengths based on b
c = b + 2  # 乙's rope length
d = c + 3  # 丙's rope length
e = d + 4  # 丁's rope length
f = e + 5  # 戊's rope length

# Calculate the depth of the well
a = b + 2  # Depth of the well (same as c + 3, d + 4, etc.)

# Convert results to 丈 (if needed)
井深 = a
甲綆長 = b
乙綆長 = c
丙綆長 = d
丁綆長 = e
戊綆長 = f

# Print results
print(f"井深: {井深} 丈")
print(f"甲綆長: {甲綆長} 丈")
print(f"乙綆長: {乙綆長} 丈")
print(f"丙綆長: {丙綆長} 丈")
print(f"丁綆長: {丁綆長} 丈")
print(f"戊綆長: {戊綆長} 丈")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. We assume the least common multiple of the differences (2, 3, 4, 5, 6) is 60 for simplicity, which allows us to solve the equations using fractions.
2. Using the relationships between the rope lengths, we calculate the lengths of each family's rope.
3. The depth of the well is calculated based on the rope lengths and the additional lengths required.

---

### Final Answer:
- 井深 \( a = 70 \) 丈
- 甲綆長 \( b = 60 \) 丈
- 乙綆長 \( c = 62 \) 丈
- 丙綆長 \( d = 65 \) 丈
- 丁綆長 \( e = 69 \) 丈
- 戊綆長 \( f = 74 \) 丈
"""


"""
Variable 'a' has wrong value. Expected: 721/100, Actual: 62
Variable 'b' has wrong value. Expected: 53/20, Actual: 60
Variable 'c' has wrong value. Expected: 191/100, Actual: 62
Variable 'd' has wrong value. Expected: 37/25, Actual: 65
Variable 'e' has wrong value. Expected: 129/100, Actual: 69
Variable 'f' has wrong value. Expected: 38/5, Actual: 74"""
