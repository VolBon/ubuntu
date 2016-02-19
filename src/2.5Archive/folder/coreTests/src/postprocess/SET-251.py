def postProcessResults(testcase, name, testLogger):
    print testLogger
    testcase.assertEqual(testLogger.phaseEndList[0]['phase'], 'prerequisites')
    testcase.assertEqual(testLogger.phaseEndList[1]['phase'], 'setup')
    testcase.assertEqual(testLogger.phaseEndList[2]['phase'], 'execution')
    testcase.assertEqual(testLogger.phaseEndList[3]['phase'], 'postconditions')
    testcase.assertEqual(testLogger.functionEndDict['execution'][0]['extraInfo'], 'Intentional exception in execution phase')
    testcase.assertNotEqual(testLogger.functionEndDict['execution'][1]['extraInfo'], 'Should not run this block in execution')
    testcase.assertNotEqual(testLogger.functionEndDict['postconditions'][0]['extraInfo'], 'Should not run postcondition block')