def typed(s1, s2):
    l1 = []
    l2 = []
    for i in range(len(s1)):
        if s1[i]=='#':
            if l1:
                l1.pop()
        else:
            l1.append(s1[i])
    for i in range(len(s2)):
        if s2[i]=='#':
            if l2:
                l2.pop()
        else:
            l2.append(s2[i])
    return l1==l2
    
        
