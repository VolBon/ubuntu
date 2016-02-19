def postProcessResults(testcase, name, testLogger):
    testcase.assertEqual(len(testLogger.phaseEndList), 1)
    testcase.assertEqual(testLogger.phaseEndList[0]['phase'], 'prerequisites')
    testcase.assertEqual(testLogger.phaseEndList[0]['execStatus'], 1)
    testcase.assertEqual(testLogger.functionEndDict['prerequisites'][0]['extraInfo'], 'Intentional exception in preconditions phase')
