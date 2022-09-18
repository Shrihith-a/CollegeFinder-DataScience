# import the libraries

import urllib.request
from datetime import datetime
from tkinter import *
from tkinter.font import Font

from covid import Covid
from matplotlib.pyplot import figure, show
from numpy import array
from pandas import DataFrame
from seaborn import despine, barplot

# create a structure of window

root = Tk()
root.title("SHRI COVID TRACKER")
root.geometry("600x450+500+150")

bluee = '#081D54'
root['bg'] = bluee

big_font = Font(family='Helvetica', size=40, weight='bold')
mid_font = Font(family='Helvetica', size=17, weight='bold')
small_font = Font(family='Helvetica', size=10, weight='bold')
textarea_font = Font(family='Rockwell', size=20, weight='bold')


# checking internet connection of user
def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False


test = connect()
connection = Label(bg=bluee, fg='white', pady=2)
connection.config(text=f'\nConnected: {test}', font=small_font)
connection.pack(fill=X)

heading = Label(text='Shri Covid Tracker', font=big_font, bd=8, bg=bluee, fg='white', pady=1)
heading.pack(fill=X)

enter_country_name_label = Label(text='Enter Country Name', fg='white', bg=bluee, bd=8, pady=1)
enter_country_name_label.pack(fill=BOTH)

enter_country_name = Entry(root, font=textarea_font, justify='center')
enter_country_name.pack(pady=15)
enter_country_name.focus()

country = Label(root, bg=bluee, fg='white', font=mid_font)
country.pack()

confirm = Label(root, bg=bluee, fg='white', font=mid_font)
confirm.pack()

active = Label(root, bg=bluee, fg='white', font=mid_font)
active.pack()

death = Label(root, bg=bluee, fg='white', font=mid_font)
death.pack()

recovered = Label(root, bg=bluee, fg='white', font=mid_font)
recovered.pack()

last_updated = Label(root)


def plotGraph(dfn):
    ndf = dfn[['confirmed', 'deaths']]
    ndf = ndf.T  #
    figure(figsize=(5.5, 5))
    for col in ndf.columns:
        pass
    plot_ = barplot(x=ndf.index, y=col, data=ndf)
    despine()  #
    for p in plot_.patches:
        plot_.annotate(format(p.get_height(), '.1f'), (p.get_width(), p.get_height()),
                       ha='center', va='center',
                       xytext=(0, 9),
                       textcoords="offset points")
    show()


def getData(country_name, country):
    global dfn, recovered_, confirm_, death_, active_, country_
    if test:  # test is true/passed/connected
        data = Covid()
        data = data.get_data()
        df = DataFrame(data)
        country_name = country_name.get()
        dfn = df[country_name == df['country'].str.lower()]
        print(dfn)
        df = array(dfn)
        country_ = df[0][1]
        confirm_ = df[0][2]
        active_ = df[0][3]
        death_ = df[0][4]
        recovered_ = df[0][5]
        time_ = df[0][8] / 1000
        last_update_ = datetime.fromtimestamp(time_).strftime('%d-%m-%Y %H:%M:%S')
        print(last_update_)

        country.configure(text=f"Country: {country_}")
        active.configure(text=f"Active: {active_}")
        death.configure(text=f"Deaths: {death_}")
        confirm.configure(text=f"Confirm: {confirm_}")
        recovered.configure(text=f"Recovered: {recovered_}")
        plotGraph(dfn)


root.bind("<Return>", (lambda x: getData(enter_country_name, country)))

root.mainloop()
