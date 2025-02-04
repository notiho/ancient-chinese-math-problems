"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
荅曰： a人 。
"""

"""
Suppose there is a dike with the following dimensions:
- Bottom width: 2 zhang
- Top width: 8 chi
- Height: 4 chi
- Length: 12 zhang 7 chi

Question 1: What is the total volume of the dike?
Answer: 7112 cubic chi.

Question 2: If one worker can handle 444 cubic chi of work, how many workers are needed?
Answer: *a* workers.
"""

# Dimensions of the dike
bottom_width = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
top_width = 8  # in chi
height = 4  # in chi
length = 12 * 10 + 7  # Convert zhang to chi and add the remaining chi

# Calculate the volume of the dike using the formula for a trapezoidal prism:
# Volume = (1/2) * (bottom_width + top_width) * height * length
volume = Fraction(1, 2) * (bottom_width + top_width) * height * length

# Verify the volume matches the given answer
assert volume == 7112, "Calculated volume does not match the given answer."

# Worker capacity
worker_capacity = 444  # in cubic chi

# Calculate the number of workers needed
a = Fraction(volume, worker_capacity)

# Final result
a
"""
"""
