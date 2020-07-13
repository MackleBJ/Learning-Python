#Party Invitations

names = ['Kyle','Kadie','Halle','Jack','Zach','Ben','Danny','Isaac','Eric','Tim']

x = 0
y = len(names)  #Counts how long our list is

#Let's say that Ben and Danny couldn't make it for the event
names.remove('Ben')
names.remove('Danny')

#Let's say that we found out that Ariel can attend but Kadie cannot
names[1] = 'Ariel'

#Let's say that Connor and Austin would like to join
names.append('Connor')
names.append('Austin')

#Let's say that I want all the names in alphabetical order
names.sort()

#Automatically makes a letter to everyone on the list
while x < y:
    try:
        print(f"Dear {names[x]},\n\tYou've been invited to the Sunday Zoom Coffee Cupping. Held every Sunday from 10 a.m. to noon. We will cup various coffees from around the world. All while, comparing aroma and flavor notes between the coffees themself but with each other.")
        x = x + 1
        continue
    except:
        break
