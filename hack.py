import requests as req

response = req.get('http://api.compropago.com/')
for user in response.json():
	print('ID:{}'.format(user))
