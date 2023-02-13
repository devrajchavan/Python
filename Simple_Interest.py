pa = float(input("Enter Principal amount :  "))
rate = int(input("Enter rate of interest :  "))
Time = float(input("Enter time Duration : "))

SimpleInterest = (pa * rate * Time) / 100

print("Simple Interest = " , SimpleInterest)

amount = SimpleInterest + pa

print("Total amount to pay = ", amount)


