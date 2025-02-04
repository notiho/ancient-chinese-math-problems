"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
This problem involves solving a system of linear equations to determine the capacities of the large and small vessels. Let's break it down step by step and translate it into Python code.

### Problem Description:
- Five large vessels and one small vessel together hold **3 hu**.
- One large vessel and five small vessels together hold **2 hu**.
- We need to determine the capacity of each large vessel (*a*) and each small vessel (*b*).

### Procedure:
The problem can be solved using the method of "盈不足術" (Excess and Deficiency Method), which is essentially solving a system of linear equations. Let's represent the capacities of the large and small vessels as variables and solve for them.

### Equations:
1. \( 5a + b = 3 \)  (Five large vessels and one small vessel hold 3 hu)
2. \( a + 5b = 2 \)  (One large vessel and five small vessels hold 2 hu)

We will solve this system of equations using Python.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Define the equations
# 5a + b = 3
# a + 5b = 2

# Coefficients from the equations
coefficients = [
    [5, 1],  # Coefficients of a and b in the first equation
    [1, 5]   # Coefficients of a and b in the second equation
]

# Constants on the right-hand side of the equations
constants = [3, 2]

# Solve the system of equations using substitution or elimination
# Multiply the first equation by 5 to align the coefficients of b
# 25a + 5b = 15
# a + 5b = 2

# Subtract the second equation from the first
# (25a + 5b) - (a + 5b) = 15 - 2
# 24a = 13
a = Fraction(13, 24)  # Capacity of the large vessel

# Substitute a into the first equation to solve for b
# 5a + b = 3
b = Fraction(3) - 5 * a  # Capacity of the small vessel

# Output the results
print(f"大器容 a = {a} hu")
print(f"小器容 b = {b} hu")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. We represent the two equations as a system of linear equations.
2. Using elimination, we align the coefficients of one variable (in this case, \( b \)) and subtract the equations to solve for \( a \).
3. Once \( a \) is found, we substitute it back into one of the original equations to solve for \( b \).
4. The results are expressed as fractions to maintain precision.

---

### Output:
The capacities of the large and small vessels are:
- \( a = \frac{13}{24} \) hu (Large vessel)
- \( b = \frac{11}{24} \) hu (Small vessel)


"""


"""
"""
