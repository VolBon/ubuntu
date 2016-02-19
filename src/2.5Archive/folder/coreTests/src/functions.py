'''
$Id: functions.py 43 2013-07-27 05:55:51Z vultuste $
Created on 7.5.2012

@author: vultuste
'''

import os
import time

import tai
from taCore.definitions import TestCaseDataDefinitionError

from defines import getUnittestObj

""" next function just for helping with code completion
def getUnittestObj():
    import unittest
    return unittest.TestCase
"""

"""
try:
    eval("tai")
except:
    crtFolder = os.path.dirname(os.path.abspath(__file__))
    tai_path = os.path.abspath(os.path.join(crtFolder,'..'))
    sys.path.append(tai_path)
    import tai
    sys.path.remove(tai_path)
"""


def storageStore(key, val, lifeTime):
    """ store object into appropriate storage """
    tai.storeObject(key, val, lifeTime)


def storageCheck(key, lifeTime, expected, clean=False):
    """ check that object is found from the appropriate storage """
    actual = tai.getStoredObject(key, lifeTime)
    global currentTestCaseObject
    getUnittestObj().assertEqual(actual, expected,
                                 "key '%s' has unexpected value: '%s', expected '%s'" % (key, str(actual), str(expected)))


def storageRemove(key, lifeTime):
    """ remove object from the appropriate storage """
    tai.removeStoredObject(key, lifeTime)


def storageCheckNonExistingKey():
    """ check situations when existing key is asked or removed """
    rightNow = time.time()
    uniqueKey = "key_time_%f" % rightNow

    global currentTestCaseObject

    for lifeTime in tai.LIFETIME.getAllAsList():
        if lifeTime in [tai.LIFETIME.END_OF_FUNCTION, tai.LIFETIME.PERSISTENT]:
            continue  # no need to check for these
        actual = tai.getStoredObject(uniqueKey, lifeTime, rightNow)
        getUnittestObj().assertEqual(actual, rightNow, "key '%s' has unexpected value: '%s', expected '%s'" %
                                     (uniqueKey, str(actual), str(rightNow)))

        tai.removeStoredObject(uniqueKey, lifeTime, False)

        # call tai.getStoredObject(uniqueKey, lifeTime, rightNow, True) and
        # expect KeyError exception:
        getUnittestObj().assertRaises(
            KeyError, tai.getStoredObject, uniqueKey, lifeTime, rightNow, True)
        getUnittestObj().assertRaises(
            KeyError, tai.removeStoredObject, uniqueKey, lifeTime, True)


def checkLoopsUsingCounter(maxCounter, index):

    expectedIndex = tai.getStoredObject(
        "checkLoopsUsingCounter", defaultValue=0)
    getUnittestObj().assertEqual(index, expectedIndex,
                                 "index parameter has unexpected value: %s, expected %s" % (str(index), str(expectedIndex)))

    indexFromAPI = tai.getBlockIterationIndex()
    getUnittestObj().assertEqual(indexFromAPI, expectedIndex,
                                 "tai.getBlockExecutionIndex() returned unexpected value: %s, expected %s" % (str(indexFromAPI), str(expectedIndex)))

    expectedIndex = expectedIndex + 1
    if expectedIndex == maxCounter:
        tai.removeStoredObject("checkLoopsUsingCounter")
    else:
        tai.storeObject("checkLoopsUsingCounter", expectedIndex)


def checkLoopsUsingIterator(loopList, index, elem):

    expectedIndex = tai.getStoredObject(
        "checkLoopsUsingIterator", defaultValue=0)
    getUnittestObj().assertEqual(index, expectedIndex,
                                 "index parameter has unexpected value: %s, expected %s" % (str(index), str(expectedIndex)))
    getUnittestObj().assertEqual(elem, loopList[
        index], "iterated element has unexpected value: '%s', expected '%s'" % (str(elem), str(loopList[index])))

    indexFromAPI = tai.getBlockIterationIndex()
    iterObjFromAPI = tai.getBlockIterationObject()
    getUnittestObj().assertEqual(indexFromAPI, expectedIndex,
                                 "tai.getBlockExecutionIndex() returned unexpected value: %s, expected %s" % (str(indexFromAPI), str(expectedIndex)))
    getUnittestObj().assertEqual(iterObjFromAPI, elem,
                                 "tai.getBlockIterationObject() returned unexpected value: '%s', expected '%s'" % (str(iterObjFromAPI), str(elem)))

    expectedIndex = expectedIndex + 1
    if expectedIndex == len(loopList):
        tai.removeStoredObject("checkLoopsUsingIterator")
    else:
        tai.storeObject("checkLoopsUsingIterator", expectedIndex)


def registerAutomaticCall(funcCall, args, when):
    tai.registerAutomaticFunctionCall(funcCall, args, when)


def deleteStoredObject(key, lifeTime):
    tai.removeStoredObject(key, lifeTime)


def check_tai_clearStoredObjects(lifetime=tai.LIFETIME.END_OF_TESTCASE):
    tai.clearStoredObjects(lifetime)


def check_tai_pause():
    tai.pause('Short pause', 'Testing', 0.01, False)


def check_tai_registerAutomaticFunctionCall(txt, when):
    tai.registerAutomaticFunctionCall(
        "taUnitTests.functions.callbackForAutomaticCall", [txt], tai.LIFETIME.END_OF_TESTCASE)


def callbackForAutomaticCall(txt):
    tai.write("callback function called, reference '%s'" %
              txt, tai.NOTIFICATION_LEVEL.HIGH)


def check_tai_getExceptionDesc():
    try:
        raise tai.TcError("nothing wrong, testing exception")
    except tai.TcError, err:
        txt = tai.getExceptionDesc(err)

    getUnittestObj().assertGreater(len(txt), 0)


def check_tai_write():
    tai.write('tai.NOTIFICATION_LEVEL.PROGRESS',
              tai.NOTIFICATION_LEVEL.PROGRESS)
    tai.write('tai.NOTIFICATION_LEVEL.DEBUG_DETAIL',
              tai.NOTIFICATION_LEVEL.DEBUG_DETAIL)
    tai.write('tai.NOTIFICATION_LEVEL.DEBUG', tai.NOTIFICATION_LEVEL.DEBUG)
    tai.write('tai.NOTIFICATION_LEVEL.LOW', tai.NOTIFICATION_LEVEL.LOW)
    tai.write('tai.NOTIFICATION_LEVEL.NORMAL', tai.NOTIFICATION_LEVEL.NORMAL)
    tai.write('tai.NOTIFICATION_LEVEL.HIGH', tai.NOTIFICATION_LEVEL.HIGH)
    tai.write('tai.NOTIFICATION_LEVEL.WARNING', tai.NOTIFICATION_LEVEL.WARNING)
    tai.write('tai.NOTIFICATION_LEVEL.ERROR', tai.NOTIFICATION_LEVEL.ERROR)


def check_tai_getExecutionLogFolder():
    txt = tai.getExecutionLogFolder()
    endTxt = "taUnitTestCases\\tc3_various_tai_functions\\Runs\\".replace(
        '\\', os.sep).replace('/', os.sep)
    ok = txt[:len(txt) - 17].endswith(endTxt)
    getUnittestObj().assertEqual(ok, True,
                                 "tai.getExecutionLogFolder() does not contain expect string '%s'" % endTxt)


def check_tai_getExecutionDataFolder():
    txt = tai.getExecutionDataFolder()
    getUnittestObj().assertEqual(txt, os.path.join(tai.getExecutionLogFolder(),
                                                   'Data'), "tai.getExecutionDataFolder() does not contain expect path")


def varCheck(varName, varParam, valParam):
    """ check that variables defined in test case are correctly passed """
    global currentTestCaseObject
    getUnittestObj().assertEqual(varParam, valParam,
                                 "variable '%s' has unexpected value: '%s', expected '%s'" % (varName, str(varParam), str(valParam)))


def envVarCheck(varName, varParam, envParam):
    """ check that variables defined in test case are correctly passed """
    global currentTestCaseObject

    """ first evaluate the env variable """
    envParamDef = envParam
    amountOfPercentageSign = envParamDef.count("%")
    for pairsCount in range(amountOfPercentageSign / 2):
        envParamDef = envParamDef.replace("%", "${", 1).replace("%", "}", 1)
    del pairsCount

    valParam = os.path.expandvars(envParamDef)

    """ now compare env param result valParam against the value from test case' vars.<variable> """

    getUnittestObj().assertEqual(varParam, valParam,
                                 "variable '%s' has unexpected value: '%s', expected '%s'" % (varName, str(varParam), str(valParam)))
    getUnittestObj().assertNotEqual(
        envParam, valParam, "environment variable not defined: '%s'" % (str(envParam)))


def raiseError(errTxt):
    tai.write("Function: raiseError will raise an exception")
    raise tai.TcError(errTxt)


def dataCheckValue(varName, varValue, expectedValue):
    """ check that variables defined in data are are correctly passed to test case functions """
    global currentTestCaseObject
    getUnittestObj().assertEqual(varValue, expectedValue, "variable '%s' has unexpected value: %s, expected %s" %
                                 (varName, repr(varValue), repr(expectedValue)))


def dataCheckFieldExists(varName, varValue, expectedFieldToExist):
    """ check that variables defined in data are are correctly passed to test case functions """
    global currentTestCaseObject

    if not hasattr(varValue, expectedFieldToExist):
        getUnittestObj().fail("variable '%s' does not have expected field '%s'" %
                              (varName, expectedFieldToExist))


def compareValues(v1, v2):
    """ check that variables defined in data are are correctly passed to test case functions """
    global currentTestCaseObject
    getUnittestObj().assertEqual(
        v1, v2, "variables not equal: %s and %s" % (str(v1), str(v2)))


def returnVal(v):
    return v


def addValues(val1, val2):
    """ add two values, concetenate strings, etc. """
    return val1 + val2


def getField(structDef, fieldName):
    return structDef[fieldName]


def setFieldSafe(dataStructure, fieldName, value):
    """ sets data field in a safe way """
    try:
        return setattr(dataStructure, fieldName, value)
    except AttributeError:
        errTxt = "Field not defined: field '%s' is required for '%s'" % (
            str(fieldName), str(dataStructure))
        raise TestCaseDataDefinitionError(errTxt)


def getFieldSafe(dataStructure, fieldName):
    """ gets data field in a safe way """
    try:
        ret = getattr(dataStructure, fieldName)
        print "### attribute: " + str(ret)
        return ret
    except AttributeError:
        errTxt = "Field not defined: field '%s' is required for '%s'" % (
            str(fieldName), str(dataStructure))
        raise TestCaseDataDefinitionError(errTxt)
