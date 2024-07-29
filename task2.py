from tkinter import *
from requests import *

root = Tk()
root.title("Motivational Quotes  Application By Sumit Gupta")
root.geometry("1200x500+400+40")
root.configure(bg="light yellow")

f = ("Ink Free",30,"bold")

lab = Label(root, font=f, wraplength=1000, bg="light yellow",fg="black")
lab.pack(pady=10)

def show():
	try:
		url = "https://quotes-api-self.vercel.app/quote"
		res = get(url)
		data = res.json()
		quote = data['quote']
		author = data['author']
		msg = str(quote) + str(author) 
		lab.configure(text=msg)
		root.after(1000,show)

	except Exception as e:
		msg = "issue" +str(e)
		lab.configure(text=msg)
root.after(10000,show)


show()

root.mainloop()