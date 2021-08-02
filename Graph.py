from motion_det import df
from bokeh.plotting import figure,show,output_file
from bokeh.models import HoverTool,ColumnDataSource
df['Start_string']=df['START'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['End_string']=df['END'].dt.strftime('%Y-%m-%d %H:%M:%S')
cds = ColumnDataSource(df)
p=figure(x_axis_type='datetime',height=200,width=800,title='MOTION GRAPH')
p.yaxis.minor_tick_line_color=None

hover=HoverTool(tooltips=[('START','@Start_string'),('END','@End_string')])
p.add_tools(hover)
q=p.quad(left="START",right="END",bottom=0,top=1,color="green",source=cds)
output_file("PLOT.html")
show(p)
