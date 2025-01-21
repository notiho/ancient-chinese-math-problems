"""
今有出錢九百八十，買矢簳五千八百二十枚。欲其貴賤率之，問︰各幾何？
反其率術曰：以錢數為法，所率為實，實如法而一。不滿法者反以實減法，法少，實多。二物各以所得多少之數乘法實，即物數。
荅曰：其 a枚 ， b枚 一錢 其 c枚 ， d枚 一錢
"""

"""
To solve this problem, we need to determine the number of arrows (矢簳) that can be bought at two different rates (貴賤). Let's translate the problem into Python code.

We are given:
- Total money: 980 (錢)
- Total arrows: 5820 (枚)
- Two rates: `a` arrows per 1 money and `c` arrows per 1 money.

The solution involves finding the values of `a`, `b`, `c`, and `d` such that:
- `a` and `c` are the number of arrows per unit of money for the two rates.
- `b` and `d` are the number of money units spent on each rate.

### Python Code:


"""


from fractions import Fraction

# Given data
total_money = 980  # Total money
total_arrows = 5820  # Total arrows

# Let the two rates be:
a = 3  # a枚 per 1錢 (higher rate)
c = 7  # c枚 per 1錢 (lower rate)

# Solve for the amount of money spent at each rate
# Let b be the money spent at rate a, and d be the money spent at rate c
# Equations:
# 1. b + d = total_money
# 2. a * b + c * d = total_arrows

# Substituting d = total_money - b into the second equation:
# a * b + c * (total_money - b) = total_arrows
# a * b + c * total_money - c * b = total_arrows
# (a - c) * b = total_arrows - c * total_money
# b = (total_arrows - c * total_money) / (a - c)

b = Fraction(total_arrows - c * total_money, a - c)
d = total_money - b

# Results
a = Fraction(a)  # a枚 per 1錢
b = Fraction(b)  # b錢 spent at rate a
c = Fraction(c)  # c枚 per 1錢
d = Fraction(d)  # d錢 spent at rate c

# Output the results
a, b, c, d


"""


### Explanation of the Code:
1. We define the total money and total arrows as `total_money` and `total_arrows`.
2. We assume two rates: `a` arrows per 1 money and `c` arrows per 1 money.
3. Using the equations:
   - `b + d = total_money`
   - `a * b + c * d = total_arrows`
   we solve for `b` (money spent at rate `a`) and `d` (money spent at rate `c`).
4. Finally, we compute the values of `a`, `b`, `c`, and `d`.

### Output:
The output will be the values of `a`, `b`, `c`, and `d` in terms of fractions.
"""


"""
Variable 'a' has wrong value. Expected: 300, Actual: 3
Variable 'b' has wrong value. Expected: 5, Actual: 260
Variable 'c' has wrong value. Expected: 5520, Actual: 7
Variable 'd' has wrong value. Expected: 6, Actual: 720"""
