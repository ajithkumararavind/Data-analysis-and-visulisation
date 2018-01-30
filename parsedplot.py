import numpy as np
import pandas as pd

data = pd.read_csv('collagedata.csv')

pdata = data.loc[:,'UNITID':'OPEID6']
nos = pdata.shape[0]
x = np.arange(1,int(nos)+1)

y = pdata['UNITID']
y1 = pdata['OPEID']
y2 = pdata['OPEID6']


from bokeh.plotting import figure, show, output_file

output_file = 'outfile.html'
p = figure(title = 'Title of the Graph')

p.circle(x,y, size = 10, color = 'red', fill_alpha = 0.2)
p.circle(x, y1, size = 10, color = 'blue', fill_alpha = 0.2)

p.circle(x,y2, size =10, color = 'orange', fill_alpha = 0.2)

show(p)
