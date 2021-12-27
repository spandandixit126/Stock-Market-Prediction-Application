import csv
import time
import webbrowser
from sys import exit
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *

import matplotlib.pyplot as plt
# import os    # if required import it!!!
import pandas
import pandas as pd
import yfinance as yf
from PIL import ImageTk, Image
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.figure import Figure
from numpy import *
from tkcalendar import DateEntry

print("© By SPANDAN DIXIT(18012011018)")
root = Tk()

lengthdata = 0
avgopen = 0.0
avgclose = 0.0


def calopen_close():
    try:
        print(csv)
        path = "F:\\Python Apps\\SMPA\\STOCKDATA\\" + e1.get() + radio.get() + ".csv"
        file = open(path, newline='')
        reader = csv.reader(file)
        # the first line is header having all the string parts
        # contains information about each and specific column
        header = next(reader)
        data = [row for row in reader]
        opentemp, closetemp = 0.0, 0.0
        temp1 = 0
        for i in range(len(data)):
            o1 = data[i][2].replace(",", "")
            c1 = data[i][7].replace(",", "")
            opentemp = opentemp + float(o1)
            closetemp = closetemp + float(c1)
            temp1 = i
        opentemp2 = opentemp / (temp1 + 1)
        closetemp2 = closetemp / (temp1 + 1)
        global lengthdata
        lengthdata = temp1
        global avgopen
        avgopen = opentemp2
        global avgclose
        avgclose = closetemp2
        # l2.config(text="Average CLOSE Price of Share is :{}".format(closetemp2))
        # l3.config(text="Average OPEN Price of Share :{}".format(opentemp2))
        l7.config(text='last Active Stock Session of ' + e1.get().upper() + ' is:' + str(data[0][0]))
        l6.config(
            text='This Calculation Data is based on the term from : ' + str(data[temp1][0]) + ' To : ' + str(
                data[0][0]))
        sby2.place(x=315, y=200, height=212)
        sbx2.place(x=10, y=413, width=304)
        lb2.delete(0, END)
        lb2.config(yscrollcommand=sby2.set, xscrollcommand=sbx2.set)
        lb2.insert(1, "1)" + "Last OPEN Price :{}".format(data[0][2]))
        lb2.insert(2, "2)" + "Last HIGH Price :{}".format(data[0][3]))
        lb2.insert(3, "3)" + "Last LOW Price :{}".format(data[0][4]))
        lb2.insert(4, "4)" + "Last Previous Close Price :{}".format(data[0][5]))
        lb2.insert(5, "5)" + "Last Traded Price :{}".format(data[0][6]))
        lb2.insert(6, "6)" + "Last CLOSE Price :{}".format(data[0][7]))
        lb2.insert(7, "7)" + "52W HIGH Price :{}".format(data[0][9]))
        lb2.insert(8, "8)" + "52W LOW Price :{}".format(data[0][10]))
        lb2.insert(9, "9)" + "Last Traded Volume :{}".format(data[0][11]))
        lb2.insert(10, "10)" + "Last Traded Value :{}".format(data[0][12]))
        lb2.insert(11, "11)" + "Last Number Of Trades :{}".format(data[0][13]))
        lb2.insert(12, "12)" + "Average OPEN Price :{}".format(opentemp2))
        lb2.insert(13, "13)" + "Average CLOSE Price :{}".format(closetemp2))
        lb2.place(x=10, y=200)
        sbx2.config(command=lb2.xview)
        sby2.config(command=lb2.yview)

    except:
        lb2.place_forget()
        sbx2.place_forget()
        sby2.place_forget()
        l6.config(text='This Prediction Data is based on the term from : None To : None')
        print("File not available in your local system")
        msgbox3 = messagebox.showwarning("Error!!! 404 Not Found!!!",
                                         "an error occured while checking your file in local storage\n"
                                         "This error occures when the"
                                         " file you are requesting for is not available there...\n"
                                         "if an error occured more than one time than please download "
                                         "again the file you are looking for...\n")


def download():
    capstock = e1.get().upper()
    print(capstock)
    if capstock != '':
        msgbox1 = messagebox.askquestion("you are about to redirecting to nse india...",
                                         "Download latest Historical data to predict...\n"
                                         "If you find any error like bad gateway please reload the site...\n"
                                         "Click Ok to Redirect")
        print(msgbox1)
        if msgbox1 == 'yes':
            url = "https://www.nseindia.com/get-quotes/equity?symbol=" + capstock
            webbrowser.open_new(url)
            msgbox2 = messagebox.showinfo("Info",
                                          "Download historical data and rename that .csv file to stockname.csv "
                                          "(e.g. RELIANCE.NS.csv)\nPut this file to SMPA Folder")
    else:
        mes1()


def graph():
    try:
        if mes1():
            raise ValueError
        else:
            bar = Progressbar(root, length=220, style='black.Horizontal.TProgressbar')
            bar.place(x=1000, y=670)
            bar['value'] = 33
            root.update_idletasks()
            time.sleep(1)
            graphstr = e1.get().upper() + radio.get()
            fig.set_facecolor("orange")
            stli = graphstr.split()
            graph1 = fig.add_subplot()
            graph1.clear()
            fig.autofmt_xdate()
            stli2 = []
            str = ''
            for element in stli:
                data = yf.download(element)
                if data.empty:
                    str = str + element + ' '
                else:
                    graph1.plot(data['Adj Close'])
                    stli2.append(element)
            bar['value'] = 66
            root.update_idletasks()
            graph1.legend(stli2)
            canvas.draw()
            canvas.get_tk_widget().place(x=850, y=120)
            toolbar.update()
            toolbar.place(x=1000, y=500)
            if str != '':
                l15.config(text=str + 'neither available nor delisted')
                l15.place(x=850, y=460)
            else:
                l15.place_forget()
            bar['value'] = 100
            root.update_idletasks()
            l14.place(x=850, y=120)
            l12.place(x=850, y=140)
            d1.place(x=910, y=140)
            l13.place(x=1020, y=140)
            d2.place(x=1070, y=140)
            cb.place(x=1180, y=140)
            b7.place(x=1280, y=135)
            b8.place(x=1280, y=455)
            bar.place_forget()

            def expand():
                nonlocal data
                plt.clf()
                plt.close('all')
                str1 = ''
                if cb.get() != '':
                    for element in stli2:
                        data = yf.download(element, d1.get(), d2.get())
                        if data.empty:
                            pass
                        else:
                            str1 = str1 + element + ' '
                        plt.plot(data[cb.get()])

                else:
                    for element in stli:
                        data = yf.download(element)
                        if data.empty:
                            pass
                        else:
                            str1 = str1 + element + ' '
                        plt.plot(data['Adj Close'])
                plt.legend(stli2)
                plt.title(str1 + 'Expanded View')
                plt.grid(True)
                plt.xlabel("Dates")
                plt.ylabel("Price")
                plt.show()

            def recal():
                graph1.clear()
                nonlocal data
                for element in stli2:
                    data = yf.download(element, d1.get(), d2.get())
                    graph1.plot(data[cb.get()])
                graph1.legend(stli2)
                fig.autofmt_xdate(bottom=0.2, rotation=30, ha='right')
                canvas.draw()
                toolbar.update()

            b7.config(command=recal)
            b8.config(command=expand)

    except ValueError:
        print("There is no value in Entry Widget")
        l12.place_forget()
        l13.place_forget()
        l14.place_forget()
        l15.place_forget()
        cb.place_forget()
        d1.place_forget()
        d2.place_forget()
        b7.place_forget()
        b8.place_forget()
        canvas.get_tk_widget().place_forget()
        toolbar.place_forget()

    except:
        msgbox8 = messagebox.showerror("Error!!! Connection not established!!!",
                                       "Cannot Connect to the Internet\n"
                                       "make sure that you have a active Internet Connection")
        print(msgbox8)


def dataana():
    bar = Progressbar(root, length=220, style='black.Horizontal.TProgressbar')
    bar.place(x=1000, y=670)
    bar['value'] = 33
    root.update_idletasks()
    time.sleep(1)
    lb1.delete(0, END)
    lb1.place(x=335, y=120)
    sbx1.config(command=lb1.xview)
    sby1.config(command=lb1.yview)
    capstock = e1.get().upper() + radio.get()
    print(capstock)
    bar['value'] = 66
    root.update_idletasks()
    try:
        stock = yf.Ticker(capstock)
        print(stock.info)
        sby1.place(x=820, y=120, height=323)
        sbx1.place(x=335, y=445, width=482)
        lb1.config(yscrollcommand=sby1.set, xscrollcommand=sbx1.set)
        i = 1
        for key, value in list(stock.info.items()):
            print(key)
            print(value)
            lb1.insert(i, str(i) + ")  " + key + " : " + str(value))
            i += 1

    except:
        lb1.place_forget()
        sbx1.place_forget()
        sby1.place_forget()
        print("there is some execption from data analysis button...")
        mes1()
        msgbox7 = messagebox.showinfo("INFO", "only work for those stocks which is fully verfied \n"
                                              "by Yahoo Finance.It may not work for all the stocks...\n"
                                              "This may also happens because of some\n"
                                              " Internet Connectivity issue...")
    bar['value'] = 100
    root.update_idletasks()
    bar.place_forget()


def Predict():
    bar = Progressbar(root, length=220, style='black.Horizontal.TProgressbar')
    bar.place(x=1000, y=670)
    bar['value'] = 33
    root.update_idletasks()
    time.sleep(1)
    capstock = e1.get().upper() + radio.get()
    print(capstock)
    try:
        print("running predict block using pandas")
        stock = yf.Ticker(capstock)
        df = pd.DataFrame(stock.recommendations)
        print(type(stock.recommendations))
        if type(stock.recommendations) == pandas.core.frame.DataFrame:
            path = "F:\\Python Apps\\SMPA\\STOCKDATA\\TEMP.csv"
            df.to_csv(path)
            file = open(path, newline='')
            reader = csv.reader(file)
            # the first line is header having all the string parts contains
            # information about each and specific column
            header = next(reader)
            data = [row for row in reader]
            i = 1
            temp = 0
            for i in range(len(data)):
                temp = i
            l4.config(text="Suggestion is :  {}".format(data[temp][2]))
            file.close()

        else:
            print("en error occured while using pandas...running else")
            cl = avgclose
            op = avgopen
            print(op)
            print(cl)
            suggest = (cl - op)  # / op
            suggesion = 'None'
            print(suggest)
            if suggest < 0:
                suggestion = "SELL"
                print("SELL")
            elif suggest == 0:
                suggestion = "HOLD"
                print("HOLD")
            else:
                suggestion = "BUY"
                print("BUY")
            # NIFTY = 0.195
            # if suggest > NIFTY:
            #     suggestion = "SELL"
            #     print("SELL")
            # elif suggest == NIFTY:
            #     suggestion = "HOLD"
            #     print("HOLD")
            # else:
            #     suggestion = "BUY"
            #     print("BUY")
            l4.config(text=" Suggestion is :  {}".format(suggestion))

    except:
        mes1()
        print("No suggestion")
        l4.config(text="there is no suggestion")

    finally:
        print("running finally block...")
        bar['value'] = 66
        root.update_idletasks()
        time.sleep(1)
        bar['value'] = 100
        root.update_idletasks()
        bar.place_forget()


def exit1():
    msgbox6 = messagebox.askquestion("Confirm", "Are you sure you want to exit?")
    print(msgbox6)
    if msgbox6 == 'yes':
        try:
            os.remove(r"F:\Python Apps\SMPA\STOCKDATA\TEMP.csv")
            print("TEMP.csv File detected")
            print("Deleted Successfully...")
        except:
            print("TEMP.csv not available exiting...")
        print("exit Successfully...")
        exit()
    else:
        print("thanks for continue...")


def mes():
    msgbox = messagebox.showwarning("Not Available", "Calculate method may not work for BSE and None")
    print(msgbox)


def mes1():
    if e1.get() == '':
        msgbox = messagebox.showwarning("Warning!!!",
                                        "Entry Field not contains any data, Please fill it first.")
        return True


def clear1():
    # calculate Field
    lb2.place_forget()
    sbx2.place_forget()
    sby2.place_forget()
    # DataAnalysis Field
    lb1.place_forget()
    sbx1.place_forget()
    sby1.place_forget()
    # General Field
    l4.config(text="Suggestion is : None")
    l7.config(text='last Active Stock Session is None')
    l6.config(text='This Prediction Data is based on the term from : None To : None')
    # Clearing a Graph Field...
    canvas.get_tk_widget().place_forget()
    toolbar.place_forget()
    cb.place_forget()
    l12.place_forget()
    l13.place_forget()
    l14.place_forget()
    l15.place_forget()
    d1.place_forget()
    d2.place_forget()
    b7.place_forget()
    b8.place_forget()
    e1.delete(0, END)


class BackgroundImage(Frame):
    def __init__(self, master, *pargs, **kw):
        super().__init__(master, **kw)
        try:
            Frame.__init__(self, master, *pargs)
            self.image = Image.open("F:\Python Apps\SMPA\Button\img1.jpg")
            self.img_copy = self.image.copy()
            self.background_image = ImageTk.PhotoImage(self.image)
            self.background = Label(self, image=self.background_image)
            self.background.pack(fill=BOTH, expand=YES)
            self.background.bind('<Configure>', self._resize_image)
        except:
            print("error here...")
        finally:
            print("Working fine...")

    def _resize_image(self, event):
        new_width = event.width
        new_height = event.height
        self.image = self.img_copy.resize((new_width, new_height))
        self.background_image = ImageTk.PhotoImage(self.image)
        self.background.configure(image=self.background_image)


root.configure(bg="lightgrey")
e = BackgroundImage(root)
e.pack(fill=BOTH, expand=YES)

# canvas
fig = Figure(figsize=(6, 4), dpi=90)
canvas = FigureCanvasTkAgg(fig, master=root)
toolbar = NavigationToolbar2Tk(canvas, root)

# Entry Field
e1 = Entry(root)
e1.place(x=200, y=10)

# Label Field
l1 = Label(root, text="Enter Company Name:")
l1.place(x=5, y=10)
l4 = Label(root, text="Suggestion is : None")
l4.place(x=200, y=570)
l5 = Label(root, text="Click TDA(Technical Data Analysis) "
                      "for Getting More Info About Stocks.Data is display here.")
l5.place(x=600, y=70)
l6 = Label(root, text='This Prediction Data is based on the term from : None To : None')
l6.place(x=10, y=500)
l7 = Label(root, text='last Active Stock Session is None')
l7.place(x=200, y=650)
l11 = Label(root, text="If Directory not consist any STOCKNAME.NS.csv "
                       "then click to Download Button to Redirect")
l11.place(x=600, y=10)
l12 = Label(root, text="From Date:", background="orange")
l13 = Label(root, text="To Date:", background="orange")
l14 = Label(root, text="Default graph is from listed date to today,To Change the graph use below options",
            background="orange")
l15 = Label(root, background="orange")

# Listbox and Scrollbar
lb1 = Listbox(root, width=80, height=20, background="orange")
sby1 = Scrollbar(root)
sbx1 = Scrollbar(root, orient="horizontal")
lb2 = Listbox(root, width=50, height=13, background="orange")
sby2 = Scrollbar(root)
sbx2 = Scrollbar(root, orient="horizontal")

# radiobutton
radio = StringVar()
r1 = Radiobutton(root, text="NSE", variable=radio, value=".NS").place(x=200, y=40)
r2 = Radiobutton(root, text="BSE", variable=radio, value=".BO", command=mes).place(x=280, y=40)
r3 = Radiobutton(root, text="Global", variable=radio, value="", command=mes).place(x=360, y=40)

# Button Field
calculate = PhotoImage(file=r"F:\Python Apps\SMPA\Button\calculate.png")
b1 = Button(root, text="Search it!", command=calopen_close, image=calculate)
b1.place(x=10, y=120)
Graphbutton = PhotoImage(file=r"F:\Python Apps\SMPA\Button\graph.png")
b2 = Button(root, text="Graph", command=graph, image=Graphbutton)
b2.place(x=450, y=10)
PredictButton = PhotoImage(file=r"F:\Python Apps\SMPA\Button\Predict.png")
b3 = Button(root, text="Predict", command=Predict, image=PredictButton)
b3.place(x=10, y=550)
DownloadButton = PhotoImage(file=r"F:\Python Apps\SMPA\Button\DownloadButton.png")
b4 = Button(root, text="Download", command=download, image=DownloadButton)
b4.place(x=10, y=620)
data = PhotoImage(file=r"F:\Python Apps\SMPA\Button\data.png")
b5 = Button(root, text="Data", command=dataana, image=data)
b5.place(x=1200, y=20)
Clearimg = PhotoImage(file=r"F:\Python Apps\SMPA\Button\clear.png")
b6 = Button(root, text="clear", command=clear1, image=Clearimg)
b6.place(x=160, y=120)
b7 = Button(root, text="graph it!")
b8 = Button(root, text="Expand")
b8.place(x=1200, y=600)
CloseButton = PhotoImage(file=r"F:\Python Apps\SMPA\Button\close80Button.gif")
b9 = Button(root, text="Exit", command=exit1, image=CloseButton)
b9.place(x=1200, y=600)

# date picker
d1 = DateEntry(root, date_pattern="yyyy-mm-dd")
d2 = DateEntry(root, date_pattern="yyyy-mm-dd")

# combobox
n = StringVar()
cb = Combobox(root, text="Select Choice", textvariable=n, width=10)
cb['values'] = ('Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume')

# root Field
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.title("Stock Market Prediction Application ( BY SPANDAN DIXIT )")
icon = PhotoImage(file=r"F:\Python Apps\SMPA\Button\smpa.png")
root.iconphoto(False, icon)

root.mainloop()
