#!/bin/bash
# Move up to project root
cd ..

# Run all pytest tests from automation/tests and generate HTML report
python3 -m pytest -v automation/tests --html=report.html --self-contained-html

# Open the report automatically (Mac uses 'open', Linux uses 'xdg-open')
if [[ "$OSTYPE" == "darwin"* ]]; then
    open report.html
else
    xdg-open report.html
fi