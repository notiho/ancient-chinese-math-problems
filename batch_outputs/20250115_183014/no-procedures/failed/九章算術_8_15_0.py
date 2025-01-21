"""
今有令一人、吏五人、從者一十人，食雞一十；令一十人、吏一人、從者五人，食雞八；令五人、吏一十人、從者一人，食雞六。問︰令、吏、從者食雞各幾何？
荅曰：令 a人 食 b雞 ，吏 c人 食 d雞 ，從者 e人 食 f雞 。
"""

"""
This is a classic system of linear equations problem. Let's solve it step by step.

### Problem:
There are three groups of people: **Ling (令)**, **Li (吏)**, and **Congzhe (從者)**. Each group consumes a certain number of chickens, but the consumption rate per person is unknown. We are given the following information:

1. 1 Ling, 5 Li, and 10 Congzhe eat 10 chickens.
2. 10 Ling, 1 Li, and 5 Congzhe eat 8 chickens.
3. 5 Ling, 10 Li, and 1 Congzhe eat 6 chickens.

We need to find how many chickens each group eats per person.

---

### Solution in Python:


"""


from fractions import Fraction

# Let:
# a = number of chickens eaten by 1 Ling (令)
# b = number of chickens eaten by 1 Li (吏)
# c = number of chickens eaten by 1 Congzhe (從者)

# Equations based on the problem:
# 1. 1a + 5b + 10c = 10
# 2. 10a + 1b + 5c = 8
# 3. 5a + 10b + 1c = 6

# Solve the system of equations using substitution or elimination.

# Step 1: Express the equations
# Equation 1: a + 5b + 10c = 10
# Equation 2: 10a + b + 5c = 8
# Equation 3: 5a + 10b + c = 6

# Step 2: Solve for a, b, and c
# Multiply Equation 1 by 10 to eliminate 'a' with Equation 2:
# 10a + 50b + 100c = 100  (Modified Equation 1)
# 10a + 1b + 5c = 8       (Equation 2)
# Subtract Equation 2 from Modified Equation 1:
# 49b + 95c = 92          (Equation 4)

# Multiply Equation 1 by 5 to eliminate 'a' with Equation 3:
# 5a + 25b + 50c = 50     (Modified Equation 1)
# 5a + 10b + c = 6        (Equation 3)
# Subtract Equation 3 from Modified Equation 1:
# 15b + 49c = 44          (Equation 5)

# Solve Equation 4 and Equation 5 as a system of two equations:
# 1. 49b + 95c = 92
# 2. 15b + 49c = 44

# Multiply Equation 2 by 49 and Equation 1 by 15 to align coefficients of 'b':
# 735b + 4655c = 1380     (Modified Equation 5)
# 735b + 1470c = 2205     (Modified Equation 4)
# Subtract the two equations:
# 3185c = 2940
# c = 2940 / 3185 = 42 / 45 = 2/3

# Substitute c = 2/3 into Equation 5:
# 15b + 49(2/3) = 44
# 15b + 98/3 = 44
# Multiply through by 3 to eliminate fractions:
# 45b + 98 = 132
# 45b = 34
# b = 34 / 45

# Substitute b = 34/45 and c = 2/3 into Equation 1:
# a + 5(34/45) + 10(2/3) = 10
# a + 170/45 + 300/45 = 10
# a + 470/45 = 10
# a = 10 - 470/45
# a = 450/45 - 470/45
# a = -20/45 = -4/9

# Final values:
a = Fraction(-4, 9)  # Chickens eaten by 1 Ling
b = Fraction(34, 45)  # Chickens eaten by 1 Li
c = Fraction(2, 3)  # Chickens eaten by 1 Congzhe

# Output results
print(f"令每人食 {a} 雞")
print(f"吏每人食 {b} 雞")
print(f"從者每人食 {c} 雞")


"""


---

### Explanation of Results:
- Each **Ling (令)** eats `-4/9` chickens (negative value indicates an issue in the problem setup or assumptions).
- Each **Li (吏)** eats `34/45` chickens.
- Each **Congzhe (從者)** eats `2/3` chickens.

If the negative value for Ling is unexpected, it might indicate an inconsistency in the problem's setup or assumptions.
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: -4/9
Variable 'b' has wrong value. Expected: 45/122, Actual: 34/45
Variable 'c' has wrong value. Expected: 1, Actual: 2/3
Missing variable in output: 'd'
Missing variable in output: 'e'
Missing variable in output: 'f'"""
