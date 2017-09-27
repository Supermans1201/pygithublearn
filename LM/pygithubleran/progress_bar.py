# coding=utf-8
from Tkinter import *
import ttk
import threading

class Progressbar_Thread(threading.Thread):
    def bt_click(self):
        print (self.name)

    def close(self):
        print "close"
        # if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
        self.root.destroy()

    def __init__(self,root,total=10000,name="progress_bar"):
        super(Progressbar_Thread, self).__init__()
        self.name=name
        self.condition =threading.Condition()
        self.total = total
        self.root=root
        # self.root.overrideredirect(True)

        self.root.title(self.name)
        self.root.iconbitmap('Icon.ico')
        self.root.configure(background='#882288')
        self.root.attributes("-topmost", 1)
        self.root.attributes("-alpha",0.83)
        # self.root.attributes("-disabled",0)
        self.root.protocol('WM_DELETE_WINDOW', lambda: None)

        self.frame = Frame(root)  # 创建一个框架
        self.frame.pack()
        self.label_str = StringVar()
        self.label_str.set("处理中ing：0%")

        self.value=0


        self.label=Label(self.frame, text=self.label_str.get(),  textvariable = self.label_str)

        self.progressbar = ttk.Progressbar(self.frame, length=500, maximum=total)
        self.progressbar.config(value=self.value)

        self.label.grid(row=0, column=0, sticky=E)
        self.progressbar.grid(row=0, column=1)
        self.bt = Button(self.frame, text="Get Name", command=self.bt_click)
        # grid布局
        self.bt.grid(row=0, column=2,sticky=W)
        self.bt.config(cursor="hand2")

        self.root.width=700
        self.root.height=30
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (self.root.width, self.root.height, (screenwidth - self.root.width) / 2, (screenheight - self.root.height) / 2-100)
        self.root.geometry(size)
        root.resizable(width=False, height=False)

    def update_value(self):
        self.progressbar.config(value=self.value)
        self.progressbar.update()
        if float(self.value) / self.total==1:
            self.label_str.set("已完成！100%")
            self.root.protocol('WM_DELETE_WINDOW', self.close)
        else:
            self.label_str.set("处理中ing:" + "{:.2f}".format(float(self.value) / self.total) + "%")

    def run(self):
        print "thread {} is ready ".format(self.name)
        with self.condition:
            self.condition.wait()

        for i in range(self.total+1):
            self.value=i

            work_thread = threading.Thread(target=self.update_value)
            work_thread.setDaemon(True)
            work_thread.start()

            with self.condition:
                self.condition.wait()
        print "end"
    def add(self):
        with self.condition:
            self.condition.notify()

class progress_bar_win:
    def __init__(self,work_func,name="progress_bar",total=100):
        self.name=name
        self.total=total
        self.root = Tk()
        self.progress_thread  = Progressbar_Thread(root=self.root, name=self.name, total=self.total)
        self.progress_thread.setDaemon(True)
        self.progress_thread.start()

        # btwindow=t_gui(name="hello world!",thread=thread)
        work_thread = threading.Thread(target=work_func, args=(self.progress_thread, self.total))
        work_thread.start()

    def mainloop(self):
        self.root.mainloop()
    def destroy(self):
        self.root.destroy()
    def add(self):
        self.progress_thread.add()



#在界面中使用进度条
class t_gui:
    def close(self):
        print "close"
        try:
            self.progress_bar.destroy()
        except:
            pass
        self.root.destroy()
    def __init__(self, name):
        self.name=name

        self.root = Tk()
        self.root.title(self.name)
        self.root.attributes("-topmost", 1)
        self.root.protocol('WM_DELETE_WINDOW', self.close)

        self.root.width = 270
        self.root.height = 30
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (self.root.width, self.root.height, (screenwidth - self.root.width) / 2,
                                (screenheight - self.root.height) / 2 - 100)
        self.root.geometry(size)

        self.frame = Frame(self.root)
        self.frame.pack()

        self.bt = Button(self.frame, text="add",command=self.bt_click)
        self.bt.grid(row=1, column=3)
        #使用进度条类
        self.progress_bar = progress_bar_win(work_func=None,total=10)
        #启动进度条
        self.progress_bar.mainloop()
        self.root.mainloop()
    # bt_click已经是在一个额外的线程中了
    def bt_click(self,p,total):
        self.progress_bar.add()

# t_gui(name="t_gui")

#在代码中使用进度条
def work_func1(progress_thread,total):
    import time
    for i in range(total+2):
        #任务的时间太短会有bug。
        time.sleep(0.05)
        progress_thread.add()
p=progress_bar_win(work_func=work_func1,total=100)
p.mainloop()

# #在代码中使用进度条2
# def work_func2(p,total):
#     import time
#     for i in range(total+2):
#         #任务的时间太短会有bug。
#         time.sleep(0.05)
#         p.add()
# p=progress_bar_win(work_func=work_func1,total=100)
# p.mainloop()
