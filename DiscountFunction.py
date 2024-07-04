
price = int(input("Enter the price :"))
discountRate = int(input("Enter the Discount rate :"))


def Calculate_Discount(price, discountRate):
    if discountRate > 1 or discountRate < 0:
        print("Discount rate cannot be less than zero or grater than one !!!")
        # return null
    else:
        Discount = price * discountRate
        return Discount


a = Calculate_Discount(1000, 0.3)
print(f" Price :{price} \n  The discount is : {a}")

