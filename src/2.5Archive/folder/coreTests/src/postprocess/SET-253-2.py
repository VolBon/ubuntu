def postProcessResults(testcase, name, testLogger):
    print testLogger
    contain = False
    if 'Error in function call tai.write(vars.a): \'RuntimeStructure\' object has no attribute \'a\' ' in testLogger.notifyDict['check'][0]['data'] :
        contain = True
    testcase.assertTrue(contain)
    