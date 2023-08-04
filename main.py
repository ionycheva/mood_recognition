from tkinter import *
from tkinter import ttk
import prediction_package as pp


m_name = 'SVC_model.joblib'
v_name = 'vectorizer.joblib'


def analyze():
    text = input_.get("1.0", END)
    result = pp.make_prediction(vectorizer_name=v_name, model_name=m_name, x=text)
    result_text = pp.str_prediction(y=result)
    if len(text) == 1:
        result_text = ""
    output.delete(1.0, END)
    output.insert(END, result_text)


if __name__ == '__main__':
    win = Tk()
    win.geometry("500x300")

    win.title(" Q&A ")

    label = Label(win, text="Enter your text and click 'Analyze' button!", font='Helvetica 15')
    label.pack()

    input_ = Text(win, height=8, width=50, font='Helvetica 15')
    input_.place(relx=.5, rely=.35, anchor=CENTER)

    ttk.Button(win, text="Analyze!", command=analyze).place(relx=.5, rely=.7, anchor=CENTER)

    output = Text(win, height=2, width=14, font='Helvetica 15')
    output.place(relx=.5, rely=.85, anchor=CENTER)

    win.mainloop()
