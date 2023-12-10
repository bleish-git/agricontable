
mkdir temp01
cd temp01
git clone https://github.com/bleish-git/agricontable .

#copia in agriwww

#controllare htaccess
#database

pip -r requirement.txt

python manage.py loaddata admin_interface_theme_bootstrap.json

python manage.py check
