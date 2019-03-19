def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    count = 0

    for i in range(len(items)-1):
        if items[i] > items[i + 1]:
            items[i],items[i + 1] = items[i + 1],items[i]
            count += 1

    if count == 0:

        return items
    else:

        return bubble_sort(items)


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''



def quick_sort(items):

    '''Return array of items, sorted in ascending order'''

    if len(items) <= 1:
        return items
    else:
        return quick_sort([i for i in items[1:] if i <= items[0]]) + [items[0]] +\
            quick_sort([i for i in items[1:] if i > items[0]])
