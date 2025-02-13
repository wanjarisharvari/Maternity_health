#echo "BUILD START"
#python3 -m pip install -r requirements.txt
#python3 manage.py collectstatic --noinput --clear
#echo "BUILD END"

#!/bin/bash
pip install --upgrade pip  # Upgrade pip
pip install --no-cache-dir numpy  # Force install NumPy
pip install --no-cache-dir -r requirements.txt  # Install all dependencies again
python3 manage.py collectstatic --noinput --clear
