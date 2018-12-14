# random-agent
A short and sweet Python Class which returns a UserAgent string by querying the simple API I hosted on http://useragent.ddns.net

```
from UserAgent import UserAgent

HTTP_HEADERS = {
	"User-Agent" : "Fallback UserAgent"
}
try: 
	HTTP_HEADERS["User-Agent"] = UserAgent.RandomAgent()
except ConnectionError:
	pass

print(HTTP_HEADERS["User-Agent"])
```

A few examples shown with the interpreter:

```
>>> UserAgent.RandomAgent()
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
>>> UserAgent.RandomAgent()
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
>>> UserAgent.RandomAgent()
'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:63.0) Gecko/20100101 Firefox/63.0'
>>> UserAgent.FirefoxAgent()
'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'
>>> UserAgent.ChromeAgent()
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
>>> UserAgent.IEAgent()
'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko'
```
