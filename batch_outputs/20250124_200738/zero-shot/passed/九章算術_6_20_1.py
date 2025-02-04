"""
今有甲發長安，五日至齊；乙發齊，七日至長安。今乙發已先二日，甲乃發長安。問︰幾何日相逢？
術曰：并五日、七日以為法。以乙先發二日減七日，餘，以乘甲日數為實。實如法得一日。
荅曰： a日 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
time_甲_to_齊 = 5  # days
time_乙_to_長安 = 7  # days
乙_先發 = 2  # days

# Calculation
法 = time_甲_to_齊 + time_乙_to_長安  # Combine 5 days and 7 days
餘 = time_乙_to_長安 - 乙_先發  # Subtract 2 days from 7 days
實 = 餘 * time_甲_to_齊  # Multiply the remainder by 甲's travel time
a = Fraction(實, 法)  # Divide the product by the combined time

# The answer
a  # a is the number of days until they meet
#----- content ends here -----


"""


The variable `a` will contain the solution in days as a `Fraction`.
"""


"""
"""
