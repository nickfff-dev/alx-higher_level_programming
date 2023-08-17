def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) == 0:
        exit()
    else:
        ([print('{}: {}'.format(item, a_dictionary[item]))
          for item in sorted(a_dictionary)])
