"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

"""
To solve this problem, we need to distribute the tax of 100 units among three people (甲, 乙, 丙) in proportion to the amount of money they each hold. Here's the Python code to compute the values of `a`, `b`, and `c`:


"""


from fractions import Fraction

# Given amounts of money held by each person
甲 = 560
乙 = 350
丙 = 180

# Total amount of money held by all three
total_money = 甲 + 乙 + 丙

# Tax to be distributed
tax = 100

# Calculate the amount each person contributes to the tax
a = Fraction(甲 * tax, total_money)  # Contribution of 甲
b = Fraction(乙 * tax, total_money)  # Contribution of 乙
c = Fraction(丙 * tax, total_money)  # Contribution of 丙

# The results are stored in variables a, b, and c


"""


### Explanation:
1. Each person's contribution to the tax is proportional to the amount of money they hold.
2. The total money held by all three people is `甲 + 乙 + 丙`.
3. The tax is distributed proportionally using the formula:
   \[
   \text{Contribution of a person} = \frac{\text{Their money} \times \text{Tax}}{\text{Total money}}
   \]
4. The `Fraction` class is used to ensure that the results are represented as fractions if they are not integers.

### Results:
- `a` is the amount contributed by 甲.
- `b` is the amount contributed by 乙.
- `c` is the amount contributed by 丙.
"""


"""
"""
