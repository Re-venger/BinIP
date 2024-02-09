
def checkPadding(bIp):
	padLen = max(0, 8-len(str(bIp)))
	paddedIp = '0'*padLen + str(bIp)
	return paddedIp


def binaryRep(ipOct):
	b = 0
	exp = 0
	while(ipOct != 0):
		dig = ipOct & 1
		ipOct = ipOct >> 1
		b = dig*(pow(10, exp)) + b
		exp+=1
	return checkPadding(b)



def ConvertIp(ipOctect):
	binRep = []
	for i in ipOctect:
		ipOct = int(i)
		binRep.append(binaryRep(ipOct))
	return binRep



def main():
	ipAddress = str(input("Enter IP Address: "))
	ipOctect = ipAddress.split('.')
	print(f"IP ADDRESS: {ipAddress}")
	print(f"BIT REPRES: {'.'.join(ConvertIp(ipOctect))}")

main()