# PythonWeb
Example web applications written in Python 3

To run in the development server locally, simply follow these steps:

```
cd flask_with_forms
./setup_venv.sh
source venv/bin/activate
./run.sh
```

To run in a production environment must be done through *wsgi*. There are many choices here. I opted for a combination of Gunicorn with a Nginx proxy. This requires a little configuration. The nginx conf requires a little experimentation. I ended up changing the config at ``/etc/nginx/sites-enabled/default`` to having these lines:

```
        location / {
                # First attempt to serve request as file,
                # then proxy to application server
                try_files $uri @proxy_to_app;
        }

        # set up as reverse proxy server to a Gunicorn server running on localhost port 8000.
        location @proxy_to_app {
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header Host $host;

                proxy_pass http://127.0.0.1:8000;
        }
```

Then you can run the app in gunicorn with:

```
gunicorn -w 1 -b 127.0.0.1:8000 app:app
```


