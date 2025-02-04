"""
今有甲發長安，五日至齊；乙發齊，七日至長安。今乙發已先二日，甲乃發長安。問︰幾何日相逢？
術曰：并五日、七日以為法。以乙先發二日減七日，餘，以乘甲日數為實。實如法得一日。
荅曰： a日 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
days_甲_to_齊 = 5  # 甲 takes 5 days to reach 齊
days_乙_to_長安 = 7  # 乙 takes 7 days to reach 長安
乙_先發_days = 2  # 乙 departs 2 days earlier than 甲

# Calculation
法 = days_甲_to_齊 + days_乙_to_長安  # Combine 5 days and 7 days as the "法"
餘 = days_乙_to_長安 - 乙_先發_days  # Subtract 2 days from 7 days
實 = 餘 * days_甲_to_齊  # Multiply the remainder by 甲's travel days
a = Fraction(實, 法)  # Divide the product by the "法" to get the meeting time

# The answer
a  # The number of days until they meet


"""


The variable `a` will hold the solution in days as a `Fraction`.
"""


"""
"""
