"""
今有隄下廣二丈，上廣八尺，高四尺，袤一十二丈七尺。問︰積幾何？
荅曰：七千一百一十二尺。
冬程人功四百四十四尺。問︰用徒幾何？
術曰：以積尺為實，程功尺數為法，實如法而一，即用徒人數。
荅曰： a人 。
"""

#----- content starts here -----
"""
Suppose there is an embankment with the following dimensions:
- Bottom width: 2 zhang
- Top width: 8 chi
- Height: 4 chi
- Length: 12 zhang and 7 chi

Question 1: What is the total volume of the embankment?
Answer: 7112 cubic chi.

For labor calculation:
The winter work rate is 444 cubic chi per person.
Question 2: How many workers are needed?

The procedure says: Take the total volume in cubic chi as the dividend.
Take the work rate in cubic chi per person as the divisor.
Divide the dividend by the divisor, and the result is the number of workers.

Answer: *a* workers.
"""

# Dimensions of the embankment
下廣 = 2 * 10  # Convert zhang to chi (1 zhang = 10 chi)
上廣 = 8  # chi
高 = 4  # chi
袤 = 12 * 10 + 7  # Convert zhang and chi to total chi

# Volume calculation
# The cross-sectional area is the average of the top and bottom widths multiplied by the height.
截面積 = Fraction((下廣 + 上廣), 2) * 高
積尺 = 截面積 * 袤  # Total volume in cubic chi

# Winter work rate
程功尺數 = 444  # cubic chi per person

# Calculate the number of workers
a = Fraction(積尺, 程功尺數)  # Number of workers needed#----- content ends here -----

"""
"""
