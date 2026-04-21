#Exercise 3.1:
friends = ["antonio", "pedro", "lucas", "gabriel"]
print(friends[0].title())
print(friends[1].title())
print(friends[2].title())
print(friends[3].title())

#Exercise 3.2:
friends = ["antonio", "pedro", "lucas", "gabriel"]
print(friends[0].title() + " is my friend.")
print(friends[1].title() + " is my friend.")
print(friends[2].title() + " is my friend.")
print(friends[3].title() + " is my friend.")

#Exercise 3.3:
vehicles = ["bike", "car", "plane", "yatch"]
print("I own a " + vehicles[0].lower() + " but i don't own a " + vehicles[1].lower() + ".")
print("When I get rich I'll own a " + vehicles[2].lower() + " and a " + vehicles[3].lower() + ".")

#Exercise 3.4:
dinner = ["mom", "dad", "brother"]
print(dinner[0].title() + ", come have dinner with me!")
print(dinner[1].title() + ", come have dinner with me!")
print(dinner[2].title() + ", come have dinner with me!")

#Exercise 3.5:
print("My " + dinner[2].lower() + " said he won't make it in time :(")
dinner.remove("brother")
dinner.append("grandmother")
print(dinner[0].title() + ", come have dinner with me!")
print(dinner[1].title() + ", come have dinner with me!")
print(dinner[2].title() + ", come have dinner with me!")

#Exercise 3.6:
print("Hey guys! I found a bigger dinner table so I'll invite 3 more people!")
dinner.insert(0, "grandfather")
dinner.insert(3, "cousin")
dinner.append("aunt")
print(dinner[0].title() + ", come have dinner with me!")
print(dinner[1].title() + ", come have dinner with me!")
print(dinner[2].title() + ", come have dinner with me!")
print(dinner[3].title() + ", come have dinner with me!")
print(dinner[4].title() + ", come have dinner with me!")
print(dinner[5].title() + ", come have dinner with me!")

#Exercise 3.7:
print("Unfortunately, because the table will arrive late, I can only invite 2 people for the dinner.")
sorry = dinner.pop()
print("I'm sorry for not inviting you, " + sorry.lower() + ".")
sorry = dinner.pop()
print("I'm sorry for not inviting you, " + sorry.lower() + ".")
sorry = dinner.pop()
print("I'm sorry for not inviting you, " + sorry.lower() + ".")
sorry = dinner.pop()
print("I'm sorry for not inviting you, " + sorry.lower() + ".")
print(dinner[0].title() + ", you're still invited!")
print(dinner[1].title() + ", you're still invited!")
del dinner[1]
del dinner[0]
print(dinner)

#Exercise 3.8:
places = ["china", "portugal", "sweden", "germany", "switzerland"]
print(places)
print(sorted(places))
print(places)
print(sorted(places, reverse=True))
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)

#Exercise 3.9:
dinner = ["mom", "dad", "brother", "grandmother"]
print("I'm inviting " + str(len(dinner)) + " people for dinner today!")

#Exercise 3.10:
jobs = ["doctor", "engineer", "teacher", "firefigher", "lawyer"]
print("Here's the original job list: " + str(jobs))
print("Here's the sorted job list: " + str(sorted(jobs)))
print("Here's the reverse-sorted job list: " + str(sorted(jobs, reverse=True)))
print("Here's the reversed job list: " + str(list(reversed(jobs))))