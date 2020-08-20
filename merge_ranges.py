def merge_these(r1,r2):
    if r1[1] >= r2[1]:
        return (r1[0],r1[1])
    else:
        return (r1[0],r2[1])

def merge_ranges(ranges):
    ranges.sort()
    merged_list = []
    current = ranges[0] #init the first range
    print("input: ",ranges)
    end = len(ranges)-1
    i = 0
    while i < end:
        current = ranges[i]
        # print(current[1],' >= ',ranges[i+1][0],' ?')
        while i < end and (current[1]) >= (ranges[i+1][0]):
            current = merge_these(current,ranges[i+1])
            i +=1
        merged_list.append(current)
        i +=1
        if i == end and ranges[i] != merged_list[-1]:
            merged_list.append(ranges[i])

    return merged_list
        

# TEST MERGE RANGES
ranges = [(0,1),(3,5),(4,8),(10,12),(9,10)]
print("merged list: ", merge_ranges(ranges))
print("--------")
ranges = [(0,1),(3,5),(4,8),(10,12),(9,10),(8,13)]
print("merged list: ", merge_ranges(ranges))
print("--------")
ranges = [(0,1),(3,4),(4,5),(11,12),(9,10),(8,9),(13,14)]
print("merged list: ", merge_ranges(ranges))