"""
今有戶不知高廣，竿不知長短。橫之不出四尺，從之不出二尺，邪之適出。問︰戶高、廣、袤各幾何？
術曰：從、橫不出相乘，倍，而開方除之。所得加從不出即戶廣，加橫不出即戶高，兩不出加之，得戶袤。
荅曰：廣 a尺 ，高 b尺 ，袤 c丈 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. The problem involves a door with unknown height (高), width (廣), and diagonal length (袤). The given information is that the horizontal projection of the diagonal is 4 feet, the vertical projection is 2 feet, and the diagonal exactly fits the door. Using the provided method, we will compute the values of the unknowns.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction
import math

# Given values
horizontal_projection = Fraction(4)  # 4 feet
vertical_projection = Fraction(2)   # 2 feet

# Step 1: Multiply the horizontal and vertical projections
product = horizontal_projection * vertical_projection

# Step 2: Double the product
doubled_product = product * 2

# Step 3: Take the square root of the doubled product
diagonal = Fraction(math.sqrt(doubled_product))  # This is the diagonal length in feet

# Step 4: Compute the width (廣, a) and height (高, b)
a = diagonal + vertical_projection  # Width in feet
b = diagonal + horizontal_projection  # Height in feet

# Step 5: Compute the diagonal length (袤, c) in zhang (1 zhang = 10 feet)
c = (horizontal_projection + vertical_projection) / 10  # Diagonal in zhang

# Results
a  # Width in feet
b  # Height in feet
c  # Diagonal in zhang
#----- content ends here -----


"""


### Explanation of the Code:
1. **Input Values**: The horizontal projection (4 feet) and vertical projection (2 feet) are given.
2. **Product and Doubling**: The product of the projections is doubled, as per the method described.
3. **Square Root**: The square root of the doubled product gives the diagonal length in feet.
4. **Width and Height**: The width (廣) is the diagonal plus the vertical projection, and the height (高) is the diagonal plus the horizontal projection.
5. **Diagonal in Zhang**: The total diagonal length is converted to zhang by dividing by 10.

### Final Values:
- `a`: Width of the door in feet
- `b`: Height of the door in feet
- `c`: Diagonal length of the door in zhang
"""


"""
Variable 'c' has wrong value. Expected: 1, Actual: 3/5"""
