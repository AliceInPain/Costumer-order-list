from pprint import pprint
import json

def get_profit(price,cost):
    return price - cost
    
def get_average(total,count):
    return total/count

def customers_with_order_in_2024(order,  customer_name):
    for item in order["items"]:
        item_quantity = item["quantity"]
        date = order["date"]
        if date.startswith("2024") and item_quantity > 1:
            print(f"{customer_name} has more than one order in 2024")
            pass
    
def get_top_products(customer):
    max_quantity = 0
    top_product = None
    top_product_profit = 0
    for order in customer["orders"]:
        for item in order["items"]:
            item_quantity = item["quantity"]
            item_price = item["price"] *item_quantity
            item_cost = item["cost"] *item_quantity
            if item_quantity > max_quantity:
                max_quantity = item_quantity
                top_product= item["name"]
                top_product_profit = get_profit(item_price,item_cost)
    if max_quantity>1:
        print("Top Product is:")
        print(f"Name: {top_product},\nTotal Sales: {max_quantity},\nProfit: {top_product_profit}")


def profit_per_customer(customer):
    total_profit = 0
    customer_name =customer["name"]
    for order in customer["orders"]:
        customers_with_order_in_2024(order, customer_name)
        for item in order["items"]:
            item_quantity = item["quantity"]
            item_price = item["price"] *item_quantity
            item_cost = item["cost"] *item_quantity
            total_profit += get_profit(item_price, item_cost)
    print(f"Total Profit gained from {customer_name}: ${total_profit}")

def average_above_500(customer,customer_above_500):
    customer_name = customer["name"]
    customer_total_value = 0
    order_count = 0

    for order in customer["orders"]:
        order_value = 0
        for item in order["items"]:
            order_value += item["price"] * item["quantity"]
        customer_total_value += order_value
        order_count +=1
    customer_total_average = get_average(customer_total_value,order_count)
    print("Customers' Average Value is:")
    print(f"   Customer Name: {customer_name},\n   Total Value: {customer_total_value},\n   Num of Orders: {order_count},\n   Total Average: {customer_total_average}")
    if customer_total_average > 500:
        customer_above_500.append(customer_name)




def main():
    with open("shop.json", mode="r", encoding="utf-8") as read_file:
        data = json.load(read_file)
        
        
    customer_above_500 = []
    for customer in data["customers"]:
        
        get_top_products(customer)
        profit_per_customer(customer)
        average_above_500(customer,customer_above_500)

    print(f"Customers with total average above 500: {customer_above_500}")   




if __name__ == "__main__":
    main()       
    
