from logging import root
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from typing import Self
import mysql.connector
from pyparsing import White
from tkcalendar import Calendar, DateEntry



class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.nameOfPatient=StringVar()
        self.patientID=StringVar()
        self.ageOfPatient=StringVar()
        self.contactNo=StringVar()
        self.dob=StringVar()
        self.tab1Name=StringVar()
        self.noOfTab1=StringVar()
        self.tab2Name=StringVar()
        self.noOfTab2=StringVar()
        self.date=StringVar()
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="+HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill="x")
        
        
        #=====================Data Frame ================================
        Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        Dataframe.place(x=0,y=130,width=1530,height=400)
        
        #=====================Input Dataframe============================
        
        DataframeInput=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Patient Information")
        DataframeInput.place(x=0,y=5,width=980,height=350)
        
        #=====================Right Dataframe============================
        DataframeRight=LabelFrame(Dataframe,bd=10,relief=RIDGE,padx=10,font=("times new roman",20,"bold"),text="Prescription")
        DataframeRight.place(x=990,y=5,width=500,height=350)
        
        #=====================Buttons Dataframe============================
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
        
        for i in range(7):
            Buttonframe.grid_columnconfigure(i, weight=1)
        
        #=====================Details Dataframe============================
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        
        #=====================Data Dataframe============================
        lblNameTablet=Label(DataframeInput,text="Name of Patient",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0)
        txtNameTablet=Entry(DataframeInput,font=("times new roman",12,"bold"),textvariable=self.nameOfPatient,width=35)
        txtNameTablet.grid(row=0,column=1)
        
        lblAge=Label(DataframeInput,text="Age of Patient",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAge.grid(row=1,column=0)
        txtAge=Entry(DataframeInput,font=("times new roman",12,"bold"),textvariable=self.ageOfPatient,width=35)
        txtAge.grid(row=1,column=1)
        
        lblDOB = Label(DataframeInput, text="DOB", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblDOB.grid(row=2, column=0)
        # Use the DateEntry widget for the "DOB" field
        dob_cal = DateEntry(DataframeInput,font=("times new roman", 12, "bold"), width=35, textvariable=self.dob)
        dob_cal.grid(row=2, column=1)
        
        
        lblNameTablet=Label(DataframeInput,text="Name of Tablet1",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=3,column=0)
        comNameTablet=ttk.Combobox(DataframeInput,textvariable=self.tab1Name,font=("times new roman",12,"bold"),width=33)
        comNameTablet["values"]=("Nice","Paracetamol","Corona Vaccine","Adderall","Ativan","Adderall")
        comNameTablet.grid(row=3,column=1)
        
        lblAge=Label(DataframeInput,text="Number of Tablet1",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAge.grid(row=4,column=0)
        txtAge=Entry(DataframeInput,textvariable=self.noOfTab1,font=("times new roman",12,"bold"),width=35)
        txtAge.grid(row=4,column=1)

        lblNameTablet2=Label(DataframeInput,text="Name of Tablet2",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblNameTablet2.grid(row=5,column=0)
        comNameTablet2=ttk.Combobox(DataframeInput,font=("times new roman",12,"bold"),textvariable=self.tab2Name,width=33)
        comNameTablet2["values"]=("Nice","Paracetamol","Corona Vaccine","Adderall","Ativan","Adderall")
        comNameTablet2.grid(row=5,column=1)
        
        lblAge=Label(DataframeInput,text="Number of Tablet2",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblAge.grid(row=6,column=0)
        txtAge=Entry(DataframeInput,font=("times new roman",12,"bold"),textvariable=self.noOfTab2,width=35)
        txtAge.grid(row=6,column=1)
               
        lblPatientID=Label(DataframeInput,text="Patient ID",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblPatientID.grid(row=0,column=2)
        txtPatientID=Entry(DataframeInput,font=("times new roman",12,"bold"),textvariable=self.patientID,width=35)
        txtPatientID.grid(row=0,column=3)
        
        lblContactNo=Label(DataframeInput,text="Contact No",font=("times new roman",15,"bold"),padx=2,pady=6)
        lblContactNo.grid(row=1,column=2)
        txtlblContactNo=Entry(DataframeInput,font=("times new roman",12,"bold"),textvariable=self.contactNo,width=35)
        txtlblContactNo.grid(row=1,column=3)
        
        lblDate = Label(DataframeInput, text="Date", font=("times new roman", 15, "bold"), padx=2, pady=6)
        lblDate.grid(row=2, column=2)
        date_cal = DateEntry(DataframeInput, font=("times new roman", 12, "bold"), width=35,textvariable=self.date)
        date_cal.grid(row=2, column=3)  
        
        
                #=====================Data Dataframe============================
        self.txtPrescription=Text(DataframeRight,font=("arial",12,"bold"),width=45,height=15,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
      
                        #=====================Data Dataframe============================
        btnPrescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"),
                                 width=23, height=13, padx=2, pady=6)
        btnPrescription.grid(row=0, column=0)

        btnPrescriptionData = Button(Buttonframe, text="PrescriptionData", bg="green", fg="white",
                                     font=("arial", 12, "bold"), width=23, height=13, padx=2, pady=6)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=23,
                           height=13, padx=2, pady=6)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=23,
                           height=13, padx=2, pady=6)
        btnDelete.grid(row=0, column=3)

        btnSearch = Button(Buttonframe, text="Search", bg="green", fg="white", font=("arial", 12, "bold"), width=23,
                           height=13, padx=2, pady=6)
        btnSearch.grid(row=0, column=4)

        btnClear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=23,
                          height=13, padx=2, pady=6)
        btnClear.grid(row=0, column=5)

        btnExit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=23,
                         height=13, padx=2, pady=6)
        btnExit.grid(row=0, column=6)


        #=====================================   TABLE -scrollbar  =============================
        #=====================================   TABLE   =============================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, columns=("nameOfPatient",  "patientID","ageOfPatient", "contactNo", "dob", "tab1Name", "noOfTab1", "tab2Name", "noOfTab2", "date"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameOfPatient",text="Name of Tablets")
        self.hospital_table.heading("patientID",text="Patient ID")
        self.hospital_table.heading("ageOfPatient",text="Age of Patient")
        self.hospital_table.heading("contactNo",text="Contact Number")
        self.hospital_table.heading("dob",text="Date of Birth")
        self.hospital_table.heading("tab1Name",text="Name of Tablet1")
        self.hospital_table.heading("noOfTab1",text="Number of Tablet1")
        self.hospital_table.heading("tab2Name",text="Name of Tablet2")
        self.hospital_table.heading("noOfTab2",text="Number of Tablet2")
        self.hospital_table.heading("date",text="Date")

        self.hospital_table["show"]="headings"
        self.hospital_table.pack(fill=BOTH,expand=1)



        self.hospital_table.column("nameOfPatient",width=100)
        self.hospital_table.column("ageOfPatient",width=100)
        self.hospital_table.column("contactNo",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("tab1Name",width=100)
        self.hospital_table.column("noOfTab1",width=100)
        self.hospital_table.column("tab2Name",width=100)
        self.hospital_table.column("noOfTab2",width=100)
        self.hospital_table.column("date",width=100)
        self.hospital_table.column("patientID",width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        
        #==================== Database Connectivity ===========================
        
        def iPrescriptionData(self):
            if self.patientID.get()=="" or self.nameOfPatient.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                conn=mysql.connector.connect(host="localhost",username="root",password="Pass@123",database="hositalmanagementsystem")
                my_cusor=conn.cursor()
                my_cusor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.nameOfPatient.get(),
                    self.patientID.get(),
                    self.ageOfPatient.get(),1
                    self.contactNo.get(),
                    self.dob.get(),
                    self.tab1Name.get(),
                    self.noOfTab1.get(),
                    self.tab2Name.get(),
                    self.noOfTab2.get(),
                    self.date.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success","Data has been inserted")
                
        def fetch_data(self):
            conn=mysql.connector.connect(host="localhost",username="root",password="Pass@123",database="hositalmanagementsystem")
            my_cusor=conn.cursor()
            my_cusor.execute

        
root=Tk()
ob=Hospital(root)
root.mainloop()
