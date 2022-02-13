import serial
import time

ser = serial.Serial("/dev/ttyS0", 115200)

W_buff = ["AT+CGNSPWR=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+CGNSINF\r\n", "AT+CGNSURC=2\r\n", "AT+CGNSTST=1\r\n"]
ser.write(W_buff[0])
ser.flushInput()
data = ""
num = 0


try:
    file = open("gpsdata.txt", "w")
    file.write("Beginning GPS data transmission \n")
    while True:

        while ser.inWaiting() > 0:
            data += ser.read(ser.inWaiting())
        if data != "":
            print("Printing Data", data)
            if num < 4:
                time.sleep(0.5)
                ser.write(W_buff[num+1])
                num += 1
            elif num == 4:
		line = data.splitlines()
		if(len(line) > 4):
			word = line[3].split(',')
			if(len(word) > 5 and (word[3] == 'N' or word[3] == 'S')):
				if  word[3] == 'N':
					Latitude = (((float)(word[2]))/100)
				else:
					Latitude = -(((float)(word[2]))/100)
				if  word[5] == 'E':
					Longitude = (((float)(word[4]))/100)
				else:
					Longitude = -(((float)(word[4]))/100)
				print("Latitude: ", ((float)(word[2]))/100, ((float)(word[2])%1)*100, word[3],"Longitude: ", ((float)(word[4]))/100,((float)(word[4])%1)*100, word[5])
                		print("Latitude: ", Latitude, " Longitude: ", Longitude)
				file.write("Latitude: " + str(Latitude) + " Longitude: " + str(Longitude) + "\n")
		time.sleep(0.5)
                ser.write(W_buff[num])
            data = ""
except KeyboardInterrupt:
    if ser != None:
	file.write("Ending GPS data transmission \n")
	file.close()
        ser.close()



# try:
#     while True:
#         print("checking")
#         while ser.inWaiting() > 0:
#             print("In Nested While Loop")
#             data += ser.read(ser.inWaiting())
#         if data != "":
#             print(data)
#             time.sleep(0.5)
#             ser.write(W_buff[num+1])
#             num = num + 1
#             if num == 4:
#                 print("num == 4 loop")
#                 time.sleep(0.5)
#                 ser.write(W_buff[4])
#             data = ""
# except KeyboardInterrupt:
#     if ser != None:
#         ser.close()

# import serial
# import time
# ser = serial.Serial("/dev/ttyS0",115200)
#
# W_buff = ["AT+CGNSPWR=1\r\n", "AT+CGNSSEQ=\"RMC\"\r\n", "AT+CGNSINF\r\n", "AT+CGNSURC=2\r\n","AT+CGNSTST=1\r\n"]
# ser.write(W_buff[0])
# ser.flushInput()
# data = ""
# num = 0
#
# try:
#     while True:
#         while ser.inWaiting() > 0:
#             data += ser.read(ser.inWaiting())
#         if data != "":
#             print(data)
#             if num < 4:
#                 time.sleep(0.5)
#                 ser.write(W_buff[num+1])
#             if num == 4:
#                 line = data.splitlines()
#                 if(len(line) > 4):
#                     print(word)
#                     word = line[3].split('.')
#                     if(len(word) > 5 and (word[3] == 'N' or word[3] == 'S')):
#                         print((int)((float)(word[2]))/100, ((float)(word[2])%1)*100, word[3],(int)((float)(word[4]))/100,((float)(word[4])%1)*100, word[5])
#                 time.sleep(0.5)
#                 ser.write(W_buff[4])
#             data = ""
# except KeyboardInterrupt:
#     if ser != None:
#         ser.close()


