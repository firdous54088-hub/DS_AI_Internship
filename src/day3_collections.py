student_list = ["suresh, 24,8.86"]
print(student_list)


car_details = ["maruthi, 24000, 2"]
print(car_details)

students = ["saiman", "firdosh", "manal", "adeeba", "madiha"]
students[1] = "shreya"
students.append("sana")
students.sort()
print(students)

numbers = [10, 20, 30, 40, 50]
numbers.append(60)
numbers.append(70)

new_list = numbers[2:6]
print("Original List:", numbers)
print("New Slice List:", new_list)

marks = (85, 90, 95)
marks[1] = 78

#task 1

inventory = ["Apples", "Bananas", "Carrots", "Dates"]
print("Current inventory:", inventory)
inventory.append("Eggs")
inventory.remove("Bananas")
inventory.sort()
print("Final updated inventory:", inventory)

#task2
 
temperature = [22, 24, 25, 28, 30, 29, 27, 26, 24, 22]
print("First reading:", temperature[0])
print("Last reading:", temperature[-1])
afternoon_peak = temperature[3:6]
print("Afternoon Peak readings:", afternoon_peak)
last_3_hours = temperature[-3:]
print("Last 3 hours readings:", last_3_hours)

#task3
screen_res = (1920, 1080)
print("Current Resolution:", screen_res[0], "x", screen_res[1])
screen_res[0] = 1280
print( "Tuples cannot be modified!")
