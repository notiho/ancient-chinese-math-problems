"""
今有差丁夫五百人合共重車一百一十三乘問各共重幾何
術曰置人數為實車數為法而一得四人共重又置一於上方命之實餘返減法訖以四加十一方一得五人共重法餘即四人共重車數實餘即五人共重車數
答曰 a乘 乘各 b人 共重 c乘 乘各 d人 共重
"""

#----- content starts here -----
"""
Suppose there are 500 workers of varying strength, collectively loading 113 carts.
Question: how many carts are loaded by groups of 4 workers and groups of 5 workers, respectively?

The procedure says: Place the number of workers as the dividend and the number of carts as the divisor.
Divide, obtaining the number of carts loaded by 4 workers.
Then, place 1 at the top and assign it as the dividend.
Subtract the remainder from the divisor and continue until complete.
Add 4 to 11, then divide, obtaining the number of carts loaded by 5 workers.
The remainder of the divisor corresponds to the carts loaded by groups of 4 workers.
The remainder of the dividend corresponds to the carts loaded by groups of 5 workers.

Answer: *a* carts, each loaded by *b* workers, collectively loading *c* carts, and *d* carts, each loaded by *e* workers, collectively loading.
"""

# Total workers and carts
workers = 500
carts = 113

# Step 1: Divide workers into groups of 4
group_of_4_carts = workers // 4
remaining_workers_after_4 = workers % 4

# Step 2: Divide remaining workers into groups of 5
group_of_5_carts = remaining_workers_after_4 // 5
remaining_workers_after_5 = remaining_workers_after_4 % 5

# Step 3: Calculate the carts loaded by groups of 4 and 5
a = group_of_4_carts
b = 4
c = group_of_5_carts
d = 5#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 65, Actual: 125
Variable 'c' has wrong value. Expected: 48, Actual: 0"""
