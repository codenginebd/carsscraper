from HTTPBrowser import *
from bs4 import BeautifulSoup

PORSCHE_SITES = {
					"ALABAMA":[
						"http://jack-ingram.porschedealer.com/",
						"http://dean-mccrary.porschedealer.com/",
						"http://huntsville.porschedealer.com/",
						"http://tom-williams.porschedealer.com/"
					],
				"ALASKA":[
					"http://anchorage.porschedealer.com/"
				],
				"ARIZONA":[
							"http://tucson.porschedealer.com/",
							"http://scottsdale.porschedealer.com/"
						],
				"CALIFORNIA":[
								"http://beverly-hills.porschedealer.com/",
								"http://carlsen.porschedealer.com/",
								"http://circle.porschedealer.com/",
								"http://desert-european.porschedealer.com/",
								"http://hoehn.porschedealer.com/",
								"http://mckenna.porschedealer.com/",
								"http://michael-stead.porschedealer.com/",
								"http://niello.porschedealer.com/",
								"http://pacific.porschedealer.com/",
								"http://bakersfield.porschedealer.com/",
								"http://downtown-la.porschedealer.com/",
								"http://fremont.porschedealer.com/",
								"http://fresno.porschedealer.com/",
								"http://livermore.porschedealer.com/",
								"http://monterey.porschedealer.com/",
								"http://san-diego.porschedealer.com/",
								"http://stevens-creek.porschedealer.com/",
								"http://santabarbara.porschedealer.com/",
								"http://newport-beach.porschedealer.com/",
								"http://rector.porschedealer.com/",
								"http://rusnak-pasadena.porschedealer.com/",
								"http://rusnak-westlake.porschedealer.com/",
								"http://sonnen.porschedealer.com/",
								"http://autogallery.porschedealer.com/",
								"http://walters.porschedealer.com/"
							],
				"COLORADO":[
							"http://ed-carroll.porschedealer.com/",
							"http://colorado-springs.porschedealer.com/",
							"http://prestige-imports.porschedealer.com/",
							"http://stevinson.porschedealer.com/"
						],
				"CONNECTICUT":[
								"http://hoffman.porschedealer.com/",
								"http://new-country.porschedealer.com/",
								"http://fairfield.porschedealer.com/",
								"http://wallingford.porschedealer.com/"
							],
				"DELEWARE":[
							"http://delaware.porschedealer.com/"
						],
				"FLORIDA":[
							"http://bert-smith.porschedealer.com/",
							"http://brumos.porschedealer.com/",
							"http://capital.porschedealer.com/",
							"http://champion.porschedealer.com/",
							"http://destin.porschedealer.com/",
							"http://fort-myers.porschedealer.com/",
							"http://melbourne.porschedealer.com/",
							"http://naples.porschedealer.com/",
							"http://ocala.porschedealer.com/",
							"http://orlando.porschedealer.com/",
							"http://reeves.porschedealer.com/",
							"http://suncoast.porschedealer.com/",
							"http://thecollection.porschedealer.com/"
						],
				"GEORGIA":[
							"http://hennessy.porschedealer.com/",
							"http://jim-ellis.porschedealer.com/"
						],
				"IDAHO":[
							"http://boise.porschedealer.com/"
						],
				"ILLINOIS":[
							"http://isringhausen.porschedealer.com/",
							"http://joe-rizza.porschedealer.com/",
							"http://loeber.porschedealer.com/",
							"http://motor-werks.porschedealer.com/",
							"http://ed-napleton.porschedealer.com/",
							"http://napletons.porschedealer.com/",
							"http://peoria.porschedealer.com/",
							"http://porsche-exchange.porschedealer.com/"
						],
				"INDIANA":[
							"http://d-patrick.porschedealer.com/",
							"http://odaniel.porschedealer.com/",
							"http://tom-wood.porschedealer.com/"
						],
				"IOWA":[
						"http://quadcities.porschedealer.com/"
					],
				"KANSAS":[
							"http://aristocrat.porschedealer.com/",
							"http://wichita.porschedealer.com/"
						],
				"KENTUCKY":[
							"http://blue-grass.porschedealer.com/"
						],
				"LOUISIANA":[
								"http://harris.porschedealer.com/",
								"http://moffitt.porschedealer.com/",
								"http://neworleans.porschedealer.com/"
							],
				"MAINE":[
							"http://morong-falmouth.porschedealer.com/"
						],
				"MARYLAND":[
							"http://len-stoler.porschedealer.com/",
							"http://annapolis.porschedealer.com/",
							"http://rockville.porschedealer.com/",
							"http://silverspring.porschedealer.com/",
							"http://towson.porschedealer.com/"		
						],
				"MASSACHUSETTS":[
									"http://fathers-sons.porschedealer.com/",
									"http://chambers.porschedealer.com/",
									"http://ira.porschedealer.com/",
									"http://burlington.porschedealer.com/",
									"http://norwell.porschedealer.com/",
									"http://westwood.porschedealer.com/"
								],
				"MICHIGAN":[
							"http://deltaimports.porschedealer.com/",
							"http://fred-lavery.porschedealer.com/",
							"http://ann-arbor.porschedealer.com/",
							"http://farmington-hills.porschedealer.com/",
							"http://okemos.porschedealer.com/",
							"http://porscheofthemotorcity.porschedealer.com/"
						],
				"MINNESOTA":[
								"http://minneapolis.porschedealer.com/",
								"http://stpaul.porschedealer.com/"
							],
				"MISSISSIPPI":[
								"http://jackson.porschedealer.com/"
							],
				"MISSOURI":[
							"http://parktown.porschedealer.com/",
							"http://plaza-motor.porschedealer.com/",
							"http://springfield.porschedealer.com/"
						],
				"NEBRASKA":[
							"http://omaha.porschedealer.com/"
						],
				"NEVADA":[
							"http://gaudin.porschedealer.com/",
							"http://reno.porschedealer.com/"
						],
				"NEW HAMPSHIRE":[
									"http://nashua.porschedealer.com/",
									"http://stratham.porschedealer.com/"
								],
				"NEW JERSEY":[
								"http://cherry-hill.porschedealer.com/",
								"http://flemington.porschedealer.com/",
								"http://jack-daniels.porschedealer.com/",
								"http://paul-miller.porschedealer.com/",
								"http://atlanticcity.porschedealer.com/",
								"http://princeton.porschedealer.com/",
								"http://ray-catena.porschedealer.com/",
								"http://schneider-nelson.porschedealer.com/"
							],
				"NEW MEXICO":[
								"http://albuquerque.porschedealer.com/"
							],
				"NEW YORK":[
							"http://legend.porschedealer.com/",
							"http://manhattan.porschedealer.com/",
							"http://buffalo.porschedealer.com/",
							"http://clifton-park.porschedealer.com/",
							"http://huntington.porschedealer.com/",
							"http://larchmont.porschedealer.com/",
							"http://rochester.porschedealer.com/",
							"http://roslyn.porschedealer.com/",
							"http://southampton.porschedealer.com/",
							"http://syracuse.porschedealer.com/",
							"http://southshore.porschedealer.com/"
						],
				"NORTH CAROLINA":[
									"http://asheville.porschedealer.com/",
									"http://hendrick.porschedealer.com/",
									"http://leith.porschedealer.com/",
									"http://performance.porschedealer.com/",
									"http://fayetteville.porschedealer.com/",
									"http://greensboro.porschedealer.com/",
									"http://hickory.porschedealer.com/"
								],
				"OHIO":[
						"http://byers.porschedealer.com/",
						"http://midwestern.porschedealer.com/",
						"http://beachwood.porschedealer.com/",
						"http://kings-automall.porschedealer.com/",
						"http://north-olmsted.porschedealer.com/",
						"http://porschevillage.porschedealer.com/",
						"http://white-allen.porschedealer.com/"
					],
				"OKLAHOMA":[
							"http://bob-moore.porschedealer.com/",
							"http://jackie-cooper.porschedealer.com/"
						],
				"OREGON":[
							"http://carrera.porschedealer.com/",
							"http://sunset.porschedealer.com/"
						],
				"PENNSYLVANIA":[
								"http://auto-palace.porschedealer.com/",
								"http://autohaus-lancaster.porschedealer.com/",
								"http://knopf.porschedealer.com/",
								"http://buckscounty.porschedealer.com/",
								"http://conshohocken.porschedealer.com/",
								"http://main-line.porschedealer.com/",
								"http://sewickley.porschedealer.com/",
								"http://sun-motor.porschedealer.com/",
								"http://wyoming-valley.porschedealer.com/"
							],
				"RHODE ISLAND":[
								"http://warwick.porschedealer.com/"
							],
				"SOUTH CAROLINA":[
									"http://baker.porschedealer.com/",
									"http://mcdaniels.porschedealer.com/",
									"http://greenville.porschedealer.com/",
									"http://hilton-head.porschedealer.com/"
								],
				"TENNESSEE":[
								"http://gossett.porschedealer.com/",
								"http://harpers.porschedealer.com/",
								"http://chattanooga.porschedealer.com/",
								"http://nashville.porschedealer.com/",
								"http://rick-hill.porschedealer.com/"
							],
				"TEXAS":[
							"http://autobahn.porschedealer.com/",
							"http://momentum.porschedealer.com/",
							"http://park-place.porschedealer.com/",
							"http://north-houston.porschedealer.com/",
							"http://plano.porschedealer.com/",
							"http://san-antonio.porschedealer.com/",
							"http://houston.porschedealer.com/",
							"http://roger-beasley.porschedealer.com/"
						],
				"UTAH":[
						"http://ken-garff.porschedealer.com/",
						"http://strong.porschedealer.com/"
					],
				"VIRGINIA":[
							"http://checkered-flag.porschedealer.com/",
							"http://euroclassics.porschedealer.com/",
							"http://arlington.porschedealer.com/",
							"http://charlottesville.porschedealer.com/",
							"http://tysons.porschedealer.com/"
						],
				"WASHINGTON":[
								"http://barrier.porschedealer.com/",
								"http://spokane.porschedealer.com/",
								"http://tacoma.porschedealer.com/",
								"http://roger-jobs.porschedealer.com/"
							],
				"WISCONSIN":[
								"http://concours.porschedealer.com/",
								"http://international-autos.porschedealer.com/",
								"http://madison.porschedealer.com/",
								"http://foxvalley.porschedealer.com/"
							]
				}

ALL_STATES = [
                "ALABAMA","ALASKA","ARIZONA","ARKANSAS","CALIFORNIA","COLORADO","CONNECTICUT","DELEWARE","FLORIDA","GEORGIA","IDAHO","ILLINOIS","INDIANA","IOWA",
                "KANSAS","KENTUCKY","LOUISIANA","MAINE","MARYLAND","MASSACHUSETTS","MICHIGAN","MINNESOTA","MINNEAPOLIS","MISSISSIPPI","MISSOURI","MONTANA","NEBRASKA",
                "NEVADA","NEW HAMPSHIRE","NEW JERSEY","NEW MEXICO","NEW YORK","NORTH DAKOTA","NORTH CAROLINA","OHIO","OKLAHOMA","OREGON","PENNSYLVANIA",
                "RHODE ISLAND","SOUTH CAROLINA","SOUTH DAKOTA","TENNESSEE","TEXAS","UTAH","VIRGINIA","VERMONT","WASHINGTON","WISCONSIN","WEST VIRGINIA"
              ]

SEARCH_LINK = "new/Porsche/Cayenne/search.php"


class PorscheScraper:
	def __init__(self):
		pass
	def ScrapeAllCarsLinks(self,baseLink,page):
		carLinks = []
		try:
			soup = BeautifulSoup(page)
			searchTable = soup.find("table",{"id":"searchTable"})
			if searchTable is not None:
				tbody = searchTable.find("tbody")
				if tbody is not None:
					allCarsRowTR = tbody.findAll("tr")
					for eachTR in allCarsRowTR:
						link = eachTR.find("a")["href"]
						carLinks.append(baseLink+link)
		except Exception,exp:
			pass
		return carLinks
	
	def ParseYearMakeModel(self,yearMakeModelText):
		yearMakeModel = {"title":yearMakeModelText}
		try:
			year = ""
			i = 0
			while yearMakeModelText[i] >= "0" and yearMakeModelText[i] <= "9":
				year += yearMakeModelText[i]
				i += 1
			makeModel = yearMakeModelText[len(year):].strip()
			make = "Porsche"
			model = makeModel.replace("Porsche","").strip()
			yearMakeModel["year"] = year
			yearMakeModel["make"] = make
			yearMakeModel["model"] = model
		except Exception,exp:
			pass
		return yearMakeModel
	
	def ScrapeCarDetails(self,siteLink,state,page):
		carDetails = {"link":siteLink,"state":state}
		try:
			soup = BeautifulSoup(page)
			yearModelElement = soup.find("h3",{"class":"firstH3"})
			if yearModelElement is not None:
				yearModel = yearModelElement.text.strip()
				yearMakeModel = self.ParseYearMakeModel(yearModel)
				carDetails = dict(carDetails.items()+yearMakeModel.items())
			featuresRowTR = soup.findAll("tr",{"class":"importantFeature"})
			for eachTR in featuresRowTR:
				featureNameElement = eachTR.find("th")
				featureValueElement = eachTR.find("td")
				if featureNameElement is not None and featureValueElement is not None:
					featureName = featureNameElement.text.strip()
					featureValue = featureValueElement.text.strip()
					if featureName is not None and featureValue is not None and featureName != "" and featureValue != "":
						featureName = featureName.lower()
						if featureName == "price":
							carDetails["price"] = featureValue
						elif featureName == "vin":
							carDetails["vin"] = featureValue
						elif featureName == "mileage":
							carDetails["mileage"] = featureValue
						elif featureName == "exterior":
							carDetails["exterior"] = featureValue
						elif featureName == "interior":
							carDetails["interior"] = featureValue
		except Exception,exp:
			return None
		return carDetails
		
from Uploader import *

class Porsche:
	def __init__(self):
		self.browser = HTTPBrowser()
		self.scraper = PorscheScraper()
		self.uploader = Uploader()
		
	def StartCrawling(self):
		try:
			for eachState in ALL_STATES:
				results = []
				sitesForASingleState = PORSCHE_SITES.get(eachState)
				if sitesForASingleState is not None:
					for eachSite in sitesForASingleState:
						print "Site: "+eachSite
						cayenneCarLink = eachSite+SEARCH_LINK
						print "Complete: "+cayenneCarLink
						pageSource = self.browser.GetPage(cayenneCarLink)
						carsLink = self.scraper.ScrapeAllCarsLinks(eachSite[:-1], pageSource)
						print "Length: "+str(len(carsLink))
						for eachCarLink in carsLink:
							page = self.browser.GetPage(eachCarLink)
							carDetails = self.scraper.ScrapeCarDetails(eachCarLink,eachState,page)
							results.append(carDetails)
				print "Uploading Started..."
				print self.uploader.Upload(results)
				print "Uploading Done!"
		except Exception,exp:
			pass