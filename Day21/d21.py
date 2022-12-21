with open("input.txt", "r") as inputFile:
    monkeysJobOrig = {}
    monkeysNumOrig = {}
    for line in inputFile.read().splitlines():
        name, job = line.split(':')
        job = job.strip().split(' ')
        if len(job) == 1:
            monkeysNumOrig[name] = int(job[0])
        else:
            monkeysJobOrig[name] = job

    monkeysJob = monkeysJobOrig.copy()
    monkeysNum = monkeysNumOrig.copy()
    while len(monkeysJob) != 0:
        for name in list(monkeysJob.keys()):
            n1, op, n2 = monkeysJob[name]
            if n1 in monkeysNum and n2 in monkeysNum:
                monkeysNum[name] = eval(
                    str(monkeysNum[n1]) + op + str(monkeysNum[n2]))
                monkeysJob.pop(name)
    print(int(monkeysNum['root']))

    #Reduce jobs to keep only those affected by 'humn'
    monkeysNumRed = monkeysNumOrig.copy()
    monkeysJobRed = monkeysJobOrig.copy()
    prevLength = 0
    while prevLength != len(monkeysJobRed):
        prevLength = len(monkeysJobRed)
        for name in list(monkeysJobRed.keys()):
            if 'humn' in monkeysJobRed[name]:
                continue
            n1, op, n2 = monkeysJobRed[name]
            if n1 in monkeysNumRed and n2 in monkeysNumRed:
                monkeysNumRed[name] = eval(
                    str(monkeysNumRed[n1]) + op + str(monkeysNumRed[n2]))
                monkeysJobRed.pop(name)

    input = 0
    foundUpperLimit = False
    inc = 100000000000000  #inc is regressed based on the return of 'root' evalution
    while True:
        monkeysNum = monkeysNumRed.copy()
        monkeysJob = monkeysJobRed.copy()
        monkeysNum['humn'] = input
        changeInput = False
        while len(monkeysJob) != 0 and not changeInput:
            for name in list(monkeysJob.keys()):
                n1, op, n2 = monkeysJobRed[name]
                if n1 in monkeysNum and n2 in monkeysNum:
                    if name == 'root':
                        if monkeysNum[n1] < monkeysNum[n2]:
                            if not foundUpperLimit:
                                inc = inc >> 2
                            foundUpperLimit = True
                            changeInput = True
                            break
                        elif monkeysNum[n1] > monkeysNum[n2]:
                            foundUpperLimit = False
                            changeInput = True
                            break
                        else:
                            print(input)
                            exit()
                    else:
                        monkeysNum[name] = eval(
                            str(monkeysNum[n1]) + op + str(monkeysNum[n2]))
                        monkeysJob.pop(name)
        input += inc if not foundUpperLimit else -inc