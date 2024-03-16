def count_to_num(num):
    if num>0:
        count_to_num(num-1)
        print(num)
count_to_num(12)