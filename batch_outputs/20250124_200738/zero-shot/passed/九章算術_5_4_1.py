"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a人 。
"""

"""
To solve the problem, we need to compute the number of workers ("a") required based on the given dimensions and the work rate.

### Step 1: Calculate the volume of the trapezoidal prism
The base of the trapezoidal prism has a width of 2丈 (20尺), the top has a width of 8尺, the height of the trapezoid is 4尺, and the length of the prism is 12丈7尺 (127尺). The formula for the volume of a trapezoidal prism is:

\[
\text{Volume} = \frac{\text{Base Width} + \text{Top Width}}{2} \times \text{Height} \times \text{Length}
\]

### Step 2: Calculate the number of workers
The work rate is given as 444尺 per worker. The formula to calculate the number of workers is:

\[
\text{Workers} = \frac{\text{Volume}}{\text{Work Rate}}
\]

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Dimensions
base_width = Fraction(20)  # 2丈 = 20尺
top_width = Fraction(8)    # 8尺
height = Fraction(4)       # 4尺
length = Fraction(127)     # 12丈7尺 = 127尺

# Work rate
work_rate = Fraction(444)  # 444尺 per worker

# Step 1: Calculate the volume
volume = (base_width + top_width) / 2 * height * length  # Volume in cubic 尺

# Step 2: Calculate the number of workers
a = volume / work_rate  # Number of workers

# Results
a
#----- content ends here -----


"""


### Explanation of Variables:
- `base_width`: Width of the base of the trapezoid in 尺.
- `top_width`: Width of the top of the trapezoid in 尺.
- `height`: Height of the trapezoid in 尺.
- `length`: Length of the prism in 尺.
- `work_rate`: Work rate in 尺 per worker.
- `volume`: Total volume of the trapezoidal prism in cubic 尺.
- `a`: Number of workers required.

### Final Answer:
The value of `a` will be the number of workers required.
"""


"""
"""
