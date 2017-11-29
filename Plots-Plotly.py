import plotly.plotly as py
import plotly
import plotly.graph_objs as go
import numpy as np
import Functions as fn


X = np.arange(-10, 10, 0.05)
Y = np.arange(-10, 10, 0.05)
X, Y = np.meshgrid(X, Y)


funcparam = fn.bentCig
Z = funcparam([X,Y])


data = [go.Surface(z=Z,x=X,y=Y ,colorscale='Viridis')]

layout = go.Layout(
    width=1000,
    height=1000,
    autosize=False,
    title=str(funcparam.func_name)+' Plot',
    scene=dict(
        xaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        yaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        zaxis=dict(
            gridcolor='rgb(255, 255, 255)',
            zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,
            backgroundcolor='rgb(230, 230,230)'
        ),
        aspectratio = dict( x=1, y=1, z=0.7 ),
        aspectmode = 'manual'
    )
)

fig = dict(data=data, layout=layout)
plotly.offline.plot(fig, filename='./Plots/'+str(funcparam.func_name)+'.html')
#print data
