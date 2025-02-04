"""
今有邑方二百步，各中開門。出東門十五步有木。問︰出南門幾何步而見木？
荅曰： a步 。
"""

#----- content starts here -----
"""
Suppose there is a square city with each side measuring 200 bu. Each side has a gate in the middle.
There is a tree located 15 bu east of the east gate. 
Question: how many bu must one walk out of the south gate to see the tree?

Answer: *a* bu.
"""

# Define the dimensions of the city
邑邊長 = 200  # Each side of the city is 200 bu

# The east gate is in the middle of the eastern side
東門位置 = Fraction(邑邊長, 2)  # 200 / 2 = 100 bu from the southern edge

# The tree is 15 bu east of the east gate
木位置東 = 15
木位置南 = 東門位置  # The tree is aligned with the east gate in the north-south direction

# The south gate is in the middle of the southern side
南門位置東 = Fraction(邑邊長, 2)  # 200 / 2 = 100 bu from the western edge
南門位置南 = 0  # The south gate is at the southern edge

# Calculate the distance from the south gate to the tree
水平距離 = 木位置東 + 南門位置東  # Horizontal distance between the south gate and the tree
垂直距離 = 木位置南 - 南門位置南  # Vertical distance between the south gate and the tree

# Use the Pythagorean theorem to calculate the distance
a = Fraction(垂直距離**2 + 水平距離**2).sqrt()  # Distance from the south gate to the tree#----- content ends here -----

"""
Code error: 'Fraction' object has no attribute 'sqrt'"""
