import random
import tkinter
from tkinter import *
from tkinter import messagebox
import random
import tkinter
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
from bokeh.io import output_file, show
from bokeh.models import Select
global stockname

#from decimal import Decimal



w2=Tk()

def trial():
    global stockname
    print(e1.get())
    stockname=e1.get()
    print(stockname)
    #stockname='AAPL'
    #w2=tkinter.Toplevel(root)
    w2.title("Staff LOGIN")
    w2.geometry("600x200")
    #Returns the current local date 
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
    end=datetime.datetime(2020,5,15)
    df=data.DataReader(name=stockname,data_source="yahoo",start=start,end=end)
    #df=pandas.read_csv('data.csv')
    print(df)


    #TRIAL SPACE
    
    max_week=0
    i=0
    j=i+4
    u=0
    maxweek=[]
    minweek=[None]
    week_open=0
    week_close=0
    weekopen=[]
    weekclose=[]
    a=0
    u=0
    #SORTING DATES ON WEEKLY BASIS
    c=0
    xyzz=len(df.index)
    #print(xyzz)
    frowfordate=xyzz%5
    tuub=0
    list1=[]
    for xx in df.index:
        tuub+=1

        if tuub>(xyzz-frowfordate):
            break

        if c%5==0:
            list1.append(xx)
        c+=1



    print(list1)
    print(len(list1))
    ########################################3
    y=len(df.High)
    filterrows=y%5
    tuu=0
    #SORTING HIGH AND LOW ON WEEKLY BASIS
    for x in df.High:
        
        if x>=max_week:
            max_week=x
            #a=1
            
       
        u+=1   
        if u%5==0:
            maxweek.append(max_week)
            max_week=0


        
        tuu+=1
        if tuu>(y-filterrows):
            break
            
        
        

        
    lowweek=[]
    lowest=99999
    lendf=len(df.High)
    filtering=lendf%5
    tuup=0
    u=0
    #SORTING HIGH AND LOW ON WEEKLY BASIS
    for x in df.Low:
        
        if x<=lowest:
            lowest=x
            
            
       
        u+=1   
        if u%5==0:
            lowweek.append(lowest)
            lowest=99999


        
        tuup+=1
        if tuup>(lendf-filtering):
            break


    print(lowweek)
    print(len(lowweek))
        

            
    new=pandas.DataFrame()
    df.to_csv('withoutheader.csv',header=None)
    new=pandas.read_csv('withoutheader.csv')
    c=0
    counter=0
    xyz=len(df.Open)
    frowforopen=xyz%5
    for x in df.Open:
        counter+=1
        if counter>(xyz-frowforopen):
            break
        if c%5==0:
            weekopen.append(x)
        c+=1
        


    df.to_csv('AAPL12.csv')
    print(len(maxweek))
    print(maxweek)

    counterr=0
    weekclose=[]
    xxyy=len(df.Close)
    frowforclose=xxyy%5
    rownum=0
    for x in df.Close:
        rownum+=1
        counterr+=1
        
        if counterr>(xxyy-frowforclose):
            break
        
        if rownum%5==0:
            weekclose.append(x)  


    print('_______________________________________________________')
    #print(len(weekopen))     
    #print(weekopen)

    new1=pandas.DataFrame()
    new1['Date']=list1
    new1['High']=maxweek
    new1['Low']=lowweek
    new1['Open']=weekopen
    new1['Close']=weekclose
    #print(len(new1))
    #print('end')






    
    """
    low=[]
    for x in df.Low:
       # x=format(x, '.2f')
        #x=
       # print(type(x))
        low.append(round(x,2))
    print(low)
    """

    f=figure(x_axis_type="datetime",height=300,width=1000)
    #f.title="CANDLESTICK CHART"
    #,sizing_mode="scale_width"
    
    #df

    def inc_dec(c,o):
        if c>o:
            value="increase"
        elif c<o:
            value="decrease"
        else:
            value="equal"
        return value


    new1['Status']=[inc_dec(c,o) for c,o in zip(new1.Close,new1.Open)] 
    new1["Middle"]=(new1.Open+new1.Close)/2
    new1['Height']=abs(new1.Close-new1.Open)

    #df

    hours_12=12*60*60*1000*7
    f.segment(new1.Date,new1.High,new1.Date,new1.Low,color="Black")

    #x=[range()]

    f.rect(new1.Date[new1.Status=='increase'],new1.Middle[new1.Status=='increase'],hours_12,new1.Height[new1.Status=='increase'],fill_color='green',line_color='black')

    f.rect(new1.Date[new1.Status=='decrease'],new1.Middle[new1.Status=='decrease'],hours_12,new1.Height[new1.Status=='decrease'],fill_color='red',line_color='black')



    f.grid.grid_line_alpha=1


    f.line([dt(2015, 1, 1),dt(year,month,day)],[150,150], line_width=5, color="green", alpha=0.5)
    strfilename=stockname+".html"
    output_file(strfilename)

    """bt3=tkinter.Button(w2,text ="DISPLAY",command=trial)
    bt3.pack()"""

    print(new1)
   

    
    show(f)
   
    

    output_notebook()



    output_file("select.html")

   # f = Select(title="Option:", value="foo", options=["foo", "bar", "baz", "quux"])

    show(f)
    
    
    #show(column(f, text_input))
    w2.withdraw()



"""pic3 = PhotoImage(file="C:\\Users\\Nilesh\\OneDrive\\Desktop\\sem4\\EXAMINATION MANAGEMENT f\\pics\\images.png")
w = Label(image=pic3, anchor=NW)
w.photo = pic3
w.place(x=300,y=100)"""
  

l8=tkinter.Label(w2,text="Mention the Ticker Symbol of the Company ")
l8.pack()
stockname=StringVar()
e1=tkinter.Entry(w2,textvariable=stockname)
e1.pack()
bt2=tkinter.Button(w2,text ="RETRIEVE",command=trial)
bt2.pack()



