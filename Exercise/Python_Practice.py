
counties=[]
counties=["Arapahoe","Denver","Jefferson"]
for i in range(len(counties)):
    print(counties[i])
if "El Paso" in counties:
    print ("El Paso is in the list")
else:
    print("El Paso is not in the list of counties")
if "El Paso" not in counties:
    print("True")
else:
    print("false")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso is not in the list of counties")
counties_dict={"Arapahoe":422829,"Denver":463353,"Jefferson":432438}
for county in counties_dict:
    print(county)
for i in range(len(counties)):
    print(counties[i])
x=0
while x<=5:
    print(x)
    x=x+1

for county in counties:
    print(county)
numbers =[0,1,2,3,4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")

for county in counties:
    print(county)
numbers=[0,1,2,3,4]

for i in range(len(counties)):
    print(counties[i])

counties_tuple=("Arapahoe","Denver","Jefferson")
for i in range(len(counties_tuple)):
    print(counties_tuple[i])
counties_dict={"Arapahoe":422829,"Denver":463353, "Jefferson":432438}
for voters in counties_dict.values():
    print(voters)

for county in counties_dict:
    print(counties_dict[county])
for county,voters ,in counties_dict.items():
    
    print(f"{county,} county has {voters,} registered voters.")

    voting_data=[{"county":"Arapahoe","registered_voters":422829},{"county":"Denver","registered_voters":463353},{"county":"Jefferson","registered_voters":432438}]

for county_dict in voting_data:
    print(county_dict)
for i in range(len(voting_data)):
    print(voting_data[i])

for county_dict in voting_data:
    for value in county_dict.values():
        print(value)
for county_dict in voting_data:
    print(county_dict["registered_voters"])
   
    for county, voters in counties_dict.items():
        print(county,"county has" , str(voters) , "registered voters.")

for county,voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

#Import the datetime class from t he datetime module .
import datetime as dt
#Use the now() attribute on the datetime class to ge the present time.
now = dt.datetime.now()

# print the present time.
print("The time right now is ",now)


def ourprettyFunction( anothernumber, icecreamflavour="chocolate", number="I am bob"):
    return f"{number}, {anothernumber},{icecreamflavour}
    string1=ourprettyFunction(2,"chocolate",1)
    print(string1)
# Create a list that prompt user for name of 5 people they know

