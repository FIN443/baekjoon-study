# a^b

a, b = input().split()

len_down = len(a) - a.index(".") - 1
if a[0] == "0":
    a, b = int(a[2:]), int(b)
    len_down *= b
    result_temp = str(a**b)
    len_result = len_down - len(result_temp)
    result = "0." + "0" * len_result + result_temp
    print(result)

else:
    a = a.replace(".", "")
    a, b = int(a), int(b)
    result = str(a**b)
    len_down *= b
    result
    result_1, result_2 = result[:-len_down], result[-len_down:]

    print(result_1 + "." + result_2)
