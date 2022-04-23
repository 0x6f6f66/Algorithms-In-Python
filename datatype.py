from Student import Student
import random

student1 = Student("Alex", "Business Management", 21, False)
student2 = Student("Alexey", "CS", 22, True)


names = ['Alex', 'Jim', 'Alexey', 'Oof', 'Stubb']
degrees = ['BM', 'CS', 'Art']
ages = [21, 20, 19, 22, 25]
is_on_probation = [True, False]

student_dict = {}
student_values_list = []
# for i in range(1, 5):
    # student_dict["student{}".format(i)] = random.choice(names), random.choice(degrees), random.choice(ages), random.choice(is_on_probation)

studentT = Student(random.choice(names), random.choice(degrees), random.choice(ages), random.choice(is_on_probation))

