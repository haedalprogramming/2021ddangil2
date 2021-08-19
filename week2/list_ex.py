# 리스트
Haedal_Friends = ['해달이', '시라용', '아리', 
                  '메기', '사스미']
print(Haedal_Friends)

# 빈 리스트
empty = []
print(empty)

# 리스트 인덱싱
print(Haedal_Friends[0])
print(Haedal_Friends[2])
print(Haedal_Friends[-1])

# 라스트 슬라이싱
a = [0,1,2,3,4,5,6,7,8,9]
print(a[0:3])
print(a[:3])
print(a[7:])
print(a[:])
print(a)
print(a[-4:-2])

# 리스트 수정, 삭제
a[0] = 100
print(a)
del a[0]
print(a)

# 길이를 구하는 len()
a = [1,2,3,4]
print(len(a))

# 값을 추가하는 append()
a = ['a', 'b', 'c', 'd']
a.append('e')
print(a)

# 값을 정렬하는 sort()
a = [4,3,2,1]
a.sort()
print(a)