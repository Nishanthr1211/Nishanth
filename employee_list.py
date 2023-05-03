import gspread
from tkinter import *
from tkinter import ttk

wd=Tk()
wd.title("PaySlip")
wd.geometry("1200x1200")

frame=Frame(wd,height=1200,width=1200,bg='Green').place(x=0,y=0)

gc = gspread.service_account('C:\\Users\\Nishanth\\Desktop\\Employee.json')
#-------------------Open a sheet from a spreadsheet------------------#
wks = gc.open("Data Form").sheet1

#-----------------------Create button def function--------------------#

#........1.To create a data and to store the google sheet.............#
def create():
    frame1=Frame(frame,height=1200,width=1200,bg="Black").place(x=0,y=0)
    def submit_data():      
        Employee_Id = Employee_Id_entry.get()
        Employee_name = Employee_name_entry.get()
        options = ["Manager", "CEO", "Operation Head"]
        Gender = Gender_entry.get()
        Blood_Group = Blood_Group_entry.get()
        Email = Email_entry.get()
        Contact_No = Contact_No_entry.get()
        Date_Of_Joining = Date_Of_Joining_entry.get()
        Date_of_salary_credited = Date_of_salary_credited_entry.get()
        Location = Location_entry.get()
        PAN = PAN_entry.get()
        Bank_Account_No = Bank_Account_No_entry.get()
        IFSC_Code = IFSC_Code_entry.get()
        Status = Status_entry.get()
        Available_Calendar_Days = Available_Calendar_Days_entry.get()
        Paid_Days = Paid_Days_entry.get()
        Loss_of_pay_Days = Loss_of_pay_Days_entry.get()

        
        
        

        wks.append_row([Employee_Id,Employee_name,Gender,Blood_Group,
                        Email,Contact_No,Date_Of_Joining,Date_of_salary_credited,
                        Location,PAN,Bank_Account_No,IFSC_Code,Status,Available_Calendar_Days,
                        Paid_Days,Loss_of_pay_Days])
        # Format the header
        wks.format('A1:Q1', {'textFormat': {'bold': True}})

        label=Label(frame,text="Data is stored in Google sheet",font=("Times new roman",20),bg='red')
        label.place(x=450,y=650)
       
    Employee_Id_label = Label(frame1, text="Employee_Id",font=("Times new roman",20))
    Employee_Id_label.place(x=8,y=30)
    Employee_Id_entry = Entry(frame1,font=("Times new roman",18))
    Employee_Id_entry.place(x=290,y=30)

    Employee_name_label = Label(frame1, text="Employee_name",font=("Times new roman",20))
    Employee_name_label.place(x=8,y=90)
    Employee_name_entry = Entry(frame1,font=("Times new roman",18))
    Employee_name_entry.place(x=290,y=90)

    Designation_label = Label(frame, text="Designtion",font=("Times new roman",20))
    Designation_label.place(x=6,y=140)
    options = ["Manager", "CEO", "Operation Head"]
    combo = ttk.Combobox(frame,values=options).place(x=290,y=160)

    Gender_label = Label(frame1, text="Gender",font=("Times new roman",20))
    Gender_label.place(x=8,y=190)
    Gender_entry = Entry(frame1,font=("Times new roman",18))
    Gender_entry.place(x=290,y=190)

    Blood_Group_label = Label(frame1, text="Blood_Group",font=("Times new roman",20))
    Blood_Group_label.place(x=10,y=250)
    Blood_Group_entry = Entry(frame1,font=("Times new roman",18))
    Blood_Group_entry.place(x=290,y=250)

    Email_label = Label(frame1, text="Email",font=("Times new roman",20))
    Email_label.place(x=10,y=310)
    Email_entry = Entry(frame1,font=("Times new roman",18))
    Email_entry.place(x=290,y=310)

    Contact_No_label = Label(frame1, text="Contact_No",font=("Times new roman",20))
    Contact_No_label.place(x=10,y=360)
    Contact_No_entry = Entry(frame1,font=("Times new roman",18))
    Contact_No_entry.place(x=290,y=360)

    Date_Of_Joining_label = Label(frame, text="Date_Of_Joining",font=("Times new roman",20))
    Date_Of_Joining_label.place(x=10,y=420)
    Date_Of_Joining_entry = Entry(frame,font=("Times new roman",18))
    Date_Of_Joining_entry.place(x=290,y=420)

    Date_of_salary_credited_label = Label(frame, text="Date_of_salary_credited",font=("Times new roman",20))
    Date_of_salary_credited_label.place(x=10,y=480)
    Date_of_salary_credited_entry = Entry(frame,font=("Times new roman",18))
    Date_of_salary_credited_entry.place(x=290,y=485)

    Location_label = Label(frame, text="Location",font=("Times new roman",20))
    Location_label.place(x=600,y=30)
    Location_entry = Entry(frame,font=("Times new roman",18))
    Location_entry.place(x=900,y=30)

    PAN_label = Label(frame, text="PAN",font=("Times new roman",20))
    PAN_label.place(x=600,y=80)
    PAN_entry = Entry(frame,font=("Times new roman",18))
    PAN_entry.place(x=900,y=80)

    Bank_Account_No_label = Label(frame, text="Bank_Account_No",font=("Times new roman",20))
    Bank_Account_No_label.place(x=600,y=135)
    Bank_Account_No_entry = Entry(frame,font=("Times new roman",18))
    Bank_Account_No_entry.place(x=900,y=135)

    IFSC_Code_label = Label(frame, text="IFSC_Code",font=("Times new roman",20))
    IFSC_Code_label.place(x=600,y=190)
    IFSC_Code_entry = Entry(frame,font=("Times new roman",18))
    IFSC_Code_entry.place(x=900,y=190)

    Status_label = Label(frame, text="Status",font=("Times new roman",20))
    Status_label.place(x=600,y=250)
    Status_entry = Entry(frame,font=("Times new roman",18))
    Status_entry.place(x=900,y=250)

    Available_Calendar_Days_label = Label(frame, text="Available_Calendar_Days",font=("Times new roman",20))
    Available_Calendar_Days_label.place(x=600,y=310)
    Available_Calendar_Days_entry = Entry(frame,font=("Times new roman",18))
    Available_Calendar_Days_entry.place(x=900,y=310)

    Paid_Days_label = Label(frame, text="Paid_Days",font=("Times new roman",20))
    Paid_Days_label.place(x=600,y=360)
    Paid_Days_entry = Entry(frame,font=("Times new roman",18))
    Paid_Days_entry.place(x=900,y=360)

    Loss_of_pay_Days_label = Label(frame, text="Loss_of_pay_Days",font=("Times new roman",20))
    Loss_of_pay_Days_label.place(x=600,y=420)
    Loss_of_pay_Days_entry = Entry(frame,font=("Times new roman",18))
    Loss_of_pay_Days_entry.place(x=900,y=420)


    submit_button = Button(frame,font=("Times new roman",20),text="Submit", command=submit_data)
    submit_button.place(x=350,y=550)
    back_btn=Button(frame,text="Back",command=back,font=("Times new roman",20)).place(x=750,y=540)

#--------------------2.Update the data to rewrite the program................#
def update():
    global Employee_Id_entry
    
    frame2=Frame(frame,height=1200,width=1200,bg="Red").place(x=0,y=0)
    ent.set(p)
    Employee_Id_label = Label(frame2, text="Employee_Id",font=("Times new roman",20))
    Employee_Id_label.place(x=8,y=30)
    Employee_Id_entry = Entry(frame2,text=ent,font=("Times new roman",18))
    Employee_Id_entry.place(x=200,y=30)
    Employee_Id = Employee_Id_entry.get()
    
    update_button = Button(frame2, text="Update Cell", command=update_cell)
    update_button.place(x=250,y=110)
    
def update_cell():
    global row
    global Employee_Id_entry
    rows = wks.get_all_values()
    
    for row in rows[1:]:
        Employee_Id = Employee_Id_entry.get()
        
        if row[0] == Employee_Id:
            frame3=Frame(frame,height=1200,width=1200,bg="Pink").place(x=0,y=0)
            l.set(p)
            l1.set(p)

            Employee_name_label = Label(frame3,text="Employee_name",font=("Times new roman",20))
            Employee_name_label.place(x=8,y=30)
            Employee_name_entry = Entry(frame3,text=l,font=("Times new roman",18))
            Employee_name_entry.place(x=290,y=30)

            drop_label=Label(frame3,text="Designation",font=("Times new roman",20))
            drop_label.place(x=8,y=90)
            options = ["Manager", "CEO", "Operation Head"]
            combo = ttk.Combobox(frame3, text=l1,values=options).place(x=290,y=90)
                
            Gender_label = Label(frame3, text="Gender",font=("Times new roman",20))
            Gender_label.place(x=6,y=140)
            Gender_entry = Entry(frame3,text=l2,font=("Times new roman",18))
            Gender_entry.place(x=290,y=140)

            Blood_Group_label = Label(frame3, text="Blood_Group",font=("Times new roman",20))
            Blood_Group_label.place(x=10,y=250)
            Blood_Group_entry = Entry(frame3,text=l3,font=("Times new roman",18))
            Blood_Group_entry.place(x=290,y=250)

            Email_label = Label(frame3, text="Email",font=("Times new roman",20))
            Email_label.place(x=8,y=190)
            Email_entry = Entry(frame3,text=l4,font=("Times new roman",18))
            Email_entry.place(x=290,y=190)

            Contact_No_label = Label(frame3, text="Contact_No",font=("Times new roman",20))
            Contact_No_label.place(x=10,y=310)
            Contact_No_entry = Entry(frame3,text=l5,font=("Times new roman",18))
            Contact_No_entry.place(x=290,y=310)

            Date_Of_Joining_label = Label(frame3, text="Date_Of_Joining",font=("Times new roman",20))
            Date_Of_Joining_label.place(x=10,y=360)
            Date_Of_Joining_entry = Entry(frame3,text=l6,font=("Times new roman",18))
            Date_Of_Joining_entry.place(x=290,y=360)

            Date_of_salary_credited_label = Label(frame3, text="Date_of_salary_credited",font=("Times new roman",20))
            Date_of_salary_credited_label.place(x=10,y=420)
            Date_of_salary_credited_entry = Entry(frame3,text=l7,font=("Times new roman",18))
            Date_of_salary_credited_entry.place(x=290,y=420)

            Location_label = Label(frame3, text="Location",font=("Times new roman",20))
            Location_label.place(x=600,y=30)
            Location_entry = Entry(frame3,text=l8,font=("Times new roman",18))
            Location_entry.place(x=900,y=30)

            PAN_label = Label(frame3, text="PAN",font=("Times new roman",20))
            PAN_label.place(x=600,y=80)
            PAN_entry = Entry(frame3,text=l9,font=("Times new roman",18))
            PAN_entry.place(x=900,y=80)

            Bank_Account_No_label = Label(frame3, text="Bank_Account_No",font=("Times new roman",20))
            Bank_Account_No_label.place(x=600,y=135)
            Bank_Account_No_entry = Entry(frame3,text=l10,font=("Times new roman",18))
            Bank_Account_No_entry.place(x=900,y=135)

            IFSC_Code_label = Label(frame3, text="IFSC_Code",font=("Times new roman",20))
            IFSC_Code_label.place(x=600,y=190)
            IFSC_Code_entry = Entry(frame3,text=l11,font=("Times new roman",18))
            IFSC_Code_entry.place(x=900,y=190)

            Status_label = Label(frame3, text="Status",font=("Times new roman",20))
            Status_label.place(x=600,y=250)
            Status_entry = Entry(frame3,text=l12,font=("Times new roman",18))
            Status_entry.place(x=900,y=250)

            Available_Calendar_Days_label = Label(frame3, text="Available_Calendar_Days",font=("Times new roman",20))
            Available_Calendar_Days_label.place(x=600,y=310)
            Available_Calendar_Days_entry = Entry(frame3,text=l13,font=("Times new roman",18))
            Available_Calendar_Days_entry.place(x=900,y=310)

            Paid_Days_label = Label(frame3, text="Paid_Days",font=("Times new roman",20))
            Paid_Days_label.place(x=600,y=360)
            Paid_Days_entry = Entry(frame3,text=l14,font=("Times new roman",18))
            Paid_Days_entry.place(x=900,y=360)

            Loss_of_pay_Days_label = Label(frame3, text="Loss_of_pay_Days",font=("Times new roman",20))
            Loss_of_pay_Days_label.place(x=600,y=420)
            Loss_of_pay_Days_entry = Entry(frame3,text=l15,font=("Times new roman",18))
            Loss_of_pay_Days_entry.place(x=900,y=420)

            
                        
                        
            save_button=Button(frame3,text="Save",command=save,font=("Times new roman",20))
            save_button.place(x=350,y=500)

            back_btn=Button(frame,text="Back",command=back,font=("Times new roman",20)).place(x=750,y=500)

        
                
        else:
            label=Label(frame,text="Data Not Found",font=("Times new roman",20))
            label.place(x=200,y=180)
            
                
        #save(row)
p=""
l=StringVar()
l1=StringVar()

l2=StringVar()
l3=StringVar()
l4=StringVar()
l5=StringVar()
l6=StringVar()
l7=StringVar()
l8=StringVar()
l9=StringVar()
l10=StringVar()
l11=StringVar()
l12=StringVar()
l13=StringVar()
l14=StringVar()
l15=StringVar()


def save():
    global p
    global row
    name=l.get()
    drop=l1.get()
    Gender=l2.get()
    Blood_Group=l3.get()
    Email=l4.get()
    Contact_No=l5.get()
    Date_Of_Joining=l6.get()
    Date_of_salary_credited=l7.get()
    Location=l8.get()
    PAN=l9.get()
    Bank_Account_No=l10.get()
    IFSC_Code=l11.get()
    Status=l12.get()
    Available_Calendar_Days=l13.get()
    Paid_Days=l14.get()
    Loss_of_pay_Days=l15.get()
    
    rows = wks.get_all_values()
    Employee_Id = Employee_Id_entry.get()
    cell = wks.find(Employee_Id)            
    cell=wks.find(Employee_Id)
    rows = wks.get_all_values()
                    #col.index=row.index
                    # some element in the `rows` list
                    
    wks.update_cell(rows.index(row)+1,2, name)
    wks.update_cell(rows.index(row)+1,3, drop)
    wks.update_cell(rows.index(row)+1,4, Gender)
    wks.update_cell(rows.index(row)+1,5, Email)
    wks.update_cell(rows.index(row)+1,6, Blood_Group)
    wks.update_cell(rows.index(row)+1,7, Contact_No)
    wks.update_cell(rows.index(row)+1,8, Date_Of_Joining)
    wks.update_cell(rows.index(row)+1,9, Date_of_salary_credited)
    wks.update_cell(rows.index(row)+1,10, Location)
    wks.update_cell(rows.index(row)+1,11, PAN)
    wks.update_cell(rows.index(row)+1,12, Bank_Account_No)
    wks.update_cell(rows.index(row)+1,13, IFSC_Code)
    wks.update_cell(rows.index(row)+1,14, Status)
    wks.update_cell(rows.index(row)+1,15, Available_Calendar_Days)
    wks.update_cell(rows.index(row)+1,16, Paid_Days)
    wks.update_cell(rows.index(row)+1,17, Loss_of_pay_Days)
    
    
    label_frame=Frame(frame,height=10,width=20,bg="Red").place(x=500,y=600)
    data_label=Label(label_frame,text="Update Data",font=("Times new roman",20)).place(x=500,y=600)


p=""
ent=StringVar()

def back():
    back_frame=Frame(frame,height=1200,width=1200,bg="Green").place(x=0,y=0)
    button=Button(back_frame,font=("Times new roman",20),text="Create", command=create)
    button.place(x=450,y=100)

    button=Button(back_frame,font=("Times new roman",20),text="Update", command=update)
    button.place(x=450,y=180)

    

#---------------------------Buttons for first frame----------------------------#
button=Button(frame,font=("Times new roman",20),text="Create", command=create)
button.place(x=250,y=100)

button=Button(frame,font=("Times new roman",20),text="Update", command=update)
button.place(x=250,y=180)
