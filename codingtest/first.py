# 1. 각 거래는 실행된 금액과 날짜를 지정한다. 금액이 음수이면 카드결제, 그렇지 않으면 수신 이체(금액의 최소는 0원)
# 2. 각 거래 날짜 형식은 YYYY-MM-DD 형식을 따른다. 또한 카드를 갖는 데 월 5달러의 수수료가 있다. 
# 3. 이 수수료는 그 달에 최소 3회 이상 카드로 지불하여 총 비용이 100달러 이상이 되지 않는 한 매월 말에 계좌잔액에서 공제된다.

# 4. 내 과제는 2020년 말에 계정의 최종 잔액을 계산하는 것이다.
# 함수를 작성해라

# 거래 금액을 나타내는 N개의 정수로 구성된 배열 A와 거래 날짜를 나타내는 N개의 문자열로 구성된 D가 주어지면 2020년 말 계좌의 최종 잔액을 반환.
# 거래번호 K(0...N-1 범위 내의 K는) D[k]로 표시된 날짜에 금액 A[K]에 대해 실행되었다.as_integer_ratio
# EX) 1. A = [100, 100, 100, -10] 이고 D = ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]dlf Eo gkatnsms 230을 반환해야한다.
# 총 수입은 100 + 100 + 100 - 10 = 290 이었고 수수료는 매달 지불되었으므로 290 - (5*12) = 230

# 2. A = [180, -50 , -25, -25 ] D= ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]인 경우 25를 반환 180 - 100 - (5*11) = 25

# 3. A = [1, -1, 0, -105, 1]이고 D = ["2020-12-31", "2020-04-04", "2020-04-04", "2020-07-12"]일 때 -164
# 1 - 1 + 0 - 105 + 1 - (5*12) = -164



# 조건
# N 은 [1 ... 100] 범위 내의 정수입니다.
# 배열 A의 각 요소는 [-1000 ... 1000] 범위 내의 정수
# D에는 2020-01-01 부터 2020-12-31을 나타내는 문자열이 포함
# 정확성에 초점을 맞춰야함

from collections import defaultdict
from datetime import datetime

def calculate_final_balance(A, D):
    balance = 0
    monthly_card_usage = defaultdict(lambda: [0, 0])
    
    for amount, date in zip(A, D):
        balance += amount
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        month = date_obj.month
        
        if amount < 0:
            monthly_card_usage[month][0] += 1

            monthly_card_usage[month][1] += amount

    for month in range(1, 13):
        card_count, card_spent = monthly_card_usage[month]
        
        if card_count < 3 or card_spent < -100:
            balance -= 5

    return balance

print(calculate_final_balance([100, 100, 100, -10], ["2020-12-31", "2020-12-22", "2020-12-03", "2020-12-29"]))
print(calculate_final_balance([180, -50, -25, -25], ["2020-01-01", "2020-01-01", "2020-01-01", "2020-01-31"]))
print(calculate_final_balance([1, -1, 0, -105, 1], ["2020-12-31", "2020-04-04", "2020-04-04", "2020-04-14","2020-07-12"]))
print(calculate_final_balance([500, -50, -30, -20], ["2023-01-05", "2023-01-10", "2023-01-15", "2023-01-20"]))


