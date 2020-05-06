
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