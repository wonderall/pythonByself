# 리스트 연결 연산자(+)와 extend()
# 연산자 - 비파괴적, extend() - 파괴적
list_a = [1,2,3]
list_b = [4,5,6]
print(list_a+list_b)
print(list_a) # 1,2,3 비파괴적
list_a.extend(list_b)
print(list_a) # 1,2,3,4,5,6 파괴적

