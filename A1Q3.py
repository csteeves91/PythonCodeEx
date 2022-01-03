def ident_prs(num_list):

    numIn = {}
    for i in range(len(num_list)):
        currEl = num_list[i]
        if currEl in numIn:
            numIn[currEl].append(i)
               
        else:
            numIn[currEl] = [i]      
    answer = []
    for key in numIn:
        if len(numIn[key]) > 1:
            identNumIn = numIn[key]
            for i in range(len(identNumIn)):
                for j in range(i+1, len(identNumIn)):
                    answer.append((identNumIn[i], identNumIn[j]))
    answer.sort()
    return len(answer), answer
totalIdentPrs, listIdentPrs = ident_prs([-1,4,5,7,2,1,2,2,3,-1,7])
print(totalIdentPrs, listIdentPrs)