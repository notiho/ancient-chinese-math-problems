"""
今有與人錢初一人與三錢次一人與四錢次一人與五錢以次與之轉多一錢與訖還歛聚與均分之人得一百錢問人㡬何
術曰置人得錢數以減初人錢數餘倍之以轉多錢數加之得人數
答曰 a人
"""

#----- content starts here -----
"""
Suppose there is a scenario where a person gives money to others. 
Initially, the first person receives 3 qian, the next person receives 4 qian, the next person receives 5 qian, and so on, with each subsequent person receiving 1 qian more than the previous one.
After distributing the money, the total amount is collected back and evenly redistributed among the people, with each person receiving 100 qian.
Question: how many people are there?

The procedure says: Place the amount of money each person receives after redistribution.
Subtract the amount of money the first person initially received.
Multiply the remainder by the amount by which the money increases for each subsequent person.
Add the result to the initial amount of money the first person received to obtain the number of people.

Answer: *a* people.
"""

# 每人得一百錢
每人得錢 = 100

# 初一人與三錢
初人錢 = 3

# 轉多一錢
轉多錢 = 1

# 置人得錢數，以減初人錢數
餘 = 每人得錢 - 初人錢

# 餘倍之以轉多錢數
倍之 = 餘 / 轉多錢

# 加之得人數
a = int(倍之 + 1)  # Adding 1 to include the first person#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 195, Actual: 98"""
