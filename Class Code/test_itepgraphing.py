import numpy as np
import matplotlib.pyplot as plt

N = 7
menMeans = np.array([22.3, 30.4, 31.9, 34.0, 37.5, 39.2, 40.8])
womenMeans = np.array([0.4, 0.8, 4.8, 9.5, 12.3, 15.5, 18.4])
menStd = (2, 3, 4, 1, 2)
womenStd = (3, 5, 2, 3, 3)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, menMeans, width)
p2 = plt.bar(ind, womenMeans, width, bottom=menMeans)

plt.ylabel('Millions of Connections')
plt.title('Fixed Connections With Downstream Speeds over 25 Mbps')
plt.xticks(ind, ('Jun 2013', 'Dec 2013', 'Jun 2014', 'Dec 2014', 'Jun 2015', 'Dec 2015', 'Jun 2016'))
plt.yticks(np.arange(0, 50, 10))
plt.legend((p1[0], p2[0]), ('25-100 Mbps', '100+ Mbps'))

plt.show()

N = 5
wireline = np.array([.114, .125, .125, .141, .158])
aDSL = np.array([.420,.598,.761, .938, 1.239])
cable = np.array([30.769, 36.095, 40.646, 45.530, 48.694])
fttp = np.array([4.603, 5.542, 6.870, 7.691, 8.599])
fixed_wireless = np.array([.019, .028, .047, .055, .068])

ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

p1 = plt.bar(ind, cable, width)
p2 = plt.bar(ind, fttp, width, bottom=cable)
p3 = plt.bar(ind, aDSL, width)
p4 = plt.bar(ind, wireline, width)
p5 = plt.bar(ind, fixed_wireless, width)

plt.ylabel('Millions of Connections')
plt.title('Fixed Connections With Downstream Speeds over 25 Mbps by Technology Type')
plt.xticks(ind, ('Jun 2014', 'Dec 2014', 'Jun 2015', 'Dec 2015', 'Jun 2016'))
plt.yticks(np.arange(0, 60, 10))
plt.legend((p1[0], p2[0], p3[0], p4[0], p5[0]), ('Cable Modem', 'FTTP', 'aDSL', 'Other Wireline', 'Fixed Wireless'))

plt.show()

x = [1,2,3,4,5,6,7,8,9,10]
med_2016 = [0.49, 0.58, 0.62, 0.64, 0.68, 0.69, 0.72, 0.74, 0.77, 0.87]
med_2014 = [0.45, 0.53, 0.57, 0.59, 0.62, 0.64, 0.65, 0.68, 0.73, 0.83]
plt.ylabel('Median Subscribership Ratio')
plt.xlabel('County Median Household Income by Decile')
plt.title('Subscribership Ratio based Upon Median Household Income')
plt.plot(x,med_2016,'bo-',label='2016 values')
plt.plot(x,med_2014,'ro-',label='2014 values')
plt.legend()
plt.show()

x = [1,2,3,4,5,6,7,8,9,10]
med_2016 = [0.53, 0.58, 0.61, 0.65, 0.65, 0.69, 0.72, 0.74, 0.80, 0.88]
med_2014 = [0.48, 0.53, 0.55, 0.59, 0.61, 0.64, 0.66, 0.69, 0.75, 0.84]
plt.ylabel('Median Subscribership Ratio')
plt.xlabel('County Share of College Graduates by Decile')
plt.title('Subscribership Ratio based Upon Share of College Graduates')
plt.plot(x,med_2016,'bo-',label='2016 values')
plt.plot(x,med_2014,'ro-',label='2014 values')
plt.legend()
plt.show()

x = [1,2,3,4,5,6,7,8,9,10]
med_2016 = [0.75, 0.73, 0.68, 0.66, 0.64, 0.65, 0.64, 0.65, 0.67, 0.71]
med_2014 = [0.71, 0.69, 0.62, 0.61, 0.60, 0.60, 0.59, 0.60, 0.62, 0.65]
plt.ylabel('Median Subscribership Ratio')
plt.xlabel('County Average Age by Decile')
plt.title('Subscribership Ratio based Upon Average Age')
plt.plot(x,med_2016,'bo-',label='2016 values')
plt.plot(x,med_2014,'ro-',label='2014 values')
plt.legend()
plt.show()



