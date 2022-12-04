# 후보 추천하기
N = int(input())
c = int(input())
rec = list(map(int, input().split()))

photo = {}
for i in range(c):
    if rec[i] in photo:  # 있으면 count + 1
        photo[rec[i]][0] += 1
    else:
        if len(photo) < N:
            photo[rec[i]] = [1, i]  # [count, seq]
        else:
            temp_lst = sorted(photo.items(), key=lambda x: (x[1][0], x[1][1]))  # count, seq 정렬
            del_key = temp_lst[0][0]  # seq가 낮은 값
            del photo[del_key]  # 지우고 값 추가
            photo[rec[i]] = [1, i]

results = list(sorted(photo.keys()))
for i in results:
    print(i, end=" ")
