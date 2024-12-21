#今有田廣十五步從十六步問爲田幾何
#方田術曰廣從步數相乘得積步以畝法二百四十步除之卽畝數百畝爲一頃
#荅曰 a畝

"""
Suppose there is a field with a width of 15 bu and a length of 16 bu.
Question: how large of a field does it make?

The procedure for rectangular fields says: The numbers of bu in width and length are multiplied with each other, obtaining the [number of] accumulated bu.
When dividing it by the mu-divisor, 240, it is the number of mu.
100 mu make 1 qing.

The answer says: *a* mu.
"""

#廣十五步
廣步數 = 15

#從十六
從步數 = 16

#廣從步數相乘得積步
積步 = 廣步數 * 從步數

#畝法二百四十步
畝法 = 240

#以畝法二百四十步除之卽畝數
畝數 = Fraction(積步, 畝法)

a = 畝數
