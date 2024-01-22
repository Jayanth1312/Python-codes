def order_biryani(size, *type, **details):
    print(f'Ordered a {size} of following type- ')
    for order_type in type:
        print(f'{order_type}')
    print(details)


order_biryani('Family Bucket', 'Boneless', 'Lollipop', 'soda', delivery=True, Tip=10)
