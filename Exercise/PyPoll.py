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
file_to_load = os.path.join("Resources","election_results.csv")
#Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis","election_analysis.txt")
    
#Open the election results and read the file.
with open(file_to_load) as election_data:
# Read and analyze the data here
# read the file object with the reader function
    file_reader = csv.reader(election_data)
#Print each row in the CSV file
    #for row in file_reader:
        #print(row)

    # print the header row . (We wnat to do this to be sure we are skipping the header row)
    headers=next(file_reader)
    print(headers)
            
