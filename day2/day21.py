friends=[
    ("Bilen"),
    ("Tsi"),
    ("Jea"),
]
def split_bill(price, rate=0.10):
    num_of_friends=3     
    tip =price * rate
    split=price + tip
    return split/num_of_friends
for name in friends:
    print(f"{name}: You have to share {split_bill(3600)} ETB ")