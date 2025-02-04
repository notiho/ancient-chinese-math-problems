"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a city, 7 li from east to west, and 9 li from south to north, with gates in the middle of each side.
There is a tree 15 li east of the east gate.
Question: how many bu must one walk from the south gate to see the tree?

Answer: *a* bu.
"""

# Conversion factor: 1 li = 300 bu
li_to_bu = 300

# Dimensions of the city
east_west = 7  # li
south_north = 9  # li

# Distance from the east gate to the tree
distance_to_tree = 15  # li

# The south gate is in the middle of the south side, so its position is 7/2 li (half of east-west distance).
# The east gate is in the middle of the east side, so its position is 9/2 li (half of south-north distance).

# The distance from the south gate to the tree forms a right triangle:
# - One leg is the distance from the south gate to the east gate (half of the south-north distance).
# - The other leg is the distance from the east gate to the tree.

# Calculate the legs of the triangle
leg1 = south_north / 2  # li
leg2 = distance_to_tree  # li

# Use the Pythagorean theorem to calculate the hypotenuse (distance from the south gate to the tree)
distance_in_li = (leg1**2 + leg2**2)**0.5  # li

# Convert the distance to bu
a = distance_in_li * li_to_bu

a  # Result in bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 315, Actual: 4698.1379290097475"""
