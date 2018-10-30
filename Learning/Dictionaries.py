monthConversions = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
}

#you can reffer to a key
#print(monthConversions["Apr"])
print(monthConversions.get("Jan", "Not a valid key"))


