# 10 Sep 2026:


# # 1. check if the number is odd or not and print the result as  Number is odd : False without if 
# number = int(input("Enter a number: "))
# is_odd = number % 2 != 0
# print("Number is odd : ", is_odd)

# # 2. WAP to print age in days. OUTPUT: 3 years = 1095 days
# age_in_years = int(input("Enter age in years : "))
# age_in_days = age_in_years * 365
# print(f'Age in years {age_in_years} = {age_in_days} days')

# 3. WAP to covert minutes into hours and print it. OUTPUT: 135 is 2 hours and 15 minutes
minutes = int(input("Enter minutes: "))
hours = minutes / 60
remaining_minutes = minutes % 60
print(f'{minutes} is {int(hours)} hours and {remaining_minutes} minutes')