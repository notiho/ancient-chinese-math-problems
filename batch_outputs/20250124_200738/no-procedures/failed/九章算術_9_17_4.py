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

# Define the dimensions of the city
東西 = 7  # li
南北 = 9  # li

# Distance from the east gate to the tree
東門至木 = 15  # li

# The south gate is in the middle of the southern wall, so the horizontal distance from the south gate to the east gate is half of 東西
南門至東門 = 東西 / 2  # li

# Using the Pythagorean theorem to calculate the diagonal distance from the south gate to the tree
南門至木 = (南門至東門**2 + 東門至木**2)**0.5  # li

# Convert the result from li to bu (1 li = 300 bu)
a = Fraction(南門至木 * 300)

# Final result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 315, Actual: 5080707486494511/1099511627776"""
