def merge_sort(my_list):
    if (len(my_list) > 1):
        mid = len(my_list) // 2
        leftside = my_list[:mid]
        rightside = my_list[mid:]

        merge_sort(leftside)
        merge_sort(rightside)

        left_index = 0
        right_index = 0
        main_index = 0

        while left_index < len(leftside) and right_index < len(rightside):
            if leftside[left_index] < rightside[right_index]:
                my_list[main_index] = leftside[left_index]
                left_index += 1
            else:
                my_list[main_index] = rightside[right_index]
                right_index += 1
            main_index += 1

        while left_index < len(leftside):
            my_list[main_index] = leftside[left_index]
            left_index += 1
            main_index += 1

        while right_index < len(rightside):
            my_list[main_index] = rightside[right_index]
            right_index += 1
            main_index += 1


# def mergeSort(alist):
#     print("Splitting ", alist)
#     if len(alist) > 1:
#         mid = len(alist)//2
#         lefthalf = alist[:mid]
#         print('left', lefthalf)
#         righthalf = alist[mid:]
#         print('right', righthalf)

#         mergeSort(lefthalf)
#         mergeSort(righthalf)

#         i = 0
#         j = 0
#         k = 0

#         print("mergin", alist, "with elements left: ",
#               lefthalf, "with right", righthalf)
#         while i < len(lefthalf) and j < len(righthalf):
#             if lefthalf[i] < righthalf[j]:
#                 alist[k] = lefthalf[i]
#                 i = i+1
#             else:
#                 alist[k] = righthalf[j]
#                 j = j+1
#             k = k+1

#         while i < len(lefthalf):
#             alist[k] = lefthalf[i]
#             i = i+1
#             k = k+1

#         while j < len(righthalf):
#             alist[k] = righthalf[j]
#             j = j+1
#             k = k+1
#     print("Merging ", alist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
merge_sort(alist)
print(alist)
