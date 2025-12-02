from productinfo import product_info   # make sure your file name is product_details.py

def test_get_product_info():
    result = product_info("B004", "BOULT ear buds", 25, 15.90)

    expected = (
        "Product Information:\n"
        "---------------------\n"
        "Product ID : B004\n"
        "Name       : BOULT ear buds\n"
        "Quantity   : 25\n"
        "Price      : $15.90"
    )

    assert result==expected