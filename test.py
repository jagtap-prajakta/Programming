# 10 Sep 2026:


# # 1. check if the number is odd or not and print the result as  Number is odd : False without if 
# number = int(input("Enter a number: "))
# is_odd = number % 2 != 0
# print("Number is odd : ", is_odd)

# # 2. WAP to print age in days. OUTPUT: 3 years = 1095 days
# age_in_years = int(input("Enter age in years : "))
# age_in_days = age_in_years * 365
# print(f'Age in years {age_in_years} = {age_in_days} days')

# # 3. WAP to covert minutes into hours and print it. OUTPUT: 135 is 2 hours and 15 minutes
# minutes = int(input("Enter minutes: "))
# hours = minutes / 60
# remaining_minutes = minutes % 60
# print(f'{minutes} is {int(hours)} hours and {remaining_minutes} minutes')

# # 4. WAP to extract the last digit of a number. OUTPUT : 1234 : last digit is 4
# number = int(input("Enter a number: "))
# last_digit = number % 10
# print(f'{number} : last digit is {last_digit}')

# # 5. WAP to check if a person is eligible for discount the criteria must be a student and age must be below 21. without if else. input values to take are role and age. OUTPUT: Eligible : True/ False
# role = input("Enter role (must be a student): ")
# age = int(input("Enter age: "))
# eligible = (role == "student") and (age < 21)
# print("Eligible : ", eligible)


#  6. WAP to swap two variables without a third variable, using arithmetic operations, Example: before swap a = 10, b = 20  after swap a = 20, b = 10

a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
print(f'Before swap a = {a}, b = {b}')
a = a + b
b = a - b
a = a - b
print(f'After swap a = {a}, b = {b}')