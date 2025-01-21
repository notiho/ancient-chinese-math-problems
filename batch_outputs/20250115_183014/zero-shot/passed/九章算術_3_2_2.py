"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

"""
To solve this problem, we need to distribute the tax of 100 units among three people (甲, 乙, 丙) in proportion to the amount of money they each hold. The amounts held by 甲, 乙, and 丙 are 560, 350, and 180 units, respectively. The solution involves proportional allocation.

Here is the Python code to compute the values of `a`, `b`, and `c`:


"""


from fractions import Fraction

# Amounts of money held by 甲, 乙, 丙
money_甲 = 560
money_乙 = 350
money_丙 = 180

# Total money held by all three
total_money = money_甲 + money_乙 + money_丙

# Tax to be distributed
tax = 100

# Proportional distribution of the tax
a = Fraction(money_甲, total_money) * tax
b = Fraction(money_乙, total_money) * tax
c = Fraction(money_丙, total_money) * tax

# Results
a, b, c


"""


### Explanation:
1. Calculate the total amount of money held by all three people: `total_money = 560 + 350 + 180`.
2. Distribute the tax (100 units) in proportion to the money each person holds:
   - 甲's share: \( a = \frac{560}{560 + 350 + 180} \times 100 \)
   - 乙's share: \( b = \frac{350}{560 + 350 + 180} \times 100 \)
   - 丙's share: \( c = \frac{180}{560 + 350 + 180} \times 100 \)
3. Use the `Fraction` class to ensure exact arithmetic for non-integer results.

### Output:
The variables `a`, `b`, and `c` will contain the exact amounts of tax each person should pay, represented as fractions.
"""


"""
"""
