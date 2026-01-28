@echo off
REM Move up to project root
cd ..

REM Run all pytest tests from automation/tests and generate HTML report
python -m pytest -v automation/tests --html=report.html --self-contained-html

REM Open the report automatically
start report.html