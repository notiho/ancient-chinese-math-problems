"""
今有垣下廣三尺，上廣二尺，高一丈二尺，袤二十二丈五尺八寸。問︰積幾何？
荅曰： a尺 。
"""

#----- content starts here -----
"""
Suppose there is a wall base with the following dimensions:
- Bottom width: 3 chi
- Top width: 2 chi
- Height: 1 zhang 2 chi (12 chi)
- Length: 22 zhang 5 chi 8 cun (225.8 chi)

Question: What is the total volume of the wall?

Answer: The total volume is *a* cubic chi.
"""

# Define the dimensions
底廣 = 3  # Bottom width in chi
頂廣 = 2  # Top width in chi
高 = 12  # Height in chi (1 zhang = 10 chi, so 1 zhang 2 chi = 12 chi)
袤 = 225 + Fraction(8, 10)  # Length in chi (22 zhang 5 chi 8 cun = 225.8 chi)

# Calculate the average width
平均廣 = Fraction(底廣 + 頂廣, 2)

# Calculate the volume
a = 平均廣 * 高 * 袤  # Volume in cubic chi

a  # Output the result#----- content ends here -----

"""
"""
