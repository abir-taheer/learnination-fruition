def problemSolving(input):
    j = 0
    data = input.split(" ")
    team = int(data[0])  # The number of teammates
    # num_questions = int(data[1]) # The number of questions
    problem_times = [int(x) for x in data[2:]]  # times spent for each question -- LIST
    problem_times.sort(reverse=True)
    newlist = []
    divy = len(problem_times) // team
    duuvy = divy if divy * 2 == len(problem_times) else divy + 1
    for x in range(duuvy):
        part = problem_times[:team]
        newlist.append(part)
        problem_times = problem_times[team:]
    # [ [7, 6, 4], [2, 1]]
    for x, i in enumerate(newlist):
        j += (x + 1) * sum(i)
    return j


print(problemSolving("3 23 3462 3202 8367 5206 9981 2747 6510 7637 6212 2275 9161 2656 7253 9825 9442 5448 4207 1107 9452 1152 8639 1181 4082"))
