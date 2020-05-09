# The Data we need to retrieve
#1. The total number of votes cast
#2. A complete list of counties where votes were casted
#3. The percentage of votes for each county
# The total number of vote each county received
# The county with the largest turnout
# Assign a variable to load a file from a path.
import csv
import os
file_to_load = os.path.join("Resources/election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
#Initialize a total vote counter.
total_votes = 0
# County options and county votes.
county_options = []
county_votes = {}
# Track the largest county turnout, vote count, and percentage.
largest_county = ""
largestcounty_count = 0
largestcounty_percentage = 0
# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # Read the header row.
    headers = next(file_reader)
    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1

        # Get the county name from each row.
        county_name = row[1]
        # If the county does not match any existing county, add the county list
        if county_name not in county_options:
            # Add the county name to the county list.
            county_options.append(county_name)
            #And begin tracking that counties vote count.
            county_votes[county_name] = 0
        #Add a vote to that county's count.
        county_votes[county_name] += 1
    
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
  
#Determine the percentage of votes for each county by looping through the county list
    for county in county_votes:
            #retrieve vote count of each county
        votes = county_votes[county]
        vote_percentage = float(votes) / float(total_votes) * 100
        county_results=(
            
            f" {county}:{vote_percentage:.1f}% ({votes:,})\n")  

         #Print each county vote count and percentage to the terminal
        print(county_results)
        #Save the county results to our text file
        txt_file.write(county_results)
        # Determine largest vote count, largest county percentage, and largest county.
        if (votes > largestcounty_count) and (vote_percentage > largestcounty_percentage):
            largestcounty_count=votes
            largestcounty_percentage=vote_percentage
            largest_county=county

    # Print the largest county turnout to the terminal.
    largest_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county}\n"
        f"-------------------------\n")
    print(largest_county_summary)
    #Save the largest county turnout result to the text file
    txt_file.write(largest_county_summary)

     