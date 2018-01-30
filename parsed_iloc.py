import pandas as pd
import numpy as np
from bokeh.plotting import figure,output_file,show

data = pd.read_csv('collagedata.csv')

pdata = data.iloc[:,0:3]

y = pdata.iloc[:,1]


y1 = pdata.iloc[:,0]

x = np.arange(1,int(len(y)+1))

output_file = 'outfile.html'
p = figure(width = 500, height = 600, title = 'My new Graph', tools = ['pan','hover'])

p.scatter(x,y, fill_alpha =0.2, size = 10, color = 'red')
p.scatter(x,y1, fill_alpha =0.2, size = 10, color = 'orange')

show(p)


