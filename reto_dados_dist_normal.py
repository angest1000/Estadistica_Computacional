# Generar un programa que lance 2 dados 
# y que al sacar la media de la sumatoria de los 2 dados
# para generar una distribucion normal
import random
from estadisticas import media,desviacion_estandar
import numpy as np
import scipy.special

from bokeh.layouts import gridplot
from bokeh.plotting import figure, output_file, show


def lanzar_dado():
    return random.randint(1,6)

def lanzamientos(numero_de_lanzamientos,numero_de_dados):
    
    resultados_dados = []

    for _ in range(numero_de_lanzamientos):
        res = 0
        for _ in range(numero_de_dados):
            res = res + lanzar_dado()
        resultados_dados.append(res)
        
    # print(resultados_dados)
    return resultados_dados

def make_plot(title, hist, edges, x, pdf, cdf):
    p = figure(title=title, tools='', background_fill_color="#fafafa")
    p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],
           fill_color="navy", line_color="white", alpha=0.5)
    p.line(x, pdf, line_color="#ff8888", line_width=4, alpha=0.7, legend_label="Funcion de densidad")
    p.line(x, cdf, line_color="orange", line_width=2, alpha=0.7, legend_label="Funcion de distribucion")

    p.y_range.start = 0
    p.legend.location = "center_right"
    p.legend.background_fill_color = "#fefefe"
    p.xaxis.axis_label = 'x'
    p.yaxis.axis_label = 'P(x)'
    p.grid.grid_line_color="white"
    return p

def main():
       
    numero_de_dados = int(input('¿Cuantos dados deseas simular?: '))   
    numero_de_lanzamientos = int(input('¿Cuantas veces los lanzaras?: '))
    muestras = int(input('¿Cuantas veces se repetira el experimento?: '))

    promedio_lanzamientos = []

    for _ in range(muestras):
        resultado = lanzamientos(numero_de_lanzamientos,numero_de_dados)

        promedio_lanzamientos.append(media(resultado))

    hist, edges = np.histogram(promedio_lanzamientos, density=True)

    mu = media(promedio_lanzamientos)
    sigma = desviacion_estandar(promedio_lanzamientos)

    print(mu)
    print(sigma)

    x = np.linspace(2, 12, 1000)
    pdf = 1/(sigma * np.sqrt(2*np.pi)) * np.exp(-(x-mu)**2 / (2*sigma**2))
    cdf = (1+scipy.special.erf((x-mu)/np.sqrt(2*sigma**2)))/2

    p1 = make_plot(f"Distribucion (μ={mu}, σ={sigma})\nMuestras: {muestras}", hist, edges, x, pdf, cdf)
    
    output_file('histogram.html', title="histogram.py")

    show(p1, plot_width=400, plot_height=400, toolbar_location=None)

if __name__ == "__main__"   :
    main()