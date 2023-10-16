# nums1 = [3, 5, 7, 2, 8]
# nums2 = [4, 2, 9, 0, 6]
#
# for num in nums1:
#     if num not in nums2:
#         print(num)

# matrix = [[2,5,1], [3,0,6], [9,15,1], [2,7,4]]
# k = 7
# javob = []
# for i in matrix:
#     for j in i:
#         javob.append(j)
#         print(javob)

import datetime
h_sana = str(datetime.date.today())
yil = h_sana[:3]
kerakli_sana = h_sana.replace(yil, str(int(yil)))
