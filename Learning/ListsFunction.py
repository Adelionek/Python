lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tommy"]
#friends.append("Creed")
friends.insert(1, "Kelly")#rest of elements are pushed out
friends.remove("Jim")#delete one
#friends.clear()
friends.pop() # delete last one
lucky_numbers.reverse()
friends.sort()

friends2 = friends.copy()

print(friends2)
print(lucky_numbers)
