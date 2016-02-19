'''
Created on 2016-02-11

@author: Patryk Pruszynski
'''
import inspect
from taCore import abstractLogger


class TestLogger(abstractLogger.AbstractLogger):
    '''
    Test logger class. Collects important events happening during
    test execution:

    - failure phase

    - phase end events with example attributes
        {
        'passCounter': 0,
        'timestamp': datetime.datetime(2016, 2, 12, 15, 3, 26, 483000),
        'extraInfo': 'Intentional exception in preconditions phase',
        'funcStatus': 1,
        'failCounter': 1,
        'functionCall': "functions.raiseError('Intentional exception in preconditions phase')",
        'phase': 'prerequisites',
        'elemId': 6
        }

    - function end event with parameters:
        {
        'execStatus': 1,
        'passCounter': 0,
        'timestamp': datetime.datetime(2016, 2, 12, 15, 3, 26, 483000),
        'failCounter': 1,
        'elemId': 1,
        'phase': 'prerequisites'
        }

    Two last event parameters are available as list and dictionary keyed
    by phase. List preserves execution order and dictionary gives more
    convenient access to log entries.
    '''

    def __init__(self):
        abstractLogger.AbstractLogger.__init__(self)
        self.failurePhase = None
        self.phaseEndList = []
        self.phaseEndDict = {}
        self.functionEndList = []
        self.functionEndDict = {}
        self.notifyList = []
        self.notifyDict = {}
        # 'check' phase is 'virtual' phase that is used before prerequisites
        self.currentPhase = 'check'
        self.initPhaseDicts()

    def __str__(self, *args, **kwargs):
        '''
        Prints conntent on the test logger
        Use print testLogger in your postprocessing script to see what
        was the execution process.
        '''

        from pprint import pformat
        text = '\n**'
        text += '\n** Printing content of testLogger:'
        text += '\n\n\nfailurePhase: %s' % self.failurePhase
        text += '\n\n\nphaseEndList:\n'
        text += pformat(self.phaseEndList)
        text += '\n\n\nphaseEndDict:\n'
        text += pformat(self.phaseEndDict)
        text += '\n\n\nfuncionEndList:\n'
        text += pformat(self.functionEndList)
        text += '\n\n\nfunctionEndDict:\n'
        text += pformat(self.functionEndDict)
        text += '\n\n\nnotifyList:\n'
        text += pformat(self.notifyList)
        text += '\n\n\nnotifyDict:\n'
        text += pformat(self.notifyDict)
        text += '\n\n**\n**\n'
        return text

    def initPhaseDicts(self):
        self.functionEndDict[self.currentPhase] = []
        self.notifyDict[self.currentPhase] = []

    def projectSelected(self, projectName, dataSetName):
        pass

    def executionListStarts(self, name=""):
        pass

    def executionListEnds(self):
        pass

    def executionBatchStarts(self, bachName):
        pass

    def executionBatchEnds(self, bachName):
        pass

    def executionOfTcInBatchStarts(self, bachName, tc, crtIndex, tcCount):
        pass

    def testCaseCheckStarts(self, timestamp, tc):
        super(TestLogger, self).testCaseCheckStarts(timestamp, tc)

    def testCaseCheckErrMsg(self, timestamp, errMsg):
        pass

    def testCaseCheckEnds(self, timestamp, tc, checkOk):
        pass

    def testCaseExecutionStarts(self, timestamp, tcName, tcFolder):
        pass

    def testCaseExecutionEnds(self, timestamp, tcName, tcState, failurePhase):
        self.failurePhase = failurePhase

    def testCasePhaseExecutionStarts(self, timestamp, elemId, phase,
                                     passCounter, failCounter):
        self.currentPhase = phase
        self.initPhaseDicts()

    def testCasePhaseExecutionEnds(self, timestamp, elemId, phase, execStatus,
                                   passCounter, failCounter):
        frame = inspect.currentframe()
        _locals = inspect.getargvalues(frame)[3]
        del _locals['self']
        del _locals['frame']
        self.phaseEndList.append(_locals)
        self.phaseEndDict[phase] = _locals
        self.currentPhase = None

    def testCaseFunctionExecutionStarts(self, timestamp, elemId, target,
                                        functionCall, passCounter,
                                        failCounter):
        pass

    def testCaseFunctionExecutionEnds(self, timestamp, elemId, functionCall,
                                      funcStatus, passCounter, failCounter,
                                      extraInfo=''):
        frame = inspect.currentframe()
        _locals = inspect.getargvalues(frame)[3]
        del _locals['self']
        del _locals['frame']
        _locals['phase'] = self.currentPhase
        self.functionEndList.append(_locals)
        self.functionEndDict[self.currentPhase].append(_locals)

    def testCaseFunctionStatusChanged(self, func):
        pass

    def notify(self, timestamp, data, notificationLevel, addCrLf=True,
               ensureCrLfBefore=True):
        frame = inspect.currentframe()
        _locals = inspect.getargvalues(frame)[3]
        del _locals['self']
        del _locals['frame']
        _locals['phase'] = self.currentPhase
        self.notifyList.append(_locals)
        self.notifyDict[self.currentPhase].append(_locals)

    def asynchDataSent(self, timestamp, serverKey, data):
        pass

    def asynchDataReceived(self, timestamp, serverKey, data,
                           endOfReceiving=False):
        pass

    def pause(self, msgTitle, message, seconds, allowUserToInterrupt=True):
        pass

    def notifyExit(self):
        pass
