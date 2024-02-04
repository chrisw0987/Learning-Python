def positive_sum(list):
    store = 0
    for i in list:
        if i > 0:
            store += i
        else: 
            continue
    print(store)
    
sample = [-3, -2, 3, 2]
positive_sum(sample)