import tkinter as tk
from tkinter import ttk
from csv import DictWriter
                            # window work
win=tk.Tk()
win.geometry("600x400")
win.minsize(width=350,height=250)
win.maxsize(width=1900,height=1500)
                                        # title
win.title('Recruitement Form')
                                        # Label work
label_greet=ttk.Label(win,text="WELCOME")
label_greet.grid(row=0,column=0,sticky=tk.N)
label_greet.configure(foreground='#FF3600')

label_name=ttk.Label(win,text="Enter Your Name:  ")
label_name.grid(row=2,column=1)
label_name.configure(foreground='#FF3600')

label_father=ttk.Label(win,text="Enter Your Father Name:  ")
label_father.grid(row=3,column=1)
label_father.configure(foreground='#FF3600')

label_mother=ttk.Label(win,text="Enter Your Mother Name:  ")
label_mother.grid(row=4,column=1)
label_mother.configure(foreground='#FF3600')

label_age=ttk.Label(win,text="Enter Your Age:  ")
label_age.grid(row=5,column=1)
label_age.configure(foreground='#FF3600')

label_class=ttk.Label(win,text="Enter Your Class:  ")
label_class.grid(row=6,column=1)
label_class.configure(foreground='#FF3600')

label_dob=ttk.Label(win,text="Date Of Birth:  ")
label_dob.grid(row=7,column=1)
label_dob.configure(foreground='#FF3600')

label_school=ttk.Label(win,text="Enter Your School Name:  ")
label_school.grid(row=8,column=1)
label_school.configure(foreground='#FF3600')

label_email=ttk.Label(win,text="Enter Your E-mail:  ")
label_email.grid(row=9,column=1)
label_email.configure(foreground='#FF3600')

label_gender=ttk.Label(win,text="Gender :  ")
label_gender.grid(row=10,column=1)
label_gender.configure(foreground='#FF3600')

label_gender=ttk.Label(win,text="Gender :  ")
label_gender.grid(row=10,column=1)
label_gender.configure(foreground='#FF3600')



                                        #    Entrybox work
name_var=tk.StringVar()
name_entrybox=ttk.Entry(win,width=22,textvariable=name_var)
name_entrybox.grid(row=2,column=3)
name_entrybox.focus()

father_var=tk.StringVar()
father_entrybox=ttk.Entry(win,width=22,textvariable=father_var)
father_entrybox.grid(row=3,column=3)

mother_var=tk.StringVar()
mother_entrybox=ttk.Entry(win,width=22,textvariable=mother_var)
mother_entrybox.grid(row=4,column=3)

age_var=tk.StringVar()
age_entrybox=ttk.Entry(win,width=22,textvariable=age_var)
age_entrybox.grid(row=5,column=3)

class_var=tk.StringVar()
class_entrybox=ttk.Entry(win,width=22,textvariable=class_var)
class_entrybox.grid(row=6,column=3)

dob_var=tk.StringVar()
dob_entrybox=ttk.Entry(win,width=22,textvariable=dob_var)
dob_entrybox.grid(row=7,column=3)

school_var=tk.StringVar()
school_entrybox=ttk.Entry(win,width=22,textvariable=school_var)
school_entrybox.grid(row=8,column=3)

email_var=tk.StringVar()
email_entrybox=ttk.Entry(win,width=22,textvariable=email_var)
email_entrybox.grid(row=9,column=3)

gender_var=tk.StringVar()
gender=ttk.Combobox(win,width=22,textvariable=gender_var,state='readonly')
gender['values']=('Female','Male','Other')
gender.current(1)
gender.grid(row=10,column=3)

# status_var=tk.StringVar
# status=ttk.Radiobutton(win,width=22,variable=status_var) 
# status['option']=('Married','Unmarried')
# status.grid(row=11,column=1)

term_var=tk.StringVar()
term=ttk.Checkbutton(win,text="Terms And Conditions",variable=term_var)
term.grid(row=14,column=1)

    # Marks Entry

label_hindi=ttk.Label(win,text="Hindi Marks :  ")
label_hindi.grid(row=16,column=1)
label_hindi.configure(foreground='#FF3600')

hindi_var=tk.IntVar()
hindi_entrybox=ttk.Entry(win,width=22,textvariable=hindi_var)
hindi_entrybox.grid(row=16,column=3)

label_english=ttk.Label(win,text="English Marks :  ")
label_english.grid(row=18,column=1)
label_english.configure(foreground='#FF3600')

english_var=tk.IntVar()
english_entrybox=ttk.Entry(win,width=22,textvariable=english_var)
english_entrybox.grid(row=18,column=3)

label_math=ttk.Label(win,text="Maths Marks :  ")
label_math.grid(row=19,column=1)
label_math.configure(foreground='#FF3600')

math_var=tk.IntVar()
math_entrybox=ttk.Entry(win,width=22,textvariable=math_var)
math_entrybox.grid(row=19,column=3)

label_physics=ttk.Label(win,text="Physics Marks :  ")
label_physics.grid(row=20,column=1)
label_physics.configure(foreground='#FF3600')

physics_var=tk.IntVar()
physics_entrybox=ttk.Entry(win,width=22,textvariable=physics_var)
physics_entrybox.grid(row=20,column=3)

label_chemistry=ttk.Label(win,text="Chemistry Marks :  ")
label_chemistry.grid(row=21,column=1)
label_chemistry.configure(foreground='#FF3600')

chemistry_var=tk.IntVar()
chemistry_entrybox=ttk.Entry(win,width=22,textvariable=chemistry_var)
chemistry_entrybox.grid(row=21,column=3)

def function():
    N=name_var.get()
    F=father_var.get()
    M=mother_var.get()
    A=age_var.get()
    C=class_var.get()
    S=school_var.get()
    D=dob_var.get()
    E=email_var.get()
    G=gender_var.get()
    H=hindi_var.get()
    E1=english_var.get()
    M1=math_var.get()
    P=physics_var.get()
    C1=chemistry_var.get()
    # t= hindi_var.get()+english_var.get()+math_var.get()+physics_var.get()+chemistry_var.get()
    t=H+E1+M1+P+C1
    pp= (t*100)/500

    if term_var.get()==0:
        print("Please Check Mark Terms And Conditions")
    else:
        with open ('file.CSV','a') as f:
            dict_writer=DictWriter(f,fieldnames=['NAME','FATHER NAME','MOTHER NAME','AGE','GENDER','CLASS','SCHOOL','DATE OF BIRTH','EMAIL ID','HINDI','ENGLISH','MATH','PHYSICS','CHEMISTRY','TOTAL','PERCENT'])
            dict_writer.writeheader()
            dict_writer.writerow({'NAME':N,'FATHER NAME':F,'MOTHER NAME':M,'AGE':A,'GENDER':G,'CLASS':C,'SCHOOL':S,'DATE OF BIRTH':D,'EMAIL ID':E,'HINDI':H,'ENGLISH':E1,'MATH':M1,'PHYSICS':P,'CHEMISTRY':C1,'TOTAL':t,'PERCENT':pp})
# def percent():
    
#     if (t<250):
#         print("FAIL")
#     else:
#         print("PASS")
# submit=ttk.Button(win,text="Submit MARKS",command=percent)
# submit.grid(row=22,column=6)


submit=ttk.Button(win,text="Submit Now",command=function)
submit.grid(row=24,column=6)
# submit.configure(foreground='Blue')
                                                 
                                        








win.mainloop()