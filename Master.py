from MarcedesBenz import *
from Porsche import *
from LandRover import *

import threading


def main():
	marcedes = MarcedesBenz()
	porsche = Porsche()
	landRover = LandRover()
	
	marcedes.StartCrawling()
	porsche.StartCrawling()
	landRover.StartCrawling()
	
if __name__ == "__main__":
	main()