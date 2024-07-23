#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input("Enter the total bill amount: "))
people = int(input("Enter the number of people: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))

tip = bill * round((tip_percentage / 100), 2)
total_bill = bill + tip
amount_per_person = total_bill / people

print(f"Each person should pay: ${amount_per_person:.2f}")

#AI generated code with cntrl + i. prompt: "split the bill adding custom tip percentage".

#My only contribution was adding a round function with 2 decimal places to the tip calculation.