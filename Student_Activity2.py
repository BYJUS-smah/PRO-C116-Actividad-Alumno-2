from flask import Flask, render_template
app = Flask(__name__)

#En la función return render_template(‘index.html’)

@app.route("/Actividad_Alumno2")
def student_webpage():
    #Crear una variable
    name = 'John'
    # Pasar la variable en la plantilla
    return render_template('Actividad_Alumno2.html', student_name = name)
app.run(debug=True)