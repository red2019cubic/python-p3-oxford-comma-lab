def oxford_comma(items):
    new_items = []
    for i in range(len(items) - 1):
        new_items.append(items[i])
    new_string = ", ".join(new_items) 
    if len(items) == 1:
        n_string = items[0]
    elif len(items) == 2: 
       n_string = new_string +  " and " + items[len(items) - 1]
    elif len(items) > 2:
       n_string = new_string +  ", and " + items[len(items) - 1]
   
    return n_string
print(oxford_comma(["fiddleheads", "okra", "kohlrabi"]))