import csv
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

highA_list = [];
lowA_list = [];
precipA_list = [];
fileA = open ("2009-June-Sept.csv") #opening the file 2009-June_Sept.csv
csv_fileA = csv.reader(fileA)
for row in csv_fileA: # here we are adding the high,low temperature values of file A to their respective lists.
    highA_list.append(float(row[1]));
    lowA_list.append(float(row[2]));
    precipA_list.append(float(row[3]));
print("\nThe high temperatures of file A");   
print(highA_list);
# reference from http://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python
for n,i in enumerate(highA_list): # here we are rounding up the average temperature values according to the conditions
    if i < 73:
        highA_list[n]=70;
    elif i>=73 and i<=77:
        highA_list[n]= 75;
    elif i>=77 and i<=82:
        highA_list[n] = 80;
    elif i>=82 and i<=87:
        highA_list[n] = 85;
    elif i>=87 and i<=92:
        highA_list[n] = 90;
    elif i>=92 and i<=97:
        highA_list[n] = 95;
    elif i>97:
        highA_list[n]=100;
print("\nThe actual high temperatures of file A after applying the given conditions");
print(highA_list);

print("\nThe low temperatures of file A");   
print(lowA_list);
for n,i in enumerate(lowA_list):
    if i < 73:
        lowA_list[n]=70;
    elif i>=73 and i<=77:
        lowA_list[n]= 75;
    elif i>=77 and i<=82:
        lowA_list[n] = 80;
    elif i>=82 and i<=87:
        lowA_list[n] = 85;
    elif i>=87 and i<=92:
        lowA_list[n] = 90;
    elif i>=92 and i<=97:
        lowA_list[n] = 95;
    elif i>97:
        lowA_list[n]=100;
print("\nThe actual low temperatures of file A after applying the given conditions");
print(lowA_list);


highB_list = [];
lowB_list = [];
precipB_list = [];
fileB = open ("2016-June-Sept.csv") #opening the file 2016-June_Sept.csv
csv_fileB = csv.reader(fileB)
for row in csv_fileB: # here we are adding the high,low temperature values of file B to their respective lists.
    highB_list.append(float(row[1]));
    lowB_list.append(float(row[2]));
    precipB_list.append(float(row[3]));
print("\nThe high temperatures of file B");   
print(highB_list);
# reference from http://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python
for n,i in enumerate(highB_list): # here we are rounding up the average temperature values according to the conditions
    if i < 73:
        highB_list[n]=70;
    elif i>=73 and i<=77:
        highB_list[n]= 75;
    elif i>=77 and i<=82:
        highB_list[n] = 80;
    elif i>=82 and i<=87:
        highB_list[n] = 85;
    elif i>=87 and i<=92:
        highB_list[n] = 90;
    elif i>=92 and i<=97:
        highB_list[n] = 95;
    elif i>97:
        highB_list[n]=100;
print("\nThe actual high temperatures of file B after applying the given conditions");
print(highB_list);

print("\nThe low temperatures of file B");   
print(lowB_list);
for n,i in enumerate(lowB_list):
    if i < 73:
        lowB_list[n]=70;
    elif i>=73 and i<=77:
        lowB_list[n]= 75;
    elif i>=77 and i<=82:
        lowB_list[n] = 80;
    elif i>=82 and i<=87:
        lowB_list[n] = 85;
    elif i>=87 and i<=92:
        lowB_list[n] = 90;
    elif i>=92 and i<=97:
        lowB_list[n] = 95;
    elif i>97:
        lowB_list[n]=100;
print("\nThe actual low temperatures of file B after applying the given conditions");
print(lowB_list);

# here we are performing test on Temperature High, Temperature Low, and Precipitation to find out whether there is a significant difference between these scores
# reference from https://docs.scipy.org/doc/scipy-0.14.0/reference/generated/scipy.stats.ttest_rel.html
np.seterr(divide='ignore', invalid='ignore')
print("\nThe High temperature statistics are : t value = %f and p value = %f" %stats.ttest_rel(highA_list,highB_list))
print("\nThe Low temperature statistics are : t value = %f and p value = %f" %stats.ttest_rel(lowA_list,lowB_list))
print("\nThe Precipitation statistics are : t value = %f and  p value = %f" %stats.ttest_rel(precipA_list,precipB_list))

"""
While conducting T-Test, for high temperatures, the p value is 0.924 which is greater than 0.05 hence we cannot reject null hypothesis. Next for low temperatures, the p value is 0.0098 which is much less than 0.05,therefore we can reject the null hypothesis. Coming to precipitation, the p value is 0.596 which is greater than 0.05 and we cannot reject the null hypothesis
"""
