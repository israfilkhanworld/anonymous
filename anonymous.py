import requests
print"                                                          "
print"   __ _ _ __   ___  _ __  _   _ _ __ ___   ___  _   _ ___ "
print"  / _` | '_ \ / _ \| '_ \| | | | '_ ` _ \ / _ \| | | / __|"
print" | (_| | | | | (_) | | | | |_| | | | | | | (_) | |_| \__ \"
print"  \__,_|_| |_|\___/|_| |_|\__, |_| |_| |_|\___/ \__,_|___/"
print"                           __/ |                          "
print"                          |___/                           "
print(" \nAnonymous Email by I͏S͏R͏ΛF͏I͏L͏ KHΛN ")
print("Coded by \033[91m github.com/israfilkhanworld \033[0m \n ")
to = input("To: ")
subject = input("Subject: '")
message = input("Message: ")

user_agent = 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
sess = requests.Session()
email_req = sess.post('http://anonymouse.org/cgi-bin/anon-email.cgi', headers={
	'Host': 'anonymouse.org',
	'User-Agent': user_agent,
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en-US,en;q=0.5',
	'Accept-Encoding': 'gzip, deflate',
	'Referer': 'http://anonymouse.org/anonemail.html',
        'Connection': 'close',
        'Upgrade-Insecure-Requests':'1',
        'Content-Type':'application/x-www-form-urlencoded'
}, data={
	'to': to,
	'subject': subject,
	'text': message
})

if 'The e-mail has been sent' in email_req.text:
    print("[+] Email Sent!")
    print("[+] In order to increase your privacy, the anonymous e-mail will be randomly delayed up to 12 hours")
