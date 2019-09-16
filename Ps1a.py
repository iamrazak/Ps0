#Haruna Abdulrazak
#U18FNSCSC1019
#This is the annual salary
annual_salary = float(input("Enter your annual salary: "))
#This is the portion saved
portion_saved = float(input("Enter the percent of your salary to save, in decimal: "))
#This is total cost
total_cost = float(input("Enter the cost of your dream home: "))
#This is the portion saved
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
months = 0
while current_savings < portion_down_ayment:
    current_savings += (annual_salary/12)*portion_saved + current_savings*(r/12)
    months += 1
print("Congratulations, you with need for save for : ", months " months to buy your dream house")