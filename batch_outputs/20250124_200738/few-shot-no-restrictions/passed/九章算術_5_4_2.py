"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is a dike with the following dimensions:
- Bottom width: 2 zhang
- Top width: 8 chi
- Height: 4 chi
- Length: 12 zhang 7 chi

Question 1: What is the total volume of the dike?
Answer: 7112 cubic chi.

Question 2: If each worker can move 444 cubic chi of earth in a day, how many workers are needed?
The procedure says: Take the total volume as the dividend, and the amount of work each worker can do as the divisor. Divide the total volume by the work per worker to find the number of workers needed.

Answer: *a* workers.
"""

from fractions import Fraction

# Dimensions of the dike
bottom_width = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
top_width = 8  # chi
height = 4  # chi
length = 12 * 10 + 7  # Convert zhang and chi to total chi

# Calculate the volume of the dike
# Volume formula for a trapezoidal prism: V = (1/2) * (bottom_width + top_width) * height * length
volume = Fraction(1, 2) * (bottom_width + top_width) * height * length

# Verify the calculated volume matches the given answer
assert volume == 7112  # cubic chi

# Worker efficiency
work_per_worker = 444  # cubic chi per worker

# Calculate the number of workers needed
workers_needed = Fraction(volume, work_per_worker)

# Final answer
a = workers_needed
a#----- content ends here -----

"""
"""
