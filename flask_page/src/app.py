from flask import Flask 
from src.routes.routes import *

app=Flask(__name__)
app.secret_key = "mysecretkey"

# Login & Register
app.add_url_rule(routes["login_route"], view_func=LoginController.as_view("login"))
app.add_url_rule(routes["logout_route"], view_func=routes["logout_controller"])

# Rutas del CRUD -regla de ruta
app.add_url_rule(routes["crud_route"], view_func=routes["crud_controller"])
app.add_url_rule(routes["delete_route"], view_func=routes["delete_controller"])
app.add_url_rule(routes["update_route"], view_func=routes["update_controller"])
app.add_url_rule(routes["category_route"], view_func=routes["category_controller"])

# Page
app.add_url_rule(routes["page_route"], view_func=routes["page_controller"])
app.add_url_rule(routes["work_route"], view_func=routes["work_controller"])
app.add_url_rule(routes["study_route"], view_func=routes["study_controller"])
app.add_url_rule(routes["hobbie_route"], view_func=routes["hobbie_controller"])

# Foro
app.add_url_rule(routes["foro_route"], view_func=routes["foro_controller"])
app.add_url_rule(routes["foro_delete_route"], view_func=routes["foro_delete_controller"])