#Ken Vu
#23 april 2024
#amortization
purchase = float(input("Please! enter the purchase price: "))
down_payment = float(input("Enter the down payment(%): "))/100
rate = float(input("Enter interest rate(%): "))/100
payment = float(input("Payment amount ($): "))
loan = purchase - (purchase*down_payment)
type_payment = input("Payment type: ").lower()
if type_payment == "monthly":
    type_payment = 12
    frequency = "Month"
elif type_payment == "semi-monthly":
    type_payment = 24
    frequency = "Half-Month"
elif type_payment == "bi-weekly":
    type_payment = 26
    freq = "Bi-Week"
elif type_payment == "weekly":
    type_payment = 52
    frequency = "Week"
amortization_chart = [["Period","Starting Balance","Payment","Interest","Principal","Ending Balance"]]
time = 0
year = 1
yrly_interest = 0
yrly_principal = 0
total_interest = 0
total_principal = 0
interest_list = []
principal_list = []
print("Loan Amount: "+str(loan))
while loan > 0:
    table = []
    time += 1
    table.append("Year "+str(year) ) 
    table.append(f"{frequency} {time}")
    table.append(loan)
    interest = loan * rate / float(type_payment)
    principal = payment - interest
    loan -= principal
    yrly_interest += interest
    yrly_principal += principal
    total_interest += interest
    total_principal += principal
    table.append(payment)
    table.append(interest)
    table.append(principal)
    table.append(loan)

    for x in range(len(table)):
        if isinstance(table[x], float):
            table[x] = round(table[x], 2)
        table[x] = "{0: >10}".format(str(table[x]))
        amortization_chart.append(table)
    if time >= type_payment:
        time = 0
        year += 1
        interest_list.append(yrly_interest)
        principal_list.append(yrly_principal)
        yrly_interest = 0
        yrly_principal = 0
interest_list.append(yrly_interest)
principal_list.append(yrly_principal)
for x in amortization_chart:
    print(x)
    print("______________________________________________________________________________")

for x in range(year):
    print(f"Year {x+1}: Interest: {round(interest_list[x], 2)}, Principal: {round(principal_list[x], 2)}")
    print("------------------------------------------")
print(f"Total interest: {round(total_interest, 2)}, Total Principal: {round(total_principal, 2)}")
print("congrat! You've paid off your loan")
loan = purchase - (purchase*down_payment)
number_year = (year+(time/12)-1)   
print(number_year)
m = loan*rate*number_year
print(loan*rate*number_year)
print(total_interest-m)
print(loan+total_interest)   