# Code để tạo cửa sổ
import tkinter as tk
from tkinter import Menu


class MyProject:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.root = root
        # Thiết lập tiêu đề cho cửa sổ
        self.root.title('Ứng dụng Tkinter OOP')
        # Thiết lập kích thước của cửa sổ
        self.root.geometry('400x300')
        
        # Tạo Menu bar
        self.menu = Menu(root)
        self.root.config(menu=self.menu)
        
        # Tạo File Menu
        self.fileMenu = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label='File', command=self.fileMenu)
        self.fileMenu.add_command(label='Text' , command=self.newTextFile)
        # # self.newTextFile.add_command(label='pdf file', command=self.PDFFileMenu)
        # self.fileMenu.add_command(label='new file', command=self.newFile)
        # self.fileMenu.add_command(label='new window', command=self.newWindow)
        # self.fileMenu.add_command(label='new windowwp', command=self.newWindowWP)
        # self.fileMenu.add_command(label='open file', command=self.openFile)
        # self.fileMenu.add_command(label='open folder', command=self.openFolder)
        # self.fileMenu.add_command(label='open workspaceff', command=self.openWorkspaceFF)
        # self.fileMenu.add_command(label='open recent', command=self.openRecent)

        # self.editMenu = Menu(self.menu, tearoff=0)
        # self.menu.add_command(label='Edit', command=self.editMenu)

        # self.openMenu = Menu(self.menu, tearoff=0)
        # self.menu.add_command(label='Open', command=self.openMenu)

        # self.closeMenu = Menu(self.menu, tearoff=0)
        # self.menu.add_command(label='Close', command=self.closeMenu)

        # self.storeMenu = Menu(self.menu, tearoff=0)
        # self.menu.add_command(label='Delete', command=self.storeMenu)

        # self.deleteMenu = Menu(self.menu, tearoff=0)
        # self.menu.add_command(label='Store', command=self.deleteMenu)

    def newTextFile(self):
        pass
    def PDFFileMenu(self):
        pass
    def newFile(self):
        pass
    def newWindow(self):
        pass
    def newWindowWP(self):
        pass
    def openFile(self):
        pass
    def openFolder(self):
        pass
    def openWorkspaceFF(self):
        pass
    def openRecent(self):
        pass



# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()