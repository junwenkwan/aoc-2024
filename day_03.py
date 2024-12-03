import string
import re

def solve_p1(line):
    mul_sum = 0
    for i in range(len(line)):
        first_num_len = 0
        first_num_index = 0
        first_num_first_seen = True
        second_num_len = 0
        second_num_index = 0
        second_num_first_seen = True

        if line[i] == "m" and line[i+1] == "u" and line[i+2] == "l" and line[i+3] == "(":    
            # find first number
            lower_bound = i
            for j in range(i+4, len(line)):
                if line[j].isdigit() and first_num_first_seen:
                    first_num_len += 1
                    first_num_index = j
                    first_num_first_seen = False
                elif line[j].isdigit():
                    first_num_len += 1
                elif line[j] == ",":
                    first_num = line[first_num_index:first_num_index+first_num_len]
                    break
                    
            # find second number
            for j in range(i+4+first_num_len, len(line)):
                if line[j].isdigit() and line[j-1] == "," and second_num_first_seen:
                    second_num_len += 1
                    second_num_index = j
                    second_num_first_seen = False
                elif line[j].isdigit():
                    second_num_len += 1
                elif line[j] in string.punctuation and line[j] != ",":
                    upper_bound = j
                    if line[j] == ")":
                        second_num = line[second_num_index:second_num_index+second_num_len]
                    else:
                        second_num = None
                    break

            if second_num:
                expression = line[lower_bound:upper_bound+1]
                mul_val = int(first_num) * int(second_num)
                mul_sum += mul_val
    return mul_sum     

def solve_p2(line):
    mul_sum = 0
    enable = True

    for i in range(len(line)):
        first_num_len = 0
        first_num_index = 0
        first_num_first_seen = True
        second_num_len = 0
        second_num_index = 0
        second_num_first_seen = True    

        if line[i:i+4] == "do()":
            enable = True
            continue

        if line[i:i+7] == "don't()":
            enable = False            
            continue
        
        if enable:
            if line[i] == "m" and line[i+1] == "u" and line[i+2] == "l" and line[i+3] == "(":    
                # find first number
                lower_bound = i
                for j in range(i+4, len(line)):
                    if line[j].isdigit() and first_num_first_seen:
                        first_num_len += 1
                        first_num_index = j
                        first_num_first_seen = False
                    elif line[j].isdigit():
                        first_num_len += 1
                    elif line[j] == ",":
                        first_num = line[first_num_index:first_num_index+first_num_len]
                        break
                        
                # find second number
                for j in range(i+4+first_num_len, len(line)):
                    if line[j].isdigit() and line[j-1] == "," and second_num_first_seen:
                        second_num_len += 1
                        second_num_index = j
                        second_num_first_seen = False
                    elif line[j].isdigit():
                        second_num_len += 1
                    elif line[j] in string.punctuation and line[j] != ",":
                        upper_bound = j
                        if line[j] == ")":
                            second_num = line[second_num_index:second_num_index+second_num_len]
                        else:
                            second_num = None
                        break

                if second_num:
                    expression = line[lower_bound:upper_bound+1]
                    mul_val = int(first_num) * int(second_num)
                    mul_sum += mul_val
                    mul_val = 0
        else:
            continue

    return mul_sum     

def main():
    # part 1
    with open("./input.txt", "r") as f:
        lines = f.readlines()

    final_sum = 0        
    for line in lines:
        val = solve_p1(line)
        final_sum += val
    print(final_sum)

    # part 2
    aoc_input = "".join([line for line in lines])
    val = solve_p2(aoc_input)
    print(val)

if __name__ == "__main__":
    main()
   
