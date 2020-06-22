import requests
payload = "{\"metricKeys\": [\"item_sold_minecraft\"]}"
r = requests.post("https://api.mojang.com/orders/statistics", data=payload).json()
costs = [29.99, 49.99, 23.95, 6.99, 20]
cost = 0
for x in costs:
    cost = cost + x
cost = cost/len(costs)-1
moneyobject = {
    'today': r["last24h"]*cost,
    'total': r["total"]*cost
}
print(moneyobject)