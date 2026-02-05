# Task 1
contacts = {"hania":8108114685, "sara":9380790060, "Ali":8088540889}
contacts["Altaf"] = 9353303943
print(contacts)
contacts["hania"] = 7406873851
print(contacts)
print(contacts.get("hania")) #exist
print(contacts.get("Anaya")) #does not exist
print(contacts.get("Anaya", "Contact not found"))
for name,number in contacts.items():
    print(name,number) 
    
# Task 2

raw_logs = ["ID01", "ID02", "ID01", "ID05", "ID02", "ID08", "ID01"]
unique_users = set(raw_logs)
is_ID05_present = "ID05" in unique_users
original_count = len(raw_logs)
unique_count = len(unique_users)
print(unique_users)
print(is_ID05_present)
print(original_count)
print(unique_count)

# Task 3

friend_a = {"Python", "Cooking", "Hiking", "Movies"}
friend_b = {"Hiking", "Gaming", "Photography", "Python"}
print(friend_a & friend_b)
print(friend_a | friend_b)
print(friend_a - friend_b)

