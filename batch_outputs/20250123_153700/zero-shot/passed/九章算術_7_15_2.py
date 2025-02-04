"""
今有玉方一寸，重七兩；石方一寸，重六兩。今有石立方三寸，中有玉，并重十一斤。問︰玉、石重各幾何？
術曰：假令皆玉，多十三兩。令之皆石，不足十四兩。不足為玉，多為石。各以一寸之重乘之，得玉石之積重。
荅曰：玉 a寸 ，重 b斤 。石 c寸 ，重 d斤 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves finding the weights and volumes of jade ("玉") and stone ("石") in a composite cube. Here's the solution:


"""


from fractions import Fraction

# Given data
jade_weight_per_cubic_inch = Fraction(7, 1)  # 7兩 per cubic inch
stone_weight_per_cubic_inch = Fraction(6, 1)  # 6兩 per cubic inch
total_volume = 3 * 3 * 3  # 3寸立方 (3寸 x 3寸 x 3寸)
total_weight = 11 * 16  # 11斤 converted to 兩 (1斤 = 16兩)

# Step 1: Assume the entire cube is jade
all_jade_weight = jade_weight_per_cubic_inch * total_volume

# Step 2: Assume the entire cube is stone
all_stone_weight = stone_weight_per_cubic_inch * total_volume

# Step 3: Calculate the difference
excess_weight = all_jade_weight - total_weight  # Excess weight if all jade
deficit_weight = total_weight - all_stone_weight  # Deficit weight if all stone

# Step 4: Solve for the volume of jade (玉) and stone (石)
jade_volume = deficit_weight / (jade_weight_per_cubic_inch - stone_weight_per_cubic_inch)
stone_volume = total_volume - jade_volume

# Step 5: Calculate the weights of jade and stone
jade_weight = jade_volume * jade_weight_per_cubic_inch
stone_weight = stone_volume * stone_weight_per_cubic_inch

# Assign the results to the variables
a = jade_volume  # 玉 volume in cubic inches
b = jade_weight / 16  # 玉 weight in 斤
c = stone_volume  # 石 volume in cubic inches
d = stone_weight / 16  # 石 weight in 斤

# Results
a, b, c, d


"""


### Explanation of the Code:
1. **Input Data**: The weight per cubic inch of jade and stone is given as 7兩 and 6兩, respectively. The total volume of the cube is \(3^3 = 27\) cubic inches, and the total weight is 11斤 (converted to 兩 as \(11 \times 16 = 176\)兩).

2. **Assumptions**: If the entire cube were jade, it would weigh more than the actual weight. If the entire cube were stone, it would weigh less than the actual weight.

3. **Difference Calculation**: The difference in weight is used to determine the proportion of jade and stone in the composite cube.

4. **Volume and Weight Calculation**: Using the differences and the weight per cubic inch, the volumes and weights of jade and stone are calculated.

5. **Output**: The results are stored in variables `a`, `b`, `c`, and `d` as required.

### Final Results:
- `a`: Volume of jade in cubic inches.
- `b`: Weight of jade in 斤.
- `c`: Volume of stone in cubic inches.
- `d`: Weight of stone in 斤.
"""


"""
"""
