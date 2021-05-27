name = "Makenson Noel"
academic_status = {"major": "Computer Science", "gpa": 3.0}
hobbies = ['Working out', 'Skating', 'Reading']

likes = "My hobbies are: \n"
for hobby in hobbies:
  likes = likes + hobby + "\n"

if academic_status['gpa'] == 4.0:
  rating = "perfect"

elif academic_status['gpa'] >= 3.0:
  rating = "very good"

else:
  rating = "not so good"


print(f"My name is {name} \n")
print(f"I am majoring in {academic_status['major']} and my GPA is {academic_status['gpa']}, which is considered {rating}\n")
print(likes)



