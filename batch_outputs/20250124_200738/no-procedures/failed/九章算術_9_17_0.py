"""
今有邑，東西七里，南北九里，各中開門。出東門十五里有木。問︰出南門幾何步而見木？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a city. The city is 7 li from east to west and 9 li from south to north, with gates in the middle of each side.
There is a tree 15 li east of the east gate. 

Question: How many bu must one walk from the south gate to see the tree?

Answer: *a* bu.
"""

# Define the dimensions of the city
東西 = 7  # li
南北 = 9  # li

# Distance from the east gate to the tree
東門到木 = 15  # li

# The south gate is at the midpoint of the southern side of the city.
# The east gate is at the midpoint of the eastern side of the city.
# The distance from the south gate to the east gate forms one leg of a right triangle,
# and the distance from the east gate to the tree forms the other leg.

# The distance from the south gate to the east gate is half the north-south distance:
南門到東門 = 南北 / 2  # li

# Use the Pythagorean theorem to calculate the hypotenuse (distance from the south gate to the tree):
南門到木 = (南門到東門**2 + 東門到木**2)**0.5  # li

# Convert the result from li to bu (1 li = 300 bu):
a = 南門到木 * 300  # bu

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 315, Actual: 4698.1379290097475"""
