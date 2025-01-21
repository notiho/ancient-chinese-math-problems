"""
今有上禾七秉損實一斗益之下禾二秉而實一十斗下禾八秉益實一斗與上禾二秉而實一十斗問上下禾實一秉各幾何
術曰如方程損之曰益益之曰損損實一斗者其實過一十斗也益實一斗者其實不滿一十斗也
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰上禾 a秉 實 b斗 下禾 c秉 實 d斗 
"""

"""
This is a complex problem involving simultaneous equations and proportional reasoning. The problem essentially asks us to determine the yield (實) per秉 (bundle) for both the upper and lower crops (上禾 and 下禾) based on the given relationships. Let's break it down and solve it step by step using the procedure provided.

---

### Problem Setup:
We are given:
1. Seven bundles (秉) of upper crops lose one dou (斗) of yield, and when combined with two bundles of lower crops, the total yield is 10 dou.
2. Eight bundles of lower crops gain one dou of yield, and when combined with two bundles of upper crops, the total yield is 10 dou.

We need to find the yield per bundle (實) for both the upper crops (上禾) and the lower crops (下禾).

---

### Procedure:
The procedure involves setting up equations and solving them step by step using proportional reasoning.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Step 1: Define the known values
# Upper crops (上禾) and lower crops (下禾) bundles and their relationships
上禾_損 = 7  # 7 bundles of upper crops lose 1 dou
下禾_益 = 8  # 8 bundles of lower crops gain 1 dou
上禾_益 = 2  # 2 bundles of upper crops
下禾_損 = 2  # 2 bundles of lower crops

# Total yields
損_總實 = 10  # Total yield when upper crops lose and combined with lower crops
益_總實 = 10  # Total yield when lower crops gain and combined with upper crops

# Step 2: Define the equations based on the problem
# Let x = yield per bundle of upper crops (上禾實)
# Let y = yield per bundle of lower crops (下禾實)

# Equation 1: 7x - 1 + 2y = 10
# Equation 2: 8y + 1 + 2x = 10

# Step 3: Solve the equations
# Rearrange Equation 1: 7x + 2y = 11
# Rearrange Equation 2: 2x + 8y = 9

# Use substitution or elimination to solve for x and y
# Multiply Equation 1 by 4: 28x + 8y = 44
# Subtract Equation 2: (28x + 8y) - (2x + 8y) = 44 - 9
# Result: 26x = 35
x = Fraction(35, 26)  # Yield per bundle of upper crops (上禾實)

# Substitute x into Equation 1 to solve for y
# 7x + 2y = 11
# 7(Fraction(35, 26)) + 2y = 11
# Fraction(245, 26) + 2y = 11
# 2y = 11 - Fraction(245, 26)
# 2y = Fraction(286, 26) - Fraction(245, 26)
# 2y = Fraction(41, 26)
y = Fraction(41, 52)  # Yield per bundle of lower crops (下禾實)

# Step 4: Output the results
a = 7  # Upper crops bundles (上禾秉)
b = x  # Yield per bundle of upper crops (上禾實)
c = 8  # Lower crops bundles (下禾秉)
d = y  # Yield per bundle of lower crops (下禾實)

print(f"上禾 {a}秉 實 {b}斗")
print(f"下禾 {c}秉 實 {d}斗")


"""


---

### Explanation of the Code:
1. **Define Variables**: The problem is translated into two equations based on the relationships provided.
2. **Solve Equations**: The equations are solved using substitution and elimination to find the yield per bundle for both upper and lower crops.
3. **Output Results**: The results are displayed in terms of the number of bundles and the yield per bundle.

---

### Final Answer:
```
上禾 7秉 實 35/26斗
下禾 8秉 實 41/52斗
```
"""


"""
Variable 'a' has wrong value. Expected: 1, Actual: 7
Variable 'c' has wrong value. Expected: 1, Actual: 8"""
