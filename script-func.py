from pprint import pprint
import json

def get_profit(price,cost):
    return price - cost
    
    
def profit_per_cutomer(customer):
    total_profit = 0
    for order in customer["orders"]:
        for item in order["items"]:
            item_price = item["price"] *item["quantity"]
            item_cost = item["cost"] *item["quantity"]
            total_profit += get_profit(item_price, item_cost)
    print(f"Total Profit gained from {customer["name"]}: ${total_profit}")


def main():
    with open("shop.json", mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)

    for customer in data["customers"]:
        profit_per_cutomer(customer)
        
if __name__ == "__main__":
    main()       
    
