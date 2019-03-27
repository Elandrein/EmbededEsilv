import smbus
import time

# Remplacer 0 par 1 si nouveau Raspberry
bus = smbus.SMBus(1)
address = 0x12 #i2c adress of the arduino raspberry connection
nbBytes = 2 #number of bytes to recieve, here nuber of data per loop to recieve 
i=1

while(i==1): #endless loop until it crash which append regularly
	time.sleep(1) #wait 1 s between each probe 
	call_i2c_arduino(address,nbBytes) # program to ask 2 bytes a adress via i2c


def call_i2c_arduino(address, nbBytes): 
	print "Demande Arduino ",address #report the begining of the listening process at adress
	bus.write_byte(address, nbBytes) # send the request for nbBytes at adress
	time.sleep(1) # wait for 1 second to let the arduino answer
	print "La reponse de l'arduino : " #print the answer
	reponse = bus.read_i2c_block_data(address, 0, nbBytes)
	reponsestr = [] #create the string that will be used to save the datas 
	for i in range(len(reponse)): 
		reponsestr.append(str(reponse[i]))#fill the string with the recieved datas
		reponsestr.append(",") # space them with a , 
		mystr = ''.join(reponsestr)# tranfer the entire string into another
	file=open("/var/www/html/meteo.csv","a") #open a Csv on the given adress to save the mystr string into it
	file.write(mystr)# write the string into the csv
	file.write("\n")# finish the line with a return to organise the data 
	file.close()#close the csv to write and save all ( all the file instruction append at this moment in reality) 
	print mystr #print the data string to show what is saved ito the csv

