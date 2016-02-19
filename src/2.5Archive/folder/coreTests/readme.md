Author: Patryk Pruszynski
Date: 2016-01-25

This file describes structure and file organization of coreTest in TiGear.

# What is coreTest
Core test is a set of tests of core TiGear functionality.
They are run as batch files (no gui involved) and test proper working of basic
TiGear functionality, like:
* execution of test case defined in tc.xml file
* execution of certain test blocks and test runs
* calling keywords (passing parameters, return values, handling exceptions)
* loading of test parameters (from param files)
* setting and reading of test variables
* conditions, loops
* etc.
The aim is to cover entire functionality that is implemented in TiGear.

# Main purpose
TiGear tool is used by various projects and developed by constantly changing
crew. This brings a challenge of having a trust that new features and bugfixes 
work correctly and do not spoil existing functionality.
This test together with automated GUI tests is a first verification step that
should be executed after introducing any change to the project.

# CI loop integration
TiGear core tests should be integrated into CI loop and called after each 
change in the code. In case for bugs the test case log should be send to all
the possible bug contributors.

# Main components
The example folder structure looks as follows:
```
│   readme.txt
│   runTest.bat
│   testset.txt
├───params
│   │   SET-182.txt
│   │   SET-184.txt
│   │   SET-185.txt
│   ├───SET-182
│   │       a.txt
│   ├───SET-184
│   │       a.txt
│   ├───SET-185a
│   │       par.txt
│   │       par1.txt
│   └───SET-185b
│           par.txt
│           par1.txt
├───src
│   │   appTestCases.py
│   │   defines.py
│   │   functions.py
│   │   verify.bat
│   ├───SET-182
│   │       mod.py
│   └───testpackage
│           abc.py
│           __init__.py
│
└───testcases
    ├───prototype
    │       tc.xml
    ├───SET-182
    │       tc.xml
    ├───SET-183
    │       tc.xml
    │       tc.xml.txt
    └───SET-184
            tc.xml
```

* params folder - contains test parameters for each test case
* src folder - contains python code for test libs
* testcases folder - contains test cases definitions (tc.xml files)
* runTest.bat - runs the test
* runTest_with_report.bat - runs the test with pytest and generates reports for CI
* testset_main.txt - contains test cases loaded during test execution; there can 
be many testset*.txt files containing tests for different functionalities

# Test cases naming and organization
Test procedure is defined in TiGear TestLink in TiGear:
https://testlink.etb.tieto.com, test project SamsungSTA, 
SamsungEnbTA->TiGear Core

Eech test case has own ID, like SET-182 and this name should be used for all 
test case specific files.

Each test case definition (tc.xml) should be stored in separate directory in 
testcases folder. 

Each test case param files should be stored in separate folder 
(e.g. params\SET-182) with test case specific txt file (e.g. SET-182.txt)
being root of the param file. The file should include other test case related
param files (if any) only from the test case specific directory.

There exist common lib (e.g. functions.py) files with set of common keywords 
(like e.d. setVariable, raiseException, assertEquals) shared among all test 
cases. In case test case needs some specific keyword that is, or with high
probabilty will not be shared among test case, then such library/keyword should
be keept in separate module in test case specific folder (e.g. SET-182).

This approach to the structure (with each exclusive test case files keept in 
test case specific folders) should support separation between test cases and
should make it easier to maintain (extend, delete, refactor) existing tests.

# Testcases categories
* VARS - everything what according to dynamic and static variables declared in <vars>, excluding loopIndex, loopItem
* BLOCKS - everything what according to <block>, including loops, blocks keywords, conditions, loopIndex, loopItem
* RUNS - everything what according to <run>, its parameters, launch of functions
* IMPORT - separate set of tests checking everything what according to <import>, some tests can be repeat on others categories, but here according only to import

# Test case results postprocessing - handling of TCs that are supposed to fail
Some TiGear functionalities are responsible for handling of the exceptions raised
during test case execution. One of the examples could be failure in prerequisites 
phase that should cause TiGear to not to run other test phases. Testing on such
functionalities requires intencional raising of an exception and the entire test to fail.
As core tests base on unittest.TestCase, exception raised during such test case
would cause entire core test to fail. In order to prevent core tests implements
test results postprocessing.
During test execution main test events (phase/function end) are collected and 
passed, via testLogger, to postprocessing module defined on coreTest/postprocessing.
The module defines function: postProcessResults(testcase, name, testLogger)
that should check test case execution and raise exception if the test should fail.
In case postprocessing function does not raise any exception the result of the 
core test will be positive.
Postprocessing is executed only when appropriate postprocessing module is defined.
Otherwise this step is not performed.

