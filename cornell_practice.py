## Michael's Space:
##




## Eric's Space:
def dudu():
    n = '-1.2 3.5 47.1 0.19'
    x = n.strip().split(" ")
    a = float(x[0])
    b = float(x[1])
    c = float(x[2])
    d = float(x[3])
    e = 3
    f = ((2 * c) - (8 * a))
    g = (4 * (a**2) + (4 * (b**2)) - (c**2) - (d**2))

    if (f**2 - (4 * e * g)) >= 0:
        sol1 = ((-1 * f) + (f**2 - (4 * e * g))**(1/2))/(2 * e)
        sol2 = ((-1 * f) - (f**2 - (4 * e * g))**(1/2))/(2 * e)
    else:
        return "NO"

    if sol1 < sol2:
        return sol1
    else:
        return sol2

#print(dudu())


def problemSolving(input):
    j = 0
	data = input.split(" ")
	team = int(data[0]) # The number of teammates
	num_questions = int(data[1]) # The number of questions
	problem_times = [int(x) for x in data[2:]] # times spent for each question -- LIST
	problem_times.sort(reverse=True)
	print(problem_times[::team])
	newlist = []
	divy = len(problem_times) // team
	duuvy = divy if divy * 2 == len(problem_times) else divy + 1
	for x in range( duuvy ):
		part = problem_times[:team]
		newlist.append(part)
		problem_times = problem_times[team:]
	# [ [7, 6, 4], [2, 1]]
    for x, i in enumerate(newlist):
    	j += (x+1) * sum(i)
    return j


print(problemSolving("5 2 4 2 6 1 7"))

## Abir's Space:
# bananas are so cool
	#
	#
    # # if you are solving n problems, and your times are a, b, and c
	#
    # 3 * a + 2 * b + 1 * c
	#
	#
    # #1st problem, you spend a seconds
    # #2nd problem, you spend a + b seconds
    # #3rd problem, you spend a + b + c
	#
    # # [1,2,4,6,7]
	#
    # A - 1 * 6 + 2 * 2 + 3 * 1
	#
    # B - 1 * 7 + 2 * 4
