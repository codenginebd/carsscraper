import urllib2
import json

class Uploader:
	def __init__(self):
		pass
	def Upload(self,data):
		temp = data
		while len(temp) >= 50:
			toBeUploaded = temp[:50]
			temp = temp[50:]
			data = {"data":toBeUploaded}
			req = urllib2.Request("http://cardealerzone.appspot.com/service/upload/", data=json.dumps(data),headers={"Content-Type": "application/json"})
			urllib2.urlopen(req).read()
		if len(temp) > 0:
			data = {"data":temp}
			req = urllib2.Request("http://cardealerzone.appspot.com/service/upload/", data=json.dumps(data),headers={"Content-Type": "application/json"})
			urllib2.urlopen(req).read()