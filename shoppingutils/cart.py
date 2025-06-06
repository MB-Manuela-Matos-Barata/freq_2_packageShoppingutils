def calculate_total_price(cart):
    
    total_compra = [
        (est['Produtos'],(sum(est['preco']))
        for est in itemCarrinho
    ]
    
    return print(total_compra)