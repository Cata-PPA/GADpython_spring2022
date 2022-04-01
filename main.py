# Homework GAD-02


my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]
print(my_list)

ordered_my_list = []
ordered_my_list = ordered_my_list + my_list
ordered_my_list.sort()
print(ordered_my_list)

revord_my_list = []
revord_my_list = revord_my_list + my_list
revord_my_list.sort(reverse=True)
print(revord_my_list)

my_sliced_even = ordered_my_list[1::2]
print(my_sliced_even)

my_sliced_odd = ordered_my_list[::2]
print(my_sliced_odd)

multiple_of_3 = ordered_my_list[2::3]
print(multiple_of_3)
