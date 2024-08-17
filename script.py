from pprint import pprint

data = {
  "customers": [
    {
      "customer_id": 1,
      "name": "John Doe",
      "email": "john@example.com",
      "orders": [
        {
          "order_id": 1001,
          "date": "2024-01-15",
          "items": [
            {
              "product_id": 2001,
              "name": "Laptop",
              "quantity": 1,
              "price": 1200.00,
              "cost": 800.00
            },
            {
              "product_id": 2002,
              "name": "Mouse",
              "quantity": 2,
              "price": 25.00,
              "cost": 10.00
            }
          ]
        },
        {
          "order_id": 1002,
          "date": "2024-02-20",
          "items": [
            {
              "product_id": 2003,
              "name": "Keyboard",
              "quantity": 1,
              "price": 50.00,
              "cost": 20.00
            }
          ]
        }
      ]
    },
    {
      "customer_id": 2,
      "name": "Jane Smith",
      "email": "jane@example.com",
      "orders": [
        {
          "order_id": 1003,
          "date": "2024-01-22",
          "items": [
            {
              "product_id": 2004,
              "name": "Smartphone",
              "quantity": 1,
              "price": 800.00,
              "cost": 500.00
            },
            {
              "product_id": 2005,
              "name": "Headphones",
              "quantity": 1,
              "price": 150.00,
              "cost": 80.00
            }
          ]
        }
      ]
    }
  ]
}


def get_profit(price,cost):
    return price - cost
    
    
#get total profit for each customer based on price and cost
for customer in data["customers"]:
    customer_name = customer["name"]
    total_profit = 0 #resets for each customer
    
    for order in customer["orders"]:
        for item in order["items"]:
            item_price = item["price"] *item["quantity"]
            item_cost = item["cost"] *item["quantity"]
            total_profit += get_profit(item_price, item_cost)
    # print(f"Total Profit gained from {customer_name}: ${total_profit}")
    #displays:
    # Total Profit gained from John Doe: $460.0
    # Total Profit gained from Jane Smith: $370.0
    
    
    
    
    
#get the information of the customers who have more than 1 order in 2024
            item_quantity = item["quantity"]
            date = order["date"]
            if date.startswith("2024") and item_quantity > 1:
                # print(customer_name)
                #displays:
                #John Doe
                break
        
# get the top products based on total sales & calculate their profit
max_quantity = 0
top_product = None
for customer in data["customers"]:    
    for order in customer["orders"]:
        for item in order["items"]:
            item_quantity = item["quantity"]
            item_price = item["price"] *item["quantity"]
            item_cost = item["cost"] *item["quantity"]
            if item_quantity > max_quantity:
                top_product = item["name"]
                max_quantity = item_quantity #==>insert next quantity to the max quantity
                top_product_profit = get_profit(item_price,item_cost)
# print(f"Top Product: {top_product}, Total Sales: {max_quantity}, Profit: {top_product_profit}")
#displays:
# Top Product: Mouse, Total Sales: 2, Profit: 30.0
  






#get the average value of each customer's orders & print the name of customers whose average order value is > 500
def get_average(total,count):
    return total/count
customer_above_500 = []

for customer in data["customers"]:
    customer_name = customer["name"]
    customer_total_value = 0 #values of all orders made by each customer
    order_count = 0
    
    for order in customer["orders"]:
        order_value = 0 #the value of the current order
        for item in order["items"]:
            order_value += item["price"] * item["quantity"]
        customer_total_value += order_value
        order_count +=1
    customer_total_average = get_average(customer_total_value,order_count)
    print(f" Customer Name: {customer_name}, Total Value: {customer_total_value}, Num of Orders: {order_count}, Total Average: {customer_total_average}")
        #dispalys:
        # Customer Name: John Doe, Total Value: 1300.0, Num of Orders: 2, Total Average: 650.0
        # Customer Name: Jane Smith, Total Value: 950.0, Num of Orders: 1, Total Average: 950.0
    if customer_total_average > 500:
        customer_above_500.append(customer_name)
print(f"Cutomers with total average above 500: {customer_above_500}")   
#displays:
# Cutomers with total average above 500: ['John Doe', 'Jane Smith']




#calculating total sales           
def get_sales(price,quantity):
    return price * quantity

total_sales = 0
for customer in data["customers"]:
    for order in customer["orders"]:
        for item in order["items"]:
            item_quantity = item["quantity"]
            item_price = item["price"]
            item_cost = item["cost"]
            total_sales += get_sales(item_price, item_quantity)
# print(f"Total Sales: ${total_sales}")
#displays:
#Total Sales: $2250.0
        
                
