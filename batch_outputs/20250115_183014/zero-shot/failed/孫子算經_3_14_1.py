"""
今有粟一十二萬八千九百四十斛九斗三合，出與人買絹一匹，直粟三斛五斗七升。問：絹幾何？
術曰：置粟一十二萬八千九百四十斛九斗三合為實，以三斛五斗七升為法，除之，得匹餘四十之所得，又以法除之，即得。
答曰： a匹 b丈 。
"""

"""
To solve this problem, we need to compute how many pieces of silk ("絹") can be purchased with the given amount of grain ("粟"). The grain is measured in "斛", "斗", and "合", and the price of one piece of silk is given in the same units. The solution involves dividing the total amount of grain by the price of one piece of silk.

Here is the Python code to compute the values of `a` (the number of full pieces of silk) and `b` (the remaining fraction of a piece of silk expressed in tenths):


"""


from fractions import Fraction

# Total amount of grain in terms of "斛", "斗", and "合"
total_grain = 128940 + Fraction(9, 10) + Fraction(3, 100)

# Price of one piece of silk in terms of "斛", "斗", and "升"
price_per_silk = 3 + Fraction(5, 10) + Fraction(7, 100)

# Compute the total number of silk pieces
total_silk = total_grain / price_per_silk

# Separate into full pieces (a) and the remaining fraction (b)
a = int(total_silk)  # Full pieces of silk
b = (total_silk - a) * 10  # Remaining fraction expressed in tenths

# Print the results
a, b


"""


This code calculates the number of full pieces of silk (`a`) and the remaining fraction (`b`) based on the given problem.
"""


"""
Variable 'b' has wrong value. Expected: 18/5, Actual: 1080/119"""
