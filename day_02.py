with open("./input.txt", "r") as f:
    lines = f.readlines()

input_arr = []
for line in lines:
    vals = line.rstrip().split(" ")
    for i in range(len(vals)):
        vals[i] = int(vals[i])
    input_arr.append(vals)

safe_sum = 0
report_status = []

# part 1
for report in input_arr:
    trend = report[1] - report[0]
    for i in range(len(report)-1):
        pointer_1 = report[i]
        pointer_2 = report[i+1]

        if pointer_2 == pointer_1:
            safe_flag = False
            break
        elif trend > 0 and pointer_2 > pointer_1 and abs(pointer_2 - pointer_1) < 4:
            safe_flag = True
        elif trend < 0 and pointer_2 < pointer_1 and abs(pointer_2 - pointer_1) < 4:
            safe_flag = True
        else:
            safe_flag = False
            break
    
    report_status.append(safe_flag)
    if safe_flag:
        safe_sum += 1    

print(safe_sum)

# part 2
for i in range(len(report_status)):
    if not report_status[i]:
        # check unsafe report here
        values = input_arr[i]
        new_safe_flag = False
        for x in range(len(values)):
            temp_arr = values.copy()
            temp_arr.pop(x)
            trend = temp_arr[1] - temp_arr[0]
            
            safe_flag_arr = []

            for y in range(len(temp_arr)-1):
                pointer_1 = temp_arr[y]
                pointer_2 = temp_arr[y+1]
                
                if pointer_2 == pointer_1:
                    safe_flag = False
                elif trend > 0 and pointer_2 > pointer_1 and abs(pointer_2 - pointer_1) < 4:
                    safe_flag = True
                elif trend < 0 and pointer_2 < pointer_1 and abs(pointer_2 - pointer_1) < 4:
                    safe_flag = True
                else:
                    safe_flag = False
                safe_flag_arr.append(safe_flag)
        
            if all(safe_flag_arr):
                new_safe_flag = True
            
            temp_arr = values.copy()
            
        report_status[i] = new_safe_flag

safe_sum = 0

for i in range(len(report_status)):
    if report_status[i]:
        safe_sum += 1

print(safe_sum)