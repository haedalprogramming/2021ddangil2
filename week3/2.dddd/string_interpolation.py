# 문자열 갖고 놀기
a = 123
new_s = f'{a}'
print(new_s)

# 문자열 옛날 방식
f'%s %s' % ('one', 'two')
print(f'%s %s' % ('one', 'two'))

# pyformat
'{} {}'.format('one', 'two')
print('{} {}'.format('one', 'two'))

# f-string
a, b = 'one', 'two'
f'{a} {b}'
print(f'오늘 {a} 나는 {b}')

# example
name = '해달'
eng_name = "Haedal"

# f-string 활용해 한국이름, 영어이름 소개
print(f'안녕 내 이름은 ')
print(f'영어 이름은')