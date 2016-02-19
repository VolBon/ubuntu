def postProcessResults(testcase, name, testLogger):
    print testLogger
    testcase.assertEqual(testLogger.phaseEndList[0]['phase'], 'prerequisites')
    testcase.assertEqual(testLogger.phaseEndList[1]['phase'], 'setup')
    testcase.assertEqual(testLogger.phaseEndList[2]['phase'], 'execution')
    testcase.assertEqual(testLogger.phaseEndList[3]['phase'], 'postconditions')
    testcase.assertEqual(testLogger.functionEndDict['execution'][0]['extraInfo'], 'Expected error FLOAT_2')
    testcase.assertEqual(testLogger.functionEndDict['execution'][2]['extraInfo'], 'Expected error FLOAT_3')
    testcase.assertEqual(testLogger.functionEndDict['execution'][3]['extraInfo'], 'Expected error FLOAT_4')
    testcase.assertEqual(testLogger.functionEndDict['execution'][7]['extraInfo'], 'Expected error TUPLE_2')
