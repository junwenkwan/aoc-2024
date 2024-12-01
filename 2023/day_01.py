with open("./data/input.txt", "r") as f:
    lines = f.readlines()

# part 1
sum_digit = 0
for line in lines:
    val = line.rstrip()
    
    digit_str = ""
    for i in val:
        if i.isdigit():
            digit_str += i
    new_digit = digit_str[0] + digit_str[-1]
    digit_int = int(new_digit)
    sum_digit += digit_int
    
print(sum_digit)

# part 2
my_map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

sum_digit = 0
for line in lines:
    val = line.rstrip()
    reversed_val = val[::-1]

    digit_str = ""
    last_wdigit_index, first_wdigit_index = 999, 999
    last_wdigit_value, first_wdigit_value = None, None
     
    first_digit_index, last_digit_index = 999, 999
    first_digit_value, last_digit_value = None, None
    
    for i in my_map:
        current_index = val.find(i)
        
        if current_index == -1:
            continue
        if current_index < first_wdigit_index:
            first_wdigit_index = current_index
            first_wdigit_value = my_map[i]

    for i in my_map:
        current_index = reversed_val.find(i[::-1])
        if current_index == -1:
            continue
        if current_index < last_wdigit_index:
            last_wdigit_index = current_index
            last_wdigit_value = my_map[i]
    
    for index, item in enumerate(val):
        if item.isdigit() and index < first_digit_index  and index < first_wdigit_index:
            first_digit_value = item
            first_digit_index = index
            
    for index, item in enumerate(reversed_val):
        if item.isdigit() and index < last_digit_index  and index < last_wdigit_index:
            last_digit_value = item
            last_digit_index = index
            print(last_digit_value)

    if first_digit_index < first_wdigit_index:
        digit_str += str(first_digit_value)
    else:
        digit_str += str(first_wdigit_value)
    
    if last_digit_index < last_wdigit_index:
        digit_str += str(last_digit_value)
    else:
        digit_str += str(last_wdigit_value)

    if "None" in digit_str:
        digit_str = digit_str.replace("None", "")
    
    digit_int = int(digit_str)
    sum_digit += digit_int

print(sum_digit)
