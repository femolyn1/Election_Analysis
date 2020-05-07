# The data we need to retrieve.
#1. the total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentatge of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote.
#open the election results and read the file
#import csv
#import os
# Assign a variable to load a file from a path
#file_to_load = os.path.join("Resources","election_results.csv")
#Open the election results and read the file
#with open(file_to_load) as election_data:
    #Print the file object.
    #print(election_data)
# Create a variable name to a direct or indirect path to the file
#file_to_save = os.path.join("analysis","election_analysis.txt")
#Using the open() funtion with the "w" mode we will write data to the file
#open( file_to_save,"w")
#Create a filename variable to a direct or indirect path to the file
#file_to_save = os.path.join( "analysis","election_analysis.txt")
#Using the with statament open the file asa text file.
#outfile=open(file_to_save,"w")
#Write some data to the file
#outfile.write("Hello World")
#Close the file
#outfile.close()
#LETS MAKE THE CODE CLEANER AND MORE CONCISE BY USING "WITH " STATEMENT
#Create a filename variable to a diecte or indirect path to the file
# This is thesame as step 21 above so i wont repeat it. Move to next step
#Using the with statement open the file as a text file
#with open(file_to_save,"w") as txt_file:
    #Write some data to the file. "Anything you write will overide the text in the text file".
    #Write three counties to the txt file
    #To separate "Arapahoe" and "Denver" by comma and space "Arapahoe,"
    #txt_file.write("Arapahoe,")
    #txt_file.write("Denver,")
    #txt_file.write("Jefferson")
    #You can also write the above txts all together
    #txt_file.write("Arapahoe,Denver,Jefferson")
    # To write each county on a new line, use the newline escape sequence \n
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    #Add our dependencies
import csv
import os
 #Assign a variable to load a file from a path
file_to_load = os.path.join("Resources/election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")
# 1. Initialize a total vote counter.(We declared this tocount the total number of votes)
total_votes = 0
#Candidate options(we declared this to det the names of candidates in the data )
candidate_options = []

# Declare the empty dictionary( This is required to det the total number of votes for each candidate)
candidate_votes = {}
#Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#Open the election results and read the file.
with open(file_to_load) as election_data:
# read the file object with the reader function
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)

    #Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        
        #Print the candidate name from each row
        candidate_name = row[2]
        
        #if thecandidate does not match any existing candidate...(This step helps to see the names of candidates )
        if candidate_name not in candidate_options:
            #Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidates vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidates count(Indent to count for all rows)
        candidate_votes[candidate_name] +=1   

    #Determine the percentage of votes for each candidate by looping through the candidate list
    for candidate in candidate_votes:
        # Retrieve vote count of a candidate list
        votes = candidate_votes[candidate]
        # Calculate the percentage of votes.
        vote_percentage =float(votes)/float(total_votes)*100

       # Print out each candinate name and percent of vote received
        #print(f"{candidate}:received{vote_percentage}% of the vote.")
        # Print out each candidates name, vote count and percentage of votes to the terminal
        print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        #Determine the winning vote count and candidate
        # Determine if the votes are greater than the winning count.

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent =vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # And set the winning _candidate equal to the candidates name
            winning_candidate = candidate
#3. Print the total votes.
#print(total_votes)
#Print the candidate list.
#print(candidate_options)  
# Print the candidate vote dictionary
#print(candidate_votes)
    # Print out the winning candidate , vote count and percentage to terminal
    winning_candidate_summary =(
        f"...........................\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"............................\n")
    print(winning_candidate_summary)


