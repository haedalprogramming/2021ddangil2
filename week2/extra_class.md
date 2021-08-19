# 현민님을 위한 보충 수업

아래 참고 자료 읽어보시고, 실습 코드 진행 부탁드립니다 :)

## 참고 자료
1. [정수형이란?](https://ko.wikipedia.org/wiki/%EC%A0%95%EC%88%98%ED%98%95)
2. [부울 자료형이란?](https://ko.wikipedia.org/wiki/%EB%B6%88%EB%A6%AC%EC%96%B8_%EC%9E%90%EB%A3%8C%ED%98%95)
3. [리스트란?](https://ko.wikipedia.org/wiki/%EB%A6%AC%EC%8A%A4%ED%8A%B8_(%EC%BB%B4%ED%93%A8%ED%8C%85))

## 실습 코드
### 홍길동은 어떤 사람인가? 
`example2.py`
```python
name = '홍길동'
age = 25
height = 184.6
print(type(name))
print(type(age))
print(type(height))
```
### 정수형이 뭐에요? 
`integer_ex.py`
``` python
# 정수형
a=154
print(type(a))
a = 0
print(type(a))
a = -25
print(type(a))

# 실수형
a= 181.34
print(type(a))
b=-22.22
print(type(b))

# 복소수
c = 1 + 4j
print(type(c))
print(c.real)
print(c.imag)
print(c.conjugate())
print(abs(c))

# 예제: 스스로 사칙연산을 활용해 확인해보자
a = 5
b = 3.14
c = 3 + 4j

18.28 + 16j

print(2b + 4c)
```
### 부울 자료형이 뭐에요? 
`bool.py`
```python
# 참, 거짓
# True, False
a = True
b = False
print(type(a), type(b))

x=1
y=2
print(x>y)
print(1==1) # =
```
### 리스트가 뭐에요? 
`list_ex.py`
```python
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
```