# Write your solution here
# Each product has name, price, and amount.

def search(products: list, criterion: callable):
    return [product for product in products if criterion(product)]
    # This took longer than it should have..
    
    # How this works:
    # For every item in the list, you want to check if each item fulfills the criteria/condition. 
    # The reason I was getting it wrong before is because I was checking if the whole list was fulfilling the criteria, 
    # instead of each item...


if __name__ == "__main__":
    products = [("banana", 5.95, 12), ("apple", 3.95, 3), ("orange", 4.50, 2), ("watermelon", 4.95, 22), ("kale", 0.99, 1)]
    for product in search(products, price_under_4_euros):
        print(product)