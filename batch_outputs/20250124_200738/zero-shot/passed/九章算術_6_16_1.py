"""
今有金箠，長五尺。斬本一尺，重四斤。斬末一尺，重二斤。問︰次一尺各重幾何？
術曰：令末重減本重，餘即差率也。又置本重，以四間乘之，為下第一衰。副置，以差率減之，每尺各自為衰。副置下第一衰以為法，以本重四斤遍乘列衰，各自為實。實如法得一斤。
荅曰：末一尺，重 a斤 。次一尺， 重 b斤 。次一尺， 重 c斤 。次一尺， 重 d斤 。次一尺， 重 e斤
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a gold rod of 5 feet in length, with the weight of the first and last foot given, and we need to calculate the weight of each of the intermediate feet.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
total_length = 5  # in feet
weight_first_foot = 4  # in jin
weight_last_foot = 2  # in jin

# Step 1: Calculate the rate of decrease per foot
rate_of_decrease = Fraction(weight_first_foot - weight_last_foot, total_length - 1)

# Step 2: Calculate the weight of each foot
a = weight_last_foot  # weight of the last foot
b = a + rate_of_decrease  # weight of the second-to-last foot
c = b + rate_of_decrease  # weight of the third foot from the end
d = c + rate_of_decrease  # weight of the fourth foot from the end
e = d + rate_of_decrease  # weight of the fifth foot from the end (first foot)

# Print the results
a, b, c, d, e
#----- content ends here -----


"""


### Explanation:
1. **Rate of Decrease**: The difference in weight between the first and last foot is divided by the number of intervals (4 intervals for 5 feet) to find the rate of decrease per foot.
2. **Weights**: Starting from the last foot (2 jin), we add the rate of decrease successively to calculate the weights of the intermediate feet.

### Output:
The variables `a`, `b`, `c`, `d`, and `e` will hold the weights of the respective feet in jin.
"""


"""
"""
