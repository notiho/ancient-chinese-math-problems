"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a人 。
"""

"""
To solve this problem, let's break it into two parts:

1. Compute the volume of the trapezoidal prism (積).
2. Determine the number of workers (徒) required based on the work rate.

### Part 1: Compute the volume (積)
The trapezoidal prism has the following dimensions:
- Bottom width = 2 丈 = 20 尺
- Top width = 8 尺
- Height = 4 尺
- Length = 12 丈 7 尺 = 127 尺

The formula for the volume of a trapezoidal prism is:
\[
\text{Volume} = \frac{\text{Top width} + \text{Bottom width}}{2} \times \text{Height} \times \text{Length}
\]

### Part 2: Determine the number of workers (徒)
The total volume (積) is given in 尺³, and the work rate per worker is 444 尺³. The formula to calculate the number of workers is:
\[
\text{Workers} = \frac{\text{Volume}}{\text{Work rate per worker}}
\]

Now, let's write the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Dimensions of the trapezoidal prism
bottom_width = 20  # in 尺
top_width = 8      # in 尺
height = 4         # in 尺
length = 127       # in 尺

# Compute the volume (積)
volume = Fraction((top_width + bottom_width), 2) * height * length

# Work rate per worker
work_rate_per_worker = 444  # in 尺³

# Compute the number of workers (徒)
a = volume / work_rate_per_worker

# Results
volume, a
#----- content ends here -----


"""


### Explanation of Variables:
- `volume`: The total volume of the trapezoidal prism in 尺³.
- `a`: The number of workers required to complete the work.

When you run this code, it will compute the volume and the number of workers as fractions or integers, depending on the values.
"""


"""
"""
