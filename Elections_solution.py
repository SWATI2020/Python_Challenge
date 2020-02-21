# Dependencies
import os
import csv
# CSV read path location
csvpath = os.path.join('c:/data1','houston_election_data.csv')
# Output path location
file2 = open("Output/Election_Results.txt","w") 
#Reading the csv file using CSV module
with open(csvpath,encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    csv_header = next(csvreader)
    count_votes = 0
    contestants_dict = {}
    for rows in csvreader:
        count_votes += 1
        if rows[0] in contestants_dict:
            contestants_dict[rows[0]]+=1
        else:
            contestants_dict[rows[0]]= 1

    print("Houston Mayoral Election Results")
    print("-----------------------------------------")
    print("The total number of votes cast {}".format(count_votes))
    top_1 = 0
    top_2 = 0
    name_1 = ""
    name_2 = ""
    for name, value in contestants_dict.items():
        if value > top_1:
            top_1 = value
            name_1 = name
        elif value > top_2 and value < top_1:
            top_2 = value
            name_2 = name
        percentage_votes = value/count_votes*100
        print(" {} {}% {}".format(name,percentage_votes,value))
        
        file2.write(" {} {}% {}\n".format(name,percentage_votes,value))
    print("-----------------------------------------")
    print("1st Advancing Candidate: {}".format(name_1))
    print("2nd Advancing Candidate: {}".format(name_2))
str1 = "Houston Mayoral Election Results\n"
str2 = "-----------------------------------------\n"
str3 = "The total number of votes cast {}\n".format(count_votes)
str4 = "-----------------------------------------\n"
str5 = "1st Advancing Candidate: {}\n".format(name_1)
str6 = "2nd Advancing Candidate: {}".format(name_2)

L = [str1,str2,str3,str4,str5,str6]

file2.writelines(L)

