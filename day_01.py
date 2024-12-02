from collections import Counter

# part 1
with open("./input.txt", "r") as f:
    lines = f.readlines()
    
left_arr = []
right_arr = []
for line in lines:
    vals = line.rstrip().split("   ")
    left_arr.append(int(vals[0]))
    right_arr.append(int(vals[1]))

sorted_left_arr = sorted(left_arr)
sorted_right_arr = sorted(right_arr)

sum_dist = 0
for i in range(len(sorted_left_arr)):
    distance = abs(sorted_left_arr[i] - sorted_right_arr[i])
    sum_dist += distance

print(sum_dist)

# part 2
counter_right_arr = Counter(sorted_right_arr)

sum_similarity = 0
for i in range(len(sorted_left_arr)):
    item = sorted_left_arr[i]
    if item in counter_right_arr:
        similarity = item * counter_right_arr[item]
        sum_similarity += similarity

print(sum_similarity)