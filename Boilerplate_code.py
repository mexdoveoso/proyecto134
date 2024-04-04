#Importar el módulo Flask en el proyecto.
from flask import Flask

#Crear un objeto de la clase Flask.
app = Flask(__name__)

#La función route() de la clase Flask.
@app.route("/")

def home ():
    
    name ="Alex"
    age ="10"
    return render_template('index.html', name = name, age = age)

#father 
@app.route("/padre") 
def father():
    
    name ="Pedro"
    age ="50"
    return render_template('father.html', name = name, age = age)

#mother 
@app.route("/madre") 
def mother():
    
    name ="marta"
    age ="25"
    return render_template('mother.html', name = name, age = age)

#friend 
@app.route("/amigo") 
def friend():
    
    name ="samuel"
    age ="7"
    return render_template('friend.html', name = name, age = age)

#ejecutar el achivo 
if __name__ == '__main__':
    app.run(debug=True)