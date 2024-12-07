from itertools import product
from tqdm import tqdm

def compute_combinations_p1(nums, ans):
    combinations = list(product("+*", repeat=len(nums)-1))

    combinations = [''.join(comb) for comb in combinations]

    val_arr = []
    for combination in combinations:
        sum_val = nums[0]
        num_operation = len(combination)
        for i in range(num_operation):
            num_next = nums[i+1]

            if combination[i] == "+":
                sum_val = sum_val + num_next
            else:
                sum_val = sum_val * num_next

        val_arr.append(sum_val)

    is_correct = False
    for val in val_arr:
        if val == ans:
            is_correct = True
            break
    return is_correct

def compute_combinations_p2(nums, ans):
    combinations = list(product("+*|", repeat=len(nums)-1))

    combinations = [''.join(comb) for comb in combinations]

    val_arr = []
    for combination in combinations:
        sum_val = nums[0]
        num_operation = len(combination)
        for i in range(num_operation):
            num_next = nums[i+1]
            if combination[i] == "+":
                sum_val = sum_val + num_next
            elif combination[i] == "*":
                sum_val = sum_val * num_next
            elif combination[i] == "|":
                concat_str = str(sum_val) + str(num_next)
                sum_val = int(concat_str)

        val_arr.append(sum_val)

    is_correct = False
    for val in val_arr:
        if val == ans:
            is_correct = True
            break 
    return is_correct

def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    expressions = [row.rstrip() for row in lines]
    
    sum_p1 = 0
    wrong_expressions = []
    for expression in expressions:
        ans, nums = expression.split(": ")
        ans = int(ans)
        nums = nums.split(" ")
        nums = [int(num) for num in nums]
    
        is_correct = compute_combinations_p1(nums, ans)
        
        if is_correct:
            sum_p1 += ans
        else:
            wrong_expressions.append(expression)
    
    print(sum_p1)

    sum_p2 = sum_p1
    for expression in tqdm(wrong_expressions):
        ans, nums = expression.split(": ")
        ans = int(ans)
        nums = nums.split(" ")
        nums = [int(num) for num in nums]
    
        is_correct = compute_combinations_p2(nums, ans)
        
        if is_correct:
            sum_p2 += ans

    print(sum_p2)

if __name__ == "__main__":
    main()