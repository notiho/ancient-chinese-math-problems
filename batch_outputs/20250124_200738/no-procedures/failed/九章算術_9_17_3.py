"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a city, 7 li from east to west, and 9 li from south to north, with gates in the middle of each side.
There is a tree 15 li east of the east gate.
Question: how many bu must one walk south from the south gate to see the tree?

Answer: *a* bu.
"""

# Define the dimensions of the city
東西 = 7  # li
南北 = 9  # li

# Distance from the east gate to the tree
東門到木 = 15  # li

# The east gate is in the middle of the east wall, so the tree is offset by half the city's north-south distance
南北偏移 = 南北 / 2  # li

# Use the Pythagorean theorem to calculate the diagonal distance from the south gate to the tree
距離 = (東門到木**2 + 南北偏移**2)**0.5  # li

# Convert the distance from li to bu (1 li = 300 bu)
a = Fraction(距離 * 300)  # bu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 315, Actual: 5165657281841673/1099511627776"""
