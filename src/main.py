import math
import calculate_RhoPhase
import plot_RhoPhase

#buka file
baca_edi = open("AZ_076.edi", "r")


readEdi = ' '

# print(fDir)
while not readEdi == '>END': 
	readEdi = baca_edi.readline()
	# if readEdi[:6] == 'REFLOC':
	# 	print(readEdi)
	# if readEdi[:6] == 'REFLAT':
	# 	print(readEdi)
	# if readEdi[:6] == 'REFLON':
	# 	print(readEdi)
	if readEdi[:6] == 'DATAID':
		siteName = readEdi.split('=')
		siteName = siteName[1].split('\"')
		siteName = siteName[1]
	if readEdi[:6] == 'NFREQ=':
		nFreq = readEdi.split('=')
		nFreq = int(nFreq[1])
	if readEdi[:8] == '>FREQ //':				#Read FREQ
		freq = []
		for i in range(0,(math.ceil(nFreq /6))):
			freq += baca_edi.readline().split()

	if readEdi[:8] == '>ZROT //':				#Read ZROT
		zrot = []
		for i in range(0,(math.ceil(nFreq /6))):
			zrot += baca_edi.readline().split()

	if readEdi[:5] == '>ZXXR':					#Read ZXXR
		zxxr = []
		for i in range(0,(math.ceil(nFreq /6))):
			zxxr += baca_edi.readline().split()
			
	if readEdi[:5] == '>ZXXI':					#Read ZXXI
		zxxi = []
		for i in range(0,(math.ceil(nFreq /6))):
			zxxi += baca_edi.readline().split()
			
	if readEdi[:8] == '>ZXX.VAR':				#Read ZXX.VAR
		zxxvar = []
		for i in range(0,(math.ceil(nFreq /6))):
			zxxvar += baca_edi.readline().split()

	if readEdi[:5] == '>ZXYR':					#Read ZXYR
		zxyr = []
		for i in range(0,(math.ceil(nFreq /6))):
			zxyr += baca_edi.readline().split()

	if readEdi[:5] == '>ZXYI':					#Read ZXYI
		zxyi = []
		for i in range(0,(math.ceil(nFreq /6))):
			zxyi += baca_edi.readline().split()

	if readEdi[:8] == '>ZXY.VAR':				#Read ZXY.VAR
		zxyvar = []
		for i in range(0,(math.ceil(nFreq /6))):
			zxyvar += baca_edi.readline().split()

	if readEdi[:5] == '>ZYXR':					#Read ZYXR
		zyxr = []
		for i in range(0,(math.ceil(nFreq /6))):
			zyxr += baca_edi.readline().split()

	if readEdi[:5] == '>ZYXI':					#Read ZYXI
		zyxi = []
		for i in range(0,(math.ceil(nFreq /6))):
			zyxi += baca_edi.readline().split()

	if readEdi[:8] == '>ZYX.VAR':				#Read ZYX.VAR
		zyxvar = []
		for i in range(0,(math.ceil(nFreq /6))):
			zyxvar += baca_edi.readline().split()

	if readEdi[:5] == '>ZYYR':					#Read ZYYR
		zyyr = []
		for i in range(0,(math.ceil(nFreq /6))):
			zyyr += baca_edi.readline().split()

	if readEdi[:5] == '>ZYYI':					#Read ZYYI
		zyyi = []
		for i in range(0,(math.ceil(nFreq /6))):
			zyyi += baca_edi.readline().split()

	if readEdi[:8] == '>ZYY.VAR':				#Read ZYY.VAR
		zyyvar = []
		for i in range(0,(math.ceil(nFreq /6))):
			zyyvar += baca_edi.readline().split()

	if readEdi[:9] == '>TROT.EXP':				#Read TROT.EXP
		trotexp = []
		for i in range(0,(math.ceil(nFreq /6))):
			trotexp += baca_edi.readline().split()

	if readEdi[:8] == '>TXR.EXP':				#Read TXR.EXP
		txrexp = []
		for i in range(0,(math.ceil(nFreq /6))):
			txrexp += baca_edi.readline().split()

	if readEdi[:8] == '>TXI.EXP':				#Read TXI.EXP
		txiexp = []
		for i in range(0,(math.ceil(nFreq /6))):
			txiexp += baca_edi.readline().split()

	if readEdi[:10] == '>TXVAR.EXP':			#Read TXVAR.EXP
		txvarexp = []
		for i in range(0,(math.ceil(nFreq /6))):
			txvarexp += baca_edi.readline().split()

	if readEdi[:8] == '>TYR.EXP':				#Read TYR.EXP
		tyrexp = []
		for i in range(0,(math.ceil(nFreq /6))):
			tyrexp += baca_edi.readline().split()

	if readEdi[:8] == '>TYI.EXP':				#Read TYI.EXP
		tyiexp = []
		for i in range(0,(math.ceil(nFreq /6))):
			tyiexp += baca_edi.readline().split()

	if readEdi[:10] == '>TYVAR.EXP':			#Read TYVAR.EXP
		tyvarexp = []
		for i in range(0,(math.ceil(nFreq /6))):
			tyvarexp += baca_edi.readline().split()

# XY
freq, per, rho_xy, phase_xy = calculate_RhoPhase.calculate_RhoPhase(zxyr, zxyi, freq)

# YX
freq, per, rho_yx, phase_yx = calculate_RhoPhase.calculate_RhoPhase(zyxr, zyxi, freq)

# print(rho_xy, rho_yx)
plot_RhoPhase.plot_RhoPhase(per, rho_xy, phase_xy,  rho_yx, phase_yx, siteName, rmin = 1, rmax = 1000, pmin = 0, pmax = 90)