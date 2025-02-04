"""
今有兔先走一百步，犬追之二百五十步，不及三十步而止。問︰犬不止，復行幾何步及之？
術曰：置兔先走一百步，以犬走不及三十步減之，餘為法。以不及三十步乘犬追步數為實，實如法得一步。
荅曰： a步 。
"""

"""
To solve this problem, let's translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given values
rabbit_steps = 100  # Rabbit initially walks 100 steps
dog_chase_steps = 250  # Dog chases 250 steps
dog_falls_short = 30  # Dog falls short by 30 steps

# Calculation
a = Fraction(dog_chase_steps * dog_falls_short, rabbit_steps - dog_falls_short)

# Result
a  # This represents the number of steps the dog needs to walk to catch the rabbit


"""


The variable `a` will contain the result in steps.
"""


"""
"""
