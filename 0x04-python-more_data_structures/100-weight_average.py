#!/usr/bin/python3
def weight_average(my_list=[]):
    result = 0
    if len(my_list) == 0:
        return result
    else:
        totalweights = 0
        totalvars = 0
        vtimesw_list = [a[0] * a[1] for a in my_list]
        w_list = [a[1] for a in my_list]
        for i in range(len(vtimesw_list)):
            totalvars += vtimesw_list[i]
        for x in range(len(w_list)):
            totalweights += w_list[x]
        result += totalvars / totalweights
        return result
