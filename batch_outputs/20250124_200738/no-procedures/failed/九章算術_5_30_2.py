"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
荅曰：積 a尺 。為菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of beans leaning against a wall. The base circumference is 3 zhang, and the height is 7 chi.
Question: what is the volume of the pile, and how many hu of beans does it make?

Answer: the volume is *a* cubic chi, and it makes *b* hu of beans.
"""

# 下周三丈 (base circumference is 3 zhang)
周 = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高七尺 (height is 7 chi)
高 = 7

# The formula for the volume of a cone-like pile is: (周^2 * 高) / (36 * π)
# Using an approximation for π as 3, the formula simplifies to: (周^2 * 高) / 108
積 = Fraction(周**2 * 高, 108)

# Convert the volume (in cubic chi) to hu
# 1 hu = 10 cubic chi
為菽 = Fraction(積, 10)

# Assign results to variables a and b
a = 積
b = 為菽

# Output results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 350, Actual: 175/3
Variable 'b' has wrong value. Expected: 35000/243, Actual: 35/6"""
