"""
今有五雀、六燕，集稱之衡，雀俱重，燕俱輕。一雀一燕交而處，衡適平。并燕、雀重一斤。問︰燕、雀一枚各重幾何？
術曰：如方程，交易質之，各重八兩。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：雀重 a兩 ，燕重 b兩 。
"""

"""
To solve this problem using the given "方程術" (method of solving systems of equations), we will translate the procedure into Python code step by step. The problem involves determining the weights of a sparrow (雀) and a swallow (燕) based on the given conditions.

### Problem Setup:
1. Let the weight of a sparrow (雀) be `x` (in 两).
2. Let the weight of a swallow (燕) be `y` (in 两).
3. The total weight of 5 sparrows and 6 swallows is 1斤 (16两).
   - Equation 1: \( 5x + 6y = 16 \)
4. The weight of 1 sparrow and 1 swallow is equal (衡適平).
   - Equation 2: \( x = y \)

We will solve this system of equations using the "方程術" described.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Step 1: Define the equations
# Equation 1: 5x + 6y = 16
# Equation 2: x = y

# Step 2: Substitute x = y into Equation 1
# 5x + 6x = 16
# 11x = 16
# Solve for x
x = Fraction(16, 11)

# Step 3: Since x = y, assign y the same value as x
y = x

# Results
a = x  # Weight of a sparrow in 两
b = y  # Weight of a swallow in 两
#----- content ends here -----


"""


---

### Explanation of the Code:
1. We represent the weights of the sparrow and swallow as `x` and `y`, respectively.
2. Using the second equation \( x = y \), we substitute \( y \) with \( x \) in the first equation.
3. This simplifies the first equation to \( 11x = 16 \), which we solve to find \( x \).
4. Since \( x = y \), the weight of the swallow is the same as the weight of the sparrow.

---

### Final Answer:
- \( a = \frac{16}{11} \) 两 (weight of a sparrow)
- \( b = \frac{16}{11} \) 两 (weight of a swallow)
"""


"""
Variable 'a' has wrong value. Expected: 32/19, Actual: 16/11
Variable 'b' has wrong value. Expected: 24/19, Actual: 16/11"""
