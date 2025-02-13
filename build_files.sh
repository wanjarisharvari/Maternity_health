#echo "BUILD START"
#python3 -m pip install -r requirements.txt
#python3 manage.py collectstatic --noinput --clear
#echo "BUILD END"

#!/bin/bash

echo "BUILD START"

# Upgrade pip
python3 -m pip install --upgrade pip --break-system-packages

# Install dependencies without cache and suppress root warning
python3 -m pip install -r requirements.txt --no-cache-dir --break-system-packages

# Collect static files (if using Django)
python3 manage.py collectstatic --noinput --clear

echo "BUILD END"

