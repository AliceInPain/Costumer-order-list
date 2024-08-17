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
    
    
#get total profit for each costumer based on price and cost
for costumer in data["customers"]:
    costumer_name = costumer["name"]
    total_profit =0 #resets for each costumer
    
    for order in costumer["orders"]:
        for item in order["items"]:
            item_price = item["price"] *item["quantity"]
            item_cost = item["cost"] *item["quantity"]
            total_profit += get_profit(item_price, item_cost)
    print(f"Total Profit gained from {costumer_name}: ${total_profit}")
    #displays:
    # Total Profit gained from John Doe: $460.0
    # Total Profit gained from Jane Smith: $370.0
    