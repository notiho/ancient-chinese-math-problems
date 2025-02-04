"""
今有二馬、一牛價過一萬，如半馬之價。一馬、二牛價不滿一萬，如半牛之價。問︰牛、馬價各幾何？
術曰：如方程，損益之。
方程術曰，置上禾三秉，中禾二秉，下禾一秉，實三十九斗，於右方。中、左禾列如右方。以右行上禾遍乘中行而以直除。又乘其次，亦以直除。然以中行中禾不盡者遍乘左行而以直除。左方下禾不盡者，上為法，下為實。實即下禾之實。求中禾，以法乘中行下實，而除下禾之實。餘如中禾秉數而一，即中禾之實。求上禾亦以法乘右行下實，而除下禾、中禾之實。餘如上禾秉數而一，即上禾之實。實皆如法，各得一斗。
荅曰：馬價 a錢 ，牛價 b錢 。
"""

"""
This problem involves solving a system of linear equations using a method similar to Gaussian elimination, as described in the ancient Chinese "fangcheng" (方程) method. Let's translate the problem and procedure into Python code.

### Problem:
Two horses and one cow together cost more than 10,000 qian, equal to the price of half a horse.  
One horse and two cows together cost less than 10,000 qian, equal to the price of half a cow.  
Question: What are the prices of a horse and a cow?

### Procedure:
The "fangcheng" method involves setting up a system of equations, performing elimination, and solving for the unknowns step by step.

### Equations:
Let:
- `x` = price of a horse (in qian)
- `y` = price of a cow (in qian)

From the problem:
1. \( 2x + y = 10000 + \frac{x}{2} \)
2. \( x + 2y = 10000 - \frac{y}{2} \)

Simplify these equations:
1. \( 2x + y - \frac{x}{2} = 10000 \) → \( \frac{4x}{2} + y - \frac{x}{2} = 10000 \) → \( \frac{7x}{2} + y = 10000 \)
2. \( x + 2y + \frac{y}{2} = 10000 \) → \( x + \frac{4y}{2} + \frac{y}{2} = 10000 \) → \( x + \frac{5y}{2} = 10000 \)

Rewriting in standard form:
1. \( 7x + 2y = 20000 \)
2. \( 2x + 5y = 20000 \)

Now solve this system using the "fangcheng" method.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 7x + 2y = 20000
a1, b1, c1 = 7, 2, 20000

# Equation 2: 2x + 5y = 20000
a2, b2, c2 = 2, 5, 20000

# Step 1: Eliminate x from the second equation
# Multiply the first equation by 2 and the second equation by 7
# to align the coefficients of x
factor1 = 2
factor2 = 7

a1_new = a1 * factor1
b1_new = b1 * factor1
c1_new = c1 * factor1

a2_new = a2 * factor2
b2_new = b2 * factor2
c2_new = c2 * factor2

# Subtract the second equation from the first to eliminate x
b_final = b1_new - b2_new
c_final = c1_new - c2_new

# Solve for y
y = Fraction(c_final, b_final)

# Step 2: Solve for x using the first equation
x = Fraction(c1 - b1 * y, a1)

# Results
a = x  # Price of a horse
b = y  # Price of a cow

# Output the results
a, b
#----- content ends here -----


"""


---

### Explanation of the Code:
1. The equations are set up based on the problem description and simplified into standard linear form.
2. The "fangcheng" method is applied to eliminate one variable (in this case, \( x \)) by aligning the coefficients of \( x \) in both equations and subtracting.
3. The resulting single-variable equation is solved for \( y \).
4. The value of \( y \) is substituted back into one of the original equations to solve for \( x \).
5. The results are expressed as fractions for exactness.

### Answer:
The price of a horse is \( a \) qian, and the price of a cow is \( b \) qian.
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 60000/31
Variable 'b' has wrong value. Expected: 20000/11, Actual: 100000/31"""
