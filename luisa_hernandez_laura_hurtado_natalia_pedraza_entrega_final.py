import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html


app = dash.Dash(__name__)

df_TE = pd.read_excel('base_limpia.xlsx')

df_TE['Año'] = df_TE['FECHA'].dt.year.astype('string')
df_TE['Mes'] = df_TE['FECHA'].dt.month.astype('string')
Teas = df_TE[(df_TE['Año'] == "2021") & (df_TE['TOTALENFERMOS']>0)]
df_TE_t = df_TE[df_TE['FECHA'] == "2021-04-21"]

 
available_provincia = df_TE['PROVINCIA'].unique()
available_tipo_centro = df_TE["TIPO_CENTRO"].unique()
available_gerencia = df_TE["NOMBREGERENCIA"].unique()

tab4 = df_TE['PROVINCIA'].value_counts().rename_axis('label').reset_index(name='counts')
tab4

fig2 = go.Figure(data=[go.Pie(labels=tab4['label'], values=tab4['counts'], hole=.3)])

mean = sum(df_TE['PCR_POSITIVOS'])/len(df_TE['PCR_POSITIVOS'])

Teas1=df_TE[(df_TE['Año'] == "2021")&(df_TE['PCR_POSITIVOS'] > mean)&(df_TE['Mes'] == "1")]

fig4 = px.density_heatmap(df_TE, x="TIPO_CENTRO", y="PROVINCIA", color_continuous_scale="Viridis")

app.layout = html.Div( #Crea una división 
    children=[ #Define que dentro del div van a ahaber varios componentes
        html.H1(children="Entrega final del Proyecto",
            style = {
                        'textAlign': 'center', #Alineado del texto
            }),
        html.P(
          children=" Esta base de datos muestra la evolución de la pandemia de COVID-19 en Castilla "
          " y León, una comunidad autónoma en España, esta evolución se muestra en las diferentes "
          "gerencias del territorio, así como en los centros de salud de estas gerencias diariamente "
          "desde el 29 de febrero del 2020 hasta el 21 de abril del 2021, día cuando se descargó la base."

          " Los datos estaban habilitados para su descarga en la página oficial de la Junta de la comunidad "
          "autónoma de Castilla y León. En este link "

          "https://analisis.datosabiertos.jcyl.es/explore/dataset/tasa-enfermos-acumulados-por-areas-de-salud/table/?disjunctive.zbs_geo&sort=-fech"),
        html.P(
          children=" Para la limpieza de esta base de datos escogimos las variables específicas que utilizaríamos en "
          " el estudio, revisamos la completitud, en la cual no había datos faltantes. posteriormente revisamos la "
          "coherencia, donde no se encontraron datos duplicados. Y por último de cambio el tipo de la variable Fecha de un "
          "objeto a datatime."),

        ### Vis Natalia ###
        html.H2(children="Visualizaciones realizadas por Natalia Pedraza Bastidas "), #Subtitulo de la primera vis
        html.P(
            children="En estas visualizaciones podemos ver una visualización espacial, específicamente un gráfico  "
            "de burbujas y una visualización de datos multivariados, específicamente un donut chart."),
        html.Div([
            html.H1(children='Gráfico 1. Mapa de burbujas'),#
            html.Div(children='''
                 En esta gráfica se puede ver el total de enfermos de las provincias elegidas por el usuario, gracias a la implementación de un filtro, a través 
                 de los cuatro primeros meses del 2021. El número de enfermos se representa con las burbujas, 
                 mientras más grande se muestra la burbuja el número de enfermos en mayor.
                 '''),#
            html.Div(children='''
                
                Provincia
            
            '''),#
            dcc.Dropdown(
                id='crossfilter_provincia',
                options=[{'label': i, 'value': i} for i in available_provincia], #Para cada una de las ciudades imprima el nombre que esta en la posicion del vector
                value='Burgos'
               ),
            dcc.Graph(
                id='example-graph-1'
               ),  
        ], className='six columns'),
### Viz 2 ###
        html.Div([ #Division dentro de la division principal
            html.Div([
                html.H1(children='Gráfico 2. Donut Chart'),#
                html.Div(children='''
                    En esta gráfica podemos ver el porcentaje de los datos que pertenece a cada provincia del estudio.
                    Tiene adicionalmente los porcentajes que pertenecen a cada provincia para que la comprensión de la gráfica sea mayor.
                    '''),
                dcc.Graph(
                    id='example-graph-2',
                    figure=fig2 #Trae la fig 2 que es el pie 
                   ),  
                ], className='six columns'), # 6 columnas, es el limite de la division 
            ]),
        ### Vis Laura ###
        html.H2(children = " Visualizaciones realizadas por Laura Daniela Hurtado Davila "),
         #Subtitulo de la primera vis
        html.P(
            children="En estas visualizaciones podemos ver una visualización espacial, específicamente un gráfico  "
            "de puntos y una visualización de datos multivariados, específicamente heat map."),
            html.Div([ #Division dentro de la division principal
            html.Div([
                html.H1(children='Gráfico 1. Mapa de puntos'),#
                html.Div(children='''
                    Esta visualización muestra la ubicación de los centros médicos de las provincias y el usuario decide si quiere ver los centros
                    que se encuentran en el área urbana o en el área rural por medio del filtro que se le aplicó.
                    '''),
                dcc.Dropdown(
                    id='crossfilter_tipo_centro',
                    options=[{'label': i, 'value': i} for i in available_tipo_centro], #Para cada una de las ciudades imprima el nombre que esta en la posicion del vector
                    value='Urbano'
                   ),
                dcc.Graph(
                    id='example-graph-3'
                   ),  
                ], className='six columns'), # 6 columnas, es el limite de la division 
            html.Div([
                html.H1(children='Gráfico 2. Heat map'),#
                html.Div(children='''
                    Esta visualización muestra una comparación entre el número de centros rurales y urbanos que se encuentran en cada una de las provincias por medio 
                    de un mapa de calor. Mientras el número de centros sea más alto el color del cuadro será más claro. 
                    '''),
                dcc.Graph(
                    id='example-graph-4',
                    figure=fig4 #Trae la fig 3 que es mapa de puntos 
                   ),  
                ], className='six columns'),
            ]),
        html.Div([
          html.H2(children="Visualizaciones realizadas por Luisa Fernanda Hernandez Serrato "), #Subtitulo de la primera vis
          html.P(
            children="En estas visualizaciones podemos ver una visualización espacial, especificamente un gráfico  "
            "de puntos y una visualización de datos multivariados, especificamente un bar chart."),
        html.Div([
            html.H1(children='Gráfico 1. Mapa de puntos'),#
            html.Div(children='''
                Se hizo un mapa de puntos para localizar cada provincia, se utilizó un filtro para diferenciar la parte Rural y Urbana de cada provincia.
            '''),#
            dcc.Checklist(
                id='crossfilter_tipo_Centro',
                options=[{'label': i, 'value': i} for i in available_tipo_centro],
                value=['Rural','Urbano']
                ),
            dcc.Graph(
                id='example-graph-5'
            ),  
        ], className='six columns'),
        
        html.Div([
            html.H1(children='Gráfico 3. Bar Plot'),
            html.Div(children='''
                Se hizo un gráfico de barras para hacer comparaciones entre las gerencias por el número de enfermos del día 21 de abril del 2021
            '''),#
                        html.Div(children='''
                
                Tipo de Contrato
            
           '''),#
            dcc.Dropdown(
                id='crossfilter_Gerencia',
                options=[{'label': i, 'value': i} for i in available_gerencia],
                value=['Gerencia de Burgos','Gerencia de León','Gerencia de Ponferrada',
                'Gerencia de Palencia','Gerencia de Salamanca','Gerencia de Segovia',
                'Gerencia de Soria','Gerencia de Valladolid Oeste','Gerencia de Valladolid Este',
                'Gerencia de Zamora','Gerencia de Ávila'
                ],
                multi = True
                ),
            dcc.Graph(
                id='example-graph-6'
            ),    
        ], className='six columns'),
   ], className='row'),

    ] #cierra el children       
) #Cierra el layout

## Viz 1 Natalia 
## Viz 1 Natalia 
@app.callback( #Arroba define que va a ser un callback 
    dash.dependencies.Output('example-graph-1', 'figure'), #EL output necesita el identificador de la figura y lo segundo es definir que es la figura 
    [dash.dependencies.Input('crossfilter_provincia', 'value')] #definir los imputs de la figura
    )

def update_graph(provincia_value):
    Teas_provincia = Teas[Teas['PROVINCIA'] == provincia_value] #hace un filtro para poner solo los datos de esa ciudad a la vis

    fig1 = px.scatter_geo(Teas_provincia, 
                     lat='y_geo',
                     lon='x_geo', 
                     hover_name="CENTRO",
                     color="PROVINCIA",
                     size="TOTALENFERMOS",
                     animation_frame="Mes", 
                     center = {"lat": 41, "lon": -5},
                     projection="equirectangular")
    fig1.update_layout(
                    title_text = 'Número de enfermos en las diferentes provincias en los 4 meses del 2021',
                    showlegend = True,
                    geo = dict(
                              scope = 'europe',
                              landcolor = 'rgb(217, 217, 217)',
                              )
                    )

    return fig1  


## Viz 1 Laura 
@app.callback( #Arroba define que va a ser un callback 
    dash.dependencies.Output('example-graph-3', 'figure'), #EL output necesita el identificador de la figura y lo segundo es definir que es la figura 
    [dash.dependencies.Input('crossfilter_tipo_centro', 'value')] #definir los imputs de la figura
    )

def update_graph(tipo_centro_value):
    Teas_tipo_centro = Teas1[Teas1['TIPO_CENTRO'] == tipo_centro_value] #hace un filtro para poner solo los datos de esa ciudad a la vis

    fig3 = px.scatter_geo(Teas_tipo_centro, 
                     lat='y_geo',
                     lon='x_geo', 
                     hover_name="CENTRO", 
                     projection="mercator")


    return fig3   

@app.callback(
    dash.dependencies.Output('example-graph-5', 'figure'),
    [dash.dependencies.Input('crossfilter_tipo_Centro', 'value')]
    )

def update_graph(Tipo_C):
    df_TE_TC = df_TE[df_TE['TIPO_CENTRO'].isin(Tipo_C)]
    
    fig5 = px.scatter_mapbox(df_TE_TC, 
                     lat='y_geo',
                     lon='x_geo',
                     color="PROVINCIA",
                     center = {"lat":41.763667, "lon": -3.74922},zoom=6)
    fig5.update_layout(mapbox_style="open-street-map")
    fig5.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
    return fig5  


@app.callback(
    dash.dependencies.Output('example-graph-6', 'figure'),
    [dash.dependencies.Input('crossfilter_Gerencia', 'value')]
    )


def update_graph(Gerencia):
    df_TE_TC = df_TE_t[df_TE_t['NOMBREGERENCIA'].isin(Gerencia)]
    fig6 = px.bar(df_TE_t, x="NOMBREGERENCIA",
             y="TOTALENFERMOS", 
             color="NOMBREGERENCIA",
             title="Número de enfermos por gerencia")

    return fig6




if __name__ == "__main__":
    app.run_server(debug=True) #para finalizar la aplicación y que empiece a correr el server local 



