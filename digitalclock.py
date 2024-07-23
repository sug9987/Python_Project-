from tkinter import *
from datetime import *

root = Tk()
root.title("Digital Clock By Sumit Gupta")
root.geometry("800x300+400+100")
root.configure(bg="dark gray")
root.resizable(False,False)

lab_msg = Label(root,text="",font=("Arial",100,"bold"),bg="dark gray",fg="white")
lab_msg.pack(pady=50)


def show():
	dt = datetime.now()

	hr = dt.hour
	shr = str(hr)
	if hr<10:
		shr = "0"+shr
	
	mi = dt.minute
	smi = str(mi)
	if mi < 10:
		smi = "0"+smi
	
	se = dt.second
	sse = str(se)
	if se < 10:
		sse = "0"+sse

	msg = shr+":"+smi+":"+sse
	lab_msg.configure(text=msg)
	root.after(1000,show)

show()


root.mainloop()