#Import dependencies
import os
import csv
from statistics import mode

#Create the csv path
election_data = os.path.join("PyPoll/election_data.csv")

#Open and read the CSV file
with open(election_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #Skip the header row
    csv_header = next(csvreader) 

    #Create starter lists
    total_votes = []
    candidate_list = []
    khan_votes = []
    correy_votes = []
    li_votes = []
    otooley_votes = []
    
    #Make a new list for unique candidates
    candidates_unique = set(candidate_list)

    #Go through the rows and add the votes and candidates to lists
    for row in csvreader: 
        total_votes.append(row[1])
        candidate_list.append(row[2])
        if row[2] == ("Khan"):
            khan_votes.append(row[2])
        elif row[2] == ("Correy"):
            correy_votes.append(row[2])
        elif row[2] == ("Li"):
            li_votes.append(row[2])
        elif row[2] == ("O'Tooley"):
            otooley_votes.append(row[2])
    
    

    print("Election Results")
    print("----------------------------")
    print(f"Total votes: {len(total_votes)}")
    print("----------------------------")
    print(f"Khan: {(int(len(khan_votes)/len(total_votes) * 100))}% ({len(khan_votes)})")
    print(f"Correy: {(int(len(correy_votes)/len(total_votes) * 100))}% ({len(correy_votes)})")
    print(f"Li: {(int(len(li_votes)/len(total_votes) * 100))}% ({len(li_votes)})")
    print(f"O'Tooley: {(int(len(otooley_votes)/len(total_votes) * 100))}% ({len(otooley_votes)})")
    print("----------------------------")
    print(f"Winner: {mode(candidate_list)}")
    print("----------------------------")

    #Create the txt output path
output_file = os.path.join("/Users/allison/Desktop/python-challenge/PyPoll/output.txt")

#Write to output file
with open(output_file,"w") as file:
    file.write("Election Results")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Total votes: {len(total_votes)}")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Khan: {(int(len(khan_votes)/len(total_votes) * 100))}% ({len(khan_votes)})")
    file.write("\n")
    file.write(f"Correy: {(int(len(correy_votes)/len(total_votes) * 100))}% ({len(correy_votes)})")
    file.write("\n")
    file.write(f"Li: {(int(len(li_votes)/len(total_votes) * 100))}% ({len(li_votes)})")
    file.write("\n")
    file.write(f"O'Tooley: {(int(len(otooley_votes)/len(total_votes) * 100))}% ({len(otooley_votes)})")
    file.write("\n")
    file.write("----------------------------")
    file.write("\n")
    file.write(f"Winner: {mode(candidate_list)}")
    file.write("\n")
    file.write("----------------------------")
