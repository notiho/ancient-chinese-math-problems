"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

"""
To solve this problem, we need to distribute the tax of 100 coins among three people (甲, 乙, 丙) in proportion to the amount of money they each hold. The amounts held by 甲, 乙, and 丙 are 560, 350, and 180 coins, respectively. Let’s compute the contributions of each person using Python.

Here is the Python code:


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

# Contributions proportional to the money held
a = Fraction(money_甲, total_money) * tax
b = Fraction(money_乙, total_money) * tax
c = Fraction(money_丙, total_money) * tax

# Results
a, b, c


"""


### Explanation:
1. The total money held by all three people is calculated as `560 + 350 + 180`.
2. Each person's contribution to the tax is proportional to the amount of money they hold. For example, 甲's contribution is `(甲's money / total money) * tax`.
3. The `Fraction` class is used to ensure precise fractional calculations.

### Solution:
After running the code, the values of `a`, `b`, and `c` will represent the amounts of tax paid by 甲, 乙, and 丙, respectively.
"""


"""
"""
