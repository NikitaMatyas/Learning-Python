def get_description():
    """ Return random weather, just like the pros"""
    from random import choice  # Импортируем функцию choice из стандартного модуля Python random
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)


