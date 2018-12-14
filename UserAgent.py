from requests import get as GET

class UserAgent():
	domain = "http://useragent.ddns.net"

	def RandomAgent():
		ua = NewUserAgent.get_data("/")
		return NewUserAgent.format_ua(ua)

	def FirefoxAgent():
		ua = NewUserAgent.get_data("/firefox")
		return NewUserAgent.format_ua(ua)

	def ChromeAgent():
		ua = NewUserAgent.get_data("/chrome")
		return NewUserAgent.format_ua(ua)

	def OperaAgent():
		ua = NewUserAgent.get_data("/opera")
		return NewUserAgent.format_ua(ua)

	def SafariAgent():
		ua = NewUserAgent.get_data("/safari")
		return NewUserAgent.format_ua(ua)

	def ChromiumAgent():
		ua = NewUserAgent.get_data("/chromium")
		return NewUserAgent.format_ua(ua)

	def IEAgent():
		ua = NewUserAgent.get_data("/ie")
		return NewUserAgent.format_ua(ua)

	def get_data(path):
		try:
			return GET("{}{}".format(NewUserAgent.domain, path)).json()
		except:
			raise ConnectionError("Failed to connect to {}".format(NewUserAgent.domain))

	def format_ua(x):
		return x["user_agent"]
