# Description: Program for creating auto insurance policies for One Stop Insurance Company.
# Author: Braeden Mercer
# Dates(s): July 20th 2024 - July 26th 2024


# Define required libraries.
import datetime
import time
import FormatValues as FV
import sys

# Define program constants from constants file

f = open('const.dat', 'r')

POL_NUM = int(f.readline())
BASIC_PREMIUM_RATE = float(f.readline())
ADD_CAR_DISCOUNT_RATE = float(f.readline())
EXTRA_LIAB_RATE = float(f.readline())
GLASS_COV_RATE = float(f.readline())
LOANER_CAR_RATE = float(f.readline())
HST_RATE = float(f.readline())
PROC_FEE_RATE = float(f.readline())

f.close()

provLst = ["BC", "ON", "AB", "SK", "MB", "NL", 
"NS", "NU", "PE", "QC", "YT", "NT", "NB"]

payOptions = ["Full", "Monthly", "Down Payment"]

claimNum = []
claimDate = []
claimCost = []

# Define program functions

def progressBar(iteration, total, prefix='', suffix='', length=30, fill='█'):

    percent = ("{0:.1f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()

def nameResponse(inputValue):
    allowedChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ'-abcdefghijklmnopqrstuvwxyz"
    if set(inputValue).issubset(allowedChars):
        return True
    else:
        return False
      
def alphaResponse(inputValue):
    if inputValue == "Y":
        return True
    elif inputValue == "N":
        return True
    else:
        return False
    
def provResponse(inputValue):
    if len(inputValue) == 2 and inputValue in provLst:
        return True
    else:
        return False
    
def postCodeResponse(inputValue):
    if len(inputValue) == 6 and inputValue[0].isalpha() and inputValue[2].isalpha() and inputValue[4].isalpha() and inputValue[1].isdigit() and inputValue[3].isdigit() and inputValue[5].isdigit() == True:
        return True
    else:
        return False

# Main program starts here.
while True:

    # Gather user inputs.

    while True:
        fName = input("Enter customer's first name: ").title()
        if nameResponse(fName) == True:
            break 
        else:
            print("Invalid input. Please enter a valid first name.")

    while True:
        lName = input("Enter customer's last name: ").title()
        if nameResponse(lName) == True:
            break
        else:
            print("Invalid input. Please enter a valid last name.")

    address = input("Enter customer's address: ").title()
    city = input("Enter customer's city: ").title()
    while True:
        province = input("Enter customer's province code (XX): ").upper()
        if provResponse(province) == True:
            break
        else:
            print("Invalid input. Please enter a valid province code (XX).")
    
    while True:
        postalCode = input("Enter customer's postal code (X9X9X9): ").upper()
        if postCodeResponse(postalCode) == True:
            break
        else:
            print("Invalid input. Please enter a valid postal code (X9X9X9).")
    
    while True:

        phoneNum = input("Enter customer's phone number: ")

        if phoneNum == "":
            print("Invalid input. Please enter a valid phone number.")
        elif len(phoneNum)!= 10:
            print("Invalid input. Please enter a valid phone number.")
        elif phoneNum.isdigit() == False:
            print("Invalid input. Please enter a valid phone number.")
        else:
            phoneNum = "(" + phoneNum[0:3] + ")" + phoneNum[3:6] + "-" + phoneNum[6:]
            break
    
    while True:

        numCars = int(input("Enter the number of cars being insured (1-10): "))
        if 0 >= numCars or numCars > 10:
            print("Invalid input. Please enter a valid number of cars (1-10).")
        else:
            break
            
    while True:

        extraLiab = input("Does the customer have any extra liability coverage? (Y/N): ").upper()

        if alphaResponse(extraLiab) == True:
            break
        else:
            print("Invalid input. Please enter either Y or N.")

    while True:

        glassCov = input("Does the customer have glass coverage? (Y/N): ").upper()

        if alphaResponse(glassCov) == True:
            break
        else:
            print("Invalid input. Please enter either Y or N.")

    while True:

        loanerCar = input("Does the customer have loaner car coverage? (Y/N): ").upper()

        if alphaResponse(loanerCar) == True:
            break
        else:
            print("Invalid input. Please enter either Y or N.")

    while True:
        
        payPlan = input("What is the payment plan? (Full/Monthly/Down Payment)").title()
        
        if payPlan not in payOptions:
            print("Invalid input. Please enter either Full, Monthly, or Down Payment.")
        elif payPlan == "Monthly":
            procFee = PROC_FEE_RATE
            downPay = 0
            break
        elif payPlan == "Full":
            procFee = 0
            downPay = 0
            break
        elif payPlan == "Down Payment":
            procFee = PROC_FEE_RATE
            while True:
                downPay = int(input("How much was the down payment? "))
                if downPay <= 0:
                    print("Invalid input. Please enter a valid down payment.")
                else:
                    break
            break

    while True:
        claim = input("Do you have any claims? (Y/N): ").upper()
        if claim not in ["Y", "N"]:
            print("Invalid input. Please enter either Y or N.")
        else:
            break
    
    while True:
        if claim == "Y":
            claimNum.append(int(input("Enter the claim number: ")))
            claimDate.append(input("Enter the claim date (yyyy-mm-dd): "))
            claimCost.append(float(input("Enter the claim cost: ")))
            addClaim = input("Do you want to add another claim? (Y/N): ").upper()
            if addClaim == "N":
                break
        elif claim == "N":
            break

    # Perform required calculations

    if extraLiab == "Y":
        extraLiabCost = numCars * EXTRA_LIAB_RATE       
    else:
        extraLiabCost = 0

    if glassCov == "Y":
        glassCovCost = numCars * EXTRA_LIAB_RATE        
    else:
        glassCovCost = 0

    if loanerCar == "Y":
        loanerCost = numCars * LOANER_CAR_RATE
    else:
        loanerCost = 0

    basePremium = numCars * BASIC_PREMIUM_RATE + ((numCars - 1)* BASIC_PREMIUM_RATE * ADD_CAR_DISCOUNT_RATE)
    extraCost = extraLiabCost + glassCovCost + loanerCost
    subTotal = basePremium + extraCost + procFee - downPay
    hst = HST_RATE * subTotal
    totalCost = subTotal + hst

    if payPlan == "Monthly":
        numPayments = 8
        monthlyPayment = totalCost / numPayments
    elif payPlan == "Full":
        numPayments = 1
    elif payPlan == "Down Payment":
        numPayments = 8
        monthlyPayment = (totalCost - downPay) / numPayments


    invoiceDate = datetime.date.today().strftime("%Y-%m-%d")
    payDueDate = datetime.date(datetime.datetime.now().year, datetime.datetime.now().month + 1, 1).strftime("%Y-%m-%d")

    # Display results

    print()
    print(f"                  One Stop Insurance Company")
    print(f"--------------------------------------------------------------")
    print()
    nameDsp = str(fName[0] + ". " + lName)
    print(f"{nameDsp}")
    print(f"{address}")
    print(f"{city}, {province}")
    print(f"{postalCode}")
    print(f"{phoneNum}")
    print(f"-----------------------------------------")
    print()
    print(f"Invoice Date: {invoiceDate}")
    print(f"Policy Number: {POL_NUM}")
    print(f"Number of Cars: {numCars}")
    print(f"Extra Liability Coverage: {FV.FYesNo(extraLiab)}")
    print(f"Glass Coverage: {FV.FYesNo(glassCov)}")
    print(f"Loaner Car Coverage: {FV.FYesNo(loanerCar)}")
    print()
    print(f"-----------------------------------------")
    print()
    print(f"Base Premium: {FV.FDollar2(basePremium)}")
    print(f"Extra Liability Cost: {FV.FDollar2(extraLiabCost)}")
    print(f"Glass Coverage Cost: {FV.FDollar2(glassCovCost)}")
    print(f"Loaner Car Coverage Cost: {FV.FDollar2(loanerCost)}")
    print(f"Total Extra Costs: {FV.FDollar2(extraCost)}")
    print()
    print(f"-----------------------------------------")
    print()
    print(f" Previous Claims:")
    print()
    print(f"  Claim #      Claim Date        Cost")
    print(f"-----------------------------------------")
    for i in range(len(claimNum)):
        print(f"  {claimNum[i]}       {claimDate[i]}      {FV.FDollar2(claimCost[i])}")
    print(f"-----------------------------------------")
    print()
    print(f"Subtotal: {FV.FDollar2(subTotal)}")
    print(f"Processing Fee: {FV.FDollar2(procFee)}")
    print(f"HST: {FV.FDollar2(hst)}")
    print(f"Total Cost: {FV.FDollar2(totalCost)}")
    print()
    print(f"-----------------------------------------")
    print(f"Payment Plan: {payPlan}")
    print(f"First Payment Date: {payDueDate}")
    print(f"Number of Payments: {numPayments}")
    while True:
        if payPlan == "Full":
            print(f"Payment Due: {FV.FDollar2(totalCost)}")
            break
        elif payPlan == "Monthly":
            print(f"Monthly Payment: {FV.FDollar2(monthlyPayment)}")
            break
        else:
            print(f"Down Payment: {FV.FDollar2(downPay)}")
            print(f"Monthly Payment: {FV.FDollar2(monthlyPayment)}")
            break
    print()
    print(f"--------------------------------------------------------------")
    print(f"      Thank you for choosing One Stop Insurance Company!")
    print()
    print()         

    f = open("policyinfo.dat", "a")
    f.write("{}, ".format(int(POL_NUM)))
    f.write("{}, ".format(fName))
    f.write("{}, ".format(lName))
    f.write("{}, ".format(address))
    f.write("{}, ".format(city))
    f.write("{}, ".format(province))
    f.write("{}, ".format(postalCode))
    f.write("{}, ".format(phoneNum))
    f.write("{}, ".format(numCars))
    f.write("{}, ".format(FV.FYesNo(extraLiab)))
    f.write("{}, ".format(FV.FYesNo(glassCov)))
    f.write("{}, ".format(FV.FYesNo(loanerCar)))
    f.write("{}, ".format(payPlan))
    f.write("{}\n".format(FV.FDollar2(totalCost)))
    f.close()

    f = open("claiminfo.dat", "a")

    for i in range(len(claimNum)):
        f.write(f"{claimNum[i]}, {claimDate[i]}, {FV.FDollar2(claimCost[i])}\n")
    f.close()

    print()
    print()
    totalIterations = 30 # The more iterations, the more time is takes.
    Message = "Saving Insurance Policy Data ..."
 
    for i in range(totalIterations + 1):
        time.sleep(0.1)
        progressBar(i, totalIterations, prefix=Message, suffix='Complete', length=50)
 
    print()
 
 
    print()
    print(f"Policy Number: {POL_NUM} has been saved successfully!")
    print()
    print()
    POL_NUM += 1

    while True:
        addPol = input("Would you like to create another policy? (Y/N): ").upper()

        if alphaResponse(addPol) == True:
            break
        else:
            print("Invalid input. Please enter either Y or N.")
    
        if addPol == "Y":
            break
        else:
            break

    if addPol == "N":
        break

# Any housekeeping duties at the end of the program
print("Have a great day!")
