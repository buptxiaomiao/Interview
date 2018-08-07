#! /usr/bin/python

def merge1(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    a = (x for x in l1)
    b = (x for x in l2)
    data = []
    tmp1 = a.next()
    tmp2 = b.next()
    flag_a = True
    try:
        while True:
            if tmp1 <= tmp2:
                data.append(tmp1)
                flag_a = True
                tmp1 = a.next()
            else:
                data.append(tmp2)
                flag_a = False
                tmp2 = b.next()
    except StopIteration as e:
        data.append(tmp2 if flag_a else tmp1)
        item = b if flag_a else a
        try:
            while True:
                data.append(item.next())
        except StopIteration as e:
            pass
    return data

def merge2(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    data = []
    flag1, flag2 = 0, 0
    for i in range(flag1, len(l1)):
        for j in range(flag2, len(l2)):
            if l1[i] <= l2[j]:
                data.append(l1[i])
                flag1 += 1
                break
            flag2 += 1
            data.append(l2[j])
    return data

if __name__ == '__main__':
    a = range(1, 10, 2)
    b = range(2, 11, 2)
    print 'a:%s, b:%s' % (a, b)
    res_1 = merge1(a, b)
    print res_1
