from tqdm import tqdm
import datetime

def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    
    disk_map = [row.rstrip() for row in lines]
    disk_map = disk_map[0]

    disk_block = []
    space_indices = []
    counter = 0
    total_num = 0

    print("Generating disk block...")
    for i in range(len(disk_map)):
        repeated_num = int(disk_map[i])
        id_num = i//2
        is_space = i%2

        for j in range(repeated_num):
            if not is_space:
                disk_block.append(str(id_num))
                total_num += 1
            else:
                disk_block.append(".")
                space_indices.append(counter)
            counter += 1
        
    assert total_num + len(space_indices) == len(disk_block)
    
    disk_block_2 = disk_block.copy()

    rev_disk_block = disk_block[::-1].copy()
    
    print("Reallocating...")
    for x in tqdm(range(len(space_indices))):
        index = space_indices[x]
        if "." in disk_block[0:total_num]:
            y = 0
            while True:
                if rev_disk_block[y] != ".":
                    disk_block[index] = rev_disk_block[y]
                    disk_block[len(disk_block)-1-y] = "."

                    rev_disk_block[y] = "."
                    break
                else:
                    y += 1
    
    print("Calculating check sum...")
    check_sum = 0
    for a in range(len(disk_block)):
        if disk_block[a] != ".":
            val = int(disk_block[a])
            check_sum += (a*val)

    print(check_sum)

    # part 2    
    rev_file_dict = update_reverse_file_dict(disk_block_2)
    
    space_dict = update_space_dict(disk_block_2)

    space_pointer = 0
    file_pointer = 0

    print("Reallocating...")
    start_t = datetime.datetime.now()
    while True:
        file = list(rev_file_dict.keys())[file_pointer]
        for i, val in enumerate(disk_block_2):
            if val == file:
                file_index = i
                break
        file_len = rev_file_dict[file]

        for space_pointer in range(len(space_dict)):
            space_index = list(space_dict.keys())[space_pointer]
            space_len = space_dict[space_index]
            if rev_file_dict[file] <= space_len and file_index > space_index:
                disk_block_2 = update_disk_block(disk_block_2, file, file_len, space_index)       
                space_dict = update_space_dict(disk_block_2)
           
                break        
        
        file_pointer += 1
        
        if file_pointer == len(rev_file_dict):
            break
    end_t = datetime.datetime.now()
    
    print("Time taken for reallocating", end_t - start_t)

    check_sum = 0
    for a in range(len(disk_block_2)):
        if disk_block_2[a] != ".":
            val = int(disk_block_2[a])
            check_sum += (a*val)

    print(check_sum)

def check_two_dict(d1, d2):
    true_arr = []
    for k1, k2 in zip(d1,d2):
        if k1 == k2:
            true_arr.append(True)
        else:
            true_arr.append(False)
    if all(true_arr):
        return True
    else:
        return False
    
def update_space_dict(disk_block, index = 0):
    space_dict = {}

    space_count = 0
    space_start = False
    space_start_index = None

    while True:
        if index == len(disk_block):
            break
        
        if disk_block[index] != ".":
            space_start = True
        
        if disk_block[index] == ".":
            if space_start:
                space_start_index = index
            space_start = False
            space_count += 1
            
        else:
            if space_start_index:
                space_dict[space_start_index] = space_count
            space_count = 0
            space_start_index = None

        index += 1
    
    return space_dict

def update_disk_block(disk_block, file, file_len, space_index):
    for i in range(file_len):
        disk_block[space_index+i] = file

    for j in range(len(disk_block)-1, 0, -1):
        if disk_block[j] == file:
            for k in range(file_len):
                disk_block[j-k] = "."
            break

    return disk_block

def update_reverse_file_dict(disk_block):
    reverse_disk_block = disk_block[::-1].copy()
    rev_file_dict = {}
    for m in range(len(reverse_disk_block)):
        file_end = reverse_disk_block[m]
        
        if file_end in rev_file_dict or file_end == ".":
            continue

        file_size = 1
        for n in range(m+1, len(reverse_disk_block)):
            file = reverse_disk_block[n]
            if file == file_end:
                file_size += 1
        rev_file_dict[file_end] = file_size
    return rev_file_dict

if __name__ == "__main__":
    main()