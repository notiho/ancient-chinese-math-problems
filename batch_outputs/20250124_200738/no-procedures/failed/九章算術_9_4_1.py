"""
今有木長二丈，圍之三尺。葛生其下，纏木七周，上與木齊。問︰葛長幾何？
荅曰： a丈 。
"""

#----- content starts here -----
"""
Suppose there is a tree 2 zhang tall, with a circumference of 3 chi. A vine grows from the base of the tree, wrapping around the tree 7 times and reaching the top of the tree.  
Question: how long is the vine?

Answer: the vine is *a* zhang long.
"""

# 木長二丈
木長 = 2  # in zhang

# 圍之三尺
圍 = 3  # in chi

# 葛纏木七周
纏周 = 7

# Convert 木長 to chi (1 zhang = 10 chi)
木長_in_chi = 木長 * 10

# The vine forms a helical path, so its length can be calculated using the Pythagorean theorem.
# Each "wrap" of the vine forms a right triangle with:
# - one side equal to the circumference of the tree (圍)
# - the other side equal to the height of one wrap (木長_in_chi / 纏周)

# Length of one wrap of the vine
單圈長度 = (圍**2 + (木長_in_chi / 纏周)**2)**0.5

# Total length of the vine
葛長_in_chi = 單圈長度 * 纏周

# Convert the vine length back to zhang (1 zhang = 10 chi)
a = Fraction(葛長_in_chi, 10)

a  # The length of the vine in zhang#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
