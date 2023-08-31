
url = 'http://127.0.0.1:5000/'


import requests
card1 = 4790729914729354
card2 = 4790729914729355
r = requests.post(url+"api/login",{"username":"user","password":"pass"
	})

r = requests.post(url+"api/balance",{"number":card1,'pin':6769})
print('card1 ',card1,'balance =',r.json())
r = requests.post(url+"api/balance",{"number":card2,'pin':3333})
print('card2 ',card2,'balance =',r.json())

print("sending money from card1 to card2")
r = requests.post(url+"api/send",{"number":card1,'pin':6769,'sendto':card2,'amount':20})
print('card1 ',card1,'balance =',r.json())

r = requests.post(url+"api/balance",{"number":card2,'pin':3333})
print('card2 ',card2,'balance =',r.json())






