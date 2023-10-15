from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3

class supplierClass:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1110x500+220+140")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        self.root.focus_force()

        # ===================
        # All Variables ====
        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()

        self.var_invoice = StringVar()
        self.var_name = StringVar()
        self.var_contact = StringVar()
        self.var_desc = StringVar()

        # === searchframe ===
        # SearchFrame = LabelFrame(self.root,text="Search Supplier",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=RIDGE)
        # SearchFrame.place(x=250,y=20,width=600,height=70)
        SearchFrame = LabelFrame(self.root,text="Search Invoice No.",font=("goudy old style",12,"bold"),bg="white",bd=2,relief=RIDGE)
        SearchFrame.place(x=250,y=20,width=600,height=70)


        # === options ===
        # cmb_search = ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
        # cmb_search.place(x=10,y=10,width=180)
        # cmb_search.current(0)

        lbl_search = Label(self.root, text="Invoice No.", font=("goudy old style",15),bg="white").place(x=300,y=50)
        text_search = Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10)
        btn_search = Button(SearchFrame, text="Search", command=self.search, font=("goudy old style",15),bg="#4caf50",fg="white",cursor="hand2").place(x=410,y=9,width=150,height=30)

        # === title ===
        title = Label(self.root, text="Suppliers Details", font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)

        # === content ===
        # === row 1 ===
        lbl_supinvoice = Label(self.root, text="Invoice No.", font=("goudy old style",15),bg="white").place(x=50,y=150)
        txt_supinvoice = Entry(self.root, textvariable=self.var_invoice, font=("goudy old style",15),bg="lightyellow").place(x=180,y=150,width=180)

        # === row 2 ===
        lbl_name = Label(self.root, text="Supplier Name", font=("goudy old style",15),bg="white").place(x=50,y=200)
        txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style",15),bg="lightyellow").place(x=180,y=200,width=180)

        # === row 3 ===
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style",15),bg="white").place(x=50,y=250)
        txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style",15),bg="lightyellow").place(x=180,y=250,width=180)

        # === row 4 ===
        lbl_desc = Label(self.root, text="Description", font=("goudy old style",15),bg="white").place(x=50,y=300)
        self.txt_desc = Text(self.root, font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=180,y=300,width=450, height=90)

        # === button ===
        btn_add = Button(self.root, text="Save",command=self.add, font=("goudy old style",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=80,y=430,width=110,height=40)
        btn_update = Button(self.root, text="Update", command=self.update, font=("goudy old style",15,"bold"),bg="#4caf50",fg="white",cursor="hand2").place(x=220,y=430,width=110,height=40)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style",15,"bold"),bg="#f44336",fg="white",cursor="hand2").place(x=360,y=430,width=110,height=40)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style",15,"bold"),bg="#607d8b",fg="white",cursor="hand2").place(x=500,y=430,width=110,height=40)

        # === Supplier Details ===
        sup_frame = Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=650,y=150,width=400,height=300)
        
        scrolly = Scrollbar(sup_frame, orient=VERTICAL)
        scrollx = Scrollbar(sup_frame, orient=HORIZONTAL)
        
        self.SupplierTable = ttk.Treeview(sup_frame,columns=('invoice','name','contact','desc'), yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)        
        scrollx.config(command=self.SupplierTable.xview)
        scrolly.config(command=self.SupplierTable.yview)

        self.SupplierTable.heading("invoice",text="INVOICE")
        self.SupplierTable.heading("name",text="NAME")
        self.SupplierTable.heading("contact",text="CONTACT")
        self.SupplierTable.heading("desc",text="DESCRIPTIONS")

        self.SupplierTable["show"] = "headings"

        self.SupplierTable.column("invoice",width=90)
        self.SupplierTable.column("name",width=90)
        self.SupplierTable.column("contact",width=100)
        self.SupplierTable.column("desc",width=200)
        self.SupplierTable.pack(fill=BOTH,expand=1)
        self.SupplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

# ====================== Functions =============================

    def add(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_invoice.get() == "":
                messagebox.showerror("Error","Supplier invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_invoice.get(),))
                row = cur.fetchone()
                if row != None:
                    messagebox.showerror("Error","This Supplier invoice already assign, try difference",parent=self.root)
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                        self.var_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier invoice added successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            cur.execute("Select * from supplier")
            rows = cur.fetchall()
            self.SupplierTable.delete(*self.SupplierTable.get_children())
            for row in rows:
                self.SupplierTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def get_data(self, ev):
        f = self.SupplierTable.focus()
        content = (self.SupplierTable.item(f))
        row = content['values']
        self.var_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END) 
        self.txt_desc.insert(END,row[3])    

    def update(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_invoice.get() == "":
                messagebox.showerror("Error","Supplier invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Supplier invoice",parent=self.root)
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=? where invoice=?",(
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Supplier invoice updated successfully",parent=self.root)
                    self.show()
                    con.close()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def delete(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_invoice.get() == "":
                messagebox.showerror("Error","Supplier invoice must be required",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(self.var_invoice.get(),))
                row = cur.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Supplier invoice",parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op == True:
                        cur.execute("Delete from supplier where invoice=?",(self.var_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Supplier invoice deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def clear(self):
        self.var_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END) 
        self.var_searchtxt.set("")
        self.show()

    def search(self):
        con = sqlite3.connect(database=r'ims.db')
        cur = con.cursor()
        try:
            if self.var_searchtxt.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:    
                cur.execute("Select * from supplier where invoice="+ self.var_searchtxt.get())
                rows = cur.fetchall()
                if len(rows) != 0:
                    self.SupplierTable.delete(*self.SupplierTable.get_children())
                    for row in rows:
                        self.SupplierTable.insert('',END,values=row)
                else:
                    messagebox.showerror("Error","No record found!!",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


if __name__=="__main__":
    root = Tk()
    obj = supplierClass(root)
    root.mainloop()      