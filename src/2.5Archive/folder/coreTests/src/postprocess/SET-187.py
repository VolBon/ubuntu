def postProcessResults(testcase, name, testLogger):
    print testLogger
    testcase.assertEqual(testLogger.phaseEndList[0]['phase'], 'prerequisites')
    testcase.assertEqual(testLogger.phaseEndList[1]['phase'], 'setup')
    testcase.assertEqual(testLogger.phaseEndList[2]['phase'], 'postconditions')
    testcase.assertEqual(testLogger.phaseEndList[1]['execStatus'], 1)
    testcase.assertEqual(testLogger.functionEndDict['setup'][0]['extraInfo'], 'Intentional exception in setup phase')
    testcase.assertEqual(testLogger.functionEndDict['postconditions'][0]['extraInfo'], 'Test work ok')
