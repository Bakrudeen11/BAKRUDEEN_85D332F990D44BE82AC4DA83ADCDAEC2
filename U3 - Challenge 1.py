def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Test the linear_search_product function
products_list = ["Laptop", "Mouse", "Antenna", "Laptop", "Monitor"]
target_product_name = "Laptop"
result = linear_search_product(products_list, target_product_name)

if result:
    print(f"{target_product_name} found at indices: {result}")
else:
    print(f"{target_product_name} not found in the list.")
