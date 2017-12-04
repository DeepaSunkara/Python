import csv

high_list = [];
low_list = [];
precip_list = [];
fileA = open ("2009-June-Sept.csv")
csv_fileA = csv.reader(fileA)
for row in csv_fileA:
    high_list.append(row[1]);
    low_list.append(row[2]);
    precip_list.append(row[3]);
highA = list(map(float, high_list));
lowA = list(map(float, low_list));
print(highA);
print(lowA);
precipA = list(map(float, precip_list));
AverageHighA = sum(highA)/len(high_list);
AverageLowA = sum(lowA)/len(low_list);
AverageTemA = (AverageHighA+AverageLowA)/2;
AveragePrecipA = sum(precipA)/len(precip_list);
print("\nThe Average details of File A ");
print("The average high temperature = " + str(AverageHighA));
print("The average low temperature = " + str(AverageLowA));
print("The average temperature = " + str(AverageTemA));
print("The average precipitation = " + str(AveragePrecipA));
fileA.close();


high_list1 = [];
low_list1 = [];
precip_list1 = [];
fileB = open ("2016-June-Sept.csv")
csv_fileB = csv.reader(fileB)
for row in csv_fileB:
    high_list1.append(row[1]);
    low_list1.append(row[2]);
    precip_list1.append(row[3]);
highB = list(map(float, high_list1));
lowB = list(map(float, low_list1));
precipB = list(map(float, precip_list1));
AverageHighB = sum(highB)/len(high_list1);
AverageLowB = sum(lowB)/len(low_list1);
AverageTemB = (AverageHighB+AverageLowB)/2;
AveragePrecipB = sum(precipB)/len(precip_list1);
print("\nThe Average details of File B ");
print("The average high temperature = " + str(AverageHighB));
print("The average low temperature = " + str(AverageLowB));
print("The average temperature = " + str(AverageTemB));
print("The average precipitation = " + str(AveragePrecipB));
fileB.close();


high_list2 = [];
low_list2 = [];
precip_list2 = [];
fileC = open ("2009-Sept.csv")
csv_fileC = csv.reader(fileC)
for row in csv_fileC:
    high_list2.append(row[1]);
    low_list2.append(row[2]);
    precip_list2.append(row[3]);
highC = list(map(float, high_list2));
lowC = list(map(float, low_list2));
precipC = list(map(float, precip_list2));
AverageHighC = sum(highC)/len(high_list2);
AverageLowC = sum(lowC)/len(low_list2);
AverageTemC = (AverageHighC+AverageLowC)/2;
AveragePrecipC = sum(precipC)/len(precip_list2);
print("\nThe Average details of File C ");
print("The average high temperature = " + str(AverageHighC));
print("The average low temperature = " + str(AverageLowC));
print("The average temperature = " + str(AverageTemC));
print("The average precipitation = " + str(AveragePrecipC));
fileC.close();





high_list3 = [];
low_list3 = [];
precip_list3 = [];
fileD = open ("2016-Sept.csv")
csv_fileD = csv.reader(fileD)
for row in csv_fileD:
    high_list3.append(row[1]);
    low_list3.append(row[2]);
    precip_list3.append(row[3]);
highD = list(map(float, high_list3));
lowD = list(map(float, low_list3));
precipD = list(map(float, precip_list3));
AverageHighD = sum(highD)/len(high_list3);
AverageLowD = sum(lowD)/len(low_list3);
AverageTemD = (AverageHighD+AverageLowD)/2;
AveragePrecipD = sum(precipD)/len(precip_list3);
print("\nThe Average details of File D ");
print("The average high temperature = " + str(AverageHighD));
print("The average low temperature = " + str(AverageLowD));
print("The average temperature = " + str(AverageTemD));
print("The average precipitation = " + str(AveragePrecipD));
fileD.close();

