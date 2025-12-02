def product_info(product_id,name,quantity,price):
 
    info = (
        f"Product Information:\n"
        f"---------------------\n"
        f"Product ID : {product_id}\n"
        f"Name       : {name}\n"
        f"Quantity   : {quantity}\n"
        f"Price      : ${price:.2f}"
    )
    return info


# Example usage:
print(product_info("B004","BOULT ear buds",25,15.9))