#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: Carlos Minutti Martinez <carlos.minutti@iimas.unam.mx>
@author: Miguel Félix Mata Rivera <mmatar@ipn.mx>


Resumen:
    
    El sistema web desarrollado tiene como objetivo modelar el riesgo espacio-temporal de diferentes tipos de delitos en la Ciudad de México mediante el uso de datos abiertos. Para ello, se utiliza un enfoque basado en mezclas gaussianas, que permite estimar el riesgo relativo de ocurrencia de un delito en un lugar determinado, para diferentes periodos de tiempo específicos.
La exposición a la violencia y el delito puede causar estrés, ansiedad, depresión y otros problemas de salud mental, así como lesiones físicas. Además, la inseguridad puede limitar el acceso a servicios de atención médica y la capacidad de realizar actividades al aire libre, lo que puede afectar la salud de las personas.

La modelización del riesgo de delitos es un aspecto importante en la prevención y control del crimen, y la técnica de mezclas gaussianas ha demostrado ser útil para analizar patrones complejos de datos espaciales y temporales. En este sentido, el sistema web permite a los usuarios visualizar mapas de riesgos, para ser utilizados en posibles análisis de tendencias y comparaciones entre diferentes tipos de delitos y áreas geográficas.

Datos abiertos:
    Carpetas de investigación PGJ
    https://datos.cdmx.gob.mx/dataset/carpetas-de-investigacion-pgj-cdmx
    

Licencia:    
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS


"""

import pandas as pd
import numpy as np
import plotly.express as px 
import plotly.graph_objects as go
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from plotly.subplots import make_subplots

import sqlite3
import matplotlib.pyplot as plt 

from sklearn.mixture import GaussianMixture
from mpl_toolkits.axes_grid1 import make_axes_locatable


class CFG:
    base_dir = './'
    seed = 0
    n_clust = 15
    max_pts = 100



BBox = (-99.3394626438541, -98.9488773, 19.1357929998345, 19.5766097622267)    


delitos_l = ["TODOS",
             "ROBO DE VEHÍCULO CON Y SIN VIOLENCIA", 
            "ROBO A TRANSEUNTE EN VÍA PÚBLICA CON Y SIN VIOLENCIA", 
            "ROBO A NEGOCIO CON VIOLENCIA", 
            "ROBO A REPARTIDOR CON Y SIN VIOLENCIA", 
            "LESIONES DOLOSAS POR DISPARO DE ARMA DE FUEGO", 
            "ROBO A PASAJERO A BORDO DEL METRO CON Y SIN VIOLENCIA", 
            "HOMICIDIO DOLOSO", 
            "ROBO A PASAJERO A BORDO DE MICROBUS CON Y SIN VIOLENCIA", 
            "VIOLACIÓN", 
            "ROBO A CASA HABITACIÓN CON VIOLENCIA", 
            "ROBO A CUENTAHABIENTE SALIENDO DEL CAJERO CON VIOLENCIA", 
            "ROBO A PASAJERO A BORDO DE TAXI CON VIOLENCIA", 
            "ROBO A TRANSPORTISTA CON Y SIN VIOLENCIA", 
            "SECUESTRO"]

def map_plot(pars):
    print(pars)
    
    a1 = pars['anio1']
    a2 = pars['anio2']
    n_clust = pars['n_clust']
    d = pars['delitos']
    d_sql = ''
    
    for (i,x) in enumerate(d):
        d_sql += f'categoria_delito="{x}"'
        if i<(len(d)-1):
            d_sql += ' OR '
            
        
        
    con = sqlite3.connect(CFG.base_dir + 'delitos.sqlite')
    cur = con.cursor()

    delitos = pd.read_sql_query(f'SELECT * FROM pgj WHERE ({d_sql}) AND ao_inicio>={a1} AND ao_inicio<={a2}', con)    
    con.close()
    print(f'SELECT * FROM pgj WHERE ({d_sql}) AND ao_inicio>={a1} AND ao_inicio<={a2}')
    print(delitos)
    
    
    X = delitos[['longitud', 'latitud']]
    idx_na = X.isna().transpose().any()
    
    delitos = delitos[~idx_na]
    X = X[~idx_na]
    
    
    np.random.seed(CFG.seed)
    gm = GaussianMixture(n_components=n_clust, random_state=CFG.seed, n_init=10, init_params='kmeans').fit(X)

    
    rnd = np.random.rand(X.shape[0])
    tmp = rnd.copy()
    tmp.sort()
    samp =  rnd<tmp[CFG.max_pts]
    
    
    x = np.linspace(BBox[0],BBox[1], 50)
    y = np.linspace(BBox[2],BBox[3], 60)
    X_m, Y_m = np.meshgrid(x, y)
    G = pd.DataFrame([X_m.flatten(), Y_m.flatten()]).transpose()
    Z_m = np.exp(gm.score_samples(G))
    Z_m = Z_m.reshape([60,50])
    


    import base64

    map_png = base64.b64encode(open('cdmx2.png', 'rb').read())
    
    fig = go.Figure()
    

    fig.add_trace(
        go.Contour(z=Z_m, x=x, y=y, contours_coloring='lines',
        line_width=2)
    )
    

    fig.add_layout_image(
            dict(
                source='data:image/png;base64,{}'.format(map_png.decode()),
                #source='data:image/svg+xml;base64,{}'.format(map_png.decode()),
                xref="x", yref="y",
                    x=BBox[0], y=BBox[3],
                    sizex=BBox[1]-BBox[0], sizey=BBox[3]-BBox[2],
                    xanchor="left",
                    yanchor="top",
                    #sizing="stretch",
                    layer="below"))
    

    fig.update_layout(template="plotly_white")    


    fig.update_layout(width=int(1000*(BBox[1]-BBox[0])/(BBox[3]-BBox[2])))
    fig.update_layout(height=1000, margin={"r":0,"t":0,"l":0,"b":0})

    return fig



app = dash.Dash(__name__)


edad_list = range(121)
sexo_list = ['M', 'F']
talla_list = range(20, 251)
peso_list = range(201)

app.layout = html.Div([
    html.H1("Delitos en CDMX", style={'text-align': 'center', 'color': '#666666'}),
    
    html.Div("Desde el año:", style={'color': '#333333', 'width':'150px', 'float':'left', 'margin-left':'20px'}),
    html.Div("Hasta el año:", style={'color': '#333333', 'width':'150px', 'float':'left', 'margin-left':'10px'}),
    html.Div("Número de clusters:", style={'color': '#333333', 'width':'150px', 'float':'left', 'margin-left':'10px'}),
    html.Div("Delito:", style={'color': '#333333', 'width':'150px', 'float':'left', 'margin-left':'10px'}),
    html.Br(),

    dcc.Dropdown(
        id='year1-select', 
        options=[{'label': i, 'value': i} for i in range(2016,2020)],
        value=2016,
        style={'width':'150px','float':'left', 'margin-left':'10px'}
    ),
    
    dcc.Dropdown(
        id='year2-select', 
        options=[{'label': i, 'value': i} for i in range(2016,2020)],
        value=2019, 
        style={'width':'150px','float':'left', 'margin-left':'10px'}
    ),

    dcc.Dropdown(
        id='n_clust-select', 
        options=[{'label': i, 'value': i} for i in range(2,21)],
        value=15, 
        style={'width':'150px','float':'left', 'margin-left':'10px'}
    ),

    

    dcc.Dropdown(
        id='delitos-list',
        options=[{'label': f"{i}", 'value': i} for i in delitos_l],
        value=[delitos_l[0]], 
        multi=True,
        searchable=True,
        style={'width':'670px','float':'left', 'margin-left':'10px'}
    ),

    html.Br(),    
    html.P(' ', style={'height':'20px'}),
        
    dcc.Graph(id='delitos-map', figure={})
])




@app.callback(
    Output('delitos-map', 'figure'),
    [Input('year1-select', 'value'),
    Input('year2-select', 'value'),
    Input('n_clust-select', 'value'),
    Input('delitos-list', 'value')]
)
def update_graph_p(anio1, anio2, n_clust, d_lst):

    pars = {}
    pars['anio1'] = anio1
    pars['anio2'] = anio2
    pars['n_clust'] = n_clust

    if pd.Series(delitos_l[0]).isin(d_lst)[0]:
        pars['delitos'] = delitos_l[1:]
    else:
        pars['delitos'] = d_lst

    
    return map_plot(pars)



# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False)