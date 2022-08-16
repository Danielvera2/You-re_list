from flask import request, render_template, redirect, session
from flask.views import MethodView
from src.db import psql

# Login & Register
class LoginController(MethodView):
    def get(self):
        return render_template("public/login.html")
      
    def post(self):
        user = request.form["user"]
        password = request.form["password"]
        print(user, password)
        
        if user == "miguel" and password == "miguel123":
            session["login"] = True
            session["user"] = user
            return redirect("/app")
        return render_template("public/login.html")

class LogoutController(MethodView):
    def get(self):
        session.clear()
        return redirect("/")

# Page
class PageController(MethodView):
    def get(self):
        if not "login" in session:
            return redirect("/")
        return render_template('public/page.html')
      
      
# Cards
class HobbieController(MethodView):
    def get(self):
      if not "login" in session:
            return redirect("/")
      else:
        with psql.cursor() as cur:
            cur.execute('SELECT * FROM tasks')
            tasks = cur.fetchall()
            cur.execute('SELECT * FROM categories')
            categories = cur.fetchall()
            print(cur)
            return render_template('public/hobbie.html', tasks=tasks, categories=categories)
          
          
class WorkController(MethodView):
    def get(self):
      if not "login" in session:
            return redirect("/")
      else:
        with psql.cursor() as cur:
            cur.execute('SELECT * FROM tasks')
            tasks = cur.fetchall()
            cur.execute('SELECT * FROM categories')
            categories = cur.fetchall()
            print(cur)
            return render_template('public/work.html', tasks=tasks, categories=categories)
          
          
class StudyController(MethodView):
    def get(self):
      if not "login" in session:
            return redirect("/")
      else:
        with psql.cursor() as cur:
            cur.execute('SELECT * FROM tasks')
            tasks = cur.fetchall()
            cur.execute('SELECT * FROM categories')
            categories = cur.fetchall()
            print(cur)
            return render_template('public/study.html', tasks=tasks, categories=categories)
          
# ***Mis cruds***
class CrudController(MethodView):
    #  Create
    def post(self):
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        category = request.form['category']
        
        with psql.cursor() as cur:
            cur.execute('INSERT INTO tasks (id_category, titulo, descripcion) VALUES (%s, %s, %s)', (category, titulo, descripcion))
            psql.commit()
            return redirect('/app/crud')
        
        
    # Read
    def get(self):
        with psql.cursor() as cur:
            cur.execute('SELECT * FROM tasks')
            tasks = cur.fetchall()
            cur.execute('SELECT * FROM categories')
            categories = cur.fetchall()
            return render_template('public/crud.html', tasks=tasks, categories=categories)
      
        
# Delete
class DeleteTaskController(MethodView):
    def post(self, code):
        with psql.cursor() as cur:
            cur.execute('DELETE FROM tasks WHERE code = %s', (code,))
            psql.commit()
            return redirect('/app/crud')
        
        
# Update
class UpdateTaskController(MethodView):
    def get(self, code):
      if not "login" in session:
            return redirect("/")
      else:
        with psql.cursor() as cur:
          cur.execute("SELECT * FROM tasks WHERE code = %s", (code,))
          task= cur.fetchone()
          cur.execute('SELECT * FROM categories')
          categories = cur.fetchall()
          return render_template('public/update.html', task=task, categories=categories)
      
    def post(self, code):
        category = request.form['category']
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        with psql.cursor() as cur:
          cur.execute("UPDATE tasks SET category = %s, titulo = %s, descripcion = %s WHERE code = %s", (category, titulo, descripcion, code))
          psql.commit()
          return redirect('/app/crud')
        
        
# Foring key, crud
class CreateTypeController(MethodView):
    def get(self):
        return render_template("public/category.html")
      
    
    def post(self):
        id = request.form['id']
        name = request.form['name']
        description = request.form['description']
        
        with psql.cursor() as cur:
            cur.execute("INSERT INTO categories (id, name, description) VALUES (%s, %s, %s)", (id, name, description))
            psql.commit()
            return redirect('/app/crud')
          
          
# Foro

class ForoController(MethodView):
    def get(self):
      if not "login" in session:
            return redirect("/")
      else:
        with psql.cursor() as cur:
            cur.execute('SELECT * FROM foro')
            comments = cur.fetchall()
            return render_template('public/foro.html', comments=comments)
          
    def post(self):
      if not "login" in session:
            return redirect("/")
      else:
        person = request.form['person']
        title = request.form['title']
        description = request.form['description']
        
        with psql.cursor() as cur:
            cur.execute('INSERT INTO foro (person, title, description) VALUES (%s, %s, %s)', (person, title, description))
            psql.commit()
            return redirect('/app/foro')
    
    
class DeleteForoController(MethodView):
    def post(self, id):
        with psql.cursor() as cur:
                cur.execute('DELETE FROM foro WHERE id = %s', (id,))
                psql.commit()
                return redirect('/app/foro')
      


