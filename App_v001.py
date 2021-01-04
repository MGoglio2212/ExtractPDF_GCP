# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:48:20 2020

@author: gogliom
"""


import os
#os.chdir("D:\Altro\RPA\Energy\IREN\TEST CTE\App\Funzioni")

#Dir = r"D:\Altro\RPA\Energy\IREN\TEST CTE\CTE\esempi cte"

######################

import pandas as pd
import base64
from urllib.parse import quote as urlquote
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_table as dt
from flask import Flask, send_from_directory
#from HomePage2 import Homepage2
#from HomePage2 import Navbar
from FilterBanner import FilterBanner #, FilterBanner_SelezionaFolder
#from FilterBanner_SelezionaFolder import SelezionaFolder

#from Funzioni.ProvePrezzo import PrezzoComponenteEnergia
#from Funzioni.ProveDurata import Durata
#from Funzioni.ProveQuoteFissaAnno import PrezzoComponenteCommVendita  

#from Loop import ElabFile, Cicla

######################


#UPLOAD_DIRECTORY = "app_uploaded_files"

#if not os.path.exists(UPLOAD_DIRECTORY):
#    os.makedirs(UPLOAD_DIRECTORY)


# Normally, Dash creates its own Flask server internally. By creating our own,
# we can create a route for downloading files directly:
server = Flask(__name__)
app = dash.Dash(server=server)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.UNITED],
                meta_tags=[{"name": "viewport", "content": "width = device-width"}])
app.layout = html.Div([
    dcc.Location(id = 'url', refresh = False),
    html.Div(id = 'page-content')
])




'''outputPrezzoUnitario = html.Div(id = 'outputPrezzoUnitario',
                children = [],
                className="pretty_container",
                )
'''



outputName = html.Div([html.H6(id="outputName"), html.P("Nome offerta")],
                                        id="outputName",
                                        className="mini_container",)


outputPrezzoUnitario = html.Div([html.H6(id="outputPrezzoUnitario"), html.P("Prezzo Unitario Energia")],
                                        id="outputPrezzoUnitario",
                                        className="mini_container",)

outputDurata = html.Div([html.H6(id="outputDurata"), html.P("Durata Condizioni")],
                                        id="outputDurata",
                                        className="mini_container",)

outputPrezzoCV = html.Div([html.H6(id="outputPrezzoCV"), html.P("Quota Commercializzazione Vendita")],
                                        id="outputPrezzoCV",
                                        className="mini_container",)

outputCodice = html.Div([html.H6(id="outputCodice"), html.P("Codice Offerta")],
                                        id="outputCodice",
                                        className="mini_container",)

outputSpesaAnnua = html.Div([html.H6(id="outputSpesaAnnua"), html.P("Spesa Annua €")],
                                        id="outputSpesaAnnua",
                                        className="mini_container",)


outputPrezzoFasciaF1 = html.Div([html.H6(id="outputPrezzoFasciaF1"), html.P("Prezzo Fascia F1")],
                                        id="outputPrezzoFasciaF1",
                                        className="mini_container",)

outputPrezzoFasciaF2 = html.Div([html.H6(id="outputPrezzoFasciaF2"), html.P("Prezzo Fascia F2")],
                                        id="outputPrezzoFasciaF2",
                                        className="mini_container",)

outputPrezzoFasciaF3 = html.Div([html.H6(id="outputPrezzoFasciaF3"), html.P("Prezzo Fascia F3")],
                                        id="outputPrezzoFasciaF3",
                                        className="mini_container",)

outputScadenza = html.Div([html.H6(id="outputScadenza"), html.P("Data fine validità offerta")],
                                        id="outputScadenza",
                                        className="mini_container",)

outputTipoPrezzo = html.Div([html.H6(id="outputTipoPrezzo"), html.P("Tipologia Prezzo")],
                                        id="outputTipoPrezzo",
                                        className="mini_container",)



OutputButton = html.Div(id='textarea-state-example-output', className = "mini_container", style={'whiteSpace': 'pre-line'})


#layout per la pagina di seleziona cartella ed elabora tutto 
'''
def AppElaboraFolder():
    layout = html.Div([
    Navbar(),
    html.Br(),
    #dbc.Row(nav, style = {'width':'100%'}),
    #dbc.Row(header),
    dbc.Row(
        [
            dbc.Col(FilterBanner_SelezionaFolder(),width = 3),
            dbc.Col(
                [dbc.Row(PlaceHolder)
                 ,
                 dbc.Row(
                     dbc.Col(OutputButton)
                     )
                 ],
                id="right-column",
                className="eight columns"
                #width=6,
                #style={}
              ),
                
        ]
    )
    ])    
    
    return layout


#callback per lanciare programma che elabora tutta cartella
@app.callback(
    Output('textarea-state-example-output', 'children'),

    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
     dash.dependencies.Input('commodity', 'value')],
    State('textarea-state-example', 'value')
    )
def update_output(n_clicks, commodity, value):
    if n_clicks > 0:
        df = Cicla(value)
        df = df[df['Commodity'] == commodity]
        data = df.to_dict('rows')
        columns =  [{"name": i, "id": i,} for i in (df.columns)]
        return dt.DataTable(data=data, columns=columns)
'''      



#layout per la pgina di carica file 

'''
def AppCaricaFile():
    layout = html.Div(
        [  
            html.H1("File Browser"),
            html.H2("Upload"),
            dcc.Upload(
                id="upload-data",
                children=html.Div(
                    ["Drag and drop or click to select a file to upload."]
                ),
                style={
                    "width": "100%",
                    "height": "60px",
                    "lineHeight": "60px",
                    "borderWidth": "1px",
                    "borderStyle": "dashed",
                    "borderRadius": "5px",
                    "textAlign": "center",
                    "margin": "10px",
                },
                multiple=True,
            ),
            
            html.Button('Submit', id='button'),
            html.Div(id='output-container-button',
            children='Enter a value and press submit'),     
            
            html.H2("File List"),
            html.Ul(id="file-list"),
        ],
        style={"max-width": "500px"},
    )
    return layout
'''

PlaceHolder = []




def AppCaricaFile():
        layout = html.Div([
        #Navbar(),
        html.Br(),
        #dbc.Row(nav, style = {'width':'100%'}),
        #dbc.Row(header),
        dbc.Row(
            [
                dbc.Col(FilterBanner(),width = 3),
                '''
                dbc.Col(
                    [dbc.Row(PlaceHolder)
                     ,
                     dbc.Row(
                         dbc.Col(outputName)
                         ),
                     dbc.Row(
                         dbc.Col(outputSpesaAnnua)
                         ),
                     dbc.Row(
                         dbc.Col(outputPrezzoUnitario)
                         ),
                     dbc.Row(
                         dbc.Col(outputTipoPrezzo)
                         ),

                     dbc.Row(
                         [dbc.Col(outputPrezzoFasciaF1)
                          ,dbc.Col(outputPrezzoFasciaF2)
                          ,dbc.Col(outputPrezzoFasciaF3)
                          ]
                         ),
                     dbc.Row(
                         dbc.Col(outputPrezzoCV)
                         ),
                     
                     dbc.Row(
                         dbc.Col(outputDurata)
                         ),
                     dbc.Row(
                         dbc.Col(outputScadenza)
                         ),
                     
                     dbc.Row(
                         dbc.Col(outputCodice)
                         ),
    
                     ],
                    id="right-column",
                    className="eight columns"
                    #width=6,
                    #style={}
                  ),
            '''                    
            ]
        )
        
        ])    


        return layout


'''
@server.route("/download/<path:path>")
def download(path):
    """Serve a file from the upload directory."""
    return send_from_directory(UPLOAD_DIRECTORY, path, as_attachment=True)



def save_file(name, content):
    """Decode and store a file uploaded with Plotly Dash."""
    data = content.encode("utf8").split(b";base64,")[1]
    with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
        fp.write(base64.decodebytes(data))


def uploaded_files():
    """List the files in the upload directory."""
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return files


def file_download_link(filename):
    """Create a Plotly Dash 'A' element that downloads a file from the app."""
    location = "/download/{}".format(urlquote(filename))
    return html.A(filename, href=location)
'''

#gestione degli indirizzi dalla navbar
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def display_page(pathname):
        if pathname == '/CaricaFile':
            return AppCaricaFile()
        elif pathname == '/SelezionaCartella':
            return AppCaricaFile()
        else:
            return AppCaricaFile()

'''
#callback per caricamento file 
@app.callback(
    Output("file-list", "children"),
    [Input("upload-data", "filename"), Input("upload-data", "contents")],
)
def update_output(uploaded_filenames, uploaded_file_contents):
    """Save uploaded files and regenerate the file list."""

    if uploaded_filenames is not None and uploaded_file_contents is not None:
        for name, data in zip(uploaded_filenames, uploaded_file_contents):
            save_file(name, data)

    files = uploaded_files()
    if len(files) == 0:
        return [html.Li("No files yet!")]
    else:
        return [html.Li(file_download_link(filename)) for filename in files]

'''





'''
directory = Dir

#callback per nome offerta
@app.callback(
    dash.dependencies.Output("outputName", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_Nome(n_clicks, filename, commodity):
    if n_clicks >0:
        Out = ElabFile(directory, filename)
        Out = Out[Out['Commodity'] == commodity]
        Out = Out['Name']
        if filename == "All":
            return ""
        else:
            return Out    

#callback per spesaannua
@app.callback(
    dash.dependencies.Output("outputSpesaAnnua", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_SpesaAnnua(n_clicks, filename, commodity):
    if n_clicks >0:
        Out = ElabFile(directory, filename)
        Out = Out[Out['Commodity'] == commodity]
        Out = Out['StimaSpesaAnnua']
        if filename == "All":
            return ""
        else:
            return Out    


#callback per prezzoUnitario
@app.callback(
    dash.dependencies.Output("outputPrezzoUnitario", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_PrezzoComponenteEnergia(n_clicks, filename, commodity):
    if n_clicks >0:
        O = ElabFile(directory, filename)
        O = O[O['Commodity'] == commodity]
        O = O['Price']
        
        Out = ""
        Out = ''.join([str(elem) for elem in O])
        Out = Out.replace("['","")
        Out = Out.replace("']","")

        if filename == "All":
            return ""
        else:
            return Out    

#callback per tipoprezzo
@app.callback(
    dash.dependencies.Output("outputTipoPrezzo", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_TipoPrezzo(n_clicks, filename, commodity):
    if n_clicks >0:
        O = ElabFile(directory, filename)
        O = O[O['Commodity'] == commodity]
        O = O['TipoPrezzo']
        
        Out = ""
        Out = ''.join([str(elem) for elem in O])
        Out = Out.replace("['","")
        Out = Out.replace("']","")

        if filename == "All":
            return ""
        else:
            return Out    

#callback per prezzo F1
@app.callback(
    dash.dependencies.Output("outputPrezzoFasciaF1", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_PrezzoComponenteFasciaF1(n_clicks, filename, commodity):
    if n_clicks >0:
        O = ElabFile(directory, filename)
        O = O[O['Commodity'] == commodity]
        O = O['F1']
        
        Out = ""
        Out = ''.join([str(elem) for elem in O])
        Out = Out.replace("['","")
        Out = Out.replace("']","")
        if filename == "All":
            return ""
        else:
            return Out    


#callback per prezzo F2
@app.callback(
    dash.dependencies.Output("outputPrezzoFasciaF2", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_PrezzoComponenteFasciaF2(n_clicks, filename, commodity):
    if n_clicks >0:
        O = ElabFile(directory, filename)
        O = O[O['Commodity'] == commodity]
        O = O['F2']
        
        Out = ""
        Out = ''.join([str(elem) for elem in O])
        Out = Out.replace("['","")
        Out = Out.replace("']","")
        
        if filename == "All":
            return ""
        else:
            return Out    



#callback per prezzo F3
@app.callback(
    dash.dependencies.Output("outputPrezzoFasciaF3", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_PrezzoComponenteFasciaF3(n_clicks, filename, commodity):
    if n_clicks >0:
        O = ElabFile(directory, filename)
        O = O[O['Commodity'] == commodity]
        O = O['F3']
        
        Out = ""
        Out = ''.join([str(elem) for elem in O])
        Out = Out.replace("['","")
        Out = Out.replace("']","")
        if filename == "All":
            return ""
        else:
            return Out    




#callback per durata
@app.callback(
    dash.dependencies.Output("outputDurata", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_Durata(n_clicks, filename, commodity):
    if n_clicks >0:
        Out = ElabFile(directory, filename)
        Out = Out[Out['Commodity'] == commodity]
        Out = Out['Durata']
        if filename == "All":
            return ""
        else:
            return Out    

#callback per prezzo cv
@app.callback(
    dash.dependencies.Output("outputPrezzoCV", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_PrezzoCV(n_clicks, filename, commodity):
    if n_clicks >0:
        Out = ElabFile(directory, filename)
        Out = Out[Out['Commodity'] == commodity]
        Out = Out['PrezzoCV']
        if filename == "All":
            return ""
        else:
            return Out    

#callback per scadenza
@app.callback(
    dash.dependencies.Output("outputScadenza", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_Scadenza(n_clicks, filename, commodity):
    if n_clicks >0:
        Out = ElabFile(directory, filename)
        Out = Out[Out['Commodity'] == commodity]
        Out = Out['Scadenza']
        if filename == "All":
            return ""
        else:
            return Out    



#callback per codice
@app.callback(
    dash.dependencies.Output("outputCodice", "children"),
    [dash.dependencies.Input('textarea-state-example-button', 'n_clicks'),
    dash.dependencies.Input('filename', 'value'),
     dash.dependencies.Input('commodity', 'value')])
def Res_Codice(n_clicks, filename, commodity):
    if n_clicks >0:
        Out = ElabFile(directory, filename)
        Out = Out[Out['Commodity'] == commodity]
        Out = Out['CodiceOfferta']
        if filename == "All":
            return ""
        else:
            return Out    
'''    

server = app.server
app.config.suppress_callback_exceptions = True

if __name__ == "__main__":
    app.run_server(debug=True, port=8000)