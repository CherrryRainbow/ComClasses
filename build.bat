@REM python -m venv env
@REM D:\680920001\personal2\env\Scripts\activate
pip install Django==5.2.5 Pillow
django-admin startproject Test
cd Test
python manage.py startapp testapp
cd ..