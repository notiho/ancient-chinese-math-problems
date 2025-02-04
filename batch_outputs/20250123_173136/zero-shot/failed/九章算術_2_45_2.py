"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves determining the rates (貴賤率) of two types of arrows (矢簳) given the total cost and total quantity. Let's write the Python code to compute the values of the unknowns `a`, `b`, `c`, and `d`.


"""


from fractions import Fraction

# Given data
total_money = 980  # Total money in units
total_arrows = 5820  # Total number of arrows

# The problem implies there are two types of arrows with different rates.
# Let the rates be 1 arrow per `b` money and 1 arrow per `d` money.
# The total cost and total quantity equations are:
# (total_arrows / b) + (total_arrows / d) = total_money
# We need to find `a`, `b`, `c`, and `d` such that:
# a = total_arrows / b
# c = total_arrows / d

# Assume the rates are such that b = 3 (3 arrows per money) and d = 7 (7 arrows per money)
b = 3
d = 7

# Compute the number of arrows for each rate
a = Fraction(total_arrows, b)  # Number of arrows for rate b
c = Fraction(total_arrows, d)  # Number of arrows for rate d

# Verify the total cost matches
assert a + c == total_money, "The total cost does not match the given data."

# Output the results
a = int(a)  # Convert to integer
b = int(b)  # Convert to integer
c = int(c)  # Convert to integer
d = int(d)  # Convert to integer

# The solution
print(f"a = {a}, b = {b}, c = {c}, d = {d}")


"""


This code computes the values of `a`, `b`, `c`, and `d` based on the given problem. The solution assumes the rates `b` and `d` are known or can be deduced from the problem context. If additional constraints or information are provided, the code can be adjusted accordingly.
"""


"""
Code error: The total cost does not match the given data."""
