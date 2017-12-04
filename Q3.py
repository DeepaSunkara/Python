import csv
import matplotlib.pyplot as plt
high_list = [];
low_list = [];
avgA_list = [];
daily_list=[];
fileA = open ("2009-June-Sept.csv") # opening a 2009-June-Sept.csv file
csv_fileA = csv.reader(fileA)
for row in csv_fileA:
    avgA_list.append(((float(row[1])+float(row[2])))/2); # here we aare finding out the average temperatures and storing it in a list
print("\nThe values of average temperatures of file A")    
print(avgA_list);
# reference from http://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python
for n,i in enumerate(avgA_list): # rounding the average temperatures values according to the conditions
    if i < 73:
        avgA_list[n]=70;
    elif i>=73 and i<=77:
        avgA_list[n]= 75;
    elif i>=77 and i<=82:
        avgA_list[n] = 80;
    elif i>=82 and i<=87:
        avgA_list[n] = 85;
    elif i>=87 and i<=92:
        avgA_list[n] = 90;
    elif i>=92 and i<=97:
        avgA_list[n] = 95;
    elif i>97:
        avgA_list[n]=100;
print("\nThe  actual values of average temperatures of file A after applying conditions");
print(avgA_list)
# drawing the histogram diagrams to calculate the frequency count of the temperatures 
plt.hist(avgA_list, color='b', label=" Averages of Temperature Count in 2009", align="left",bins=40, range=(65,105))# mentioning the specifications for the histogram chart
#naming the X-axis and Y-axis of the histograms
plt.xlabel("Average value of Tepmeratures")
plt.ylabel("Frequency Count of  Temperatures")
plt.legend()
# Displaying the File A histogram
print("\nPlease close the histogram chart window of file A inorder to view the results of file B and its histogram chart");
plt.show()

# Here the average temperatures for file B are calculated and the histogram diagram is generated for those values. 
high_list1 = [];
low_list1 = [];
avgA_list1 = [];
daily_list1=[];
fileB= open ("2016-June-Sept.csv") # opening the 2016-June-Sept.csv file
csv_fileB = csv.reader(fileB)
for row in csv_fileB:
    avgA_list1.append(((float(row[1])+float(row[2])))/2); # performing the averege of temperatures and storing it in a list
    daily_list1.append((row[0]));
print("\n")
print("\nThe values of average temperatures of file B") 
print(avgA_list1);
# reference from http://stackoverflow.com/questions/2582138/finding-and-replacing-elements-in-a-list-python
for n,i in enumerate(avgA_list1): # rounding up the average temperature values according to the conditions
    if i < 73:
        avgA_list1[n]=70;
    elif i>=73 and i<=77:
        avgA_list1[n]= 75;
    elif i>=77 and i<=82:
        avgA_list1[n] = 80;
    elif i>=82 and i<=87:
        avgA_list1[n] = 85;
    elif i>=87 and i<=92:
        avgA_list1[n] = 90;
    elif i>=92 and i<=97:
        avgA_list1[n] = 95;
    elif i>97:
        avgA_list1[n]=100;
print("\nThe actual values of average temperatures of file B") 
print(avgA_list1)
# the following code represents to generate a histogram diagram for the averege temperature values of file b
plt.hist(avgA_list1, color='b', label=" Averages of Temperature Count in 2016", align="left",bins=40, range=(65,105)) #mentioning the specifications for the histogram chart
#Lableling the x axis and the y axis of the histogram chart
plt.xlabel("Average values of Tepmeratures")
plt.ylabel("Frequency Count of  Temperatures")
plt.legend()
#finally displaying the histogram chart for the file B
plt.show()





    
        


