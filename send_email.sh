PATH="/home/jacob/Desktop/projects/project_automation/ProjectAutomation"
PYTHON_DIR="$PATH/send_email_venv/bin/python"
cd "$PATH" || exit 1

EMAIL="$PATH/send_email.py"
WEATHER="$PATH/weather_project/weather.py"
AFFIRMATION="$PATH/affirmations_project/affirmations.py"

$PYTHON_DIR $EMAIL "Weather for Today" $($PYTHON_DIR $WEATHER)
$PYTHON_DIR $EMAIL "Your Daily Affirmation" $($PYTHON_DIR $AFFIRMATION)
