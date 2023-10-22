def shop_from_grocery_list(budget: int, grocery_list: list, *products):
    purchased_goods = []
    for product, price in products:
        if product not in purchased_goods and product in grocery_list:
            if price > budget:
                break
            purchased_goods.append(grocery_list.pop(grocery_list.index(product)))
            budget -= price

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."
    return f"You did not buy all the products. Missing products: {', '.join(x for x in grocery_list)}."


