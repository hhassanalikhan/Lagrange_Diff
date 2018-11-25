import time
import _thread 
import math
import copy
import csv
# Define a function for the thread
def Lagrange_Diff(startingInd, data,sign1):
	formulaFile = "WristFlexFormula.txt"
	defRange = 7
	optimizationMul = 1
	AnswerEq = []
	print ("")
	time.sleep(1)
	count = 0
	minimum = float (data[startingInd])
	minIndex = startingInd
	countCheck = 50
	while count < countCheck:
		temp = float (data[startingInd+count])
		#0 find the least number , 1 find the max numb
		if sign1 == 1 or 1: 
		#	print(startingInd+count, " ", minimum," = ", temp)
			if minimum > temp:
				minimum = temp
				minIndex = startingInd+count
				if((count > 0.9*countCheck) and data[startingInd+count] > data[startingInd+count+1] ):
					countCheck+=1
				#print(sign1,"Temp at = ",startingInd+count," = ", temp)
				#print ("Swapped")
		#elif sign1 == 0: 
		#	print(startingInd+count, " ", minimum," = ", temp)
		#	if minimum < temp:
		##		minimum = temp
			#	minIndex = startingInd+count
				#print(sign1,"Temp at = ",startingInd+count," = ", temp)
				#print ("Swapped")
		count += 1
		
	print ("Most significant number in this muscle movement part{",startingInd+10,"} is at[",minIndex,"]","=",minimum)
	count = 0
	#make equation now 
	fx = ''
	
	#dummyList = [-2,1,4,7]
	diffPercentageList = copy.deepcopy(data[minIndex-defRange:minIndex+defRange])
	tempVal = 0
	for i in range(0,len(diffPercentageList)):
		tempVal =  float(data[(minIndex-defRange) + i-1])/ float(data[(minIndex-defRange) + i-2])
		if i == 0:
			diffPercentageList[i] = 1
		else:
			diffPercentageList[i] = tempVal
			

	#dummyList = data[minIndex-defRange:minIndex+defRange]
	dummyList = copy.deepcopy(diffPercentageList)
	degree = len(dummyList)
	xVal = 0
	print('')
	print('')
	for sample in dummyList:
		fx += "("
		for indX in range(0,len(dummyList)):
			if indX != xVal:
				fx += '(x-'+str(indX+1)+')'
		fx += '/'
		for indX in range(0,len(dummyList)):
			if indX != xVal:
				fx += '('+str(xVal+1)+'-'+str(indX+1)+')'
		fx += ')*'+'('+str(sample)+')'
		if xVal < (len(dummyList)-1):
			fx += '+'
		xVal += 1

	print(fx)
	print('')
	polynomials = fx.split('+')
	#print (polynomials)
	finalEquation = ''
	for currPol in range(0,len(polynomials)):
		#find degree
		factors = polynomials[currPol].split('/')
		i1 = 0
		tempintermediateResult = []
		intermediateResult = []
		while i1 < len(factors):
			
			nominator = factors[i1]
			nominator = nominator.replace('((','(')
			#print (nominator)
			denominator = factors[i1+1]
			tempDnominator = denominator.split('*')
			#print (denominator)
			multiplier = tempDnominator[1]
			denominator = tempDnominator[0]
			denominator = denominator.replace('))',')')
			multiplier = multiplier.replace('(','')
			multiplier = multiplier.replace(')','')
			print('Nom=',nominator,'Denom=',denominator,'Mul=',multiplier)
			i1 += 2

			#process nominator
			temp = denominator.split(')')
			i2= 0 
			tempDenom = 0
			while i2 < len(temp):
				temp[i2] = temp[i2].replace('(','')
				i2 +=1
			temp.remove('')
			#print(temp)
			i2=0
			temp = denominator.split(')')
			temp.remove('')
			tempDDenom = 1
			while i2 < len(temp):
				tempDenom = 0
				tds= temp[i2]
				tds = tds.replace('(','')
				tds = tds.split('-')
				i44 = 1
				tempDenom = int(tds[0])
				while i44 < len(tds):
					tempDenom  -= int(tds[i44])
					i44 += 1
				i2 +=1
				tempDDenom *=tempDenom
		#	print (temp)
			temp = nominator.split(')')
			i2= 0
			while i2 < len(temp):
				temp[i2] = temp[i2].replace('(','')
				i2 +=1
			temp.remove('')
			i2= 0 
			nfacList = []
			
			while i2 < len(temp):
				#multiply factors of 1 nominator 
				#print (temp[i2]))
				nfac = ''
				i3 = 0
				while i3 < len(temp[i2]):
					c = temp[i2][i3]
					#print (c)
					if c!='-' and c!='+':
						nfac += c
					else: 
					#	print ('Factor in mult',nfac)
						nfacList.append(nfac)
						nfac = ''
						nfac +=c
						#i3 += 1
					i3 += 1
				nfacList.append(nfac)
				#print ('Int Result:',intermediateResult,'Factor in mult',nfacList)
				i4 = i5 = 0
				varIR = False
				varIC = False
				
				if len(intermediateResult) == 0:
					intermediateResult = nfacList
				else:
					tempintermediateResult = []
					i4 = 0
					xvlen = len(intermediateResult)
					while i4 < xvlen:
						i5=0
						while i5 < len(nfacList):
							#print(i4,',',i5,)	
							res = intermediateResult[i4]
							comput = nfacList[i5]
							cof = ''
							cofy = '';
							if 'x' in res:
								varIR = True
								i6 = 0
								ressTemp = res.split('x')
								cof = xvj = ressTemp[0]
								#while i6 < len(res):
								#	if res[i6] == 'x':
								#		i6 = len(res)
								#	else:
								#		cof +=res[i6]
								#	i6 += 1
							else:
								cof = res
							#	print (cof,varIR,varIC )
							if cof =='':
								cof = '1'
							if 'x' in comput:
								i6 = 0
								varIC = True
								ressTemp = comput.split('x')
								cofy = xvj = ressTemp[0]
								#while i6 < len(comput):
								#	if comput[i6] == 'x':
								#		i6 = len(comput)
								#	else:
								#		cofy +=comput[i6]
							else:
								cofy = comput
							#	print (cofy,varIR,varIC )
							if cofy =='':
								cofy = '1'
							if varIC or varIR:
								if varIC== True and varIR== True:
									varIC = varIR = False;
									if '^' in res:
										#inc ^ in res
										pw = ''
										i7 = 0
										ressTemp = res.split('^')
										xvj = ressTemp[1]
										#while res[i7] !='^':
										#	i7 += 1
										#i7 += 1
										#while i7 < len(res):
										#	pw += res[i7]
										#	i7 += 1
										#pow = int(pw)
										pow = int(xvj)
										pow +=1;
										res = str(float(cof)*float(cofy))+'x^'+str(pow)
										#print("Computed X",res)
										tempintermediateResult.append(res)
									else:
										#add ^ in res
										res = str(float(cof)*float(cofy))+'x^'+str(2)
										#print("Computed X",res)
										tempintermediateResult.append(res)
								else:
									target =''
									if varIC == True:
										target = comput
									else:
									#	print (res)
										target = res
									i7 = 0
									pw = ''
									if '^' in target:
										ressTemp = target.split('^')
										pw = xvj = ressTemp[1]
										#while target[i7] !='^':
										#	i7 += 1
										#i7 += 1
										#while i7 < len(target):
										#	pw += res[i7]
										#	i7 += 1
										pow = int(pw)
										#pow = int(xvj)
										#print (pow,pw)
										res = str(float(cof)*float(cofy))+'x^'+pw
										tempintermediateResult.append(res)
										varIC = varIR = False;
									else:
										res = str(float(cof)*float(cofy))+'x^'+str(1)
										#print("Computed X",res)
										tempintermediateResult.append(res)
							else:
								# no var in these two factors 
								xr = '' + str(float(cof) * float(cofy))
								tempintermediateResult.append(xr)
							#print (tempintermediateResult)
							i5 +=1
							varIC = varIR = False;
						i4 += 1
					ajeebKaam = copy.deepcopy(tempintermediateResult)
					newIndex1 = degree
					while newIndex1 > 0:
						newCof = 0
						for newIndex2 in range(0,len(tempintermediateResult)-1):
							cc = tempintermediateResult[newIndex2]
							cchkstr = '^'+str(newIndex1)
							cchkstr = cc[len(cc)-len(cchkstr):len(cc)]
							bstr = '^'+str(newIndex1)
							if bstr == cchkstr:
								ajeebKaam.remove(cc)
								newCof +=float(cc.split('x^')[0])
						if int(newCof) != 0:
							ajeebKaam.append(str(newCof)+ 'x^'+str(newIndex1))
						newIndex1 -=1
					#ajeebKaam.reverse()
					if optimizationMul == 1:
						intermediateResult = ajeebKaam
					else:
						intermediateResult = tempintermediateResult
				i2 += 1
			#	print (intermediateResult)
				nfacList = []
				#print (intermediateResult)
		#	print (intermediateResult)
			thisPom =[]
			i9 = degree-1;
			i10 = 0
			tempintermediateResult2 =[]
			while i9 >= 0 :
				degreeFactors = []
				chkStr = '^'
				i10 = 0
				while i10 < len(intermediateResult):
					if i9 < 1:
						if chkStr not in intermediateResult[i10]:
							degreeFactors.append(intermediateResult[i10])
					else:
						chkStr = '^'+str(i9)
						if chkStr in intermediateResult[i10]:
							degreeFactors.append(intermediateResult[i10])

					i10 += 1
			#	print("Degree:",i9,"Factors",degreeFactors)
				i11 = 0
				tempCofPol = 0
				while i11 < len(degreeFactors):
					tt = degreeFactors[i11]
					chkstring = "x^"+str(i9)
					if i9 < 1:
						chkstring = "x^"
						if chkstring not in tt:
							tempCofPol += float(tt)
					elif chkstring in tt:
						tt = tt.replace("x^"+str(i9),"")
						tempCofPol += float(tt)
					i11 +=1
				#print("Degree:",i9,"Factors",tempCofPol,"X^",i9)
				if i9 < 1:
					thisPom.append((tempCofPol/tempDDenom) * float(multiplier))
				else:
					strrr = str((tempCofPol/tempDDenom) * float(multiplier))+"x^"+str(i9)
					thisPom.append(strrr)
				i9 -= 1
			#print("Result:",thisPom,'(after devision with',tempDDenom,') and mul with')
			AnswerEq.append(thisPom)
		#have to work on denominatior and multiplier
	#print(AnswerEq)
	i2 = 0
	i3 = 0
	sum = 0
	samePowerPol = ''
	smp = []
	while i2 < degree:
		samePowerPol = ''
		i3 = 0
		while i3 < len(AnswerEq):
			
			temp = AnswerEq[i3][i2]
			#print(temp)
			samePowerPol += str(temp) + '+'
			i3 +=1
		samePowerPol = str(samePowerPol) + '0'
		#print(samePowerPol)
		smp.append(samePowerPol)
		i2+=1
	i2 = 0
	smp2 = []
	deg = degree - 1
	while i2 < len(smp):
		temp = smp[i2];
		temp = temp.split('+')
		#temp.remove('')
		i3 = 0
		
		currSum = 0
		while i3 < len(temp):
			t1 = temp[i3]
			if deg!=0:
				t1 = t1.replace('x^'+str(deg),'')
			currSum += float(t1)
			i3 += 1
		if deg!=0:
			eq = str(currSum) +'x^'+str(deg)
		else:
			eq = str(currSum)
		smp2.append(eq)
		deg -= 1
		i2 += 1
	print('\n')
	print('\n')
	print(smp2)
	i3 = 0
#	while i3 < len(smp):
		#print(smp2)
#		smp2[i3] = smp2[i3].replace('x','(1)')
#		i3+=1
	print('\n')
	print('\n')
	print(smp2)
	with open(formulaFile, "a") as myfile:
		for i in range(0,len(smp2)):
			myfile.write(smp2[i])
			myfile.write('---')
		myfile.write('\n')
	myfile.close()
	realValue = 0;
	for i in range(1,len(dummyList)):
		i3=0
		realValue = 0
		while i3 < len(smp):
			#base = 1
			#print(smp2)
			temp = smp2[i3]
			if 'x' in temp:
				temp = smp2[i3].replace('x','*'+str(i))
				t11 = temp.split('*')
				t12 = t11[1]
				t12 = t12.split('^')
				base = float(t12[0])
				expc =1
				for exp in range(1,int(t12[1])+1):
					expc *=base
				base = expc * float(t11[0])
				realValue += base
			else:
				realValue += float(temp)
			i3+=1
		print('[',(i+minIndex-(degree/2)),']',(1- realValue), ', Difference of two elements (i/i-1) in percentage:',1 - diffPercentageList[i-1])
		if 1 - diffPercentageList[i-1] != 0:
			pval =1
			#print('Difference is ', abs(1 - diffPercentageList[i-1]) - (1- realValue))
			if(abs(1 - diffPercentageList[i-1]) - (1- realValue)) < float(0.00005):
				pval = (1- realValue)
			elif 1 - diffPercentageList[i-1] > 0:
				pval = (1 - diffPercentageList[i-1])*0.9
			else:
				pval = (1 - diffPercentageList[i-1])*1.1
			print('Accuracy: ', round((1- realValue),8)/ round(pval, 8))


columns = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
ifg = len(columns)
with open('WristSamples/WristFlex.csv') as f:
    reader = csv.reader(f)
   # reader.next()
    for row in reader:
        for (i,v) in enumerate(row):
            columns[i].append(v)

Tes1 = 1
for mainI in range(Tes1,Tes1+1):

	lines = columns[mainI]
	#lines.replace('\n','')
	i = 0
	runningAverage = [0] * 5
	runningAverageTotal = -1;
	difference = 1
	diffAverage = 10
	checkVal = 15
	countInc = 0
	ind = 0
	phaseStart = 0
	ignore = 0;
	fomulaDone = 0
	for i in range(0,len(lines)):
		if ignore == 0:
		#	if i > 0:
		#		runningAverageTotal = (float (runningAverageTotal)*(i-1) + float(lines[i])) / i
		#		diffAverage = (diffAverage+(difference/i))
			if i > 2*checkVal:
				diffAverage = 0;
				for x in range(i-(2*checkVal),i-checkVal):
					diffAverage += abs(float(lines[x]) - float(lines[x+1]))
				diffAverage = diffAverage/checkVal
			if i > 0 and i<len(lines):
				difference = abs(float(lines[i]) - float(lines[i-1]))
		#	if abs(difference/diffAverage) > 0.
	#		print(i,lines[i],", Difference:",difference,"-",abs(difference/diffAverage),", Running average: ",diffAverage)
			if i> 100 and abs(difference/diffAverage) >= 5 and (difference > 70 or diffAverage > 20):
				countInc += 1
				if countInc >= 4:
					#print(i,lines[i],", Difference:",difference,"-",abs(difference/diffAverage),", Running average: ",diffAverage,"Range of avrg = ",i-(2*checkVal), "-",i-checkVal )
					if phaseStart == 0:
						print('Found contraction at :',i)
					if phaseStart == 1:
						print('Found Relaxation at :',i)
					phaseStart += 1
					phaseStart = phaseStart % 2
					ignore = 50
					sign = 0
					print('Current Difference and sign',int(float(lines[i])) - int(float(lines[i-1])))
					if float(lines[i-1]) - float(lines[i]) > 0:
						sign = 0
					else:
						sign = 1
					if phaseStart==1 and fomulaDone == 0 :
						Lagrange_Diff((i-10),lines,sign)
						#_thread.start_new_thread( Lagrange_Diff, ((i-15),lines,sign,))
					else:
						fomulaDone = 1
			else:
				countInc = 0
		else:
			ignore -= 1


