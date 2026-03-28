PATH="/home/jacobg/Desktop/projects/ProjectAutomation/"
PYTHON_DIR="$PATH/automation_venv/bin/python"
cd "$PATH" || exit 1

EMAIL="$PATH/send_email.py"
WEATHER="$PATH/weather_project/weather.py"
AFFIRMATION="$PATH/affirmations_project/affirmations.py"
BIBLE="$PATH/bible_project/bible.py"

$PYTHON_DIR $EMAIL "Weather for Today" $($PYTHON_DIR $WEATHER)
$PYTHON_DIR $EMAIL "Your Daily Affirmation" $($PYTHON_DIR $AFFIRMATION)
$PYTHON_DIR $EMAIL "Daily Bible Verse" $($PYTHON_DIR $BIBLE)
