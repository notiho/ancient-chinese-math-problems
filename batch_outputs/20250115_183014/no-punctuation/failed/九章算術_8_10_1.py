"""
今有二馬一牛價過一萬如半馬之價一馬二牛價不滿一萬如半牛之價問牛馬價各幾何
術曰如方程損益之
方程術曰置上禾三秉中禾二秉下禾一秉實三十九斗於右方中左禾列如右方以右行上禾遍乘中行而以直除又乘其次亦以直除然以中行中禾不盡者遍乘左行而以直除左方下禾不盡者上為法下為實實即下禾之實求中禾以法乘中行下實而除下禾之實餘如中禾秉數而一即中禾之實求上禾亦以法乘右行下實而除下禾中禾之實餘如上禾秉數而一即上禾之實實皆如法各得一斗荅曰馬價 a錢 牛價 b錢 
"""

"""
This problem involves solving a system of linear equations using the ancient Chinese method of "fangcheng" (方程), which is equivalent to solving simultaneous equations. Let's break it down step by step and translate it into Python code.

The problem states:
- The price of 2 horses and 1 cow exceeds 10,000.
- The price of 1 horse and 2 cows is less than 10,000.
- The price of half a horse equals the price of half a cow.

We are tasked with finding the price of a horse (*a*) and the price of a cow (*b*).

The procedure for solving this uses the "fangcheng" method, which involves setting up a matrix-like structure and performing operations to solve for the unknowns.

---

### Python Code Implementation:


"""


from fractions import Fraction

# Define the equations based on the problem:
# 2a + b = 10000 + x (exceeds 10,000 by some amount x)
# a + 2b = 10000 - y (less than 10,000 by some amount y)
# a / 2 = b / 2 (half a horse equals half a cow, so a = b)

# From the third equation, we know:
a = b  # The price of a horse equals the price of a cow.

# Substitute a = b into the first two equations:
# 2b + b = 10000 + x -> 3b = 10000 + x
# b + 2b = 10000 - y -> 3b = 10000 - y

# Since x and y are unknown but must balance, we assume x = y = 0 for simplicity:
# 3b = 10000
b = Fraction(10000, 3)  # Solve for b (price of a cow).

# Since a = b:
a = b  # The price of a horse is the same as the price of a cow.

# Output the results:
a_price = a
b_price = b

# Answer:
print(f"馬價 a = {a_price} 錢")
print(f"牛價 b = {b_price} 錢")


"""


---

### Explanation of the Code:
1. The problem states that the price of half a horse equals the price of half a cow, so the price of a horse (*a*) equals the price of a cow (*b*).
2. Substituting this relationship into the first two equations, we simplify the system to solve for *b*.
3. The solution assumes that the excess and deficit (x and y) balance out, leading to a straightforward solution for *b*.
4. The result is expressed as a fraction to maintain precision.

---

### Final Answer:
The price of a horse (*a*) and the price of a cow (*b*) are both:

**a = b = 3333 1/3 錢 (or 10,000/3 錢).**
"""


"""
Code error: name 'b' is not defined"""
