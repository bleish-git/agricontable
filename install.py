
#ATTENZIONE: manage.py deve essere quello di sistema, non il convertito per far girare il server wsgi

mkdir temp01
cd temp01
git clone https://github.com/bleish-git/agricontable .

#copia in agriwww

#controllare htaccess
#database

pip install --upgrade pip setuptools wheel

pip install -r requirements.txt --upgrade --no-cache-dir --force-reinstall

pip -r requirement.txt

python manage.py loaddata admin_interface_theme_bootstrap.json

python manage.py collectstatic -c -v 2

python manage.py check
