# Application server
The goal for this project is to transfer serving dynamic content from our web server to our application server.

### Requirements
- Allowed editors: vi, vim, emacs
- Everything Python-related must be done using python3

### File Descriptions
| File | Description |
| ------------- |:-------------:|
| 0-welcome_gunicorn-upstart_config | Script to start Gunicorn instance to serve route |
| 0-welcome_gunicorn-nginx_config | Sets up Nginx so that the route points to Gunicorn instance |
| 1-pass_parameter-upstart_config | Configures Gunicorn to serve script |
| 1-pass_parameter-nginx_config | Configures Nginx so that the route points to Gunicorn instance |
| 2-api-upstart_config | Starts a Gunicorn instance to serve app.py |
| 2-api-nginx_config | Sets up Nginx so the route /api/ points to Gunicorn instance |
| 3-complete_webapp-upstart_config | Starts a Gunicorn instance to serve 2-hbnb.py |
| 3-complete_webapp-nginx_config | Sets up route / to point to Gunicorn and serves static assets found in web_dynamic/static/ |

#### Author
Lisa Olson
