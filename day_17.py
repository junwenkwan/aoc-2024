def solve_p1(reg_a, reg_b, reg_c, program):
    instruction_ptr = 0
    output = []

    while True:
        if instruction_ptr >= len(program):
            return output

        opcode = int(program[instruction_ptr])
        operand = int(program[instruction_ptr+1])
        combo_operand = None
        
        if operand <= 3:
            combo_operand = operand
        elif operand == 4:
            combo_operand = reg_a
        elif operand == 5:
            combo_operand = reg_b
        elif operand == 6:
            combo_operand = reg_c
        elif operand == 7:
            raise ValueError("Invalid operand")
        
        if opcode == 0: # adv
            reg_a = reg_a >> combo_operand
            instruction_ptr += 2
        elif opcode == 1: # bxl
            reg_b = reg_b ^ operand
            instruction_ptr += 2
        elif opcode == 2: # bst
            reg_b = combo_operand % 8
            instruction_ptr += 2
        elif opcode == 3: # jnz
            if reg_a != 0:
                instruction_ptr = operand
            else:
                instruction_ptr += 2
        elif opcode == 4: # bxc
            reg_b = reg_b ^ reg_c
            instruction_ptr += 2
        elif opcode == 5: # out
            output.append(combo_operand % 8)
            instruction_ptr += 2
        elif opcode == 6: # bdv
            reg_b = reg_a >> combo_operand
            instruction_ptr += 2
        elif opcode == 7: # cdv
            reg_c = reg_a >> combo_operand
            instruction_ptr += 2

def solve_p2(program, inp):
    if program == []:
        return inp
    
    for i in range(8):
        val_a = (inp << 3) + i
        val_b = val_a % 8
        val_b = val_b ^ 5
        val_c = val_a >> val_b
        val_b = val_b ^ 6
        val_b = val_b ^ val_c
        
        if val_b % 8 == int(program[-1]):
            ans = solve_p2(program[:-1], val_a)
            if ans is None:
                continue
            return ans

def main():
    input = [
        "Register A: 51064159",
        "Register B: 0",
        "Register C: 0",
        "Program: 2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0"
    ]

    reg_a = 0
    reg_b = 0
    reg_c = 0
    program = None

    for line in input:
        if "Register A" in line:
            reg_a = int(line.split("Register A: ")[1])
        elif "Register B" in line:
            reg_b = int(line.split("Register B: ")[1])
        elif "Register C" in line:
            reg_c = int(line.split("Register C: ")[1])
        elif "Program" in line:
            program = line.split("Program: ")[1].split(",")
    
    output = solve_p1(reg_a, reg_b, reg_c, program)
    
    print(','.join([str(x) for x in output]))
    
    ops = [2,4,1,5,7,5,1,6,0,3,4,6,5,5,3,0]
    # 2,4 -> B = A % 8
    # 1,5 -> B = B ^ 5
    # 7,5 -> C = A >> B
    # 1,6 -> B = B ^ 6
    # 0,3 -> A = A >> 3
    # 4,6 -> B = B ^ C
    # 5,5 -> out(B % 8)
    # 3,0 -> jnz
    
    val_a = 0
    out = solve_p2(ops, val_a)
    print(out)    

if __name__ == "__main__":
    main()