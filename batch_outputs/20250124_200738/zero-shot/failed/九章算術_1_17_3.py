"""
又有三人，三分人之一，分六錢三分錢之一，四分錢之三。問：人得幾何？
經分術曰：以人數為法，錢數為實，實如法而一。有分者通之；重有分者同而通之。
荅曰：人得 a錢 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. The problem involves dividing money among three people, with fractions of people and money involved. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
people = Fraction(3)  # Total people
money = Fraction(6) + Fraction(3, 10) + Fraction(3, 4)  # Total money

# Calculate money per person
a = money / people

# Output the result
a  # This represents the money each person gets
#----- content ends here -----


"""


The variable `a` will hold the value of money each person gets.
"""


"""
Variable 'a' has wrong value. Expected: 17/8, Actual: 47/20"""
