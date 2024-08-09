# Programmer: [Darcy Ostrander]
# Course: CS701/GB-731, Dr. Yalew
# Date: [8/9/2024]
# Programming Assignment: 4
# Program Inputs: A positive integer < 1000
# Program Outputs: The English name of the integer


def main():
    num = int(input("Please enter an integer < 1000: "))
    while num > 1000 or num < 0:
        num = int(input("Please enter an integer < 1000: "))
    print(intName(num))

## Turns a number into its English name.
#  @param number a positive integer < 1,000
#  @return the name of the number (e.g. "two hundred seventy four")
#
def intName(x):
     if x > 100:
        return hundredsName(x)
     elif x >= 20 and x <= 99:
         return tensName(x)
     elif x >= 10 and x <= 19:
         return teenName(x)
     else:
         return digitName(x)
     

## Turns a digit into its English name.
#  @param digit an integer between 1 and 9
#  @return the name of digit ("one" ... "nine")
#
def digitName(x):
    if x == 1:
        return "one"
    elif x == 2:
        return "two"
    elif x == 3:
        return "three"
    elif x == 4:
        return "four"
    elif x == 5:
        return "five"
    elif x == 6:
        return "six"
    elif x == 7:
        return "seven"
    elif x == 8:
        return "eight"
    elif x == 9:
        return "nine"
    
## Turns a number between 10 and 19 into its English name.
#  @param number an integer between 10 and 19
#  @return the name of the given number ("ten" ... "nineteen")
#
def teenName(x):
    if x == 10:
        return "ten"
    elif x == 11:
       return "eleven"
    elif x == 12:
       return "twelve"
    elif x == 13:
       return "thirteen"
    else:
        return digitName(x - 10) + "teen"

## Gives the name of the tens part of a number between 20 and 99.
#  @param number an integer between 20 and 99
#  @return the name of the tens part of the number ("twenty" ... "ninety")
#

def tensName(x):
  if x >= 20 and x <= 29:
    return "twenty " + digitName(x-20)
  if x >= 30 and x <= 39:
    return "thirty " + digitName(x-30)
  if x >= 40 and x <= 49:
    return "forty " + digitName(x-40)
  if x >= 50 and x <= 59:
    return "fifty " + digitName(x-50)
  if x >= 60 and x <= 69:
    return "sixty " + digitName(x-60)
  if x >= 70 and x <= 79:
    return "seventy " + digitName(x-70)
  if x >= 80 and x <= 89:
    return "eighty " + digitName(x-80)
  if x >= 90 and x <= 99:
    return "ninety " + digitName(x-90)


## Gives the name of the hundreds part of a number between 100 and 999.
#  @param number an integer between 100 and 999
#  @return the name of the hundreds part of the number

def hundredsName(x):
   #100s
   if x >= 100 and x <= 109:
      return "one hundred " + digitName(x-100)
   elif x >=110 and x <= 119:
      return "one hundred " + teenName(x-100)
   elif x >= 120 and x <= 199:
      return "one hundred " + tensName(x-100)
   #200s
   if x >= 200 and x <= 209:
      return "two hundred " + digitName(x-200)
   elif x >=210 and x <= 219:
      return "two hundred " + teenName(x-200)
   elif x >= 220 and x <= 299:
      return "two hundred " + tensName(x-200)
   #300s
   if x >= 300 and x <= 309:
      return "three hundred " + digitName(x-300)
   elif x >=310 and x <= 319:
      return "three hundred " + teenName(x-300)
   elif x >= 320 and x <= 399:
      return "three hundred " + tensName(x-300)
   #400s
   if x >= 400 and x <= 409:
      return "four hundred " + digitName(x-400)
   elif x >=410 and x <= 419:
      return "four hundred " + teenName(x-400)
   elif x >= 420 and x <= 499:
      return "four hundred " + tensName(x-400)
   #500s
   if x >= 500 and x <= 509:
      return "five hundred " + digitName(x-500)
   elif x >=510 and x <= 519:
      return "five hundred " + teenName(x-500)
   elif x >= 520 and x <= 599:
      return "five hundred " + tensName(x-500)
   #600s
   if x >= 600 and x <= 609:
      return "six hundred " + digitName(x-600)
   elif x >=610 and x <= 619:
      return "six hundred " + teenName(x-600)
   elif x >= 620 and x <= 699:
      return "six hundred " + tensName(x-600)
   #700s
   if x >= 700 and x <= 709:
      return "seven hundred " + digitName(x-700)
   elif x >=710 and x <= 719:
      return "seven hundred " + teenName(x-700)
   elif x >= 720 and x <= 799:
      return "seven hundred " + tensName(x-700)
   #800s
   if x >= 800 and x <= 809:
      return "eight hundred " + digitName(x-800)
   elif x >=810 and x <= 819:
      return "eight hundred " + teenName(x-800)
   elif x >= 820 and x <= 899:
      return "eight hundred " + tensName(x-800)
   #900s
   if x >= 900 and x <= 909:
      return "nine hundred " + digitName(x-900)
   elif x >=910 and x <= 919:
      return "nine hundred " + teenName(x-900)
   elif x >= 920 and x <= 999:
      return "nine hundred " + tensName(x-900)
   
# Start the program.
if __name__ == "__main__":
    main()
