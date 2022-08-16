from src.controllers.controller import *

# Diccionarios clave, ruta y controlador
routes = {
  # Login & Register
  "login_route": "/", "login_controller": LoginController.as_view("login"),
  "logout_route": "/logout", "logout_controller": LogoutController.as_view("logout"),
  
  # Page
  "page_route": "/app", "page_controller": PageController.as_view("index"),
  "work_route": "/app/work", "work_controller": WorkController.as_view("work"),
  "study_route": "/app/study", "study_controller": StudyController.as_view("study"),
  "hobbie_route": "/app/hobbie", "hobbie_controller": HobbieController.as_view("hobbie"),
  
  # Mis CRUDS
  "crud_route": "/app/crud", "crud_controller": CrudController.as_view("todoList"),
  "delete_route": "/app/crud/delete/<int:code>", "delete_controller": DeleteTaskController.as_view("deleteTask"),
  "update_route": "/app/crud/update/<int:code>", "update_controller": UpdateTaskController.as_view("update"),
  "category_route": "/mysecretcrud", "category_controller": CreateTypeController.as_view("category"),
  
  # Foro
  "foro_route": "/app/foro", "foro_controller": ForoController.as_view("my_foro"),
  "foro_delete_route": "/app/foro/delete/<int:id>", "foro_delete_controller": DeleteForoController.as_view("delete_foro")
}