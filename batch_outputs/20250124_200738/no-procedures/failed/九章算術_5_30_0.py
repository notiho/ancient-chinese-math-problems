"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
荅曰：積 a尺 。為菽 b斛 。
"""

#----- content starts here -----
"""
Suppose there is a pile of beans leaning against a wall. The base circumference is 3 zhang, and the height is 7 chi.
Question: what is the volume of the pile, and how many hu of beans does it contain?

Answer: the volume is *a* cubic chi, and it contains *b* hu of beans.
"""

# 下周三丈 (base circumference is 3 zhang)
base_circumference = 3 * 10  # Convert zhang to chi (1 zhang = 10 chi)

# 高七尺 (height is 7 chi)
height = 7

# Volume of a cone: V = (1/3) * base_area * height
# Base area (circle): A = (C^2) / (4 * π), where C is the circumference
# For simplicity, ancient Chinese math approximates π as 3, so:
base_area = (base_circumference ** 2) / (4 * 3)

# Volume of the pile
a = Fraction(1, 3) * base_area * height

# Convert volume to hu (1 hu = 10 cubic chi)
b = a / 10

# Results
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 350, Actual: 175.0
Variable 'b' has wrong value. Expected: 35000/243, Actual: 17.5"""
