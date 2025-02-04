"""
今有兔先走一百步，犬追之二百五十步，不及三十步而止。問︰犬不止，復行幾何步及之？
術曰：置兔先走一百步，以犬走不及三十步減之，餘為法。以不及三十步乘犬追步數為實，實如法得一步。
荅曰： a步 。
"""

"""
To solve this problem, we translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given values
rabbit_steps = 100  # Rabbit's initial steps
dog_steps = 250  # Dog's steps
gap = 30  # Distance dog is short of catching the rabbit

# Calculation
a = Fraction(dog_steps * gap, rabbit_steps - gap)

# The result is stored in variable 'a'
a
#----- content ends here -----


"""


The variable `a` will contain the number of steps the dog needs to take to catch the rabbit.
"""


"""
"""
