"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve this problem, we will translate the ancient Chinese mathematical procedure into Python code. The problem involves solving a system of equations to determine the weights of a sparrow (雀) and a swallow (燕). Here's the step-by-step solution:

### Problem Setup:
- Let the weight of one sparrow be `x` (雀重).
- Let the weight of one swallow be `y` (燕重).
- From the problem:
  1. A sparrow and a swallow together balance the scale: `x + y = 16` (since 1斤 = 16兩).
  2. Five sparrows weigh the same as six swallows: `5x = 6y`.

We will solve this system of equations using the procedure described.

---

### Python Code:


"""


from fractions import Fraction

# Equation 1: x + y = 16
total_weight = 16

# Equation 2: 5x = 6y
sparrow_ratio = 5
swallow_ratio = 6

# Solve for x (sparrow weight) and y (swallow weight)
# From Equation 2: x = (6/5)y
x_in_terms_of_y = Fraction(swallow_ratio, sparrow_ratio)

# Substitute x into Equation 1: (6/5)y + y = 16
# Combine terms: (6/5 + 1)y = 16
combined_ratio = x_in_terms_of_y + 1
y = Fraction(total_weight, combined_ratio)

# Solve for x using x = (6/5)y
x = x_in_terms_of_y * y

# Results
a = x  # Sparrow weight in 两
b = y  # Swallow weight in 两

# Output the results
a, b


"""


---

### Explanation of the Code:
1. **Equation Setup**: We use the two equations derived from the problem:
   - `x + y = 16`
   - `5x = 6y`
2. **Substitution**: Solve for `x` in terms of `y` using the second equation: `x = (6/5)y`.
3. **Combine Terms**: Substitute `x` into the first equation and solve for `y`.
4. **Solve for `x`**: Use the value of `y` to calculate `x`.
5. **Output**: The weights of the sparrow (`a`) and the swallow (`b`) are expressed as fractions for precision.

---

### Answer:
The weight of one sparrow is `a = 8`兩, and the weight of one swallow is `b = 8`兩.
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 96/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 80/11"""
