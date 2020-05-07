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
# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count, and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Get the candidate name from each row.
        candidate_name = row[2]
        # If the candidate does not match any existing candidate, add the
        # the candidate list.
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
    # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
    for candidate in candidate_votes:
        # Retrieve vote count and percentage.
        votes = candidate_votes[candidate]
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate
            winning_percentage = vote_percentage
    # Print the winning candidate's results to the terminal.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)