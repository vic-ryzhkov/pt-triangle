from random import randint
from random import uniform as randfloat
import sys,re

symbols_list = ['!','@','#','$','%','^','*','(',')','-','_','+','=','~','`',';',':','"','?','<','>','.',',','&']

lower_int_bound = 1 
upper_int_bound = sys.maxint

lower_float_bound = 1.0
upper_float_bound = sys.float_info.max/10.0

lower_long_bound = sys.maxint + 1
upper_long_bound = (1<<10) * lower_long_bound

def getFloat(low = lower_float_bound, up = upper_float_bound):
    return randfloat(low, up)

def getInt(low = lower_int_bound, up = upper_int_bound):
    return randint(low, up)

def getLong(low = lower_long_bound, up = upper_long_bound):
    return randint(low,up)

def getRandSymb():
    return symbols_list[randint(0, len(symbols_list) - 1)]

def toStr(a,b,c):
    return '['  + str(a) + ',' + str(b) + ',' + str(c) + ']'


def printRandom(a,b,c):
    order = randint(0,5)
    if order == 0:
        result = toStr(a,b,c)
    elif order == 1:
        result = toStr(a,c,b)
    elif order == 2:
        result = toStr(c,a,b)
    elif order == 3:
        result = toStr(c,b,a)
    elif order == 4: 
        result = toStr(b,c,a)
    elif order == 5:
        result = toStr(b,a,c)
    
    return result

def getNotTriangle(error_type):
    a = getInt(low = lower_int_bound + 3, up = upper_int_bound/2 - 1)
    b = getInt(up = a - 1)
    if error_type == 'specSymbol':
        c = getRandSymb()
    elif error_type == 'zeroNumber':
        c = 0    
    elif error_type == 'negativeNumber':
        c = -getInt()
    elif error_type == 'triangleInequalityTrouble':
        c = getInt(low = a + b + 1)
    return printRandom(a, b, c)


def getEquilateral(leg_type):
    if leg_type == 'int':
        a = getInt()
        b = c = a
    elif leg_type == 'float':
        a = getFloat()
        b = c = a
    elif leg_type == 'long':
        a = getLong()
        b = c = a
    elif leg_type == 'intfloat':
        a = getInt()
        b = a
        c = float(b)
    elif leg_type == 'floatlong':
        a = getFloat()
        b = a
        c = long(b)
    return toStr(a,b,c)
    

def getIsosceles(leg_type):
    if leg_type == 'int':
        a = getInt(low = lower_int_bound + 2)
        b = c = a
        while c == a or c == b:
            c = getInt(up = a + b - 1)
    elif leg_type == 'float':
        a = getFloat(low = lower_float_bound + 2.0)
        b = c = a
        while c == a or c == b:
            c = getFloat(up = a + b - 1.0)       
    elif leg_type == 'long':
        a = getLong(low = lower_long_bound + 2)
        b = c = a
        while c == a or c == b:
            c = getLong(up = a + b - 1)
    elif leg_type == 'intfloat':
        a = getInt()
        b = c = a
        while c == a or c == b:
            c = getFloat(up = a + b - 1)      
    elif leg_type == 'intlong':
        a = getInt(low = lower_long_bound - 100000)
        b = c = a
        while c == a or c == b:
            c = getLong(up = a + b - 1)
    elif leg_type =='floatlong':
        a = getFloat(low = lower_long_bound - 100000)
        b = c = a
        while c == a or c == b:
            c = getLong(up = a + b - 1)        
    return printRandom(a,b,c)
        

def getVarious(leg_type):
    if leg_type == 'int':
        a = getInt(low = lower_int_bound + 5)
        b = getInt(low = lower_int_bound + 3, up = a - 1)
        c = b
        while c == a or c == b:
            c = getInt(low = a - b + 1, up = a + b - 1)
    elif leg_type == 'float':
        a = getFloat(low = lower_float_bound + 5.0)
        b = getFloat(low = lower_float_bound + 3.0, up = a - 1.0)
        c = b
        while c == a or c == b:
            c = getFloat(low = a - b + 1.0, up = a + b - 1.0)      
    elif leg_type == 'long':
        a = getLong(low = lower_long_bound + 5)
        b = getLong(low = lower_long_bound + 3, up = a - 1)
        c = b
        while c == a or c == b:
            c = getLong(a - b + 1, a + b - 1)
    elif leg_type == 'intfloat':
        a = getInt(low = lower_int_bound + 5)
        b = getFloat(low = lower_float_bound + 3.0, up = a - 1.0)
        c = b
        while c == a or c == b:
            c = getInt(int(a - b + 1), int(a + b - 1))         
    elif leg_type == 'intlong':
        a = getInt(low = lower_long_bound - 99998)
        b = getInt(low = lower_long_bound - 100000, up = a - 1.0)
        c = b
        while c == a or c == b:
            c = getLong(low = a - b + 1, up = a + b - 1)
    elif leg_type =='floatlong':
        a = getFloat(low = lower_long_bound + 5)
        b = getLong(low = lower_long_bound + 3, up = a - 1.0)
        c = b
        while c == a or c == b:
            c = getLong(low = int(a - b + 1), up = (a + b - 1)) 
    return printRandom(a, b, c)

def getInput(TEST_TYPE, triangle_type ,data_type, data_value):
    if TEST_TYPE == 'static':
        return re.compile('\'| ').sub('',str(data_value))
    elif TEST_TYPE == 'dynamic':
        getMethod = globals()['get' + triangle_type]
        return getMethod(data_type)
    