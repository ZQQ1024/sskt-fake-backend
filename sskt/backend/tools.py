# arry format like: {'rank': 0, 'username': 'null', 'money': 0, 'number': 0}
# sort for money in arry
def cus_quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        cus_quick_sort(array, l, q - 1)
        cus_quick_sort(array, q + 1, r)


def partition(array, l, r):
    x = array[r]['money']
    i = l - 1
    for j in range(l, r):
        if array[j]['money'] >= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1
