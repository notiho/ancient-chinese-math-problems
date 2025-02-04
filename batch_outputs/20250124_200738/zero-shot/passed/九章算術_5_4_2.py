"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a人 。
"""

"""
To solve the problem, we first calculate the volume of the trapezoidal prism (積, "ji") and then determine the number of workers (徒, "a") required based on the given worker efficiency.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
lower_width = Fraction(2 * 10)  # Convert 2丈 to 尺 (1丈 = 10尺)
upper_width = Fraction(8)      # 8尺
height = Fraction(4)           # 4尺
length = Fraction(12 * 10 + 7) # Convert 12丈7尺 to 尺

# Calculate the volume (積)
# Formula for the area of a trapezoid: (lower_width + upper_width) * height / 2
# Multiply by the length to get the volume
volume = (lower_width + upper_width) * height / 2 * length

# Worker efficiency
worker_efficiency = Fraction(444)  # 444尺 per worker

# Calculate the number of workers (a)
# Formula: volume / worker_efficiency
a = volume / worker_efficiency

# The result
a
#----- content ends here -----


"""


This code calculates the number of workers (`a`) required to complete the task. The result will be stored in the variable `a` as a `Fraction`.
"""


"""
"""
