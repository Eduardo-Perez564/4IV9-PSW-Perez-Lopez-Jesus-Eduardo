import pandas as pd
from pandas.core.frame import DataFrame
import re
import webbrowser

#Vamos a ver si puedo mandar a llamar a las columnas xd

datos = pd.read_csv("Encuestas.csv")
df = pd.DataFrame(datos)


#Con un for vamos de columna en columna buscando las respuestas de los encuestados y comparandolas para contar cuantas respuestas son
#Contando los datos para la gráfica 1
def P1_edad_encuestado(Respuesta1, Respuesta2, Respuesta3, Respuesta4, Respuesta5):

    for i in range(0, len(df.index)):
        
        Pregunta_Resp = str(datos['¿Cuántos años tienes?'].loc[i])
        if Pregunta_Resp == "15 - 16":
            Respuesta1 += 1
        elif Pregunta_Resp == "17 - 18":
            Respuesta2 += 1
        elif Pregunta_Resp == "19 - 20":
            Respuesta3 += 1
        elif Pregunta_Resp == "más de 20":
            Respuesta4 += 1
        elif Pregunta_Resp == "menos de 15":
            Respuesta5 += 1
    
    return Respuesta1, Respuesta2, Respuesta3, Respuesta4, Respuesta5

#Contando los datos para la gráfica 2
def P2_Tiempo_dormir(Respuesta1, Respuesta2, Respuesta3, Respuesta4):

    for i in range(0, len(df.index)):
        
        Pregunta_Resp = str(datos['¿En promedio cuantas horas duermes al día?'].loc[i])
        if Pregunta_Resp == "10 a 12 horas":
            Respuesta1 += 1
        elif Pregunta_Resp == "8 horas":
            Respuesta2 += 1
        elif Pregunta_Resp == "6 a 8 horas":
            Respuesta3 += 1
        elif Pregunta_Resp == "Menos de 6 horas":
            Respuesta4 += 1
    
    return Respuesta1, Respuesta2, Respuesta3, Respuesta4

#Contando los datos para la gráfica 3
def P3_Tiempo_de_Estudio(Respuesta1, Respuesta2, Respuesta3, Respuesta4):

    for i in range(0, len(df.index)):
        
        Pregunta_Resp = str(datos['¿En promedio cuantas horas las dedicas a el estudio al día?'].loc[i])
        if Pregunta_Resp == "Menos de 8 horas":
            Respuesta1 += 1
        elif Pregunta_Resp == "8 a 10 horas":
            Respuesta2 += 1
        elif Pregunta_Resp == "10 a 12 horas":
            Respuesta3 += 1
        elif Pregunta_Resp == "mas de 12 horas":
            Respuesta4 += 1
    
    return Respuesta1, Respuesta2, Respuesta3, Respuesta4

#Contando los datos para la gráfica 4
def P4_Semestre(Respuesta1, Respuesta2, Respuesta3, Respuesta4, Respuesta5, Respuesta6):

    for i in range(0, len(df.index)):
        
        Pregunta_Resp = str(datos['¿Qué semestre de media superior estudias?'].loc[i])
        if Pregunta_Resp == "Primer Semestre":
            Respuesta1 += 1
        elif Pregunta_Resp == "Segundo Semestre":
            Respuesta2 += 1
        elif Pregunta_Resp == "Tercer Semestre":
            Respuesta3 += 1
        elif Pregunta_Resp == "Cuarto Semestre":
            Respuesta4 += 1
        elif Pregunta_Resp == "Quinto Semestre":
            Respuesta5 += 1
        elif Pregunta_Resp == "Sexto Semestre":
            Respuesta6 += 1
    
    return Respuesta1, Respuesta2, Respuesta3, Respuesta4, Respuesta5, Respuesta6

#Contando los datos para la gráfica 5
def P5_Desempenio(Respuesta1, Respuesta2, Respuesta3, Respuesta4):

    for i in range(0, len(df.index)):
        
        Pregunta_Resp = str(datos['¿Cómo consideras que has desarrollado tu situación académica en cuarentena y clases a distancia ?'].loc[i])
        if Pregunta_Resp == "Excelente":
            Respuesta1 += 1
        elif Pregunta_Resp == "Buena":
            Respuesta2 += 1
        elif Pregunta_Resp == "Mala":
            Respuesta3 += 1
        elif Pregunta_Resp == "Pésima":
            Respuesta4 += 1
    
    return Respuesta1, Respuesta2, Respuesta3, Respuesta4

#Contando los datos para la gráfica 6
def P6_Problemas(Respuesta1, Respuesta2, Respuesta3, Respuesta4, Respuesta5):

    for i in range(0, len(df.index)):
        
        Pregunta1_Resp = str(datos['¿Has tenido problemas psicológicos?'].loc[i])
        if re.findall(r'Depresión',Pregunta1_Resp):
            Respuesta1 += 1
        if re.match(r'Trastornos de Ansiedad',Pregunta1_Resp):
            Respuesta2 += 1
        if re.findall(r'Trastornos Alimenticios',Pregunta1_Resp):
            Respuesta3 += 1
        if re.findall(r'Estrés',Pregunta1_Resp):
            Respuesta4 += 1

    return Respuesta1, Respuesta2, Respuesta3, Respuesta4, Respuesta5

#Contando los datos para la gráfica 7
def P7_Ayuda(Respuesta1, Respuesta2):

    for i in range(0, len(df.index)):
        
        Pregunta_Resp = str(datos['¿Has acudido a ayuda profesional?'].loc[i])
        if Pregunta_Resp == "Sí":
            Respuesta1 += 1
        elif Pregunta_Resp == "No":
            Respuesta2 += 1

    return Respuesta1, Respuesta2

P1_15_16, P1_17_18, P1_19_20, P1_mas_de_20, P1_menos_de_15 =P1_edad_encuestado(0,0,0,0,0)

P2_10_a_12_horas, P2_8_horas, P2_6_a_8_horas, P2_menos_de_6_horas = P2_Tiempo_dormir(0,0,0,0)

P3_Menos_de_8_horas, P3_8_a_10_horas, P3_10_a_12_horas, P3_mas_de_12_horas = P3_Tiempo_de_Estudio(0,0,0,0)

P4_Primer_Semestre, P4_Segundo_Semestre, P4_Tercer_Semestre, P4_Cuarto_Semestre, P4_Quinto_Semestre, P4_Sexto_Semestre = P4_Semestre(0,0,0,0,0,0)

P5_Excelente, P5_Buena, P5_Mala, P5_Pesima = P5_Desempenio(0,0,0,0)

P6_Depresion, P6_Ansiedad, P6_Trastornos_Alimenticios, P6_Estres, P6_Nada = P6_Problemas(0,0,0,0,0)

P7_Si, P7_No = P7_Ayuda(0,0)

f = open('Graficas.html', 'w')
mensaje = """<html lang="es">
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['15-16', """+str(P1_15_16)+"""],
          ['16-17', """+str(P1_17_18)+"""],
          ['18-19', """+str(P1_19_20)+"""],
          ['Más de 20 años', """+str(P1_mas_de_20)+"""],
          ['Menos de 15 años', """+str(P1_menos_de_15)+"""]
        ]);

        var options = {
          title: 'Edad de las personas Encuestadas'
        };

        var chart = new google.visualization.PieChart(document.getElementById('Grafica1_Container'));

        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['10 a 12 horas', """+str(P2_10_a_12_horas)+"""],
          ['8 horas', """+str(P2_8_horas)+"""],
          ['6 a 8 horas', """+str(P2_6_a_8_horas)+"""],
          ['Menos de 6 horas', """+str(P2_menos_de_6_horas)+"""]
        ]);

        var options = {
          title: 'Promedio de tiempo que duermen las personas encuestadas'
        };

        var chart = new google.visualization.PieChart(document.getElementById('Grafica2_Container'));

        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['Menos de 8 horas', """+str(P3_Menos_de_8_horas)+"""],
          ['8 a 10 horas', """+str(P3_8_a_10_horas)+"""],
          ['10 a 12 horas', """+str(P3_10_a_12_horas)+"""],
          ['Más de 12 horas', """+str(P3_mas_de_12_horas)+"""]
        ]);

        var options = {
          title: 'Promedio de tiempo que le dedican al estudio las personas encuestadas'
        };

        var chart = new google.visualization.PieChart(document.getElementById('Grafica3_Container'));

        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['Primer Semestre', """+str(P4_Primer_Semestre)+"""],
          ['Segundo Semestre', """+str(P4_Segundo_Semestre)+"""],
          ['Tercer Semestre', """+str(P4_Tercer_Semestre)+"""],
          ['Cuarto Semestre', """+str(P4_Cuarto_Semestre)+"""],
          ['Quinto Semestre', """+str(P4_Quinto_Semestre)+"""],
          ['Sexto Semestre', """+str(P4_Sexto_Semestre)+"""]
        ]);

        var options = {
          title: 'Semestre que cursan las personas encuestadas'
        };

        var chart = new google.visualization.PieChart(document.getElementById('Grafica4_Container'));

        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['Excelente', """+str(P5_Excelente)+"""],
          ['Buena', """+str(P5_Buena)+"""],
          ['Mala', """+str(P5_Mala)+"""],
          ['Pésima', """+str(P5_Pesima)+"""]
        ]);

        var options = {
          title: 'Desarrollo de la situación académica en cuarentena y clases a distancia de las personas encuestadas'
        };

        var chart = new google.visualization.PieChart(document.getElementById('Grafica5_Container'));

        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['Depresión', """+str(P6_Depresion)+"""],
          ['Trastornos de Ansiedad', """+str(P6_Ansiedad)+"""],
          ['Trastornos Alimenticios', """+str(P6_Trastornos_Alimenticios)+"""],
          ['Estrés', """+str(P6_Estres)+"""]
        ]);

        var options = {
          title: 'Problemas psicológicos que han presentado las personas encuestadas'
        };

        var chart = new google.visualization.PieChart(document.getElementById('Grafica6_Container'));

        chart.draw(data, options);
      }
    </script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          ['Task', 'Hours per Day'],
          ['Si', """+str(P7_Si)+"""],
          ['No', """+str(P7_No)+"""]
        ]);

        var options = {
          title: 'Cantidad de personas que pidieron ayuda profesional'
        };

        var chart = new google.visualization.PieChart(document.getElementById('Grafica7_Container'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>

    <h1><center>Gráficas</center></h1>
    <hr width = "80%" height = 25px>

    <div id="Grafica1_Container" style="width: 800px; height: 500px;"></div>
    <div id="Grafica2_Container" style="width: 800px; height: 500px;"></div>
    <div id="Grafica3_Container" style="width: 800px; height: 500px;"></div>
    <div id="Grafica4_Container" style="width: 800px; height: 500px;"></div>
    <div id="Grafica5_Container" style="width: 800px; height: 500px;"></div>
    <div id="Grafica6_Container" style="width: 800px; height: 500px;"></div>
    <div id="Grafica7_Container" style="width: 800px; height: 500px;"></div>
  </body>
</html>
"""
f.write(mensaje)
f.close

webbrowser.open('Graficas.html')

#insertar <html>script de python en donde se agrega el html</html>
#Aquí, al final escribir el html y abrir el documento con webbrowser
