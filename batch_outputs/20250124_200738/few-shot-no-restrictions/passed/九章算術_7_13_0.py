"""
今有大器五、小器一容三斛；大器一、小器五容二斛。問︰大、小器各容幾何？
術曰：假令大器五斗，小器亦五斗，盈一十斗。令之大器五斗五升，小器二斗五升，不足二斗。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰：大器容 a斛 ，小器容 b斛 。
"""

"""
This is a classic "excess and deficit" problem from ancient Chinese mathematics. Let's solve it step by step using Python.

### Problem Statement:
There are two types of containers: large containers and small containers.  
- 5 large containers and 1 small container hold 3 hu.  
- 1 large container and 5 small containers hold 2 hu.  

Question: How much does each large container and each small container hold?

### Procedure:
The method involves using the "excess and deficit" algorithm:
1. Assume hypothetical values for the capacities of the large and small containers.
2. Use the given conditions to calculate the total capacity and compare it to the actual values (excess or deficit).
3. Solve the system of equations using the excess and deficit method.

### Python Code:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
# 5 large containers + 1 small container = 3 hu
# 1 large container + 5 small containers = 2 hu
large_rate_1 = 5
small_rate_1 = 1
total_1 = 3  # in hu

large_rate_2 = 1
small_rate_2 = 5
total_2 = 2  # in hu

# Step 1: Calculate excess and deficit
# Assume large container = 1 hu and small container = 1 hu
# Calculate the excess or deficit for each scenario
excess_1 = large_rate_1 * 1 + small_rate_1 * 1 - total_1  # Excess for the first condition
excess_2 = large_rate_2 * 1 + small_rate_2 * 1 - total_2  # Excess for the second condition

# Step 2: Use the excess and deficit method
# Multiply the rates by the respective excess/deficit values
numerator_large = small_rate_2 * total_1 - small_rate_1 * total_2
numerator_small = large_rate_1 * total_2 - large_rate_2 * total_1
denominator = large_rate_1 * small_rate_2 - large_rate_2 * small_rate_1

# Step 3: Solve for the capacities
large_capacity = Fraction(numerator_large, denominator)
small_capacity = Fraction(numerator_small, denominator)

# Output the results
a = large_capacity
b = small_capacity

print(f"Large container capacity: {a} hu")
print(f"Small container capacity: {b} hu")
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input the given data**: The rates of large and small containers in each scenario and the total capacities.
2. **Calculate excess/deficit**: Assume both containers have a capacity of 1 hu and calculate the excess or deficit for each scenario.
3. **Apply the excess and deficit method**: Use the formula to solve for the capacities of the large and small containers.
4. **Output the results**: The capacities of the large and small containers are expressed as fractions for precision.

### Answer:
The capacities of the large and small containers are:
- Large container: **a hu**
- Small container: **b hu**
"""


"""
"""
