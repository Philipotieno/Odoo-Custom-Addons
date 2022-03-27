### To do app Odoo 15
### Make sure you have poetry installed.

1. Clone the repository

2. After cloning the app clone odoo 15 
 ```
    $ git clone http://www.github.com/odoo/odoo --depth 1 --branch 15.0 odoo
 ```
3. Get into the cloned repository and install dependancies
```
    $ poetry install
```
4. Activate your work environment
```
    $ poetry shell
```
5. Update configs >>> odoo.conf and lauch.json file to point to your paths

6. Start the app with
```
    ./odoo/odoo-bin -c odoo.conf -i base
```
7. Later
```
    ./odoo/odoo-bin -c odoo.conf
```

8. Other
```
    ./odoo/odoo-bin -c odoo.conf -u {name of mudule to upgrade}
```