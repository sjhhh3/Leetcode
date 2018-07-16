cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
dic = {}
ans = []

for visit in cpdomains:
    # dic[visit.split(' ')[1]] += visit.split(' ')[0]
    # print(visit.split('.', 1))
    if not dic.get(visit.split(' ')[1]):
        dic[visit.split(' ')[1]] = visit.split(' ')[0]
    else:
        dic[visit.split(' ')[1]] = int(dic[visit.split(' ')[1]]) + int(visit.split(' ')[0])

    if not dic.get(visit.split('.', 1)[1]):
        dic[visit.split('.', 1)[1]] = visit.split(' ')[0]
    else:
        dic[visit.split('.', 1)[1]] = int(dic[visit.split('.', 1)[1]]) + int(visit.split(' ')[0])

    if len(visit.split('.')) == 3:
        if not dic.get(visit.split('.')[2]):
            dic[visit.split('.')[2]] = visit.split(' ')[0]
        else:
            dic[visit.split('.')[2]] = int(dic[visit.split('.')[2]]) + int(visit.split(' ')[0])

for key in dic:
    ans.append(str(dic[key])+' '+key)

print(ans)