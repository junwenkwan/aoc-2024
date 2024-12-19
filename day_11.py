def solve_p1(stones, max_blinks):
    counter = 0
    num_blinks = 0

    while True:
        if num_blinks == max_blinks:
            break

        if counter == len(stones):            
            num_blinks += 1
            counter = 0    
            print("blinks:", num_blinks, "stones:", len(stones))

        stone = stones[counter]

        if stone == 0:
            stone = 1
            stones[counter] = stone
            counter += 1
        elif len(str(stone)) % 2 == 0:
            split_stone_1 = int(str(stone)[:len(str(stone))//2])
            split_stone_2 = int(str(stone)[len(str(stone))//2:])
            stones[counter] = split_stone_1
            stones.insert(counter+1, split_stone_2)
            counter += 2
        else:
            stone *= 2024
            stones[counter] = stone
            counter += 1

    return stones        

def solve_p2(stone, num_blinks, memo):
    if num_blinks == 0:
        return 1
    
    if (stone,num_blinks) in memo:
        return memo[(stone,num_blinks)]
    
    if stone == 0:
        result = solve_p2(1, num_blinks-1, memo)
    elif len(str(stone)) % 2 == 0:
        mid_pt = len(str(stone))//2
        split_stone_1 = int(str(stone)[:mid_pt])
        split_stone_2 = int(str(stone)[mid_pt:])
        result = solve_p2(split_stone_1, num_blinks-1, memo) + solve_p2(split_stone_2, num_blinks-1, memo)
    else:
        result = solve_p2(stone*2024, num_blinks-1, memo)
    
    memo[(stone,num_blinks)] = result 
    
    return result
    

def main():
    stones = [0, 7, 198844, 5687836, 58, 2478, 25475, 894]
    max_blinks = 25
    stones = solve_p1(stones, max_blinks)
    
    max_blinks = 10
    memo = {}

    sum_p2 = 0
    for stone in stones:
        ans = solve_p2(stone, max_blinks, memo)
        sum_p2 += ans
    
    print(sum_p2)

if __name__ == "__main__":
    main()