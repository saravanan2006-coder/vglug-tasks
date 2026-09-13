#find duplicate element in the list

roll_no = [712,532,812,340,411,712,340,91,122,57,]

duplicate = []
for i in range(len(roll_no)):
    for j in range(i+1,len(roll_no)):
        if roll_no[i] == roll_no[j]:
            if roll_no[i] not in duplicate:
                duplicate.append(roll_no[i])

print(duplicate)
