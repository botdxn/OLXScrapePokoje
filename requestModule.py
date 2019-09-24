import requests, smtplib, time, concurrent.futures

pageNum = 10
baseURL = 'https://www.olx.pl/nieruchomosci/mieszkania/wynajem/wroclaw/?search%5Bfilter_enum_rooms%5D%5B0%5D=two&page='
listURL = []
for x in range(1, pageNum):
	listURL.append(baseURL + str(x))
#print(listURL)

def requestSites():
	for x in range(1, pageNum):
		requestURL = requests.get(baseURL + str(x))
		requestURL.encoding = 'utf-8'

		while requestURL.status_code != 200:
			print(f"{baseURL + str(x)} status: {requestURL.status_code} Trying again.")
			time.sleep(5)
			requestURL = requests.get(baseURL + str(x))

		print(f"{baseURL + str(x)} status: {requestURL.status_code}")
	return requestURL
