:: set run parameters
set testset=testset_main.txt

:: set testset to run
del .runTest
@echo %testset% >> .runTest

:: run test with plain unittest loader
cd src
python -m unittest appTestCases

:: cleanup
del ..\.runTest

pause
