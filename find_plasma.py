def adddonor():
    def submitadd():
        BG = bgval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        age = ageval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        try:
            strr = 'insert into donor values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(strr, (BG, name, mobile, email, address, gender, age,
                                    addeddate, addedtime))
            con.commit()
            res = messagebox.askyesnocancel('Notifications',
             'mobile {} Name {} Added successfully.. and want to clean the form'.format(mobile,
             name),parent=addroot)
            if (res == True):
                bgval.set('')
                nameval.set('')
                mobileval.set('')
                emailval.set('')
                addressval.set('')
                genderval.set('')
                ageval.set('')
        except:
            messagebox.showerror('Notifications', 'mobile Already Exist try another mobile'
                                                  ' number...', parent=addroot)
        strr = 'select * from donor'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        donortable.delete(*donortable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            donortable.insert('', END, values=vv)
    print("Donor added")
    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('470x470+220+200')
    addroot.title('Find Plasma')
    addroot.config(bg='ivory4')
    addroot.iconbitmap('plasma.ico')
    addroot.resizable(False, False)

    #--------------------------------------------------- Add donor Labels
    bglabel = Label(addroot,text='Enter BG : ',bg='gold2',font=('times',20,'bold')
                    ,relief=GROOVE,borderwidth=3,width=12,anchor='w')
    bglabel.place(x=10,y=10)
    namelabel = Label(addroot,text='Enter Name : ',bg='gold2',font=('times',20,'bold')
                      ,relief=GROOVE,borderwidth=3,width=12,anchor='w')
    namelabel.place(x=10,y=70)
    mobilelabel = Label(addroot,text='Enter Mobile : ',bg='gold2',font=('times',20,'bold')
                        ,relief=GROOVE,borderwidth=3,width=12,anchor='w')
    mobilelabel.place(x=10,y=130)
    emaillabel = Label(addroot,text='Enter Email : ',bg='gold2',font=('times',20,'bold')
                       ,relief=GROOVE,borderwidth=3,width=12,anchor='w')
    emaillabel.place(x=10,y=190)
    addresslabel = Label(addroot,text='Enter Address : ',bg='gold2',font=('times',20,'bold')
                         ,relief=GROOVE,borderwidth=3,width=12,anchor='w')
    addresslabel.place(x=10,y=250)
    genderlabel = Label(addroot,text='Enter Gender : ',bg='gold2',font=('times',20,'bold')
                        ,relief=GROOVE,borderwidth=3,width=12,anchor='w')
    genderlabel.place(x=10,y=310)
    agelabel = Label(addroot,text='Enter Age: ',bg='gold2',font=('times',20,'bold'),
                     relief=GROOVE,borderwidth=3,width=12,anchor='w')
    agelabel.place(x=10,y=370)
    ##----------------------------------------------------------- Add donor Entry
    bgval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    ageval = StringVar()

    identry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=bgval)
    identry.place(x=250,y=10)
    nameentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=nameval)
    nameentry.place(x=250,y=70)
    mobileentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=mobileval)
    mobileentry.place(x=250,y=130)
    emailentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=emailval)
    emailentry.place(x=250,y=190)
    addressentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=addressval)
    addressentry.place(x=250,y=250)
    genderentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=genderval)
    genderentry.place(x=250,y=310)
    ageentry = Entry(addroot,font=('roman',15,'bold'),bd=5,textvariable=ageval)
    ageentry.place(x=250,y=370)
    ############------------------------- add button
    submitbtn = Button(addroot,text='Submit',font=('roman',15,'bold'),width=20,bd=5,
        activebackground='blue',activeforeground='white',bg='red',command=submitadd)
    submitbtn.place(x=150,y=420)
    addroot.mainloop()

def searchdonor():
    def submitsearch():
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        age = ageval.get()
        addedtime = time.strftime("%H:%M:%S")
        addeddate = time.strftime("%d/%m/%Y")
        search = searchval.get()
        if (search != ''):
            strr = 'select * from donor where location=%s'
            mycursor.execute(strr, (search))
            datas = mycursor.fetchall()
            donortable.delete(*donortable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
                donortable.insert('', END, values=vv)
        strr = 'insert into viewer values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        strrr='select * from donor where address=%s'
        mycursor.execute(strr,(name, mobile, email, address, gender, age,
                               addeddate, addedtime,search))
        mycursor.execute(strr,(search))
        con.commit()
        res = messagebox.askyesnocancel('Notifications',
                                                'mobile {} Name {} Added '
         'successfully.. and want to clean the form'.format(mobile,name),
                                                parent=searchroot)
        if (res == True):
            nameval.set('')
            mobileval.set('')
            emailval.set('')
            addressval.set('')
            genderval.set('')
            ageval.set('')
            searchval.set('')
            messagebox.showerror('Notifications', 'mobile Already Exist try another'
                                 'mobile number...', parent=searchroot)
    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('470x470+220+200')
    searchroot.title('Enter your details')
    searchroot.config(bg='ivory4')
    searchroot.iconbitmap('plasma.ico')
    searchroot.resizable(False, False)

    # --------------------------------------------------- search donor Labels
    # namelabel = Label(searchroot, text='Enter Name ', bg='gold2', font=('times', 20,
    #     'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    # namelabel.place(x=10, y=10)
    # mobilelabel = Label(searchroot, text='Enter Mobile : ', bg='gold2', font=('times', 20,
    #     'bold'), relief=GROOVE, borderwidth=3, width=12, anchor='w')
    # mobilelabel.place(x=10, y=70)
    # emaillabel = Label(searchroot, text='Enter Email : ', bg='gold2', font=('times', 20,
    # 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    # emaillabel.place(x=10, y=130)
    # addresslabel = Label(searchroot, text='Enter Address : ', bg='gold2', font=('times', 20,
    # 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    # addresslabel.place(x=10, y=190)
    # genderlabel = Label(searchroot, text='Enter Gender : ', bg='gold2', font=('times', 20,
    #     'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    # genderlabel.place(x=10, y=250)
    # doblabel = Label(searchroot, text='Enter Age: ', bg='gold2', font=('times', 20,
    #  'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    # doblabel.place(x=10, y=310)
    searchlabel = Label(searchroot, text='Search location : ', bg='gold2', font=('times',
        20, 'bold'), relief=GROOVE,borderwidth=3, width=12, anchor='w')
    searchlabel.place(x=10, y=370)
    ##----------------------------------------------------------- search donor Entry

    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    ageval = StringVar()
    searchval = StringVar()

    # nameentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    # nameentry.place(x=250, y=10)
    #
    # mobileentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    # mobileentry.place(x=250, y=70)
    #
    # emailentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    # emailentry.place(x=250, y=130)
    #
    # addressentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    # addressentry.place(x=250, y=190)
    #
    # genderentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    # genderentry.place(x=250, y=250)
    #
    # ageentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=ageval)
    # ageentry.place(x=250, y=310)

    searchentry = Entry(searchroot, font=('roman', 15, 'bold'), bd=5, textvariable=searchval)
    searchentry.place(x=250, y=370)
    ############------------------------- add button
    submitbtn = Button(searchroot, text='Submit', font=('roman', 15, 'bold'), width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=submitsearch)
    submitbtn.place(x=150, y=420)
    searchroot.mainloop()


def deldonor():
    cc = donortable.focus()
    content = donortable.item(cc)
    pp = content['values'][2]
    strr = 'delete from donor where mobile=%s'
    mycursor.execute(strr, (pp))
    con.commit()
    messagebox.showinfo('Notifications', 'number {} details deleted'
                                         ' sucessfully...'.format(pp))
    strr = 'select * from donor'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    donortable.delete(*donortable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        donortable.insert('', END, values=vv)
    print("Donor deleted")

def updatedonor():
    def submitupdate():
        bg = Bgval.get()
        name = nameval.get()
        mobile = mobileval.get()
        email = emailval.get()
        address = addressval.get()
        gender = genderval.get()
        age = ageval.get()
        ttime = time.strftime("%H:%M:%S")
        date = time.strftime("%d/%m/%Y")
        strr = 'update donor set blood_group=%s,name=%s,email=%s,location=%s,' \
               'gender=%s,age=%s,date=%s,time=%s where mobile=%s'
        mycursor.execute(strr, (bg,name,email, address, gender, age, date, ttime,
                                mobile))
        con.commit()
        messagebox.showinfo('Notifications', 'data having {} Modified sucessfully'
                                        '...'.format(mobile), parent=updateroot)
        strr = 'select * from donor'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        donortable.delete(*donortable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
            donortable.insert('', END, values=vv)
    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('470x470+220+200')
    updateroot.title('Update details')
    updateroot.config(bg='ivory4')
    updateroot.iconbitmap('plasma.ico')
    updateroot.resizable(False, False)

    # --------------------------------------------------- Add donor Labels
    blood_grplabel = Label(updateroot, text='Update BG : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                           borderwidth=3, width=12, anchor='w')
    blood_grplabel.place(x=10, y=10)

    namelabel = Label(updateroot, text='Update Name : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                      borderwidth=3, width=12, anchor='w')
    namelabel.place(x=10, y=70)

    mobilelabel = Label(updateroot, text='Update Mobile : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    mobilelabel.place(x=10, y=130)

    emaillabel = Label(updateroot, text='Update Email : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                       borderwidth=3, width=12, anchor='w')
    emaillabel.place(x=10, y=190)

    addresslabel = Label(updateroot, text='Update Address : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                         borderwidth=3, width=12, anchor='w')
    addresslabel.place(x=10, y=250)

    genderlabel = Label(updateroot, text='Update Gender : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                        borderwidth=3, width=12, anchor='w')
    genderlabel.place(x=10, y=310)

    agelabel = Label(updateroot, text='Update Age : ', bg='gold2', font=('times', 20, 'bold'), relief=GROOVE,
                     borderwidth=3, width=12, anchor='w')
    agelabel.place(x=10, y=370)
    ##----------------------------------------------------------- Add donor Entry
    Bgval = StringVar()
    nameval = StringVar()
    mobileval = StringVar()
    emailval = StringVar()
    addressval = StringVar()
    genderval = StringVar()
    ageval = StringVar()
    dateval=StringVar()
    timeval=StringVar()

    bgentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=Bgval)
    bgentry.place(x=250, y=10)

    nameentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=nameval)
    nameentry.place(x=250, y=70)

    mobileentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=mobileval)
    mobileentry.place(x=250, y=130)

    emailentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=emailval)
    emailentry.place(x=250, y=190)

    addressentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=addressval)
    addressentry.place(x=250, y=250)

    genderentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=genderval)
    genderentry.place(x=250, y=310)

    ageentry = Entry(updateroot, font=('roman', 15, 'bold'), bd=5, textvariable=ageval)
    ageentry.place(x=250, y=370)
    ############------------------------- add button
    submitbtn = Button(updateroot, text='Update', font=('roman', 15, 'bold'),
                       width=20, bd=5, activebackground='blue',
                       activeforeground='white',
                       bg='red', command=submitupdate )
    submitbtn.place(x=150, y=420)
    cc = donortable.focus()
    content = donortable.item(cc)
    pp = content['values']
    if (len(pp) != 0):
        Bgval.set(pp[0])
        nameval.set(pp[1])
        mobileval.set(pp[2])
        emailval.set(pp[3])
        addressval.set(pp[4])
        genderval.set(pp[5])
        ageval.set(pp[6])
        dateval.set(pp[7])
        timeval.set(pp[8])
    updateroot.mainloop()

def showdonor():
    strr = 'select * from donor'
    mycursor.execute(strr)
    datas = mycursor.fetchall()
    donortable.delete(*donortable.get_children())
    for i in datas:
        vv = [i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]]
        donortable.insert('', END, values=vv)

def hospitals():
    print("list of hospitals ")
    strr='select * from hospitals'
    mycursor.execute(strr)
    datas=mycursor.fetchall()
    print(datas)

def exit():
    res=messagebox.askyesnocancel('Notification ','Do you want to exit ?')
    if (res==True):
        root.destroy()
########### connection database
def connectdb():
    def submitdb():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con=pymysql.connect(host=host,user=user,password=password)
            mycursor=con.cursor()
        except:
            messagebox.showerror("Notifiction","Data is incorrect please try again")
            return
        try:
            strr = 'create database plasma'
            mycursor.execute(strr)
            strr = 'use plasma'
            mycursor.execute(strr)
            messagebox.showinfo('Notification',
                                'database created and now you are connected connected to the database ....',
                                parent=dbroot)

        except:
            strr = 'use plasma'
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Now you are connected to the database ....', parent=dbroot)
        dbroot.destroy()

    dbroot=Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+700+230')
    dbroot.iconbitmap('heart.ico')
    dbroot.resizable(False,False)
    dbroot.config(bg='gold2')
    #-----------connectdb labels
    hostlabel =Label(dbroot,text='Enter host :',bg='papaya whip',font=('times',20,'bold'),relief=GROOVE,
                   width=13,anchor='w')
    hostlabel.place(x=10,y=10)

    userlabel = Label(dbroot, text='Enter user :', bg='papaya whip', font=('times', 20, 'bold'), relief=GROOVE,
                    width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text='Enter Password :', bg='papaya whip', font=('times', 20, 'bold'), relief=GROOVE,
                    width=13, anchor='w')
    passwordlabel.place(x=10, y=130)
    ###############################------connectdb entry
    hostval=StringVar()
    userval=StringVar()
    passwordval=StringVar()
    # hostval.set('hello')
    hostentry=Entry(dbroot,font=('roman ',15,'bold'),bd=5,textvariable=hostval)
    hostentry.place(x=250,y=10)

    userentry = Entry(dbroot, font=('roman ', 15, 'bold'), bd=5, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = Entry(dbroot, font=('roman ', 15, 'bold'), bd=5, textvariable=passwordval)
    passwordentry.place(x=250, y=130)

###############################connect db button
    submitbutton=Button(dbroot,text='Submit',font=('roman',15,'bold'),width=20,command=submitdb)
    submitbutton.place(x=150,y=180)

    dbroot.mainloop()


#########clock
def tick():
    time_st=time.strftime("%H:%M:%S")
    date_st=time.strftime("%d/%m/%y")
    clock.config(text='Date :'+date_st+'\n'+'Time : '+time_st)
    clock.after(100,tick)

############### intro slider
def IntroLabelTick():
    global count,text
    if(count>=len(s)):
        count=-1
        text=''
        SliderLabel.config(text=text)
    else:
        text=text+s[count]
        SliderLabel.config(text=text)
        count+=1
    SliderLabel.after(100,IntroLabelTick)

from tkinter import *
from tkinter import Toplevel,messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
root=Tk()
root.title("FIND PLASMA")
root.config(bg='white')
root.geometry('1174x700+100+30')
root.iconbitmap('heart.ico')
root.resizable(False,False)

###################################### frames
####################################### dataentry frame
DataEntryFrame = Frame(root,bg='ivory4',relief=GROOVE,borderwidth=5)
DataEntryFrame.place(x=10,y=80,width=500,height=600)
frontlabel=Label(DataEntryFrame,text=' -----Welcome----- ',width=30,font=('arial',22,'italic bold'),bg='ivory4')
frontlabel.pack(side=TOP,expand=True)
addbtn=Button(DataEntryFrame,text='1. Donor',width=25,font=('chiller',20,'bold'),bd=6,bg='red',command=adddonor)
addbtn.pack(side=TOP,expand=True)
searchbtn=Button(DataEntryFrame,text='2. Search Donor',width=25,font=('chiller',20,'bold'),bd=6,bg='red',command=searchdonor)
searchbtn.pack(side=TOP,expand=True)
deletebtn=Button(DataEntryFrame,text='3. Delete Donor',width=25,font=('chiller',20,'bold'),bd=6,bg='red',command=deldonor)
deletebtn.pack(side=TOP,expand=True)
updatebtn=Button(DataEntryFrame,text='4. Update Donor',width=25,font=('chiller',20,'bold'),bd=6,bg='red',
                 command=updatedonor)
updatebtn.pack(side=TOP,expand=True)
showbtn=Button(DataEntryFrame,text='5. Show all',width=25,font=('chiller',20,'bold'),bd=6,bg='red',
               command=showdonor)
showbtn.pack(side=TOP,expand=True)
hospitalbtn=Button(DataEntryFrame,text='6. Show Hospitals',width=25,font=('chiller',20,'bold'),bd=6,bg='red',
                   command=hospitals)
hospitalbtn.pack(side=TOP,expand=True)
exitbtn=Button(DataEntryFrame,text='7. Exit  ',width=25,font=('chiller',20,'bold'),bd=6,bg='red',
               command=exit)
exitbtn.pack(side=TOP,expand=True)

############################################# show data frame
ShowDataFrame =Frame(root,bg='ivory4',relief=GROOVE,borderwidth=5)
ShowDataFrame.place(x=540,y=80,width=620,height=600)
######################################### show data frames
style = ttk.Style()
style.configure('Treeview.Heading',font=('times',20,'bold'),foreground='black')
style.configure('Treeview',font=('times',15,'bold'),background='cyan',foreground='black')
scroll_x=Scrollbar(ShowDataFrame,orient=HORIZONTAL)
scroll_y=Scrollbar(ShowDataFrame,orient=VERTICAL)
donortable=Treeview(ShowDataFrame,columns=('BG','Name','Mobile No','Email','Address',
                                           'Gender','Age','Added Date','Added Time'),
                         yscrollcommand=scroll_y.set,xscrollcommand=scroll_x.set)
scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_x.config(command=donortable.xview)
scroll_y.config(command=donortable.yview)
donortable.heading('BG',text='BG')
donortable.heading('Name',text='Name')
donortable.heading('Mobile No',text='Mobile No')
donortable.heading('Email',text='Email')
donortable.heading('Address',text='Address')
donortable.heading('Gender',text='Gender')
donortable.heading('Age',text='Age')
donortable.heading('Added Date',text='Added Date')
donortable.heading('Added Time',text='Added Time')
donortable['show'] = 'headings'
donortable.pack(fill=BOTH,expand=1)

###################################### slider
s='Welcome to Find plasma -Save Life '
count=0
text=''
SliderLabel=Label(root,text=s,font=('chiller',30,'italic bold'),relief=RIDGE,borderwidth=5,
                  width=35,bg='cyan')
SliderLabel.place(x=320,y=5)
IntroLabelTick()

######## clock
clock=Label(root,font=('times',14,'bold'),relief=RIDGE,borderwidth=4,bg='lawn green')
clock.place(x=0,y=5)
tick()

############ connect to database
connnectbutton=Button(root,text='Connect to Server ',width=22,font=('chiller',19,'italic bold')
                      ,relief=RIDGE,borderwidth=4,bg='green2',
                      activebackground='blue',activeforeground='white',command=connectdb)
connnectbutton.place(x=930,y=5)
root.mainloop()