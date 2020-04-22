#Saskia Savage 20/04/2020 HardwareShop.py

VAT_RATE = 0.15


class Product:

    discount = 0

    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    # b. Calculate total (cost by qty)
    def calcTotal(self, qty):
        return self.cost * qty

    # c. Calculate discount (different for each product type)
    def calcDiscount(self, qty):
        total = self.calcTotal(qty)
        return self.discount * total

    def getDiscountedTotal(self, qty):
        total = self.calcTotal(qty)
        discountValue = self.calcDiscount(qty)
        return total - discountValue

    # d. Calculate VAT (15% (total - discount))
    def calcVAT(self, qty):
        discounted = self.getDiscountedTotal(qty)
        return discounted * VAT_RATE

    # e. calculate the payment due (total - discount + VAT)
    def calcPaymentDue(self, qty):
        if qty < 0:
            return 0
        discounted = self.getDiscountedTotal(qty)
        vat = self.calcVAT(qty)
        paymentDue = discounted + vat
        return round(paymentDue, 2)

    
class Gardening(Product):

    discount = 0.05


class Home(Product):

    discount = 0.08


class Building(Product):

    discount = 0.09


def outputProductPaymentDue(product, qty):
    print(str(qty) + 
        " x " + 
        product.description + 
        " cost= " + 
        str(product.calcPaymentDue(qty)))


def getProductFromTypeSelection():
    while True:
        print("Select product type number from the options below: ")
        print("\t1) Home")
        print("\t2) Building")
        print("\t3) Gardening")
        productType = input("Type number: ")
        if productType == "1":
            return createHomeProduct()
        elif productType == "2":
            return createBuildingProduct()
        elif productType == "3":
            return createGardeningProduct()


def createHomeProduct():
    descriptionInput = input("Product decription: ")
    priceInput = getPriceInput()
    product = Home(descriptionInput, priceInput) 
    return product


def createBuildingProduct():
    descriptionInput = input("Product decription: ")
    priceInput = getPriceInput()
    product = Building(descriptionInput, priceInput) 
    return product


def createGardeningProduct():
    descriptionInput = input("Product decription: ")
    priceInput = getPriceInput()
    product = Gardening(descriptionInput, priceInput) 
    return product


def getPriceInput():
    while True:
        priceInput = input("Product price:")
        try:
            price = float(priceInput)
        except ValueError:
            print("A money value is required.. .")
        if isinstance(priceInput, float):
            break
    return price


def getProductQty():
    while True:
        qtyInput = input("Product quantity: ")
        try:
            qty = int(qtyInput)
        except ValueError:
            print("An integer value is required.. .")
        if isinstance(qty, int):
            break
    return qty


def main():
    # Test data:
    #
    # product = Home("taps", 12.99)
    # qty = 3
    #
    # product = Building("bricks", 1.89)
    # qty = 300
    #
    # product = Gardening("shovel", 11.20)
    # qty = 2
    #
    # product = Home("bathtub", 120)
    # qty = 2
    while True:
        product = getProductFromTypeSelection()
        qty = getProductQty()
        outputProductPaymentDue(product, qty)
        repeatInput = input("Repeat? (y/n): ")
        if repeatInput != "y":
            break


if __name__ == "__main__":
    main()