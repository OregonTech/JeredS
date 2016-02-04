from datetime import datetime
from math import pi, e, sqrt, factorial, fabs
from decimal import getcontext, Decimal
import getpass


"GET TIME AND DATE"
def dateTime():
    return datetime.now().strftime('%m: %d: %y: %H:%M:%S')


"FIBONACCI: Assumes starting with 1"
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)


"NTH DIGIT OF PI-(precision is 48 places to the right of the decimal)"
def piN(n):
    if n == 1:
        return '3'
    elif n == 0:
        return "invalid"
    else:
        npi = str(Decimal(pi))
        return npi[int(n)]


"OPEN THE DOOR HAL-(should be portable to UNIX and WIN"
def openDoor():
    return str('I\'m afraid I can\'t do that ' + getpass.getuser())


"CONVERT METRIC"
def convertMetric(myNum, myUnit, convertTo):

    "local variables to store starting and convert to units"
    pow1 = 0
    pow2 = 0

    "dictionary stores keyword and value for metric units"
    unitDict = {'tera': 6,
                'giga': 5,
                'mega': 4,
                'kilo': 3,
                'hecto': 2,
                'deka': 1,
                'noConvert': 0,
                'deci': -1,
                'centi': -2,
                'milli': -3,
                'micro': -4,
                'nano': -5,
                'pico': -6}

    "starting unit power conversion"
    for myKey in unitDict.iterkeys():
        if myKey == myUnit:
            pow1 = unitDict.get(myUnit)
            break
    "unit power to convert to"
    for myKey in unitDict.iterkeys():
        if myKey == convertTo:
            pow2 = unitDict.get(convertTo)
            break

    "power difference"
    powDif = pow1-pow2
    powPow = 10 ** powDif

    return str(myNum * powPow) + " " + convertTo


"PRINT UNITS ONE CAN CONVERT BETWEEN"
def convertTenUnits():
    return "tera: 6, giga: 5, mega: 4,"\
           "kilo: 3, hecto: 2,deka: 1,"\
           "noConvert: 0, deci: -1, centi: -2,"\
           "milli: -3, micro: -4, nano: -5, pico: -6"


"FAVORITE NUMBER"
def favNum(yourNum):
    "my favorite number"
    myNum = 13.0

    "check your number and my number for match"
    if float(yourNum) != myNum:  # no match
        return 'My number ' + str(myNum) + ' is better than your number!'
    else:  # match
        return 'Hey we are favorite number ' + str(myNum) + ' buddies!'


"COLOR MIXER"
def mixColor(color1, color2):
    "match color"
    if (color1 == 'red' and color2 == 'blue') or (color1 == 'blue' and color2 == 'red'):
        return 'purple'
    elif (color1 == 'red' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'red'):
        return 'orange'
    elif (color1 == 'blue' and color2 == 'yellow') or (color1 == 'yellow' and color2 == 'blue'):
        return 'green'
    elif (color1 == 'red' and color2 == 'red'):
        return 'red'
    elif (color1 == 'blue' and color2 == 'blue'):
        return 'blue'
    elif (color1 == 'yellow' and color2 == 'yellow'):
        return 'yellow'


"PRINT COLOR FOR MIXER"
def colorPrint():
    return 'Red, Yellow, and Blue are the color that can be mixed'


"NTH DIGIT OF e-(precision is 48 places to the right of the decimal)"
def eN(n):
    if n == 1:  # n is left of decimal
        return '2'
    elif n == 0:  # n is invalid
        return "invalid"
    else:  # n is valid: find number
        ne = str(Decimal(e))
        return ne[int(n)]

"SQUARE ROOT OF N"
def sqrtN(n):
    return str(sqrt(n))

"N FACTORIAL"
def factN(n):
    return str(factorial(n))

"JOKE OF THE DAY"
def joke():
    return 'beer'

"ABSOLUTE VALUE"
def absN(n):
    return str(fabs(n))

"HYPOTENUSE"
def hypotXY(myX, myY):
    p = pow(myX, 2) + pow(myY, 2)
    return str(sqrt(p))

"ANOTHER STORY"
def mayIHaveAnother():
    return 'Uuum no...'


