"""
今有粟七斗，三人分舂之，一人為糲米，一人為粺米，一人為鑿米，令米數等。問︰取粟為米各幾何？
術曰：列置糲米三十，粺米二十七，鑿米二十四，而反衰之，副并為法。以七斗乘未并者，各自為取粟實。實如法得一斗。若求米等者，以本率各乘定所取粟為實，以粟率五十為法，實如法得一斗。
荅曰：糲米取粟 a斗 。粺米取粟 b斗 。鑿米取粟 c斗 。為米各 d斗 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Let's compute the values of the unknowns `a`, `b`, `c`, and `d` using the given relationships.


"""


from fractions import Fraction

# Given data
total_grain = 7  # 7斗
grain_rates = [30, 27, 24]  # Rates for 糲米, 粺米, 鑿米
grain_sum_rate = sum(grain_rates)  # Sum of rates

# Compute the amount of grain each person takes (a, b, c)
a = Fraction(total_grain * grain_rates[0], grain_sum_rate)
b = Fraction(total_grain * grain_rates[1], grain_sum_rate)
c = Fraction(total_grain * grain_rates[2], grain_sum_rate)

# Compute the amount of 米 each person produces (d)
# 米 rate is 50 for all types
rice_rate = 50
d = Fraction(total_grain, rice_rate)

# Outputs
a, b, c, d


"""


### Explanation:
1. **Grain Distribution**:
   - The total grain (7斗) is divided among three people based on their respective rates: 30, 27, and 24.
   - The proportion of grain each person takes is calculated as:
     \[
     \text{Amount of grain for 糲米 (a)} = \frac{7 \times 30}{30 + 27 + 24}
     \]
     Similarly for 粺米 (b) and 鑿米 (c).

2. **米 Production**:
   - Each type of grain produces 米 at a rate of 50. Therefore, the 米 produced by each person is:
     \[
     \text{Amount of 米 (d)} = \frac{7}{50}
     \]

3. **Output**:
   - The variables `a`, `b`, `c`, and `d` represent the respective amounts of grain taken and 米 produced.

### Results:
The values of `a`, `b`, `c`, and `d` will be computed as fractions.
"""


"""
Variable 'a' has wrong value. Expected: 252/121, Actual: 70/27
Variable 'b' has wrong value. Expected: 280/121, Actual: 7/3
Variable 'c' has wrong value. Expected: 315/121, Actual: 56/27
Variable 'd' has wrong value. Expected: 756/605, Actual: 7/50"""
