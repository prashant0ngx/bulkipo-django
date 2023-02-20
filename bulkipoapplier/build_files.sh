
# Path: bulkipoapplier\build_files.sh
# Description: Build files for bulkipoapplier

pip install --upgrade pip
pip install wheel
pip install -r requirements.txt
python3.9 manage.py collectstatic
python3.9 manage.py makemigrations
python3.9 manage.py migrate
python3.9 manage.py createsuperuser
python3.9 manage.py runserver
