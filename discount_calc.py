original_price = float(input('Enter original price: '))
discount = float(input('Enter discount: '))

def discount_calc(original_price, discount):
    if(discount >=20):
        final_price = original_price * (discount/100)
        return final_price
    else:
        return original_price

final_price = discount_calc(original_price, discount)

print('Final price is ', final_price)