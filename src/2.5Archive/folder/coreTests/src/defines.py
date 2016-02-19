'''
$Id: defines.py 13 2013-02-14 12:59:58Z vultuste $
Created on 10.5.2012

@author: vultuste
'''
global currentTestCaseObject
currentTestCaseObject = None


def getUnittestObj():
    global currentTestCaseObject
    return currentTestCaseObject


def setUnittestObj(testingObj):
    global currentTestCaseObject
    currentTestCaseObject = testingObj

if __name__ == "__main__":
    print getUnittestObj()
