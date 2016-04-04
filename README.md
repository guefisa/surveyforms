# Surveyforms
Surveryforms pretende ser una API para realizar encuestas que pueda ser consumida desde diferentes clientes.
La API se está desarrollando sobre Django REST Framework y el cliente de ejemplo sobre Angular JS.

# Requerimientos
- Python 2.7+
- Django 1.9+
- Django CORS 1.1
- Django REST Framework 3.3.3

# Instalación (Develop)
- git clone git://github.com/guefisa/surveyforms.git
- pip install -r requirements.txt
- python manage.py makemigrations cuestionario
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

Con esto ya tenemeos el backend de Django y la API funcionando ahora sólo necesitamos ejecutar el cliente desde un navegador.
