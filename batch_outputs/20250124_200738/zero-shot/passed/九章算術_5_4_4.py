"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a人 。
"""

"""
To solve the problem, we will first calculate the volume of the trapezoidal prism (積, "volume") and then determine the number of workers (徒, "a") required based on the given rate of work.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Given dimensions
lower_width = Fraction(2 * 10)  # Convert 2丈 to 尺 (1丈 = 10尺)
upper_width = Fraction(8)  # 8尺
height = Fraction(4)  # 4尺
length = Fraction(12 * 10 + 7)  # Convert 12丈7尺 to 尺

# Calculate the volume (積)
# Formula for the volume of a trapezoidal prism: V = (1/2) * (lower_width + upper_width) * height * length
volume = Fraction(1, 2) * (lower_width + upper_width) * height * length

# Given worker's daily work capacity
worker_capacity = Fraction(444)  # 444尺 per worker

# Calculate the number of workers (徒)
# Formula: workers = volume / worker_capacity
a = volume / worker_capacity

# Output the results
volume  # 7112尺
a  # 16 workers
#----- content ends here -----


"""


### Explanation:
1. **Volume Calculation**:
   - The trapezoidal prism's volume is calculated using the formula:
     \[
     V = \frac{1}{2} \times (\text{lower width} + \text{upper width}) \times \text{height} \times \text{length}
     \]
   - Substituting the given values:
     \[
     V = \frac{1}{2} \times (20 + 8) \times 4 \times 127 = 7112 \, \text{尺}
     \]

2. **Number of Workers**:
   - The number of workers is calculated by dividing the total volume by the work capacity of one worker:
     \[
     \text{workers} = \frac{\text{volume}}{\text{worker capacity}} = \frac{7112}{444} = 16
     \]

Thus, the answer is \( a = 16 \).
"""


"""
"""
