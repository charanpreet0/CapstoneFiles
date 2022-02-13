from serial import Serial
import serial
#from gsmHat import GSMHat,SMS,GPS
import time
ser = serial.Serial("/dev/ttyS0", 115200)

#gsm = GSMHat("/dev/ttyS0",115200)
#if gsm.SMS_available() > 0:
#	number = '8187950022'
#	message = "Hello World"
#	gsm.SMS_write(number,message)

W_buf_logoin = "AT+CPIN?\r\n"
W_buf_phone = "ATD8187950022;\r\n"
ser.write(W_buf_logoin)

#W_buff = ["AT\r\n", "AT+CREG?\r\n", "AT+CPIN?\r\n", "ATD8187950022;\r\n", "AT\r\n", "AT+CMGF=1\r\n", "AT+CSCA=?\r\n", "AT+CMGS=\"8187950022\"\r\n", "helloworld!"]
#W_buff = ["AT\r\n", "AT+CMGF=1\r\n", "AT+CSCA=\"+12063130004\"\r\n", "AT+CMGS=\"18187950022\"\r\n", "helloworld"]
#W_buff = ["AT\r\n", "AT+CGATT?\r\n", "AT+CSTT=\"CMNET\"\r\n","AT+CIICR\r\n","AT+CIFSR\r\n", "AT+CIPGSMLOC=1,1\r\n"]
#W_buff = [ "AT\r\n", "AT+CGATT?\r\n", "AT+CSQ\r\n", "AT+CSTT=\"CMNET\"\r\n","AT+CIICR\r\n","AT+CIFSR\r\n","AT\r\n", "AT+SAPBR=3,1,\"CONTYPE\",\"GPRS\"\r\n", "AT+SAPBR=3,1,\"CMNET\",\"www\"\r\n", "AT+SAPBR=1,1\r\n", "AT+SAPBR=2,1\r\n", "AT+CIPGSMLOC=1,1\r\n"]
W_buff = ["AT\r\n","ATE0\r\n","AT+CMGF=1\r\n","AT+CNMI=2,1,0,0,0\r\n","AT+CMGS=\"8187950022\"\r\n", "helloworld\r\n", "\x1A"]
ser.write(W_buff[0])
data = ""
num = 0
ser.flushInput()

try:
    while True:
        while ser.inWaiting() > 0:
            data += ser.read(ser.inWaiting())
        if data != "":
            print("Printing Data", data)
            if num < len(W_buff)-1:
                time.sleep(0.5)
                ser.write(W_buff[num+1])
                num += 1
            # elif num == 3:
            #     time.sleep(5)
            elif num == len(W_buff)-1:
                time.sleep(0.5)
                ser.write(W_buff[num])

            data = ""
except KeyboardInterrupt:
    if ser != None:
        ser.close()
