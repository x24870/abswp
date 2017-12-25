cost = 10000
buied_bitcon = 427000
trade_rate = 0.1
sell_bitcon = 520000

wallet = 10000 / (buied_bitcon * trade_rate + buied_bitcon)

print(wallet)

sold = wallet * (sell_bitcon - sell_bitcon * trade_rate)

print(sold)

paid_rate = (sold - cost) / cost

print('the value is : ' + '{:.2%}'.format(paid_rate))