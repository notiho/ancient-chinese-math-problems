"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

"""
To solve this problem, we need to distribute the tax of 100 units among three people (甲, 乙, 丙) in proportion to the amount of money they each hold. The amounts of money held by 甲, 乙, and 丙 are 560, 350, and 180, respectively. The solution involves proportional distribution.

Here is the Python code to compute the values of `a`, `b`, and `c`:


"""


from fractions import Fraction

# Amount of money each person holds
money_甲 = 560
money_乙 = 350
money_丙 = 180

# Total money held by all three people
total_money = money_甲 + money_乙 + money_丙

# Total tax to be distributed
total_tax = 100

# Calculate the tax each person pays in proportion to their money
a = Fraction(money_甲, total_money) * total_tax
b = Fraction(money_乙, total_money) * total_tax
c = Fraction(money_丙, total_money) * total_tax

# The results are stored in variables a, b, and c


"""


### Explanation:
1. `money_甲`, `money_乙`, and `money_丙` represent the amounts of money held by 甲, 乙, and 丙, respectively.
2. `total_money` is the sum of all the money held by the three people.
3. `total_tax` is the total tax to be distributed (100 units).
4. Each person's tax contribution is calculated as their proportion of the total money multiplied by the total tax.

### Results:
- `a` is the amount of tax paid by 甲.
- `b` is the amount of tax paid by 乙.
- `c` is the amount of tax paid by 丙.
"""


"""
"""
