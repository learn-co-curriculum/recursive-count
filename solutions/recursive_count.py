def recursive_count(num = 0):

    # BASE CASE
    if num >= 10:
        return
    
    print(num)
    recursive_count(num + 1)
    
    # IF YOU PRINT NUM BELOW, THE NUMBERS PRINT BACKWARDS FROM 9 TO 0. WHY?
    # print(num)

if __name__ == "__main__":
    recursive_count()