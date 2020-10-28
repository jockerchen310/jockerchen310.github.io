import tkinter

def on_click():
    print('plt.show()')

top=tkinter.Tk(className='按钮') 

plt.subplot(221)
t = np.linspace(-5.0,5.0,1000) 
plt.ylim(0,2)
x = np.exp(-1.5*t)
plt.plot(t,x)
x = np.exp(1.5*t)
plt.plot(t,x)
x = np.exp(0*t)
plt.plot(t,x)
plt.xlabel("t")
plt.ylabel("x")

top.geometry('700x450')
#加上按钮
button1 = tkinter.Button(top)
button1['text'] = '离散信号1'
#添加按钮操作 
button1['command'] = on_click 
button1.pack()

#进入消息循环体
top.mainloop()