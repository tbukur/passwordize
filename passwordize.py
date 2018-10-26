###################################
# creates random passwords of given length
# using a Pseudo Random-Number Generator (PRNG)
# based on a Linear Congruential Number Generator (LCNG) [Lehmer 1949]
# and on suggestions by J.J. Schneider [Schneider and Kirkpatrick 2006, 32-37]
# adapted to a 64-bit system and implemented by Thomas Bukur, November 2013
#
# Lehmer, D. H. (1949). Mathematical methods in large-scale computing units. In Proc. 2nd Symp. on Large-Scale Digital Calculating Machinery, Cambridge, MA, pages 141-146. Harvard University Press
# Schneider, J. J. and Kirkpatrick, S. (2006). Stochastic Optimization. Springer
############################################

import math
import sys
import string

## global variables for PRNG
a = 1664525
b = 1013904223
x1 = 0

class randomizer():
	def __init__(self, seed):
		global x1
		x1 = seed
		for i in range(0,999):
			self.getNext()

	def getNext(self):
		global x1
		## simulating integer overflow
		x2 = (a * x1&0xffffffffffffffff) + b
		z = math.fabs( float(x2) * (float(1)/(2**64)) )
		x1 = x2
		return z

def main():

	if len(sys.argv)==2:
		try:
			PWlength = int(sys.argv[1])
		except ValueError:
			sys.exit("Given argument is not an integer!?")
	else:
		sys.exit("Please give one number (INT) as the length of the requested passphrase!")

	if PWlength < 6:
		sys.exit("You really should use longer passwords!")

	from datetime import datetime
	dt = datetime.now()
	seed = dt.microsecond

	print("Seed: "+str(seed))

	r = randomizer(seed)

	## only alphabetic characters
	myLettersStartAndEnd = string.ascii_letters
	## make letters and numbers appear more frequently than special characters
	myLetters = string.ascii_letters + string.digits + "()[]{}?!$%&/=*+~,.;:<>-_" + string.ascii_letters + string.digits

	for i in range(0,1111):
		rdm_number = r.getNext()

	while True:
		passphrase = ""
		for i in range(0,PWlength):
			rdm_number = r.getNext()
			# make sure the first and last character are alphabetic characters (just for convenience)
			if(i == 0 or i == PWlength-1):
				passphrase += myLettersStartAndEnd[int(rdm_number * len(myLettersStartAndEnd))]
			else:
				passphrase += myLetters[int(rdm_number * len(myLetters))]
		# check whether we have at least one number and one special character
		if(any(char.isdigit() for char in passphrase)):
			if(any(not char.isalnum() for char in passphrase)):
				break

	print("Passphrase: "+ passphrase)



if __name__ == '__main__':
	main()

## eof
