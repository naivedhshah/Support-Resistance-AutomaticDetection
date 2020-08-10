from pandas_datareader import data
from datetime import datetime as dt
import pandas
import datetime
from bokeh.plotting import figure,show,output_file
from bokeh.io import output_file, show
from bokeh.models import RangeSlider
from bokeh.io import output_file, show
from bokeh.models import Panel, Tabs
from bokeh.plotting import figure
from bokeh.models import *
from bokeh.layouts import *
from bokeh.plotting import figure
from bokeh.models.widgets import RadioButtonGroup
from bokeh.io import *
from datetime import date 
  
  
# Returns the current local date 
today =str(date.today())
today1=today.replace('-',',')
print(today1)
today1=today1.replace('(',' ')
today1=today1.replace(')',' ')
today1=today1.split(',')
year=int(today1[0])
month=int(today1[1])
day=int(today1[2])

start=datetime.datetime(2015,11,2)
end=datetime.datetime(2020,5,19)
df=data.DataReader(name="AAPL",data_source="yahoo",start=start,end=end)
#df=pandas.read_csv('data.csv')
#df

f=figure(x_axis_type="datetime",height=300,width=1000)
#f.title="CANDLESTICK CHART"
#,sizing_mode="scale_width"
"""text_input = TextAreaInput(value="default", rows=6, title="Label:")

show(text_input)"""
"""def my_text_input_handler(attr, old, new):
    print("Previous label: " + old)
    print("Updated label: " + new)

text_input = TextInput(value="default", title="Label:")
text_input.on_change("value", my_text_input_handler)


output_file("radio_button_group.html")

radio_button_group = RadioButtonGroup(
        labels=["Option 1", "Option 2", "Option 3"], active=0)

show(vform(radio_button_group))
"""
#df

def inc_dec(c,o):
    if c>o:
        value="increase"
    elif c<o:
        value="decrease"
    else:
        value="equal"
    return value


df['Status']=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)] 
df["Middle"]=(df.Open+df.Close)/2
df['Height']=abs(df.Close-df.Open)

#df

hours_12=12*60*60*1000
f.segment(df.index,df.High,df.index,df.Low,color="Black")

#x=[range()]

f.rect(df.index[df.Status=='increase'],df.Middle[df.Status=='increase'],hours_12,df.Height[df.Status=='increase'],fill_color='green',line_color='black')

f.rect(df.index[df.Status=='decrease'],df.Middle[df.Status=='decrease'],hours_12,df.Height[df.Status=='decrease'],fill_color='red',line_color='black')



f.grid.grid_line_alpha=1


f.line([dt(2015, 1, 1),dt(year,month,day)],[150,150], line_width=5, color="green", alpha=0.5)

output_file('Candlestick.html')



"""range_slider = RangeSlider(start=0, end=10, value=(1,9), step=.1, title="Stuff")
show(range_slider)
output_file("range_slider.html")"""


show(f)



"""

p = gridplot([[f,text_input,p]], toolbar_location=None)

show(p)
"""
#show(column(f, text_input))
