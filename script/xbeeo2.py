#!/usr/bin/python

# /**
#  @file xbeeo2.sh
#  @author  Oscar Gomez Fuente <oscargomezf@gmail.com>
#  @ingroup iElectronic
#  @date 11/05/2014
#  @version 1.0.0
#  @section DESCRIPTION
#   script to send remote at commands in API mode.
#  */

import serial
from xbee import ZigBee
import time
import sys 
import getopt
from time import sleep
from binascii import hexlify

VER = "1.0"
PORT = '/dev/ttyUSB0'
BAUD_RATE = 9600

def usage() :  
	"""xbeeo2: appplication to ON/OFF two reles with ZigBee in API mode"""
	print "xbeeo2: appplication to ON/OFF two reles with ZigBee in API mode, version: ", VER
	print "usage:", sys.argv[0], "[options]"
	print "  --help (-h)\t\tthis message"
	print "  --test (-t)\t\ttest outputs"
	print "  --output (-o)\t\tnumber of output: {'0': D12, '1': D11}"
	print "  --mode (-m)\t\tmode: {'0': OFF (0x04), '1': ON(0x05)}"

def main(argv):
	try:   
		#output = 'vacio'
		value = 'vacio'

		opts, args = getopt.getopt(argv, 'hto:m:', ['help', 'test', 'output=', 'mode='])
		if not opts:
			print 'No options supplied\n'
			usage()
			sys.exit(2)
		else:
			for opt, arg in opts:
				if opt in ('-h', '--help'):
					usage()
					sys.exit(0)
				elif opt in ('-t', '--test'):
					test()
					sys.exit(0)
				elif opt in ('-o', '--output'):
					if arg == '0':
						output = 'P2' #D12
					else:
						output = 'P1' #D11
				elif opt in ('-m', '--mode'):
					if arg == '0':
						value = '\x04' #OFF
					else:
						value = '\x05' #ON
				else:
					assert False, "unhandled option"

			if (len(opts) < 2):
				usage()
				sys.exit(2)
			else:
				return output, value
	except getopt.GetoptError:
		usage()
		sys.exit(2)

def test():
	#print "Output: %s value: %s" % (numOutput, value)
	ser = serial.Serial(PORT, BAUD_RATE)

	# ZB XBee here. If you have Series 1 XBee, try XBee(ser) instead
	xbee = ZigBee(ser)

	#MAC, number written on the back of the XBee module
	# CO1 = my coordinator
	# EP1 = my endpoint with 2 outputs. D12(UP) y D11(DOWN)
	device = {
		'CO1': '\x00\x13\xA2\x00\x40\xA0\xD4\xA3',
		'EP1': '\x00\x13\xa2\x00\x40\x99\x2e\x62'
	}
	#64 bit address

	xbee.remote_at(dest_addr_long = device['EP1'], command = 'P1', parameter = '\x05')
	sleep(1)
	xbee.remote_at(dest_addr_long = device['EP1'], command = 'P1', parameter = '\x04')
	sleep(1)
	xbee.remote_at(dest_addr_long = device['EP1'], command = 'P2', parameter = '\x05')
	sleep(1)
	xbee.remote_at(dest_addr_long = device['EP1'], command = 'P2', parameter = '\x04')
	sleep(1)
	ser.close()

if __name__== '__main__':
	numOutput, value = main(sys.argv[1:])

	#print "Output: %s value: %s" % (numOutput, value)
	ser = serial.Serial(PORT, BAUD_RATE)

	# ZB XBee here. If you have Series 1 XBee, try XBee(ser) instead
	xbee = ZigBee(ser)

	#MAC, number written on the back of the XBee module
	# CO1 = my coordinator
	# EP1 = my endpoint with 2 outputs. D12(UP) y D11(DOWN)
	device = {
		"CO1":'\x00\x13\xA2\x00\x40\xA0\xD4\xA3',
		"EP1":'\x00\x13\xa2\x00\x40\x99\x2e\x62'
	}
	#64 bit address

	#change remote device function
	xbee.remote_at(dest_addr_long = device['EP1'], command = numOutput, parameter = value)
	
	print "Output: %s Value: 0x%s" % (numOutput, hexlify(value))

	ser.close()