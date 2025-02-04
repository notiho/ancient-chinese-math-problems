"""
今有邑東西七里南北九里各中開門出東門十五里有木問出南門幾何步而見木
術曰東門南至隅步數以乘南門東至隅步數為實以木去門步數為法實如法而一
荅曰 a步 
"""

#----- content starts here -----
"""
Suppose there is a city with an east-west length of 7 li and a north-south length of 9 li. 
Each side has a gate in the middle. 
From the east gate, the tree is 15 li away. 
Question: how many steps must one walk out of the south gate to see the tree?

The procedure says: Multiply the number of steps from the east gate to the southeast corner by the number of steps from the south gate to the southeast corner, obtaining the dividend. 
Take the distance from the tree to the east gate as the divisor. 
Divide the dividend by the divisor to obtain the number of steps.

The answer says: *a* steps.
"""

# 城邑東西七里
東西 = 7

# 南北九里
南北 = 9

# 出東門十五里有木
木距東門 = 15

# 東門南至隅步數
東門南至隅 = 南北 / 2

# 南門東至隅步數
南門東至隅 = 東西 / 2

# 以乘為實
實 = 東門南至隅 * 南門東至隅

# 以木去門步數為法
法 = 木距東門

# 實如法而一
a = Fraction(實, 法) * 1000  # Convert li to steps (assuming 1 li = 1000 steps)#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
