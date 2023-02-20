class Bike:
    gear = 4            # Static variable 

    def __init__(self, company, color) :
        self.Company = company 
        self.Color = color

    def MyFunc(self, price, torque, average) :
        self.Price = price
        self.Torque = torque
        self.Avg = average
        print("Company Name = ", self.Company)
        print("Color = ", self.Color)
        print("Onroad price = ", self.Price)
        print("Torque = ", self.Torque)
        print("Average = ", self.Avg)
        print("No. of Gears = ", self.gear)


b1 = Bike("Honda", "Black")
b1.MyFunc(75663, "15Nm", "60 kmpl")

print('----------------------------------------------------------------')

Bike.gear = 5                    #--> Accessing Static variable
b2 = Bike("Hero", "Red")
b2.MyFunc(98000, "23Nm", "62 Kmpl")

