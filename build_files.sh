#echo "BUILD START"
#python3 -m pip install -r requirements.txt
#python3 manage.py collectstatic --noinput --clear
#echo "BUILD END"

#!/bin/bash

echo "BUILD START"

# Upgrade pip first
python3 -m pip install --upgrade pip

# Force reinstall NumPy and all dependencies
python3 -m pip install --no-cache-dir --force-reinstall numpy
python3 -m pip install --no-cache-dir -r requirements.txt

# Ensure the environment detects NumPy
python3 -c "import numpy; print('NumPy Installed:', numpy.__version__)"

# Collect static files (if using Django)
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"
