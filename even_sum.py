def even_sum(sv,ev):
    count = 0
    if sv>=ev:
        return -1
    else:
        for i in range(sv, ev+1, 1):
            if(i % 2 == 0):
                count += i
        return count

print(even_sum(7,11))