"""
今有甲持錢五百六十，乙持錢三百五十，丙持錢一百八十，凡三人俱出關，關稅百錢。欲以錢數多少衰出之，問︰各幾何？
術曰：各置錢數為列衰，副并為法，以百錢乘未并者，各自為實，實如法得一錢。
荅曰：甲出 a錢 。乙出 b錢 。丙出 c錢 。
"""

"""
To solve this problem, we need to distribute the tax of 100 units among three people (甲, 乙, 丙) in proportion to the amount of money they each hold. Here's how we can compute the values of `a`, `b`, and `c` in Python:


"""


from fractions import Fraction

# Given amounts of money each person holds
甲 = 560
乙 = 350
丙 = 180

# Total amount of money held by all three
total_money = 甲 + 乙 + 丙

# Tax to be distributed
tax = 100

# Calculate the amount each person contributes to the tax
a = Fraction(甲 * tax, total_money)
b = Fraction(乙 * tax, total_money)
c = Fraction(丙 * tax, total_money)

# Results
a, b, c


"""


### Explanation:
1. Each person's contribution to the tax is proportional to the amount of money they hold.
2. The total money held by all three is `甲 + 乙 + 丙`.
3. The tax is distributed proportionally:  
   - 甲's contribution: \( \text{甲's money} \times \frac{\text{tax}}{\text{total money}} \)  
   - 乙's contribution: \( \text{乙's money} \times \frac{\text{tax}}{\text{total money}} \)  
   - 丙's contribution: \( \text{丙's money} \times \frac{\text{tax}}{\text{total money}} \)  

### Output:
The variables `a`, `b`, and `c` will hold the contributions of 甲, 乙, and 丙 respectively as fractions.
"""


"""
"""
