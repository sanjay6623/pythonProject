REM pytest -s -v -m "regression" testCases --html=Reports/report.html --browser chrome
REM pytest -s -v -m "sanity" testCases --html=Reports/report.html --browser chrome
REM pytest -s -v -m "regression and sanity" testCases --html=Reports/report.html --browser chrome
REM pytest -rA -m "regression or sanity" testCases --html=Reports/report.html --browser chrome
pytest -rA testCases --html=Reports/report.html --browser chrome

REM https://github.com/sanjay6623/pythonProject.git


