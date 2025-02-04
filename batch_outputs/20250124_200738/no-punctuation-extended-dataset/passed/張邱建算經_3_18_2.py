"""
今有差丁夫五百人合共重車一百一十三乘問各共重幾何
術曰置人數為實車數為法而一得四人共重又置一於上方命之實餘返減法訖以四加十一方一得五人共重法餘即四人共重車數實餘即五人共重車數
答曰 a乘 乘各 b人 共重 c乘 乘各 d人 共重
"""

#----- content starts here -----
"""
Suppose there are 500 laborers, divided into groups of 4 and 5 people, collectively pulling 113 carts.
Question: how many carts does each group pull, and how many laborers are assigned to each cart?

The procedure says:
1. Place the total number of people as the dividend (實) and the total number of carts as the divisor (法). Divide to find how many carts are pulled by 4 people.
2. Place 1 above the quotient (商) and call it the dividend. Subtract the remainder (餘) from the divisor (法). When finished, add 4 to 11, and then divide to find how many carts are pulled by 5 people.
3. The divisor remainder (法餘) corresponds to the carts pulled by groups of 4 people, and the dividend remainder (實餘) corresponds to the carts pulled by groups of 5 people.

Answer: *a* carts pulled by groups of 4 people, with *b* people per cart, and *c* carts pulled by groups of 5 people, with *d* people per cart.
"""

# Total laborers and carts
人數 = 500
車數 = 113

# Step 1: Divide total people by total carts to find carts pulled by 4-person groups
實 = 人數
法 = 車數
四人共重 = 實 // 法  # Quotient
餘 = 實 % 法         # Remainder

# Step 2: Adjust for 5-person groups
五人共重 = 四人共重 + 1  # Add 1 to the quotient for 5-person groups
法餘 = 法 - 餘            # Remaining carts for 4-person groups
實餘 = 餘                # Remaining carts for 5-person groups

# Step 3: Assign results
a = 法餘  # Carts pulled by 4-person groups
b = 4     # People per cart for 4-person groups
c = 實餘  # Carts pulled by 5-person groups
d = 5     # People per cart for 5-person groups#----- content ends here -----

"""
"""
