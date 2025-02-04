"""
今有委菽依垣，下周三丈，高七尺。問︰積及為菽各幾何？
委粟術曰：下周自乘，以高乘之，三十六而一。其依垣者，十八而一。其依垣內角者，九而一。程粟一斛，積二尺七寸。其米一斛，積一尺六寸、五分寸之一。其菽、答、麻、麥一斛，皆二尺四寸、十分寸之三。
荅曰：積 a尺 。為菽 b斛 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the step-by-step breakdown:

1. **Understand the problem**:  
   - We are given a structure with a base perimeter of 3丈 (30尺) and a height of 7尺.
   - The problem asks for the total volume (積, denoted as `a`) and the amount of 菽 (a type of grain) it can hold (denoted as `b`).

2. **Ancient formula**:  
   - The volume of a structure depends on its shape:
     - For a base perimeter (下周), the formula is:  
       \[ \text{Volume} = \frac{\text{Base Perimeter}^2 \times \text{Height}}{36} \]
   - For structures leaning against a wall (依垣), the formula is:  
       \[ \text{Volume} = \frac{\text{Base Perimeter}^2 \times \text{Height}}{18} \]
   - For structures leaning against a corner (依垣內角), the formula is:  
       \[ \text{Volume} = \frac{\text{Base Perimeter}^2 \times \text{Height}}{9} \]

3. **Grain volume conversion**:  
   - 1斛 of 菽 occupies a volume of \( 2尺4寸3分 \), which is \( 2 + \frac{4}{10} + \frac{3}{100} = 2.43 \) 尺³.

4. **Implementation in Python**:  
   - Use the `Fraction` class to ensure precise calculations.

Here is the Python code:


"""


from fractions import Fraction

# Given dimensions
base_perimeter = Fraction(30)  # 3丈 = 30尺
height = Fraction(7)           # 7尺

# Volume calculation using the formula for "依垣" (leaning against a wall)
a = (base_perimeter ** 2 * height) / 18

# Volume occupied by 1斛 of 菽
volume_per_hu = Fraction(243, 100)  # 2尺4寸3分 = 2.43尺³

# Calculate the amount of 菽 the structure can hold
b = a / volume_per_hu

# Results
a  # Total volume in 尺³
b  # Amount of 菽 in 斛


"""


### Explanation of the Code:
1. **Base Perimeter and Height**: These are given as 30尺 and 7尺, respectively.
2. **Volume Calculation**: The formula for a structure leaning against a wall is used.
3. **菽 Volume Conversion**: The volume of 1斛 of 菽 is converted to a fraction for precise calculations.
4. **Final Results**: The total volume (`a`) and the amount of 菽 (`b`) are computed.

### Output:
- `a`: Total volume in 尺³.
- `b`: Amount of 菽 in 斛.
"""


"""
"""
