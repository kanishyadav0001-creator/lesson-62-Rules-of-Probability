def pro_a_or_b(a, b, all_possible_outcomes):
    pro_a = len(a)/len(all_possible_outcomes)

    pro_b = len(b)/len(all_possible_outcomes)

    inter = a.intersection(b)

    prob_inter = len(inter)/len(all_possible_outcomes)

    return (pro_a + pro_b - prob_inter)

even = {2, 4, 6}
greater_than_two = {3, 4, 5, 6}
all_possible_rolls = {1, 2, 3, 4, 5, 6}

print('Probability of greettingan even number or a number greater than 2')
print(pro_a_or_b(even, greater_than_two, all_possible_rolls))