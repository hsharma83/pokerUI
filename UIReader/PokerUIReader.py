'''
Created on 6 Mar 2016

@author: Behzad

1. Take a screenshot of poker table --DONE
<<<<<<< HEAD
2. We need to get coordinates or sub-windows and have them expressed as a percentage
    of the parent window dimensions.
=======
2. Write algorithm to 
>>>>>>> c7772c6d402c0cac9e5a0ee55e0b76bb175124b1
3 Read dealt hand
    a. Crop to hand position


4. Read current table cards
5. Identify when action needs to be taken.
6. Read chip balance
7. Write algorithm

Algorithm:
- Take picture of screen
- Assess game status
    a) Not started
    b) Hand dealt (no table cards)
    ...
- Action needed
    


'''
import win32gui
from win32gui import EnumWindows, SetActiveWindow, CreateHatchBrush
from win32gui import FindWindow
from test.test_logging import pywintypes
import win32ui
import win32con
import datetime
import time

def windowEnumerationHandler(hwnd, top_windows):
    if hwnd is not '':
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
        
def childWindowEnumerationHandler(hwnd, children):
    children.append((hwnd, win32gui.GetWindowText(hwnd)))

def findOpenPokerWindows():
    '''
Iterates through all open windows, fills an array with windows containing "No Limit Hold'em"
returns array containing (HWND, "string of window name") for each poker window
    '''
    openWindows = []
    pokerWindows = []
    win32gui.EnumWindows(windowEnumerationHandler, openWindows)
    
    for window in openWindows:
        if "No Limit Hold'em" in window[1]:
            pokerWindows.append(window)
    
    return pokerWindows

def getChildWindows(parentWindows):
    childWindows = []
    
    for windows in parentWindows:
        win32gui.EnumChildWindows(windows[0], windowEnumerationHandler, childWindows)
    
    return childWindows
    
def getWindowPosition(window):
    windowCoordinates = (win32gui.GetWindowRect(window))#Takes handle
    
    return windowCoordinates

def getClientDimensions(window):
    clientDimensions = win32gui.GetClientRect(window)#Takes handle
    return clientDimensions

def takePokerWindowScreenshot(window):
    windowHandle = window[0]
    windowName = window[1]
    
    wDC = win32gui.GetWindowDC(windowHandle)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dimensions = getClientDimensions(windowHandle)
    print(dimensions)
    width = dimensions[2]
    height = dimensions[3]

    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (width, height), dcObj, (0, 0), win32con.SRCCOPY)
    print(windowName)
    
    #Save file
    timeStamp = '{:%Y-%m-%d %H-%M-%S-%f}'.format(datetime.datetime.now())
    print(timeStamp)
    dataBitMap.SaveBitmapFile(cDC, "C:\\temp\\" + timeStamp +".bmp")
    #Freeing resources
    
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(windowHandle, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())


def getTableCardsBMP(window):
    '''
    Eventual aim is to return table cards for each window?
    or maybe return BMP and pass to another 
    1. Make BMP of picture cards
    2. Count number of cards
    3. 
    '''
    windowHandle = window[0]
    windowName = window[1]
    
    wDC = win32gui.GetWindowDC(windowHandle)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()
    dimensions = getClientDimensions(windowHandle)
    print(dimensions)
    pwWidth = dimensions[2]
    pwHeight = dimensions[3]
    
    allTableCardsBox = [int(0.33*pwWidth), int(0.388*pwHeight), int(0.38*pwWidth), int(0.085*pwHeight)] #All table cards
    firstTableCardBox = [int(0.344*pwWidth), int(0.388*pwHeight), int(0.021*pwWidth), int(0.065*pwHeight)]
    secondTableCardBox = [int(0.412*pwWidth), int(0.388*pwHeight), int(0.021*pwWidth), int(0.065*pwHeight)]
    thirdTableCardBox = [int(0.480*pwWidth), int(0.388*pwHeight), int(0.021*pwWidth), int(0.065*pwHeight)]
    fourthTableCardBox = [int(0.549*pwWidth), int(0.388*pwHeight), int(0.021*pwWidth), int(0.065*pwHeight)]
    fithTableCardBox = [int(0.617*pwWidth), int(0.388*pwHeight), int(0.021*pwWidth), int(0.065*pwHeight)]

    tableCardDimensionsArray = []
    tableCardDimensionsArray.append(firstTableCardBox)
    tableCardDimensionsArray.append(secondTableCardBox)
    tableCardDimensionsArray.append(thirdTableCardBox)
    tableCardDimensionsArray.append(fourthTableCardBox)
    tableCardDimensionsArray.append(fithTableCardBox)
    
    tableCardsBMPArray = []
    
    for tableCard in tableCardDimensionsArray:
        
        print(tableCard)
        width = tableCard[2]
        height = tableCard[3]
        
        dataBitMap = win32ui.CreateBitmap()
        dataBitMap.CreateCompatibleBitmap(dcObj, width, height)
        cDC.SelectObject(dataBitMap)
        cDC.BitBlt((0, 0), (width, height), dcObj, (tableCard[0], tableCard[1]), win32con.SRCCOPY)
        print(windowName)
        
        #Save file
        timeStamp = '{:%Y-%m-%d %H-%M-%S-%f}'.format(datetime.datetime.now())
        print(timeStamp)
        dataBitMap.SaveBitmapFile(cDC, "C:\\temp\\" + timeStamp +".bmp")
        
        tableCardsBMPArray.append(dataBitMap)
        
        
    #Freeing resources
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(windowHandle, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
        
        
    
    return tableCardsBMPArray

if __name__ == '__main__':
    pokerWindows = findOpenPokerWindows()
    childWindows=[]
    coordinates = []
    
    print(257/766)
    print(201/518)
    print(" ")
    print(268/766)
    print(40/518)
    
    print(260/766, 205/518, 14/766, 32/518)
    print(314/766, 205/518, 14, 32)
    print(368/766, 205/518, 14, 32)
    print(422/766, 205/518, 14, 32)
    print(476/766, 205/518, 14, 32)


    childWindows = getChildWindows(pokerWindows)
    
    for window in pokerWindows:
        takePokerWindowScreenshot(window)
        tableCardsBMP = getTableCardsBMP(window)

 
    '''
    for window in childWindows:
        coordinates = (win32gui.GetClientRect(window[0]))
        DC = win32gui.GetDC(window[0])
        win32gui.DrawEdge(DC, coordinates, 10, 10)
        print(coordinates)
        #win32gui.DrawFocusRect(DC, coordinates)
'''
    
'''

    a = FindWindow(None, "PyDev - PokerUI_reader/src/UIReader/PokerUIReader.py - Eclipse")
    
    win32gui.EnumWindows(windowEnumerationHandler, openWindows)
    for window in openWindows:
        coordinates = (win32gui.GetClientRect(window[0]))
        DC = win32gui.GetDC(window[0])
        win32gui.DrawFocusRect(DC, coordinates)
        
'''        