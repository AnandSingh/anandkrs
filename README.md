## Personal blog for anandkrs.com

Install the virtualenv and activate the venv
``` 
 $ pip install virtualenv
 $ cd myproject/
 $ virtualenv venv
```
 or
```
 $ virtualenv venv --distribute
```

If you want your virtualenv to also inherit globally installed packageA
```
 $ virtual venv --system-site-packages
```

Install the project dependencies
```
 $ pip install -r requirements.rxt
```

Acitivate the venv
```
 $ source venv/bin/activate
```

 https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html

Running our tests
```
 $ python manage.py jenkins --enable-coverage
```

For deployment
```
 $ fab deploy
```
