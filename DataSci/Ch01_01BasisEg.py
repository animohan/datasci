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
print(users[0]["friends"][0]["friends"][0],"\n")
print(users[0]["friends"][0]["friends"][0]["friends"],"\n")
#this loop goes on !

#understanding the dictionary loops
print(users[0]["friends"])
#prints the self referential internal loop as demonstrated in example above.
#However note the self referential dictionary is all attached to one element
#"friends" of the dicitionary and hence its lenght is 1.
print(len(users[0]["friends"]))
"""
#the problem here is that the dictionary become self referential and loopy
# because in this example Hero's friends dictionary contains "Dunn" entry,
# which in turn contains an entry for hero, hence the dictionary just loops around
# python shows this bysaying "friends" element ==[{...}]
#may be its a not a problem


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

print("Total Connections=",total_connections)
print("Average connection=", total_connections/float(len(users)) )

#Now we can sort them by folks who have largest number of friends
num_friends_by_id =[(user["id"],number_of_friends(user))for user in users]
print(num_friends_by_id)

num_friends_by_name=[(user["name"],number_of_friends(user)) for user in users]
print(num_friends_by_name)

#sorting
"""soring a list of tuples is an interersting exercise.
Both type of functions a.sort or sort(a) take a key argument 
key privdes a way to specify a fucntion that returns what you would
like your items sorted by. The function get an "invisible" argument 
passed to it that represents an item in the list and returns a value 
would like to be the items "key" for sorting
"""
def getkey(item):
	return item[0]
print("\n")
print "Sorted List='\n'",sorted(num_friends_by_name,key=getkey)

#another way to achiev this using lambda
print("Another way to print sorted list \n")
print(sorted(num_friends_by_id, key=lambda(user_id,num_friends):num_friends,reverse=True))
print(sorted(num_friends_by_name, key=lambda(user_name,num_friends):num_friends,reverse=True))
print("\nSort by user name:")
print(sorted(num_friends_by_name, key=lambda(user_name,num_friends):user_name,reverse=True))

print("\n--------------------NEW ASSIGNEMENT---------------------------------\n")
#Now looking at people you may know.

#can we get a list of friends of friends
"""
1. Get a list of all your friends.
2. The list of friends has a dictionary of all their friends, get the list from that
"""
def friends_of_friends_ids(user):
	return [foaf["id"]
			for friend in user["friends"]
			for foaf in friend["friends"]]

def friends_of_friends_names(user):
	return [foaf["name"]
			for friend in user["friends"]
			for foaf in friend["friends"]]

for user in users:
	print (user["name"], friends_of_friends_names(user))

for user in users:
	print (user["name"], friends_of_friends_ids(user))
"""
Two problems with above example:
1. Hero is friend of Sue who is a friend of Hero. So the list will refer itself.
2. It does not eleminate people who are already in your friendlist
"""
#How about we count the mutual number of friends
from collections import Counter

def not_the_same(user, other_user):
	#two users are not the same if they have different ids
	return user["id"]!=other_user["id"]

def not_friends(user, other_user):
	""" other_user is not a friend if he is not in user["friends]
	i.e the function defined above not_the_same is false all user, other user"""
	return all(not_the_same(friend,other_user) for friend in user["friends"])

def friends_of_friend_ids2(user):
	return [foaf["id"]
					for friend in user["friends"]
					for foaf in friend["friends"]
					if not_the_same(user,foaf)
					and not_friends(user,foaf)]
print("\nNew and improved friend of friends")
for user in users:
	print (user["name"], friends_of_friend_ids2(user))

#Data showing interest of each id
interests =[ (0,"Hadoop"),(0,"Big Data"),(0,"Hbase"),(0,"Java"),(0,"Spark"),
			(0,"Storm"),(0,"Cassandra"),(1,"NoSQL"),(1,"MongoDB"),(1,"Cassandra"),(1,"HBase"),
			(1,"PostGres"),(2,"Python"),(2,"scikit-learn"),(2,"scipy"),
			(2,"numpy"),(2,"statmodels"),(2,"pandas"),(3,"R"),(3,"python"),
			(4,	"machine	learning"),	(4,	"regression"),	(4,	"decision	trees"),
			(4,	"libsvm"),	(5,	"Python"),	(5,	"R"),	(5,	"Java"),	(5,	"C++"),
			(5,	"Haskell"),	(5,	"programming	languages"),	(6,	"statistics"),
			(6,	"probability"),	(6,	"mathematics"),	(6,	"theory"),
			(7,	"machine	learning"),	(7,	"scikit-learn"),	(7,	"Mahout"),
			(7,	"neural	networks"),	(8,	"neural	networks"),	(8,	"deep learning"),
			(8,	"Big Data"),	(8,	"artificial	intelligence"),	(9,	"Hadoop"),
			(9,	"Java"),(9,"MapReduce"),(9,"Big Data")]


#find users with certain interest
def data_scientists_who_like(target_interest):
	return [user_id
			for user_id, user_interest in interests
			if user_interest==target_interest]

#the above function works, but it searches for entire list fo every search
# can we build an index from interest to users

from collections import defaultdict

#keys are interest and values are lists for user_ids with that interest
user_ids_by_interest = defaultdict(list)
for user_id, interest in interests:
		user_ids_by_interest[interest].append(user_id)

print(user_ids_by_interest)

#this can be done by mapping from users to interests

#keys are user_ids, values are lists of interests for that user_id

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
		interests_by_user_id[user_id].append(interest)

#now find the interestmatch
def most_common_interests_with(user):
	return Counter(interested_user_id
			for interest in interests_by_user_id[user["id"]]
			for interested_user_id in user_ids_by_interest[interest]
			if  interested_user_id!=user["id"])

#lengtheir version of function above
def most_common_interests_with2(user):
	common_interest_list=[]
	for interest in interests_by_user_id[user["id"]]:
		for interested_user_id in user_ids_by_interest[interest]:
			if(interested_user_id!=user["id"]):
				common_interest_list.append(interested_user_id)

	return common_interest_list


for user in users:
	print("\n")
	print(user["id"],user["name"])
	print("Common Interests with:")
	print(most_common_interests_with2(user))
	print(most_common_interests_with(user))