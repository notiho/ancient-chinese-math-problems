"""
今有堤，下廣五丈，上廣三丈，高二丈，長六十尺，欲以一千尺作一方。問：計幾何？
答曰： a 方。
"""

#----- content starts here -----
"""
Suppose there is a dike (堤) with the following dimensions:
- Bottom width: 5 zhang
- Top width: 3 zhang
- Height: 2 zhang
- Length: 60 chi

It is desired to calculate the volume of the dike in cubic chi (方). 

Answer: *a* cubic chi.
"""

# Dimensions of the dike
下廣 = 5 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上廣 = 3 * 10  # Convert zhang to chi
高 = 2 * 10    # Convert zhang to chi
長 = 60        # Already in chi

# Formula for the volume of a trapezoidal prism:
# Volume = (1/2) * (Bottom Width + Top Width) * Height * Length
a = Fraction(1, 2) * (下廣 + 上廣) * 高 * 長

# Result: a 方 (cubic chi)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 48, Actual: 48000"""
