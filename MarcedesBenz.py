from Browser import *
from HTTPBrowser import *
from bs4 import BeautifulSoup
import time
from django.core.files import temp

MARCEDES_BENZ_SITES = {
						"ALABAMA":[
									"http://www.crown.mercedesdealer.com/",
									"http://www.ingram.mercedesdealer.com/",
									"http://www.leigh.mercedesdealer.com/",
									"http://www.dothan.mercedesdealer.com/",
									"http://www.huntsville.mercedesdealer.com/",
									"http://www.mobile.mercedesdealer.com/"
								],
					"ALASKA":[
								"http://www.anchorage.mercedesdealer.com/"
							],
					"ARKANSAS":[
								"http://www.riverside.mercedesdealer.com/",
								"http://www.nwarkansas.mercedesdealer.com/"
							],
					"ARIZONA":[
								"http://www.arrowhead.mercedesdealer.com/",
								"http://www.chandler.mercedesdealer.com/",
								"http://www.tucson.mercedesdealer.com/",
								"http://www.phoenix.mercedesdealer.com/",
								"http://www.schumacher.mercedesdealer.com/"
							],
					"CALIFORNIA":[
									"http://www.alfano.mercedesdealer.com/",
									"http://www.autobahn.mercedesdealer.com/",
									"http://www.berberian.mercedesdealer.com/",
									"http://www.beshoffmotorcars.mercedesdealer.com/",
									"http://www.calstar.mercedesdealer.com/",
									"http://www.courtesy.mercedesdealer.com/",
									"http://www.los-angeles.mercedesdealer.com/",
									"http://www.fletcher.mercedesdealer.com/",
									"http://www.fremont.mercedesdealer.com/",
									"http://www.hoehn.mercedesdealer.com/",
									"http://www.imports.mercedesdealer.com/",
									"http://www.keyes.mercedesdealer.com/",
									"http://www.anaheim.mercedesdealer.com/",
									"http://www.bakersfield.mercedesdealer.com/",
									"http://www.beverlyhills.mercedesdealer.com/",
									"http://www.calabasas.mercedesdealer.com/",
									"http://www.eldoradohills.mercedesdealer.com/",
									"http://www.encino.mercedesdealer.com/",
									"http://www.escondido.mercedesdealer.com/",
									"http://www.fairfieldca.mercedesdealer.com/",
									"http://www.foothillranch.mercedesdealer.com/",
									"http://www.fresno.mercedesdealer.com/",
									"http://www.laguna-niguel.mercedesdealer.com/",
									"http://www.long-beach.mercedesdealer.com/",
									"http://www.monterey.mercedesdealer.com/",
									"http://www.oakland.mercedesdealer.com/",
									"http://www.ontario.mercedesdealer.com/",
									"http://www.oxnard.mercedesdealer.com/",
									"http://www.palm-springs.mercedesdealer.com/",
									"http://www.pleasanton.mercedesdealer.com/",
									"http://www.rocklin.mercedesdealer.com/",
									"http://www.sacramento.mercedesdealer.com/",
									"http://www.san-diego.mercedesdealer.com/",
									"http://www.san-francisco.mercedesdealer.com/",
									"http://www.smothers.mercedesdealer.com/",
									"http://www.southbay.mercedesdealer.com/",
									"http://www.santaclarita.mercedesdealer.com/",
									"http://www.walnutcreek.mercedesdealer.com/",
									"http://www.penske.mercedesdealer.com/",
									"http://www.modesto.mercedesdealer.com/",
									"http://www.rabmotors.mercedesdealer.com/",
									"http://www.rusnak.mercedesdealer.com/",
									"http://www.santabarbara.mercedesdealer.com/",
									"http://www.star.mercedesdealer.com/",
									"http://www.smythe.mercedesdealer.com/",
									"http://www.simonson.mercedesdealer.com/",
									"http://www.walters.mercedesdealer.com/"
								],
					"COLORADO":[
								"http://www.coloradosprings.mercedesdealer.com/",
								"http://www.murray.mercedesdealer.com/",
								"http://www.littleton.mercedesdealer.com/",
								"http://www.loveland.mercedesdealer.com/",
								"http://www.westminster.mercedesdealer.com/"
							],
					"CONNECTICUT":[
									"http://www.carriagehouse.mercedesdealer.com/",
									"http://www.danbury.mercedesdealer.com/",
									"http://www.fairfield.mercedesdealer.com/",
									"http://www.greenwich.mercedesdealer.com/",
									"http://www.northhaven.mercedesdealer.com/",
									"http://www.newcountry.mercedesdealer.com/"
								],
					"DELEWARE":[
								"http://www.burton.mercedesdealer.com/",
								"http://www.wilmington.mercedesdealer.com/"
							],
					"FLORIDA":[
								"http://www.brumos.mercedesdealer.com/",
								"http://www.capital.mercedesdealer.com/",
								"http://www.centennial.mercedesdealer.com/",
								"http://www.crowneuro.mercedesdealer.com/",
								"http://www.fieldsmotorcars.mercedesdealer.com/",
								"http://www.lokey.mercedesdealer.com/",
								"http://www.coconutcreek.mercedesdealer.com/",
								"http://www.ussery.mercedesdealer.com/",
								"http://www.cutlerbay.mercedesdealer.com/",
								"http://www.daytona-beach.mercedesdealer.com/",
								"http://www.delray.mercedesdealer.com/",
								"http://www.fort-lauderdale.mercedesdealer.com/",
								"http://www.fort-myers.mercedesdealer.com/",
								"http://www.fort-pierce.mercedesdealer.com/",
								"http://www.duval.mercedesdealer.com/",
								"http://www.melbourne.mercedesdealer.com/",
								"http://www.miami.mercedesdealer.com/",
								"http://www.naples.mercedesdealer.com/",
								"http://www.northorlando.mercedesdealer.com/",
								"http://www.northpalmbeach.mercedesdealer.com/",
								"http://www.orangepark.mercedesdealer.com/",
								"http://www.orlando.mercedesdealer.com/",
								"http://www.palm-beach.mercedesdealer.com/",
								"http://www.pembroke.mercedesdealer.com/",
								"http://www.pompano.mercedesdealer.com/",
								"http://www.sarasota.mercedesdealer.com/",
								"http://www.southorlando.mercedesdealer.com/",
								"http://www.tampa.mercedesdealer.com/",
								"http://www.quality.mercedesdealer.com/"
							],
					"GEORGIA":[
								"http://www.albany.mercedesdealer.com/",
								"http://www.duluth.mercedesdealer.com/",
								"http://www.critz.mercedesdealer.com/",
								"http://www.athens.mercedesdealer.com/",
								"http://www.augusta.mercedesdealer.com/",
								"http://www.buckhead.mercedesdealer.com/",
								"http://www.columbus.mercedesdealer.com/",
								"http://www.jackson.mercedesdealer.com/",
								"http://www.southatlanta.mercedesdealer.com/",
								"http://www.atlanta.mercedesdealer.com/",
								"http://www.rbmatlantanorth.mercedesdealer.com/"
							],
					"IDAHO":[
								"http://www.boise.mercedesdealer.com/"
							],
					"ILLINOIS":[
								"http://www.edens.mercedesdealer.com/",
								"http://www.peoria.mercedesdealer.com/",
								"http://www.brianbemismercedesbenz.com/",
								"http://www.isringhausen.mercedesdealer.com/",
								"http://www.jpmotors.mercedesdealer.com/",
								"http://www.knauz.mercedesdealer.com/",
								"http://www.loeber.mercedesdealer.com/",
								"http://www.chicago.mercedesdealer.com/",
								"http://www.hoffman.mercedesdealer.com/",
								"http://www.marion.mercedesdealer.com/",
								"http://www.naperville.mercedesdealer.com/",
								"http://www.orlandpark.mercedesdealer.com/",
								"http://www.st-charles.mercedesdealer.com/",
								"http://www.laurel.mercedesdealer.com/",
								"http://www.motorwerks.mercedesdealer.com/",
								"http://www.napletons.mercedesdealer.com/",
								"http://www.suds.mercedesdealer.com/",
								"http://www.sullivan-parkhill.mercedesdealer.com/"
							],
					"INDIANA":[
								"http://www.patrick.mercedesdealer.com/",
								"http://www.gurley.mercedesdealer.com/",
								"http://www.fortwayne.mercedesdealer.com/",
								"http://www.indianapolis.mercedesdealer.com/",
								"http://www.raisor.mercedesdealer.com/",
								"http://www.schererville.mercedesdealer.com/",
								"http://www.wwmotors.mercedesdealer.com/"
							],
					"IOWA":[
							"http://www.iowacity.mercedesdealer.com/",
							"http://www.lujack.mercedesdealer.com/",
							"http://www.desmoines.mercedesdealer.com/"
						],
					"KANSAS":[
								"http://www.aristocrat.mercedesdealer.com/",
								"http://www.scholfield.mercedesdealer.com/"
							],
					"KENTUCKY":[
								"http://www.fannin.mercedesdealer.com/",
								"http://www.james.mercedesdealer.com/",
								"http://www.bowlinggreen.mercedesdealer.com/",
								"http://www.tafel.mercedesdealer.com/"
							],
					"LOUISIANA":[
									"http://www.holmes.mercedesdealer.com/",
									"http://www.alexandriala.mercedesdealer.com/",
									"http://www.batonrouge.mercedesdealer.com/",
									"http://www.neworleans.mercedesdealer.com/",
									"http://www.moss.mercedesdealer.com/"
								],
					"MAINE":[
								"http://www.primemb.mercedesdealer.com/",
								"http://www.quirk.mercedesdealer.com/"
							],
					"MARYLAND":[
								"http://www.germantown.mercedesdealer.com/",
								"http://www.euromotorcars.mercedesdealer.com/",
								"http://www.annapolis.mercedesdealer.com/",
								"http://www.catonsville.mercedesdealer.com/",
								"http://www.hagerstown.mercedesdealer.com/",
								"http://www.huntvalley.mercedesdealer.com/",
								"http://www.salisbury.mercedesdealer.com/",
								"http://www.silverspring.mercedesdealer.com/",
								"http://www.rhmotor.mercedesdealer.com/"
							],
					"MASSACHUSETTS":[
										"http://www.flagship.mercedesdealer.com/",
										"http://www.boston.mercedesdealer.com/",
										"http://www.natick.mercedesdealer.com/",
										"http://www.shrewsbury.mercedesdealer.com/",
										"http://www.westwood.mercedesdealer.com/",
										"http://www.smith.mercedesdealer.com/"
									],
					"MICHIGAN":[
								"http://www.betten.mercedesdealer.com/",
								"http://www.grand.mercedesdealer.com/",
								"http://www.annarbor.mercedesdealer.com/",
								"http://www.bloomfield-hills.mercedesdealer.com/",
								"http://www.novi.mercedesdealer.com/",
								"http://www.rochester.mercedesdealer.com/",
								"http://www.st-clairshores.mercedesdealer.com/",
								"http://www.traversecity.mercedesdealer.com/",
								"http://www.lansingimports.mercedesdealer.com/",
								"http://www.orrin.mercedesdealer.com/"
							],
					"MINNESOTA":[
									"http://www.feldmanns.mercedesdealer.com/",
									"http://www.maplewood.mercedesdealer.com/",
									"http://www.rochestermn.mercedesdealer.com/",
									"http://www.sears.mercedesdealer.com/"
								],
					"MISSISSIPPI":[
									"http://www.higginbotham.mercedesdealer.com/",
									"http://www.southmississippi.mercedesdealer.com/"
								],
					"MISSOURI":[
								"http://www.elite.mercedesdealer.com/",
								"http://www.frankfletcherimports.mercedesdealer.com/",
								"http://www.machens.mercedesdealer.com/",
								"http://www.kansascity.mercedesdealer.com/",
								"http://www.plaza.mercedesdealer.com/",
								"http://www.progresspoint.mercedesdealer.com/",
								"http://www.tristar.mercedesdealer.com/"
							],
					"MONTANA":[
								"http://www.demarois.mercedesdealer.com/",
								"http://www.billings.mercedesdealer.com/"
							],
					"NEBRASKA":[
								"http://www.husker.mercedesdealer.com/",
								"http://www.omaha.mercedesdealer.com/"
							],
					"NEVADA":[
								"http://www.fletcherjones.mercedesdealer.com/",
								"http://www.henderson.mercedesdealer.com/",
								"http://www.reno.mercedesdealer.com/"
							],
					"NEW HAMPSHIRE":[
										"http://www.dreher.mercedesdealer.com/",
										"http://www.holloway.mercedesdealer.com/"
									],
					"NEW JERSEY":[
									"http://www.benzel.mercedesdealer.com/",
									"http://www.contemporarymotor.mercedesdealer.com/",
									"http://www.globe.mercedesdealer.com/",
									"http://www.intercar.mercedesdealer.com/",
									"http://www.atlantic-city.mercedesdealer.com/",
									"http://www.cherry-hill.mercedesdealer.com/",
									"http://www.flemington.mercedesdealer.com/",
									"http://www.freehold.mercedesdealer.com/",
									"http://www.morristown.mercedesdealer.com/",
									"http://www.princeton.mercedesdealer.com/",
									"http://www.bridgewater.mercedesdealer.com/",
									"http://www.prestige.mercedesdealer.com/",
									"http://www.catena.mercedesdealer.com/",
									"http://www.union.mercedesdealer.com/"
								],
					"NEW MEXICO":[
									"http://www.albuquerque.mercedesdealer.com/",
									"http://www.santafe.mercedesdealer.com/"
								],
					"NEW YORK":[
								"http://www.estatemotors.mercedesdealer.com/",
								"http://www.keeler.mercedesdealer.com/",
								"http://www.manhattan.mercedesdealer.com/",
								"http://www.brooklyn.mercedesdealer.com/",
								"http://www.mercedesbenzbflo.mercedesdealer.com/",
								"http://www.huntington.mercedesdealer.com/",
								"http://www.massapequa.mercedesdealer.com/",
								"http://www.nanuet.mercedesdealer.com/",
								"http://www.newrochelle.mercedesdealer.com/",
								"http://www.rochesterny.mercedesdealer.com/",
								"http://www.lakeview.mercedesdealer.com/",
								"http://www.smithtown.mercedesdealer.com/",
								"http://www.southampton.mercedesdealer.com/",
								"http://www.wappingers.mercedesdealer.com/",
								"http://www.white-plains.mercedesdealer.com/",
								"http://www.rallye.mercedesdealer.com/",
								"http://www.romano.mercedesdealer.com/",
								"http://www.silverstar.mercedesdealer.com/"
							],
					"NORTH DAKOTA":[
									"http://www.valleyimports.mercedesdealer.com/"
								],
					"NORTH CAROLINA":[
										"http://www.king.mercedesdealer.com/",
										"http://www.hendrick-charlotte.mercedesdealer.com/",
										"http://www.leith.mercedesdealer.com/",
										"http://www.cary.mercedesdealer.com/",
										"http://www.fayetteville.mercedesdealer.com/",
										"http://www.greensboro.mercedesdealer.com/",
										"http://www.northlake.mercedesdealer.com/",
										"http://www.southcharlotte.mercedesdealer.com/",
										"http://www.salem.mercedesdealer.com/",
										"http://www.skyland.mercedesdealer.com/"
									],
					"OHIO":[
							"http://www.coppus.mercedesdealer.com/",
							"http://www.crowneurocar.mercedesdealer.com/",
							"http://www.martin.mercedesdealer.com/",
							"http://www.kempthorn.mercedesdealer.com/",
							"http://www.mansfield.mercedesdealer.com/",
							"http://www.akron.mercedesdealer.com/",
							"http://www.bedford.mercedesdealer.com/",
							"http://www.centerville.mercedesdealer.com/",
							"http://www.cincinnati.mercedesdealer.com/",
							"http://www.easton.mercedesdealer.com/",
							"http://www.northolmsted.mercedesdealer.com/",
							"http://www.mbwestchester.mercedesdealer.com/",
							"http://www.willoughby.mercedesdealer.com/",
							"http://www.devers.mercedesdealer.com/"
						],
					"OKLAHOMA":[
								"http://www.cooper.mercedesdealer.com/",
								"http://www.oklahoma-city.mercedesdealer.com/"
							],
					"OREGON":[
								"http://www.beaverton.mercedesdealer.com/",
								"http://www.bend.mercedesdealer.com/",
								"http://www.eugene.mercedesdealer.com/",
								"http://www.medford.mercedesdealer.com/",
								"http://www.portland.mercedesdealer.com/",
								"http://www.salemor.mercedesdealer.com/",
								"http://www.wilsonville.mercedesdealer.com/"
							],
					"PENNSYLVANIA":[
									"http://www.bobbyrahal.mercedesdealer.com/",
									"http://www.smail.mercedesdealer.com/",
									"http://www.cml.mercedesdealer.com/",
									"http://www.devon.mercedesdealer.com/",
									"http://www.sisson.mercedesdealer.com/",
									"http://www.keenan.mercedesdealer.com/",
									"http://www.knopf.mercedesdealer.com/",
									"http://www.fortwashington.mercedesdealer.com/",
									"http://www.lancaster.mercedesdealer.com/",
									"http://www.pittsburgh.mercedesdealer.com/",
									"http://www.statecollege.mercedesdealer.com/",
									"http://www.westchester.mercedesdealer.com/",
									"http://www.motorworld.mercedesdealer.com/",
									"http://www.sunmotor.mercedesdealer.com/",
									"http://www.masano.mercedesdealer.com/"
								],
					"RHODE ISLAND":[
									"http://www.warwick.mercedesdealer.com/",
									"http://www.viti.mercedesdealer.com/"
								],
					"SOUTH CAROLINA":[
										"http://www.baker.mercedesdealer.com/",
										"http://www.carlton.mercedesdealer.com/",
										"http://www.dyer.mercedesdealer.com/",
										"http://www.florence.mercedesdealer.com/",
										"http://www.hiltonhead.mercedesdealer.com/",
										"http://www.myrtlebeach.mercedesdealer.com/"
									],
					"SOUTH DAKOTA":[
									"http://www.siouxfalls.mercedesdealer.com/"
								],
					"TENNESSEE":[
									"http://www.longco.mercedesdealer.com/",
									"http://www.knoxville.mercedesdealer.com/",
									"http://www.memphis.mercedesdealer.com/",
									"http://www.nashville.mercedesdealer.com/",
									"http://www.rhimports.mercedesdealer.com/"
								],
					"TEXAS":[
								"http://www.midland.mercedesdealer.com/",
								"http://www.lubbock.mercedesdealer.com/",
								"http://www.alexrodriguez.mercedesdealer.com/",
								"http://www.alexrodriguez.mercedesdealer.com/",
								"http://www.cardenas.mercedesdealer.com/",
								"http://www.hicks.mercedesdealer.com/",
								"http://www.austin.mercedesdealer.com/",
								"http://www.boerne.mercedesdealer.com/",
								"http://www.el-paso.mercedesdealer.com/",
								"http://www.georgetown.mercedesdealer.com/",
								"http://www.houston-greenway.mercedesdealer.com/",
								"http://www.houston-north.mercedesdealer.com/",
								"http://www.plano.mercedesdealer.com/",
								"http://www.san-antonio.mercedesdealer.com/",
								"http://www.sanjuantx.mercedesdealer.com/",
								"http://www.sugarland.mercedesdealer.com/",
								"http://www.texarkana.mercedesdealer.com/",
								"http://www.tyler.mercedesdealer.com/",
								"http://www.samuels.mercedesdealer.com/",
								"http://www.autoplex.mercedesdealer.com/",
								"http://www.park.mercedesdealer.com/",
								"http://www.fortworth.mercedesdealer.com/",
								"http://www.parkplace-grapevine.mercedesdealer.com/",
								"http://www.wichitafalls.mercedesdealer.com/",
								"http://www.powell.mercedesdealer.com/",
								"http://www.starmotorcars.mercedesdealer.com/"
							],
					"UTAH":[
							"http://www.lindon.mercedesdealer.com/",
							"http://www.garff.mercedesdealer.com/"
						],
					"VIRGINIA":[
								"http://www.browns.mercedesdealer.com/",
								"http://www.roanoke.mercedesdealer.com/",
								"http://www.mcgeorge.mercedesdealer.com/",
								"http://www.alexandria.mercedesdealer.com/",
								"http://www.arlington.mercedesdealer.com/",
								"http://www.chantilly.mercedesdealer.com/",
								"http://www.fredericksburg.mercedesdealer.com/",
								"http://www.richmond.mercedesdealer.com/",
								"http://www.tysonscorner.mercedesdealer.com/",
								"http://www.virginiabeach.mercedesdealer.com/",
								"http://www.tysinger.mercedesdealer.com/"
							],
					"VERMONT":[
								"http://www.automaster.mercedesdealer.com/"
							],
					"WASHINGTON":[
									"http://www.bellevue.mercedesdealer.com/",
									"http://www.lynnwood.mercedesdealer.com/",
									"http://www.seattle.mercedesdealer.com/",
									"http://www.spokane.mercedesdealer.com/",
									"http://www.tacoma.mercedesdealer.com/",
									"http://www.tri-cities.mercedesdealer.com/",
									"http://www.hahn.mercedesdealer.com/",
									"http://www.wilson.mercedesdealer.com/"
								],
					"WISCONSIN":[
									"http://www.concours.mercedesdealer.com/",
									"http://www.enterprise.mercedesdealer.com/",
									"http://www.internationalautos.mercedesdealer.com/",
									"http://www.elmbrook.mercedesdealer.com/",
									"http://www.zeuropean.mercedesdealer.com/"
								],
					"WEST VIRGINIA":[
										"http://www.astorg.mercedesdealer.com/",
										"http://www.university.mercedesdealer.com/",
										"http://www.smithcompany.mercedesdealer.com/"
									]
					}
					
ALL_STATES = [
                "ALABAMA","ALASKA","ARIZONA","ARKANSAS","CALIFORNIA","COLORADO","CONNECTICUT","DELEWARE","FLORIDA","GEORGIA","IDAHO","ILLINOIS","INDIANA","IOWA",
                "KANSAS","KENTUCKY","LOUISIANA","MAINE","MARYLAND","MASSACHUSETTS","MICHIGAN","MINNESOTA","MINNEAPOLIS","MISSISSIPPI","MISSOURI","MONTANA","NEBRASKA",
                "NEVADA","NEW HAMPSHIRE","NEW JERSEY","NEW MEXICO","NEW YORK","NORTH DAKOTA","NORTH CAROLINA","OHIO","OKLAHOMA","OREGON","PENNSYLVANIA",
                "RHODE ISLAND","SOUTH CAROLINA","SOUTH DAKOTA","TENNESSEE","TEXAS","UTAH","VIRGINIA","VERMONT","WASHINGTON","WISCONSIN","WEST VIRGINIA"
              ]

NEW_CAR_SEARCH_DIRECTORY = "new"



class MarcedesParser:
	def __init__(self):
		pass
	def ParseAllCarsLinks(self,baseUrl,page):
		carLinks = []
		try:
			soup = BeautifulSoup(page)
			allDivRows = soup.findAll("div",{"class":"list_vehicle"})
			for eachDiv in allDivRows:
				carLinkElement = eachDiv.find("div",{"class":"list_specification"})
				if carLinkElement is not None:
					carLink = carLinkElement["onclick"]
					carLink = carLink.replace("window.location=","")
					carLink = carLink.replace("\'","")
					carLink = carLink.replace('\"','')
					carLink = carLink.strip()
					carLinks.append(baseUrl+carLink)
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
			make = "MERCEDES-BENZ"
			yearMakeModel["year"] = year
			yearMakeModel["make"] = make
		except Exception,exp:
			pass
		return yearMakeModel
	
	def ParseCarDetails(self,siteLink,state,page):
		details = {"link":siteLink,"state":state}
		try:
			soup = BeautifulSoup(page)
			"""Find phone number."""
			phoneNumberElement = soup.find("span",{"class":"phone"})
			if phoneNumberElement is not None:
				phoneNumber = phoneNumberElement.text.strip()
				details["phone"] = phoneNumber
			vehicleDetailSpecificationElement = soup.find("div",{"id":"details_vehicle_specification"})
			if vehicleDetailSpecificationElement is not None:
				"""Find the make model of the vehicle"""
				yearModelElement = vehicleDetailSpecificationElement.find("h1")
				if yearModelElement is not None:
					yearModel = yearModelElement.text.strip()
					makeModelYear = self.ParseYearMakeModel(yearModel)
					details = dict(details.items()+makeModelYear.items())
				vehiclePriceElement = vehicleDetailSpecificationElement.find("div",{"class":"vehicle_price"})
				if vehiclePriceElement is not None:
					vehiclePrice = vehiclePriceElement.text.strip()
					if vehiclePrice != "":
						details["price"] = vehiclePrice
				vehicleSpecificationTableElement = vehicleDetailSpecificationElement.find("table",{"id":"specifiation_table"})
				if vehicleSpecificationTableElement is not None:
					specificationListRows = vehicleSpecificationTableElement.findAll("tr")
					for eachSpecRow in specificationListRows:
						specTitleElement = eachSpecRow.find("th")
						specDataElement = eachSpecRow.find("td")
						if specTitleElement is not None and specDataElement is not None:
							specTitle = specTitleElement.text.strip()
							specData = specDataElement.text.strip()
							if "Model Year" in specTitle:
								details["model"] = specData
							elif "Exterior" in specTitle:
								details["exterior"] = specData
							elif "Trim" in specTitle:
								details["trim"] = specData
							elif "Mileage" in specTitle:
								details["mileage"] = specData
							elif "VIN" in specTitle:
								details["vin"] = specData
							elif "Location" in specTitle:
								details["location"] = specData
		except Exception,exp:
			pass
		return details
	
	def ParseTotalPageCount(self,page):
		pageCountTuple = None
		try:
			soup = BeautifulSoup(page)
			pageCountElement = soup.find("div",{"class":"pages"})
			if pageCountElement is not None:
				pageCountText = pageCountElement.text.strip()
				ofIndex = pageCountText.find('of')
				if ofIndex != -1:
					currentPageCountPart = pageCountText[:ofIndex]
					totalPageCountPart = pageCountText[ofIndex:]
					currentPageCountPart = currentPageCountPart.replace('Page','').strip()
					totalPageCountPart = totalPageCountPart.replace('of','').strip()
					pageCountTuple = (int(currentPageCountPart),int(totalPageCountPart))
		except Exception,exp:
			pass
		return pageCountTuple
	
from Uploader import *
	
class MarcedesBenz:
	def __init__(self):
		self.parser = MarcedesParser()
		self.httpBrowser = HTTPBrowser()
		self.uploader = Uploader()
	
	def GetNextPageButton(self):
		nextPageButtonElement = self.browser.FindElementByClassName(".pagination.next")
		return nextPageButtonElement
	
	def WaitUntillResultsAvailable(self):
		startTime = time.time()
		searchResultContainerElement = self.browser.FindElementById("Searchresult")
		while searchResultContainerElement is not None:
			time.sleep(2)
			searchResultContainerElement = self.browser.FindElementById("Searchresult")
			
			
		
		endTime = time.time()
		timeDiff = int(endTime - startTime)
		print timeDiff
		
		
	
	def StartCrawling(self):
		self.browser = Browser()
		allCarDetailsList = []
		for eachState in ALL_STATES:
			sitesForASingleState = MARCEDES_BENZ_SITES.get(eachState)
			if sitesForASingleState is not None:
				for eachSite in sitesForASingleState:
					fullLink = eachSite+NEW_CAR_SEARCH_DIRECTORY
					self.browser.OpenURL(fullLink)
					time.sleep(2)
					pageSource = self.browser.GetPage()
					pageCount = self.parser.ParseTotalPageCount(pageSource)
					startTime = time.time()
					while pageCount is None:
						time.sleep(2)
						pageSource = self.browser.GetPage()
						pageCount = self.parser.ParseTotalPageCount(pageSource)
						if pageCount is None:
							endTime = time.time()
							timeDiff = int(endTime-startTime)
							if timeDiff > 5:
								break
							else:
								continue
						else:
							break
					carsLinksList = []
					pageSource = self.browser.GetPage()
					allCarsLinks = self.parser.ParseAllCarsLinks(eachSite[:-1],pageSource)
					carsLinksList.extend(allCarsLinks)
					pageCount = self.parser.ParseTotalPageCount(pageSource)
					if len(allCarsLinks) == 24:
						currentPageCount,totalPageCount = 0,0
						if pageCount is not None:
							currentPageCount,totalPageCount = tuple(pageCount)
						while currentPageCount < totalPageCount:
							nextPageButton = self.GetNextPageButton()
							if nextPageButton is not None:
								self.browser.ClickElement(nextPageButton)
								time.sleep(1)
								pageSource = self.browser.GetPage()
								allCarsLinks = self.parser.ParseAllCarsLinks(eachSite[:-1],pageSource)
								carsLinksList.extend(allCarsLinks)
								pageCount = self.parser.ParseTotalPageCount(pageSource)
								if pageCount is not None:
									currentPageCount,totalPageCount = tuple(pageCount)
							else:
								break
					#Now we have found all cars links for a single domain. Now need to get car details.
					carDetailsList = []
					for eachCarLink in carsLinksList:
						carDetailsPageSource = self.httpBrowser.GetPage(eachCarLink)
						carDetails = self.parser.ParseCarDetails(eachCarLink, eachState, carDetailsPageSource)
						carDetailsList.append(carDetails)
					print "Uploading Started..."
					print self.uploader.Upload(carDetailsList)
					print "Uploading Done!"
#					allCarDetailsList.extend(carDetailsList)
		self.browser.Close()
		return allCarDetailsList
				
				
	


