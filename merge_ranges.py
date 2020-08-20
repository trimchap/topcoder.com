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
            # merge these two meetings
            current = merge_these(current,ranges[i+1])
            i +=1 # move to the next and see if it overlaps with them too
        # current = either the merged meeting or the next one that doesn't overlap
        merged_list.append(current)
        i +=1
        # add the last meeting to the merged list if it wasn't part of the merge
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
ranges = [(1, 10), (2, 6), (3, 5), (7, 9)]
print("merged list: ", merge_ranges(ranges))
print("--------")
ranges = [(0,1),(3,4),(4,5),(11,12),(9,10),(8,9),(13,14)]
print("merged list: ", merge_ranges(ranges))
print("--------")
ranges = [(1, 2), (2, 3)]
print("merged list: ", merge_ranges(ranges))
print("--------")
ranges =  [(1, 5), (2, 3)]
print("merged list: ", merge_ranges(ranges))
  