'''
$Id: appTestCases.py 33 2013-05-24 18:11:50Z vultuste $

Main module to run self-tests.

Created on 7.5.2012

@author: vultuste

'''
import os
import sys
import defines
import unittest

# add taCore path to python sys paths

tafSrc = os.path.abspath(os.path.join('..', '..'))
print tafSrc
if not os.path.isdir(tafSrc):
    raise StandardError("taCore path not found: %s" % tafSrc)
sys.path.append(tafSrc)

# those imports should be done after adding taCore parent dir to sys.path
from testLogger import TestLogger


class BaseTestCase(unittest.TestCase):
    """ Base for any class implementing self tests. """

    def __init__(self, *args, **kwargs):
        super(BaseTestCase, self).__init__(*args, **kwargs)
        self.unitTestsFolder = os.path.dirname(os.path.abspath(__file__))
        self.postProceessFolder = os.path.abspath(
            os.path.join(self.unitTestsFolder, '..', 'src', 'postprocess'))

    def setUp(self):
        """ Set the "unit test object". This is used inside the tests. """

        self.baseFolder = None

        defines.setUnittestObj(self)

    def tearDown(self):
        """ Reset the "unit test object". This is used inside the tests. """
        defines.setUnittestObj(None)

    def __verifyTestCase(self, tcFolder, dataSetFilePathname, testLogger):

        try:
            eval("taCore.appContext")
        except:
            import taCore.appContext  # @UnresolvedImport
            import taCore.tcSet  # @UnresolvedImport @UnusedImport
            import taCore.tcExecutor  # @UnresolvedImport
            import taCore.consoleLogger  # @UnresolvedImport

        eval("taCore.appContext")
        eval("taCore.tcSet")
        eval("taCore.tcExecutor")
        eval("taCore.consoleLogger")

        try:
            eval("definitions")
        except:
            # sys.path.append(extraPath)
            import taCore.definitions  # @UnresolvedImport
            # sys.path.remove(extraPath)

        appCtx = taCore.appContext.AppContext.getAppContextObject()
        testConfiguration = appCtx.loadMainTestParams(
            dataSetFilePathname) if dataSetFilePathname else None

        tcExec = taCore.tcExecutor.TcExecutor(tcFolder, testConfiguration)
        tcExec.registerLogger(taCore.consoleLogger.ConsoleLogger())
        tcExec.registerLogger(testLogger)

        status = tcExec.run()

        tcExec.notifyExit()

        self.assertEqual(status, taCore.definitions.ExecStatus.OK,
                         "execution status of test case is other than OK")

    def postProcessResults(self, name, testLogger):
        '''
        :summary: Post processing of test case results. Processing is done
        in module placed in coreTest/src/postprocess directory in form
        of python module named the same as tc name (e.g. SET-186.py).
        The module should define function as in the example:

            def postProcessResults(testcase, name, testLogger):
                testcase.assertEqual(len(testLogger.phaseEnd[0]), 1)
                ...

        The function gets testcase object, test case name, and
        test loggger. It is supposed to check if test execution went
        properly. The check should be done with testcase object with
        use of standard assert* methods.
        :param name: test case name
        :param testLogger: test logger collecting execution steps and statuses
        :returns: True in case postprocess module has been found, False
        otherwise
        '''

        # check if postprocess module exists for a method
        postProcessHandlerPath = os.path.join(self.postProceessFolder, name + '.py')
        if os.path.exists(postProcessHandlerPath):
            # load and execute postprocess
            print '## Postprocessing module found for the test case: %s' % postProcessHandlerPath
            try:
                import imp
                mod = imp.load_source(name, postProcessHandlerPath)
                print '## Postprocessing module loaded succesfully, running...'
                mod.postProcessResults(self, name, testLogger)
                print '## Postprocessing PASSED'
            except Exception as e:
                print '## Postprocessing FAILED'
                raise e

            # indicate that postprocess module has been found
            return True

        return False

    def runTestCase(self, tcFolder, dataSetPathname=None):
        print '\n##'
        print '## Running test case: %s, with params: %s' % (tcFolder, dataSetPathname)
        print '##'

        testLogger = TestLogger()
        err = None
        try:

            absTcFolder = os.path.abspath(
                os.path.join(self.unitTestsFolder, '..', 'testcases', tcFolder))

            if dataSetPathname is None:
                absDataSetPathname = None
            else:
                absDataSetPathname = os.path.abspath(
                    os.path.join(self.unitTestsFolder, '..', 'params', dataSetPathname))

            self.__verifyTestCase(absTcFolder, absDataSetPathname, testLogger)
        except Exception, detail:
            err = detail

        # postprocess test results
        errPost = None
        try:
            if self.postProcessResults(tcFolder, testLogger):
                err = None
        except Exception, detail:
            errPost = detail

        if errPost:
            err = errPost

        status = 'FAILED'
        if not err:
            status = 'PASSED'

        print '##'
        print '## Test case %s execution %s' % (tcFolder, status)
        print '##'

        if err:
            self.fail(repr(err))


class CoreTest(BaseTestCase):

    @classmethod
    def makeTestFunction(cls, name):

        def testMethod(self):
            # check if param file is defined for a test case
            paramPath = os.path.join('..', 'params', name + '.txt')
            if not os.path.exists(paramPath):
                paramPath = None

            self.runTestCase(name, paramPath)

        return testMethod

    @classmethod
    def makeTestFunctionDefinition(cls):
        # read what test to run from .runTest config file
        # .runTest file has been added as it is not possible to pass
        # parameters to unit test when running via python -m unittest
        configPath = os.path.join('..', '.runTest')
        with open(configPath, 'r') as f:
            testset = f.read()
            testset = testset.split()[0]

        print '%s has been pointed as test set file in .runTest config file' % testset

        # read test set file and find test cases to run
        testSetPath = os.path.join('..', testset)
        with open(testSetPath, 'r') as f:
            testcases = f.read()
        testcases = testcases.split()
        print '%s test cases has been found in the test set' % len(testcases)

        print 'Creating test methods:'
        for name in testcases:
            tm = cls.makeTestFunction(name)
            testMethodName = 'test_' + name.replace('-', '_')
            print '  %s' % testMethodName
            setattr(cls, testMethodName, tm)


# dynamically add test methods to test case class
CoreTest.makeTestFunctionDefinition()

""" for running in command line:
..>python -m unittest appTestCases
"""

if __name__ == "__main__":
    unittest.main()
