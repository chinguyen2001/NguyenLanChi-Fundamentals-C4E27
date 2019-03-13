def get_even_list(l):
    evenlist = []
    for v in l:
        if v % 2 == 0:
            evenlist.append(v)
    print("The new even list is", evenlist)
    return evenlist

even_list = get_even_list([1, 2, 5, 9, -10, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")
