def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    
    button_a = []
    button_b = []
    prize = []
    
    for line in lines:
        if "Button A:" in line:
            x_a, y_a = line.split("Button A: ")[1].split(", ")
            x_a = int(x_a[2:])
            y_a = int(y_a[2:])
            button_a.append((x_a, y_a))

        if "Button B: " in line:
            x_b, y_b = line.split("Button B: ")[1].split(", ")
            x_b = int(x_b[2:])
            y_b = int(y_b[2:])
            button_b.append((x_b, y_b))

        if "Prize: " in line:
            x_p, y_p = line.split("Prize: ")[1].split(", ")
            x_p = int(x_p[2:])
            y_p = int(y_p[2:])
            prize.append((x_p, y_p))

    # part 1
    p1_ans = 0
    for i in range(len(button_a)):
        x_a, y_a = button_a[i]
        x_b, y_b = button_b[i]
        x_p, y_p = prize[i]

        num_b = (y_p * x_a - x_p * y_a) / (x_a * y_b - x_b * y_a)
        num_a = (x_p - x_b * num_b)/ x_a

        if num_a.is_integer() and num_b.is_integer():
            p1_ans += 3 * num_a + num_b

    print(p1_ans)

    # part 2
    p2_ans = 0
    for i in range(len(button_a)):
        x_a, y_a = button_a[i]
        x_b, y_b = button_b[i]
        x_p, y_p = prize[i]
        x_p += 10000000000000
        y_p += 10000000000000

        num_b = (y_p * x_a - x_p * y_a) / (x_a * y_b - x_b * y_a)
        num_a = (x_p - x_b * num_b)/ x_a

        if num_a.is_integer() and num_b.is_integer():
            p2_ans += 3 * num_a + num_b

    print(p2_ans)

if __name__ == "__main__":
    main()