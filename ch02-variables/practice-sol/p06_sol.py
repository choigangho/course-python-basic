"""
실습 6 풀이: 자료형 변환 활용하기
"""

# [1] 총 금액 계산
price = "4500"
quantity = "3"

print(int(price) * int(quantity))

# [2] 문자열 연결
name = "홍길동"
score = 95

print(name + "님의 점수는 " + str(score) + "점입니다.")

# [3] 두 숫자 입력받아 합계 출력
num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))

print("합계:", num1 + num2)
