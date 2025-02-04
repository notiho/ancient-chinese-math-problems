"""
今有人持金十二斤出關。關稅之，十分而取一。今關取金二斤，償錢五千。問︰金一斤值錢幾何？
荅曰： a 。
"""

#----- content starts here -----
"""
Suppose someone carries 12 jin of gold out of the border. The border tax is 1/10 of the gold. 
The border takes 2 jin of gold and compensates with 5000 qian. 
Question: how much is 1 jin of gold worth in qian?

Answer: *a* qian.
"""

from fractions import Fraction

# Total gold carried
total_gold = 12  # jin

# Tax rate
tax_rate = Fraction(1, 10)

# Gold taken as tax
gold_taken = 2  # jin

# Compensation for the gold taken
compensation = 5000  # qian

# Value of 1 jin of gold
# The tax rate implies that 1/10 of the gold should have been taken, but instead, 2 jin was taken.
# Therefore, the value of 1 jin of gold is the compensation divided by the excess gold taken.
excess_gold_taken = gold_taken - (total_gold * tax_rate)
a = Fraction(compensation, excess_gold_taken)

a#----- content ends here -----

"""
"""
