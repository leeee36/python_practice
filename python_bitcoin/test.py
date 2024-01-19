import pyupbit

access = "04w4w4to7pcMWiWsA3UkqK1SOtZXzlPqMI4xl8xN"
secret = "StrbMb4W8JoKyp6ABxrz4AeghoV0msYHUC6vaO6p"
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-BTC 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회

# 연결이 잘 되고 있다는 것을 알 수 있음