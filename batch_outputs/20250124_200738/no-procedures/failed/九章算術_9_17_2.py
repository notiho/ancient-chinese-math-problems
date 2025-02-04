"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a city, 7 li from east to west and 9 li from south to north, with gates in the middle of each side.
There is a tree 15 li east of the east gate.
Question: how many bu must one walk out of the south gate to see the tree?

Answer: *a* bu.
"""

# Define the dimensions of the city
東西 = 7  # li
南北 = 9  # li

# Distance from the east gate to the tree
東門到木 = 15  # li

# The south gate is in the middle of the southern wall, so its distance to the tree forms a right triangle.
# The horizontal leg of the triangle is the distance from the south gate to the tree, which is half the city's width plus the distance from the east gate to the tree.
水平距離 = 東門到木 + 東西 / 2  # li

# The vertical leg of the triangle is half the city's height.
垂直距離 = 南北 / 2  # li

# Use the Pythagorean theorem to calculate the hypotenuse (distance from the south gate to the tree in li).
距離_里 = (水平距離**2 + 垂直距離**2)**0.5  # li

# Convert the distance from li to bu (1 li = 300 bu).
a = Fraction(距離_里 * 300)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 315, Actual: 196256978540651/34359738368"""
