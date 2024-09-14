import tkinter as tk
class MyProject:
    def __init__(self, root):
        # Thiết lập cửa sổ màn hình
        self.root = root
        # Thiết lập tiêu đề cho cửa sổ
        self.root.title('Ứng dụng Tkinter OOP')
        # Thiết lập kích thước của cửa sổ
        self.root.geometry('400x300')

        self.x = 10
        self.y = 10

        self.lblUsername = tk.Label(self.root, text='Your Username')
        self.lblUsername.place(x=self.x, y=self.y)
        self.etyUsername = tk.Entry(self.root)
        self.etyUsername.place(x=self.x, y=self.y + 20)

        self.lblEmail = tk.Label(self.root, text='Your Email')
        self.lblEmail.place(x=self.x, y=self.y + 40)
        self.etyEmail = tk.Entry(self.root)
        self.etyEmail.place(x=self.x, y=self.y + 60)

        self.lblPassword = tk.Label(self.root, text='Your Password')
        self.lblPassword.place(x=self.x, y=self.y + 80)
        self.etyPassword = tk.Entry(self.root)
        self.etyPassword.place(x=self.x, y=self.y + 100)

        self.lblCheckPassword = tk.Label(self.root, text='Check Your Password')
        self.lblCheckPassword.place(x=self.x, y=self.y + 120)
        self.etyCheckPassword = tk.Entry(self.root)
        self.etyCheckPassword.place(x=self.x, y=self.y +140)

# Chạy ứng dụng
if __name__=='__main__':
    # Tạo cửa sổ chính
    root = tk.Tk()
    # Khởi tạo đối tượng MyProject với cửa sổ chính
    app = MyProject(root)
    # Cho người dùng điều khiển cửa sổ
    root.mainloop()