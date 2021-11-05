from pyfiglet import Figlet
custom_fig = Figlet(font='banner')
print(custom_fig.renderText('PhoneFy'))

import argparse
import phonenumbers
from phonenumbers import carrier, geocoder

class Details:
	def __init__(self,phonenumber):
		
		self.parse_phonenumber = phonenumbers.parse("+"+phonenumber)
		
	def main(self,phonenumber):
		print(self.parse_phonenumber)
		print(f"Compañia Movil: {carrier.name_for_number(self.parse_phonenumber,'es')}")
		print(f"Localizacion: {geocoder.description_for_number(self.parse_phonenumber,  'es')}")
		
		
		if args.output:
			with open(f"{phonenumber}.txt", "w") as file:
				file.write(f"{self.parse_phonenumber}\n{carrier.name_for_number(self.parse_phonenumber,'es')}\n{geocoder.description_for_number(self.parse_phonenumber,  'es')}")
		
if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Obtener informacion del numero")
	parser.add_argument("phonenumber", help="Objetivo")
	parser.add_argument("-O","--output-resultados",help="guardar resultados",dest="output",action="store_true")
	args = parser.parse_args()
	phonenumber = args.phonenumber
	output = args.output
	try:
		Details(phonenumber).main(phonenumber)
		
	except Exception as e:
		print(e)





from pyfiglet import Figlet
custom_fig = Figlet(font='big')
print(custom_fig.renderText('@giines.zl'))

print('By: B4rc0d37')