import PIL.ImageGrab
import math

def color(x,y):
	rgb = PIL.ImageGrab.grab().load()[x,y] #imagegrab is a class and grab is a function in that class
	return rgb
no=[(205,193,180),(238,228,218),(237,224,200),(242,177,121)
,(245,149,99),(246,124,95)
,(246,94,59)
,(237,207,114)
,(237,204,97)
,(237,200,80)
,(237,197,63)
,(237,194,46)]



matrix=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
def mat():

	for m in range(0,12):
		if color(691,307)==no[m]:
			matrix[0][0]=int(math.pow(2,m))
		if color(839,307)==no[m]:
			matrix[0][1]=int(math.pow(2,m))
		if color(966,307)==no[m]:
			matrix[0][2]=int(math.pow(2,m))
		if color(1100,307)==no[m]:
			matrix[0][3]=int(math.pow(2,m))	
		if color(691,443)==no[m]:
			matrix[1][0]=int(math.pow(2,m))
		if color(827,443)==no[m]:
			matrix[1][1]=int(math.pow(2,m))
		if color(964,443)==no[m]:
			matrix[1][2]=int(math.pow(2,m))
		if color(1100,443)==no[m]:
			matrix[1][3]=int(math.pow(2,m))
		if color(691,583)==no[m]:
			matrix[2][0]=int(math.pow(2,m))
		if color(827,583)==no[m]:
			matrix[2][1]=int(math.pow(2,m))
		if color(964,583)==no[m]:
			matrix[2][2]=int(math.pow(2,m))
		if color(1100,583)==no[m]:
			matrix[2][3]=int(math.pow(2,m))
		if color(691,712)==no[m]:
			matrix[3][0]=int(math.pow(2,m))
		if color(827,712)==no[m]:
			matrix[3][1]=int(math.pow(2,m))
		if color(964,712)==no[m]:
			matrix[3][2]=int(math.pow(2,m))
		if color(1100,712)==no[m]:
			matrix[3][3]=int(math.pow(2,m))										

mat()
matup=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
matdown=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
matleft=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
matright=[[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1],[-1,-1,-1,-1]]
def matrup():
	for i in range (0,4):
		for j in range (0,4):
			matup[i][j]=matrix[i][j]

def matrdown():
	for i in range (0,4):
		for j in range (0,4):
			matdown[i][j]=matrix[i][j]
def matrright():			
	for i in range (0,4):
		for j in range (0,4):
			matright[i][j]=matrix[i][j]
def matrleft():			
	for i in range (0,4):
		for j in range (0,4):
			matleft[i][j]=matrix[i][j]



def left():
	
	for i in range (0,4):
		for j in range (1,4):
			if(matleft[i][j]!=1):
				k=j-1
				while(matleft[i][k]==1 and k>0):
					k=k-1
				if(matleft[i][k]==1):
					matleft[i][k]=matleft[i][j]
					matleft[i][j]=1
				elif(matleft[i][k]==matleft[i][j]):
					matleft[i][k]=matleft[i][k]*2
					matleft[i][j]=1
				else:
					matleft[i][k+1]=matleft[i][j]
					if(k+1!=j):
						matleft[i][j]=1
	return matleft				
def right():
	
	for i in range (0,4):
		for j in range (2,-1,-1):
			if(matright[i][j]!=1):
				k=j+1
				while(matright[i][k]==1 and k<3):
					k=k+1
				if(matright[i][k]==1):
					matright[i][k]=matright[i][j]
					matright[i][j]=1
				elif(matright[i][k]==matright[i][j]):
					matright[i][k]=matright[i][k]*2
					matright[i][j]=1
				else:
					matright[i][k-1]=matright[i][j]
					if(k-1!=j):
						matright[i][j]=1  				
def up():
	
	for i in range (0,4):
		for j in range (1,4):
			if(matup[j][i]!=1):
				k=j-1
				while(matup[k][i]==1 and k>0):
					k=k-1
				if(matup[k][i]==1):
					matup[k][i]=matup[j][i]
					matup[j][i]=1
				elif(matup[k][i]==matup[j][i]):
					matup[k][i]=matup[k][i]*2
					matup[j][i]=1
				else:
					matup[k+1][i]=matup[j][i]
					if(k+1!=j):
						matup[j][i]=1
def down():
	
	for i in range (0,4):
		for j in range (2,-1,-1):
			if(matdown[j][i]!=1):
				k=j+1
				while(matdown[k][i]==1 and k<3):
					k=k+1
				if(matdown[k][i]==1):
					matdown[k][i]=matdown[j][i]
					matdown[j][i]=1
				elif(matdown[k][i]==matdown[j][i]):
					matdown[k][i]=matdown[k][i]*2
					matdown[j][i]=1
				else:
					matdown[k-1][i]=matdown[j][i]
					if(k-1!=j):
						matdown[j][i]=1


import ctypes
from ctypes import wintypes
import time

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_TAB  = 0x09
VK_MENU = 0x12
VK_LEFT = 0x25
VK_RIGHT = 0x27
VK_UP = 0x26
VK_DOWN = 0x28

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
    _fields_ = (("dx",          wintypes.LONG),
                ("dy",          wintypes.LONG),
                ("mouseData",   wintypes.DWORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

class KEYBDINPUT(ctypes.Structure):
    _fields_ = (("wVk",         wintypes.WORD),
                ("wScan",       wintypes.WORD),
                ("dwFlags",     wintypes.DWORD),
                ("time",        wintypes.DWORD),
                ("dwExtraInfo", wintypes.ULONG_PTR))

    def __init__(self, *args, **kwds):
        super(KEYBDINPUT, self).__init__(*args, **kwds)
        # some programs use the scan code even if KEYEVENTF_SCANCODE
        # isn't set in dwFflags, so attempt to map the correct code.
        if not self.dwFlags & KEYEVENTF_UNICODE:
            self.wScan = user32.MapVirtualKeyExW(self.wVk,
                                                 MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
    _fields_ = (("uMsg",    wintypes.DWORD),
                ("wParamL", wintypes.WORD),
                ("wParamH", wintypes.WORD))

class INPUT(ctypes.Structure):
    class _INPUT(ctypes.Union):
        _fields_ = (("ki", KEYBDINPUT),
                    ("mi", MOUSEINPUT),
                    ("hi", HARDWAREINPUT))
    _anonymous_ = ("_input",)
    _fields_ = (("type",   wintypes.DWORD),
                ("_input", _INPUT))

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
    if result == 0:
        raise ctypes.WinError(ctypes.get_last_error())
    return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
                             LPINPUT,       # pInputs
                             ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    x = INPUT(type=INPUT_KEYBOARD,
              ki=KEYBDINPUT(wVk=hexKeyCode,
                            dwFlags=KEYEVENTF_KEYUP))
    user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))
def checkempty(m):
	count=0
	for i in range(0,4):
		for j in range (0,4):
			if m[i][j]==1:
				count=count+1
	return count	
def total(m):
	total=0
	for i in range(0,4):
		for j in range (0,4):
			total=total+m[i][j]
	return total		
def checkdes(m):
	count=0
	for i in range(0,3):
		if m[0][i]>=m[0][i+1]:
			count=count+1 ## continue from here
	return count
def checkrow(m):
	count=0
	for i in range(0,3):
		if m[0][i]!=1:
			count=count+1
	return count
def checkcolumn(m):
	count=0
	for i in range(0,3):
		if m[i][0]!=1:
			count=count+1
	return count			


def heuristic():
	left()
	up()
	right()
	down()
	if(matleft==matrix and matup==matrix): #no moves available
		g=checkrow(matrix)
		h=checkcolumn(matrix)
		if(g==4):
			return "VK_RIGHT"
		elif(h==4):
			return "VK_DOWN"	
		elif(g<h):
			return "down"
		elif(g>h):
			return "right"


	

	else:   #moves available
		a=checkempty(matleft)
		b=checkempty(matup)
		c=total(matleft)
		d=total(matup)
		if(a>b):
			return "VK_LEFT"
		elif(b>a):
			return "VK_UP"
		elif(a==b):
			if(c>d):
				return "VK_LEFT"
			elif(c<d):
				return "VK_UP"
		e=checkdes(matleft)
		f=checkdes(matup)
		if(e>f):
			return "VK_LEFT"
		elif(f>e):
			return "VK_UP"
			
		'''if(e==f):
			if(matup==matrix):
				return "VK_LEFT"
			if(matleft[3][0]==1 or matup[3][0]==1):
				return "VK_LEFT"
			if(matleft[0][3]==1 or matup[0][3]==1):
				return "VK_UP"
			else:
				return "VK_UP"	'''	
		if(matup==matrix):
			return "VK_LEFT"
		else:
			return "VK_UP"	    

def AltTab():
	PressKey(VK_UP)
    
	ReleaseKey(VK_UP)
	PressKey(VK_LEFT)
	ReleaseKey(VK_LEFT)
	while(1):
		a=heuristic()
		if a=="VK_LEFT":
			PressKey(VK_LEFT)
			ReleaseKey(VK_LEFT)
		elif a=="VK_RIGHT":

			PressKey(VK_RIGHT)
			ReleaseKey(VK_RIGHT)
			mat()
			if(matrix[1][0]==1):
				PressKey(VK_LEFT)
				ReleaseKey(VK_LEFT)
		elif a=="VK_DOWN":
			PressKey(VK_DOWN)
			ReleaseKey(VK_DOWN)
			mat()
			if(matrix[0][1]==1):
				PressKey(VK_UP)
				ReleaseKey(VK_UP)

		elif a=="right":
			PressKey(VK_RIGHT)
			ReleaseKey(VK_RIGHT)
			mat()
			if(matrix[0][0]==1):
				PressKey(VK_LEFT)
				ReleaseKey(VK_LEFT)
					
		elif a=="down":
			PressKey(VK_DOWN)
			ReleaseKey(VK_DOWN)
			mat()
			if(matrix[0][0]==1):
				PressKey(VK_UP)
				ReleaseKey(VK_UP)		

		elif a=="VK_UP":
			PressKey(VK_UP)
			ReleaseKey(VK_UP)
		else:
			PressKey(VK_RIGHT)
			ReleaseKey(VK_RIGHT)
		mat()
		matrdown()
		matrleft()
		matrright()
		matrup()
      
    
        
if __name__ == "__main__":
	AltTab()


		

					
				


