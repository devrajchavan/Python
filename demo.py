
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

CompoundInterest = principal * (1 + rate/100) ** time - principal

print("Compound interest:", CompoundInterest )

amount = CompoundInterest  + principal

print("Total amount to pay with interest = ", amount)  