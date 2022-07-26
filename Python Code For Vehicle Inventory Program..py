#------------------------------------------------------------------------
# Program Name: Vehicle Inventory Program
# Author: Oyenike Oyeneye
# Date: 07/26/2022
#------------------------------------------------------------------------
# Pseudocode: 
# 1. Initialize private members
# 2. Create data structure to hold vehicle catalog
# 3. Create public member function to access private members
#         a. function to add
#         b. function to remove vehicle
#         c. function update vehicle
#         d. function to list vehicle
#         e. Export Catalog to text file
#
# 4. Driver to run vehicle collection and to take user input
#------------------------------------------------------------------------
# Program Inputs: Make, Model, Color, year, and mileage of vehicle to be added and adjustments to be made to vehicle collection
# Program Outputs: Vehicle information that has been entered by the user. 
#                  Output seleted options by the user such as add, remove, update, list and export vehicle information to text file.
#------------------------------------------------------------------------

class Automobile:
	__make = ""
	__model = ""
	__color = ""
	__year = ""
	__mileage = ""
	vehicle_list = []

	def __init__(self, make, model, color, year, mileage):
		self.__make = make
		self.__model = model
		self.__color = color
		self.__year = year
		self.__mileage = mileage
		self.vehicle_list.append([make, model, color, year, mileage])
		
	def add_vehicle():
		make = input("Enter vehicle make: ")
		model = input("Enter vehicle model: ")
		color = input("Enter vehicle color: ")
		year = input("Enter vehicle year: ")
		mileage = input("Enter vehicle mileage: ")
		Automobile(make, model, color, year, mileage)
	    #print(Automobile.vehicle_list)
	
	    
	def remove_vehicle(index):
		Automobile.vehicle_list.remove(Automobile.vehicle_list[index])
		print("Removed successfully")
		print("New Catalog is: ")
		Automobile.list_vehicles()
	    
	def update_vehicle():
		print("Select the one you would like to update: ")
		Automobile.list_vehicles()
		index = int(input())
		option = input("Would you like to update vehicle Make? y/n: ")
		if(option.capitalize() == 'Y'):
			make = input("To update make, enter new make: ")
			Automobile.vehicle_list[index-1][0] = make
		option = input("Would you like to update vehicle Model? y/n: ")
		if(option.capitalize() == 'Y'):
			model = input("To update model, enter new model: ")
			Automobile.vehicle_list[index-1][1] = model
		option = input("Would you like to update vehicle Color? y/n: ")
		if(option.capitalize() == 'Y'):
			color = input("To update color, enter new color: ")
			Automobile.vehicle_list[index-1][2] = color
		option = input("Would you like to update vehicle Year? y/n: ")
		if(option.capitalize() == 'Y'):
			year = input("To update year, enter new year: ")
			Automobile.vehicle_list[index-1][3] = year
		option = input("Would you like to update vehicle Mileage? y/n: ")
		if(option.capitalize() == 'Y'):
			mile = input("To update mileage, enter new mileage: ")
			Automobile.vehicle_list[index-1][4] = mile
	    
	def list_vehicles():
		print("{:10} {:10} {:10} {:10} {:10} {:10}".format('#', 'MAKE', 'MODEL', 'COLOR', 'YEAR', 'MILEAGE'))
		for i in range(0, len(Automobile.vehicle_list)):
			make, model, color, year, mileage = Automobile.vehicle_list[i][0], Automobile.vehicle_list[i][1], Automobile.vehicle_list[i][2], Automobile.vehicle_list[i][3], Automobile.vehicle_list[i][4]
			print("{:10} {:10} {:10} {:10} {:10} {:10}".format(i+1, make, model, color, year, mileage))

	def export():
		f = open("Catalog.txt", "w+")
		f.write("Index"+"\tMAKE"+"\tMODEL"+"\tCOLOR"+"\tYEAR"+"\tMILEAGE\n")
		for i in range(0, len(Automobile.vehicle_list)):
			f.write(str(i+1)+".\t"+Automobile.vehicle_list[i][0]+"\t"+Automobile.vehicle_list[i][1]+"\t"+Automobile.vehicle_list[i][2]+"\t"+Automobile.vehicle_list[i][3]+"\t"+Automobile.vehicle_list[i][4])
			if(i != len(Automobile.vehicle_list)-1): f.write("\n")
			
		f.close()
		
	def is_empty():
		return len(Automobile.vehicle_list)==0


cars = Automobile


while True:
	print("1. Add vehicle")
	print("2. Remove vehicle")
	print("3. Update vehicle")
	print("4. List vehicles")
	print("5. Export catalog")
	print("6. Quit")
	
	choice = int(input("Pick from the options above enter corresponding number: "))
	if(choice == 1): cars.add_vehicle()
	elif(choice == 2): 
		if(cars.is_empty()):
			print("Collection is empty, you cannot remove vehicle.")
			print("Pick another option!")
			continue
		else:
			cars.list_vehicles()
			op = int(input("Enter number corresponding to entry to remove: "))
			cars.remove_vehicle(op-1)
			
	elif(choice == 3):
		if(cars.is_empty()):
			print("Collection is empty, No vehicles to update.")
			print("Pick another option!")
			continue
		else:
			cars.update_vehicle()
	elif(choice == 4): cars.list_vehicles()
	elif(choice == 5): cars.export()
	elif(choice == 6):
		print("Thanks for visiting!")
		break
	else: print("Invalid choice, give it another go :)")
