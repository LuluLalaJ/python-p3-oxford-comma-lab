# def oxford_comma(items):
#     if len(items) == 0:
#         return "List can't be empty"
#     elif len(items) == 1:
#         return(items[0])
#     elif len(items) == 2:
#         return(f'{items[0]} and {items[1]}')
#     else:
#         before_and = items[:-1]
#         return ", ".join(before_and) + f', and {items[-1]}'

def oxford_comma(items):
    if len(items) > 1:
        items[-1] = "and " + items[-1]

    if len(items) > 2:
        return ', '.join(items)
    else:
        return ' '.join(items)
