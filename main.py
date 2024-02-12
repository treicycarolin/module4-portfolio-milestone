class ItemToPurchase:
  def __init__(self):
      self.item_name = "none"
      self.item_price = 0.0
      self.item_quantity = 0

  def print_item_cost(self):
      print(f"{self.item_name} {self.item_quantity} @ ${self.item_price} = ${self.item_quantity * self.item_price}")


if __name__ == "__main__":
  # Ask the user for the number of items to add
  num_items = int(input("How many items do you want to add?\n"))

  # Create a list to store the items
  items_list = []

  # Loop to get input for each item
  for i in range(num_items):
      print(f"\nItem {i + 1}")
      item = ItemToPurchase()
      item.item_name = input("Enter the item name:\n")
      item.item_price = float(input("Enter the item price:\n"))
      item.item_quantity = int(input("Enter the item quantity:\n"))
      items_list.append(item)

  # Output the costs of the items
  print("\nTOTAL COST")
  total_cost = 0
  for item in items_list:
      item.print_item_cost()
      total_cost += item.item_quantity * item.item_price

  # Output the total cost
  print(f"\nTotal: ${total_cost}")
