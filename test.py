from pprint import pprint
import json

with open("shop.json", mode="r", encoding="utf-8") as read_file:
    data = json.load(read_file)


def get_customer_price(data):
    order_prices = dict()
    for customer in data:
        for order in customer["orders"]:
            for item in order["items"]:
                item_quantity = item["quantity"]
                item_price = item["price"] *item["quantity"]
                item_cost = item["cost"] *item["quantity"]
        order_prices[customer['customer_id']] = { "item_quantity" :item_quantity , "item_price":item_price,"item_cost":item_cost}   
    return order_prices   


test = get_customer_price(data["customers"])
print(test)