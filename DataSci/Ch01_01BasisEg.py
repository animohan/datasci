users=[
	{"id":0, "name": "Hero"},
	{"id":1, "name": "Dunn"},
	{"id":2, "name": "Sue"},
	{"id":3, "name": "Chi"},
	{"id":4, "name": "Thor"},
	{"id":5, "name": "Clive"},
	{"id":6, "name": "Hicks"},
	{"id":7, "name": "Devin"},
	{"id":8, "name": "Kate"},
	{"id":9, "name": "Klein"},
	]

"""
 # An aside to check how values are printed. For loop written like this loops
 #through each tuple. it does not take a cross product of the tuple

friendships=[(0,5),(1,2),(4,7)]
for i, j in friendships:
	print(i)
	print(j)
"""
"""
#set of dictionaries i.e there are two dictionaries in the set.
D=[{'spam':1,'ham':1,'eggs':1}, 
   {'spam':5,'ham':5,'eggs':5}]

print(D)
print(D[0]['spam']) # access to first dictionary

D[0]["meal"]=[2] #adds a new element to dictionary at D[0]
print(D[0]) 
"""
"""
#shortened example to try
friendships=[(0,1)]
for user in users:
	user["friends"]=[] #adds a new dictionary element "friends and sets it to null"
	
for i, j in friendships:
	#this works because user[1] is the user whose id is i
	print(i)
	users[i]["friends"].append(users[j]) #friends is a dictionary element that is a list of other dictionary elements from users
	users[j]["friends"].append(users[i])
	#print(users[i],"\n")

print(users[0],"\n")
print(users[0]["friends"],"\n")
print(users[0]["friends"][0],"\n")
print(users[0]["friends"][0]["friends"],"\n")

#the problem here is that the dictionary become self referential and loopy
# because in this example Hero's friends dictionary contains "Dunn" entry,
# which in turn contains an entry for hero, hence the dictionary just loops around
# python shows this bysaying "friends" element ==[{...}]
#may be its a not a problem
"""

friendships=[(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]
for user in users:
	user["friends"]=[] #adds a new dictionary element "friends and sets it to null"
	
for i, j in friendships:
	#this works because user[1] is the user whose id is i
	users[i]["friends"].append(users[j]) #friends is a dictionary element that is a list of other dictionary elements from users
	users[j]["friends"].append(users[i])

#How many friends does a user have
def number_of_friends(user):
	return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)

print(total_connections)