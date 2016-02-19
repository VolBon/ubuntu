@ECHO OFF
setlocal

:: set run parameters
set report_dir=_test_results
set testset=testset_main.txt

:: prepare report directory
rmdir /Q /S %report_dir%
mkdir %report_dir%

:: set testset to run
del .runTest
@echo %testset% >> .runTest

:: run pytest
cd src
SET PYTHONPATH=%PYTHONPATH%%cd%;
py.test -v appTestCases.py --cov-report=html --cov-report=xml --cov=%cd%/../../taCore --resultlog=%cd%/../%report_dir%/pytest_result.txt --junitxml=%cd%/../%report_dir%/pytest_result.xml

:: store report files and cleanup unnecessary files
rmdir /Q /S __pycache__
move htmlcov ../%report_dir%
move .coverage ../%report_dir%
move coverage.xml ../%report_dir%
del ..\.runTest

endlocal
pause
