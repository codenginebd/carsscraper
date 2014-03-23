from selenium import webdriver
import time
class Browser:
	def __init__(self):
		try:
#			self.browser = webdriver.Firefox()
			self.browser = webdriver.Chrome()
		except Exception,exp:
			print "Webdriver open failed."
	def OpenURL(self,url):
		try:
			self.browser.get(url)
		except Exception,exp:
			pass
	def GetPage(self):
		try:
			self.page = self.browser.page_source
			encodedStr = self.page.encode("ascii","xmlcharrefreplace") 
			return encodedStr
		except Exception,exp:
			return None
	def FindMoreLinkedElements(self):
		try:
			elements = self.browser.find_elements_by_class_name("mediaRowRevealer")
			return elements
		except Exception,exp:
			return None
	def ClickElement(self,element):
		try:
			if element is not None:
				try:
					element.click()
					time.sleep(10)
					return True
				except Exception,e:
					print "Click Exception: "+str(e)
					return False
		except Exception,exp:
			return False
	def ClickOnMoreInfoElements(self):
		try:
			elements = self.FindMoreLinkedElements()
			for anElement in elements:
				if anElement is not None:
					try:
						anElement.click()
					except Exception,e:
						pass
			time.sleep(6)
		except Exception,exp:
			pass
	def FindLikesYearLinkElement(self):
		elements = self.browser.find_elements_by_class_name("prl")
		return elements
	def FindElementByName(self,elementName):
		try:
			element = self.browser.find_element_by_name(elementName)
			return element
		except Exception,exp:
			return None
	def FindElementById(self,elementId):
		try:
			element = self.browser.find_element_by_id(elementId)
			return element
		except Exception,exp:
			return None
		
	def FindElementByClassName(self,elementClassName):
		try:
			element = self.browser.find_element_by_css_selector(elementClassName)
			return element
		except Exception,exp:
			return None
	
	def ExecuteScriptAndWait(self,code):
		try:
			self.browser.execute_script(code)
			time.sleep(10)
		except Exception,exp:
			pass
	def GetPageURL(self):
		try:
			return self.browser.current_url
		except Exception,exp:
			return None
	def Close(self):
		try:
			self.browser.close()
		except Exception,exp:
			print "Browser closing failed."