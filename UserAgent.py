from requests import get as GET, exceptions

class UserAgent():
	domain = "http://useragent.ddns.net"

	def RandomAgent():
		ua = UserAgent.__get_data("/")
		return UserAgent.__format_ua(ua)

	def FirefoxAgent():
		ua = UserAgent.__get_data("/firefox")
		return UserAgent.__format_ua(ua)

	def ChromeAgent():
		ua = UserAgent.__get_data("/chrome")
		return UserAgent.__format_ua(ua)

	def OperaAgent():
		ua = UserAgent.__get_data("/opera")
		return UserAgent.__format_ua(ua)

	def SafariAgent():
		ua = UserAgent.__get_data("/safari")
		return UserAgent.__format_ua(ua)

	def ChromiumAgent():
		ua = UserAgent.__get_data("/chromium")
		return UserAgent.__format_ua(ua)

	def IEAgent():
		ua = UserAgent.__get_data("/ie")
		return UserAgent.__format_ua(ua)

	def __get_data(path):
		try:
			return GET("{}{}".format(UserAgent.domain, path)).json()
		except exceptions.ConnectionError:
			raise ConnectionError("Failed to connect to {}".format(UserAgent.domain))

	def __format_ua(x):
		return x["user_agent"]
