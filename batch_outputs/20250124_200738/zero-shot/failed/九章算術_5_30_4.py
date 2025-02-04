"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為菽 b斛 。
"""

"""
To solve this problem, we need to calculate the volume of the grain heap (積, denoted as `a` in the answer) and the number of "斛" (a traditional Chinese unit of volume, denoted as `b` in the answer) of beans (菽) it represents.

### Problem Breakdown:
1. The grain heap is described as being against a wall:
   - The base perimeter (下周) is 3丈 (1丈 = 10尺, so 3丈 = 30尺).
   - The height (高) is 7尺.

2. The formula for the volume of the grain heap is given:
   - For the part not against the wall: `(下周自乘 × 高) ÷ 36`.
   - For the part against the wall: `(下周自乘 × 高) ÷ 18`.
   - For the inner corner against the wall: `(下周自乘 × 高) ÷ 9`.

3. The volume of one "斛" of beans (菽) is given as 2尺4寸3分 (convert this to a fraction of 尺 for calculations).

### Conversion Notes:
- 1尺 = 10寸, 1寸 = 10分.
- 2尺4寸3分 = \( 2 + \frac{4}{10} + \frac{3}{100} = \frac{243}{100} \) 尺.

### Python Code:

"""

#----- content starts here -----

from fractions import Fraction

# Given values
base_perimeter = Fraction(30)  # 下周 in 尺
height = Fraction(7)           # 高 in 尺
volume_per_hu = Fraction(243, 100)  # 1斛 of beans in 尺³

# Calculate the total volume of the grain heap
volume_not_against_wall = (base_perimeter ** 2 * height) / 36
volume_against_wall = (base_perimeter ** 2 * height) / 18
volume_inner_corner = (base_perimeter ** 2 * height) / 9

# Total volume
a = volume_not_against_wall + volume_against_wall + volume_inner_corner

# Calculate the number of "斛" of beans
b = a / volume_per_hu

# Results
a  # Total volume in 尺³
b  # Number of 斛 of beans
#----- content ends here -----


"""


### Explanation of the Code:
1. **Volume Calculation**:
   - The volume of the grain heap is calculated by summing up the contributions from the three parts: not against the wall, against the wall, and the inner corner against the wall.
   - Each part uses the formula provided in the problem.

2. **Conversion to "斛"**:
   - The total volume `a` is divided by the volume of one "斛" of beans to find the number of "斛" (`b`).

3. **Units**:
   - All calculations are performed in terms of 尺³, ensuring consistency.

### Results:
- `a`: The total volume of the grain heap in 尺³.
- `b`: The number of "斛" of beans the grain heap represents.
"""


"""
Variable 'a' has wrong value. Expected: 350, Actual: 1225
Variable 'b' has wrong value. Expected: 35000/243, Actual: 122500/243"""
