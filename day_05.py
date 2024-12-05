def main():
    with open("./input.txt", "r") as f:
        lines = f.readlines()
    
    rules_raw = []
    updates_raw = []
    boundary = False
    for line in lines:
        if line == "\n":
            boundary = True
            continue
        if not boundary:
            rules_raw.append(line)
        else:
            updates_raw.append(line)
    
    rules = {}

    for i in range(len(rules_raw)):
        a, b = rules_raw[i].rstrip().split("|")
        a, b = int(a), int(b)
        if a not in rules:
            rules[a] = [b]
        else:
            rules[a] += [b]
    
    updates = []
    for pages_raw in updates_raw:
        pages_raw = pages_raw.rstrip().split(",")
        pages = []
        for page in pages_raw:
            page = int(page)
            pages.append(page)
        updates.append(pages)

    correct_pages = []
    wrong_pages = []
    for pages in updates:
        is_correct = True
        
        for i in range(len(pages)-1, -1, -1):
            page = pages[i]

            if page in rules:
                after_pages_constraints = rules[page]
            else:
                after_pages_constraints = []

            if len(after_pages_constraints) == 0:
                continue
            for j in range(i-1, -1, -1):
                prev_page = pages[j]
                if prev_page in after_pages_constraints:
                    is_correct = False
        
        if is_correct:
            correct_pages.append(pages)
        else:
            wrong_pages.append(pages)

    middle_sum = 0
    for correct_page in correct_pages:
        middle_val = correct_page[len(correct_page)//2]
        
        middle_sum += middle_val

    print(middle_sum)

    # part 2
    modified_pages = []
    for idx in range(len(wrong_pages)):
        pages = wrong_pages[idx]
        
        pointer_1 = len(pages) - 1
        
        is_correct = False
        while pointer_1 >= 0:   
            page = pages[pointer_1]
            
            if page in rules:
                after_pages_constraints = rules[page]
            else:
                after_pages_constraints = []

            if len(after_pages_constraints) == 0:
                pointer_1 -= 1
                continue
            
            pointer_2 = pointer_1 - 1
            
            while pointer_2 >= 0:
                prev_page = pages[pointer_2]
                if prev_page in after_pages_constraints:
                    temp_val = prev_page
                    pages[pointer_2] = page
                    pages[pointer_1] = temp_val
                    
                    temp_p = pointer_2
                    pointer_2 = pointer_1
                    pointer_1 = temp_p

                    pointer_1 = len(pages) - 1
                    pointer_2 = pointer_1 - 1
                    is_correct = False
                    break
                else:
                    is_correct = True
                    pointer_2-=1
                    
            if is_correct:
                pointer_1-=1

        modified_pages.append(pages)
        
    middle_sum = 0

    for modified_page in modified_pages:
        
        middle_val = modified_page[len(modified_page)//2]
        
        middle_sum += middle_val

    print(middle_sum)

if __name__ == "__main__":
    main()