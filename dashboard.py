from tkinter import*
from PIL import Image, ImageTk
from supplier import supplierClass
from category import categoryClass
from product import productClass

class IMS:
    def __init__(self,root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System | Dev by SWT")

        # Title
        self.icon_title = Image.open('images/inventory.png')
        self.icon_title = self.icon_title.resize((50,50))
        self.icon_title = ImageTk.PhotoImage(self.icon_title)
        title = Label(self.root, text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1)

        # btn logout
        btn_logout = Button(self.root,text="Logout",font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1150,y=20,height=40,width=150)

        # clock
        self.lbl_clock = Label(self.root, text = "Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white").place(x=0, y=70, relwidth=1, height=30)

        # Left menu
        self.menu_logo= Image.open('images/menu_im.png')
        self.menu_logo = self.menu_logo.resize((200,200))
        self.menu_logo = ImageTk.PhotoImage(self.menu_logo)

        LeftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        LeftMenu.place(x=0,y=102,width=200,height=565)

        lbl_menuLogo = Label(LeftMenu, image=self.menu_logo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        # self.icon_side = PhotoImage(file='images/supplier.png')
        self.icon_side= Image.open('images/arrows.png')
        self.icon_side = self.icon_side.resize((40,40))
        self.icon_side = ImageTk.PhotoImage(self.icon_side)
        lbl_menu = Label(LeftMenu,text="Menu",font=("time new roman", 20),bg="#009688").pack(side=TOP,fill=X)

        btn_supplier = Button(LeftMenu,text="Supplier",command=self.supplier,font=("times new roman", 20, "bold"),bg="white",bd=3,image=self.icon_side,compound=LEFT,padx=5,anchor="w",cursor="hand2").pack(side=TOP,fill=X)
        btn_category = Button(LeftMenu,text="Category",command=self.category,font=("times new roman", 20, "bold"),bg="white",bd=3,image=self.icon_side,compound=LEFT,padx=5,anchor="w",cursor="hand2").pack(side=TOP,fill=X)
        btn_product = Button(LeftMenu,text="Product",command=self.product, font=("times new roman", 20, "bold"),bg="white",bd=3,image=self.icon_side,compound=LEFT,padx=5,anchor="w",cursor="hand2").pack(side=TOP,fill=X)
        btn_sales = Button(LeftMenu,text="Sales",font=("times new roman", 20, "bold"),bg="white",bd=3,image=self.icon_side,compound=LEFT,padx=5,anchor="w",cursor="hand2").pack(side=TOP,fill=X)
        btn_exit = Button(LeftMenu,text="Exit",font=("times new roman", 20, "bold"),bg="white",bd=3,image=self.icon_side,compound=LEFT,padx=5,anchor="w",cursor="hand2").pack(side=TOP,fill=X)

        # Content
        self.lbl_supplier = Label(self.root, text = "Total Suppliers\n [ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold")).place(x=300,y=120,height=150,width=300)
        self.lbl_category = Label(self.root, text = "Total Category\n [ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold")).place(x=650,y=120,height=150,width=300)
        self.lbl_product = Label(self.root, text = "Total Product\n [ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold")).place(x=1000,y=120,height=150,width=300)
        self.lbl_sales = Label(self.root, text = "Total Sales\n [ 0 ]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold")).place(x=300,y=300,height=150,width=300)

# =============================================================

    def supplier(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = supplierClass(self.new_win)

    def category(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = categoryClass(self.new_win)
        
    def product(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = productClass(self.new_win)


root = Tk()
obj = IMS(root)
root.mainloop()