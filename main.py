class ItemToPurchase:
  def __init__(self):
      self.item_name = "none"
      self.item_price = 0.0
      self.item_quantity = 0

  def print_cart_items_cost(self):
      print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")

if __name__ == "__main__":
  # Ask the user for the number of items to add
  number_items = int(input("How many items do you wish to add?\n"))

  # Create a list to store the items
  items_list = []

  # Loop to get input for each item
  for i in range(number_items):
      print(f"\nItem {i + 1}")
      cart_item = ItemToPurchase()
      cart_item.item_name = input("Input the name of the item:\n")
      cart_item.item_price = float(input("Input the price of the item:\n"))
      cart_item.item_quantity = int(input("Input the quantity of the item:\n"))
      items_list.append(cart_item)

  # Output the costs of the items
  print("\n***TOTAL COST***")
  total_amount_cost = 0
  for cart_item in items_list:
      cart_item.print_cart_items_cost()
      total_amount_cost += cart_item.item_quantity * cart_item.item_price

  # Output the total cost
  print(f"\nTotal: ${total_amount_cost}")