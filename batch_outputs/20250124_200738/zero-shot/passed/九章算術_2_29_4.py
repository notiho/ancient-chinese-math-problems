"""
今有麥八斗六升、七分升之三，欲為小䵂，問︰得幾何？
術曰：以麥求小䵂，三之，十而一。
荅曰：為小䵂 a斗 。
"""

"""
To solve this problem, we need to calculate the total amount of wheat (麥) in terms of a single unit (斗), then divide it by 10/3 (as the problem states "三之，十而一," which means 1 small 䵂 requires 10/3 of a 斗). Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Total wheat in terms of 斗
wheat = Fraction(8) + Fraction(6, 10) + Fraction(3, 70)

# Amount of wheat required for 1 small 䵂
wheat_per_small_䵂 = Fraction(10, 3)

# Calculate the number of small 䵂
a = wheat / wheat_per_small_䵂

# Result
a  # This is the number of small 䵂
#----- content ends here -----


"""


The variable `a` will contain the solution in terms of the number of small 䵂.
"""


"""
"""
