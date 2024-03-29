def processRawHeight(heightFt, heightIn):
    feet = float(heightFt) # convert to float
    inch = float(heightIn) # convert to float
    totalIN = inch + (feet * 12) # convert and add feet to totalIN
    return totalIN #return totalIN

def imperialToMetric(weight, heightIN):
    try:
        weight = float(weight) * 0.45 # convert pounds to kilogrammes
    except:
        print("Error processing weight input")
        return("Error processing weight input")
    try:
        heightM = float(heightIN) * 0.025 #convert total inches into metres
    except:
        return("Error processing height input")
    heightM = heightM * heightM # BMI requires square metres
    return weight, heightM

def categoriseBMI(inputBMI):
    try:
        inputBMI = float(inputBMI) #done to ensure comparisons work
    except:
        raise ValueError("Error converting your inputs") #if conversion fails, then raise error
    if (inputBMI < 18.5):
        BMIcat = "Underweight"
    elif (18.5 <= inputBMI < 25.0): #using < rather than <= to ensure coverage
        BMIcat = "Normal Weight"
    elif (25.0 <= inputBMI < 30.0):
        BMIcat = "Overweight"
    elif (30.0 <= inputBMI):
        BMIcat = "Obese"
    else:
        raise ValueError("Error calculating your BMI")
    return BMIcat

#calculates the BMI
def calculateBMI(weight, height):
    try:
        BMI = float(weight)/float(height)
    except:
        raise ValueError("Error converting your inputs")
    return BMI

def processHost(weight, heightFt, heightIn):
    totalIn = processRawHeight(heightFt, heightIn)  # process raw height, outputs the height in inches
    weight, heightM = imperialToMetric(weight, totalIn)  # converts from imperial to metric
    BMI = calculateBMI(weight, heightM)  # calculate BMI
    category = categoriseBMI(BMI)  # categorise BMI
    return BMI, category