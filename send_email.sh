PATH="/home/jacob/Desktop/projects/project_automation/ProjectAutomation"
PYTHON_DIR="$PATH/send_email_venv/bin/python"
cd "$PATH" || exit 1

FILE1="$PATH/send_email.py"
FILE2="$PATH/weather_project/weather.py"

$PYTHON_DIR $FILE1 "Weather for Today" $($PYTHON_DIR $FILE2)
