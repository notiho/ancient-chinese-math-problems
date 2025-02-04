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

# The formula for the volume of a cone-like pile is: (周 * 周 * 高) / 36
積 = Fraction(周 * 周 * 高, 36)

# Convert the volume into hu (1 hu = 10 cubic chi)
為菽 = Fraction(積, 10)

# Assign results
a = 積
b = 為菽#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 350, Actual: 175
Variable 'b' has wrong value. Expected: 35000/243, Actual: 35/2"""
