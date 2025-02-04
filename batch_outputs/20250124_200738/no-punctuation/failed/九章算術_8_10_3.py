"""
今有二馬一牛價過一萬如半馬之價一馬二牛價不滿一萬如半牛之價問牛馬價各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗
荅曰馬價 a錢 牛價 b錢 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving simultaneous equations. Let's break it down step by step and translate it into Python code.

The problem states:
- The price of 2 horses and 1 cow exceeds 10,000 by the price of half a horse.
- The price of 1 horse and 2 cows is less than 10,000 by the price of half a cow.
- We are tasked with finding the price of one horse and one cow.

The procedure (術) for solving this uses the "fangcheng" method, which involves systematically eliminating variables to solve for unknowns.

### Equations:
1. \( 2x + y = 10000 + \frac{x}{2} \)  
   Simplifies to: \( \frac{5x}{2} + y = 10000 \)  
   Multiply through by 2 to eliminate fractions:  
   \( 5x + 2y = 20000 \)  

2. \( x + 2y = 10000 - \frac{y}{2} \)  
   Simplifies to: \( x + \frac{5y}{2} = 10000 \)  
   Multiply through by 2 to eliminate fractions:  
   \( 2x + 5y = 20000 \)  

We now have the system of equations:
1. \( 5x + 2y = 20000 \)  
2. \( 2x + 5y = 20000 \)  

We will solve this using the fangcheng method.

---

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Coefficients of the equations
# Equation 1: 5x + 2y = 20000
a1, b1, c1 = 5, 2, 20000

# Equation 2: 2x + 5y = 20000
a2, b2, c2 = 2, 5, 20000

# Step 1: Eliminate one variable (e.g., y) using the fangcheng method
# Multiply the first equation by 5 (coefficient of y in the second equation)
# Multiply the second equation by 2 (coefficient of y in the first equation)
factor1 = b2  # 5
factor2 = b1  # 2

new_a1 = a1 * factor1  # 5 * 5 = 25
new_b1 = b1 * factor1  # 2 * 5 = 10
new_c1 = c1 * factor1  # 20000 * 5 = 100000

new_a2 = a2 * factor2  # 2 * 2 = 4
new_b2 = b2 * factor2  # 5 * 2 = 10
new_c2 = c2 * factor2  # 20000 * 2 = 40000

# Subtract the second equation from the first to eliminate y
final_a = new_a1 - new_a2  # 25 - 4 = 21
final_c = new_c1 - new_c2  # 100000 - 40000 = 60000

# Solve for x
x = Fraction(final_c, final_a)  # x = 60000 / 21

# Step 2: Substitute x back into one of the original equations to solve for y
# Using the first equation: 5x + 2y = 20000
y = Fraction(c1 - a1 * x, b1)  # y = (20000 - 5x) / 2

# Results
a = x  # Price of one horse
b = y  # Price of one cow

print(f"馬價 a = {a} 錢")
print(f"牛價 b = {b} 錢")
#----- content ends here -----


"""


---

### Explanation of the Code:
1. The coefficients of the equations are defined based on the simplified system of equations.
2. The fangcheng method is applied to eliminate one variable (in this case, \( y \)) by aligning the coefficients of \( y \) in both equations and subtracting.
3. After eliminating \( y \), the resulting equation is solved for \( x \) (price of one horse).
4. The value of \( x \) is substituted back into one of the original equations to solve for \( y \) (price of one cow).
5. The results are printed as fractions for exact values.

---

### Final Answer:
The prices of the horse and cow are given as fractions of money (錢).
"""


"""
Variable 'a' has wrong value. Expected: 60000/11, Actual: 20000/7
Variable 'b' has wrong value. Expected: 20000/11, Actual: 20000/7"""
