"""
실습 6: 시간 변환

초(seconds)를 입력받아 시, 분, 초로 변환하여 출력하세요.

힌트: //(몫)과 %(나머지)를 사용합니다.
      1시간 = 3600초, 1분 = 60초
"""

seconds = int(input("초를 입력하세요: "))

# 아래에 시, 분, 초로 변환하여 출력하세요

# 입력 받은 초(seconds)를 3600(1시간)초로 나눈 몫과 나머지를 구한다.
hour = seconds // 3600 # 몫 = 시간(hour)
hour_remain = seconds % 3600 # 나머지 hour_remain은 다음 계산에서 변수 seconds를 대신함

minute = hour_remain // 60 # 몫 = 분(minute)
minute_remain = hour_remain % 60 
# 나머지 minute_remain은 출력 할 초(output_seconds)의 값임
output_seconds = minute_remain

print(f"{hour}시간 {minute}분 {output_seconds}초")

"""
[실행 결과 예시] (입력: 3725)
3725초
= 1시간 2분 5초
"""
