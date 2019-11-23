# Lists

friends = ["John","Jordan","Dane"]
nums = [10, 14, 16, 17, 21]

#friends.extend(nums)
friends.append("yeew culture")
friends.insert(1,"Aha")
friends.remove("Dane")  
friends.pop()
print(friends.index("John"))
print(friends.count("John"))
friends.sort()
print(friends)

friends2 = friends
# print("friends2: ",+friends2)
print("friends2: " + str(friends2))