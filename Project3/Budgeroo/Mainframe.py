import pandas as p
from matplotlib.pyplot import pie, axis, show
from matplotlib import pyplot as plt
import tkinter as tk



#read in .csv file of expenses, drop empty column.
df = p.read_csv("Expense data - Sheet1.csv")
df.drop('Unnamed: 3', axis = 1, inplace=True)
#ensure that the total price amount of each repeating product is calculated
totals = df.groupby(df["Product"])["Price"].sum()
#var for sum of all expenses
tv = df.iat[0, 3]
#var for the most frequent purchase made in expense report
#frq = (df.Product.mode())
frq = df.mode()['Product'][0]
def expense_analyzer(totals,tv):

    #plotting of pie chart
    axis('equal')
    pie(totals, labels = totals.index, autopct= '%1.1f%%', pctdistance=0.8)
    plt.suptitle('Total amount of money spent this month: $'+str(tv))
    plt.title('Your Expenses (percentage)')

    #create legend specifying total amount spent on each section of expenses
    plt.legend(totals,
              facecolor="#2cdbd5",
               title="Total spent in each category (in U.S. Dollars)",
               loc="lower right",
              #bbox_to_anchor=(1, 0, 0.5, 1)
               )
    show()

#Frequency Analyzer function
def freq_analyzer(frq):

    #plot the product name and amount of times purchased on a line graph
    plt.plot(df['Product'].value_counts())
    #specify what the most frequent purchase was
    plt.suptitle('Your most frequent purchase looks like its ' + str(frq) ,fontsize = 14, fontweight = 'bold')
    plt.title("Frequency of purchases by product")
    plt.xlabel("Expense Name")
    plt.ylabel("Frequency of purchase/charge")

    plt.show()

#define function to open a new GUI window with relevant entry boxes
def budge_mkr_open():
    #define function to create a budget based off of entry fields
    def budge_mkr_pies():
        #format the entries so they are non-case sensitive and do not contain commas
        sal = salary.get().upper().replace(",","")
        life = lifestyle.get().upper()
        #check to see if salary contains numbers, convert it to an integer, and identify how much the user has to spend each month
        if sal.isnumeric():
            val = int(sal)/12 #monthly pay
            #begin algorithim for matching responses with a budget
            if life == 'LAVISH':
                housing = round(val * 0.35) #35 % of monthly pay for housing
                food = round(val * 0.15) #restaurants...grass finished meat...
                savings = round(val * 0.05) #who cares about saving money? its about spending!
                transportation = round(val * 0.20) #expensive car...
                utilities = round(val * 0.10) #utilities high bc of cost of housing
                rec = round(val * 0.15) #lets spend our money!!! luxury goods!

                labels = 'Housing','Food','Savings','Transportation','Utilities','Recreation'
                cats = [housing,food,savings,transportation,utilities,rec]
                fig1, ax1 = plt.subplots()
                ax1.pie(cats, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.suptitle('Total salary: $' + sal,fontsize = 14, fontweight = 'bold')
                plt.title('Your generated Monthly Budget!')
                plt.legend(cats)
                # plt.savefig('budgetpie.png', bbox_inches = 'tight')

                # create legend specifying total amount spent on each section of expenses
                plt.legend(cats,
                           facecolor="#2cdbd5",
                           title="Total budget in each category (in U.S. Dollars)",
                           loc="lower right",
                           #bbox_to_anchor=(1, 0, 0.5, 1)
                           )
                plt.show()
                #print(housing,food,savings,transportation,utilities,rec)

            elif life == 'NORMAL':
                housing = round(val *0.31) #31% of monthly pay for housing
                food = round(val * 0.14)  # 14%
                savings = round(val * 0.21)  #21% for savings who cares about saving money? its about spending!
                transportation = round(val * 0.14)  # 14% average car...
                utilities = round(val * 0.08)  # 8 % utils
                rec = round(val * 0.12) #lets have some fun
                labels = 'Housing', 'Food', 'Savings', 'Transportation', 'Utilities', 'Recreation'
                cats = [housing, food, savings, transportation, utilities, rec]
                fig1, ax1 = plt.subplots()
                ax1.pie(cats, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.suptitle('Total salary: $' + sal,fontsize = 14, fontweight = 'bold')
                plt.title('Your generated Monthly Budget!')
                plt.legend(cats)
                # plt.savefig('budgetpie.png', bbox_inches = 'tight')

                # create legend specifying total amount spent on each section of expenses
                plt.legend(cats,
                           facecolor="#2cdbd5",
                           title="Total budget in each category (in U.S. Dollars)",
                           loc="lower right",
                           #bbox_to_anchor=(1, 0, 0.5, 1)
                           )
                plt.show()


                #print(housing,food,savings,transportation,utilities,rec)

            elif life == 'CHEAP':
                housing = round(val * 0.25) #25% monthly pay for housing
                food = round(val * 0.10)  # 10%
                savings = round(val * 0.45)  # stashing $$$ underneath the bed
                transportation = round(val * 0.10)  # 10% poor car...
                utilities = round(val * 0.05)  # 5% utils cheap home
                rec = round(val * 0.05)  # lets have no fun
                labels = 'Housing', 'Food', 'Savings', 'Transportation', 'Utilities', 'Recreation'
                cats = [housing, food, savings, transportation, utilities, rec]
                fig1, ax1 = plt.subplots()
                ax1.pie(cats, labels=labels, autopct='%1.1f%%',
                        shadow=True, startangle=90)
                ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
                plt.suptitle('Total salary: $' + sal,fontsize = 14, fontweight = 'bold')
                plt.title('Your generated Monthly Budget!')
                plt.legend(cats)
                # plt.savefig('budgetpie.png', bbox_inches = 'tight')

                # create legend specifying total amount spent on each section of expenses
                plt.legend(cats,
                           facecolor="#2cdbd5",
                           title="Total budget in each category (in U.S. Dollars)",
                           loc="lower right",
                           #bbox_to_anchor=(0.05, 0., 0.5, 0.5)
                           )
                plt.show()
        #error message that will exit you out the tool if you do not type in a valid salary and print this string to the screen
        else:
            print('Please enter a valid number for the salary or a valid keyword!')
            exit()
#begin the creation of the second Tkinter window for the budget maker
    HEIGHT = 1800
    WIDTH = 1800
    # creation of gui using tkinter
    root2 = tk.Toplevel(root)
    # creation of size of entire window
    canvas = tk.Canvas(root2, height=HEIGHT, width=WIDTH,bg='#8EC6DF')
    canvas.pack()

    label1= tk.Label(canvas,text="Welcome to Budgeroo's budget creation tool!",font=("arial",19,"bold"),bg='#8EC6DF')
    label1.place(relx=0.2, rely=0, relwidth=0.60,relheight = 0.1)

    label2 = tk.Label(canvas, text="Q1) What is your yearly salary? Please enter an integer value.", font=("arial", 19, "bold"),bg='#8EC6DF')
    label2.place(relx=0.2, rely=0.1, relwidth=0.60,relheight = 0.1)

    salary = tk.Entry(canvas,font=40)
    salary.place(relx=0.2, rely=0.2, relwidth=0.60,relheight=0.05)

    label3 = tk.Label(canvas, text="Q2) What is your lifestyle? Please type one of the three options: Lavish, Cheap, or Normal.",font=("arial", 19, "bold"),bg='#8EC6DF')
    label3.place(relx=0.2, rely=0.3, relwidth=0.60, relheight=0.1)

    lifestyle = tk.Entry(canvas, font=40)
    lifestyle.place(relx=0.2, rely=0.4, relwidth=0.60, relheight=0.05)

    submit = tk.Button(canvas, text="Submit!", font=40,command=lambda:budge_mkr_pies())
    submit.place(relx=0.2,rely=0.5,relwidth=0.60,relheight=0.05)

#MAIN GUI WINOOW
##make height and width vars to be passed into canvas creation
HEIGHT = 1800
WIDTH = 1800
#creation of gui using tkinter
root = tk.Tk()

#creation of size of entire window
canvas = tk.Canvas(root,height=HEIGHT, width=WIDTH)
canvas.pack()

#create frame to fill entire screen with color
frame = tk.Frame(root, bg='#8EC6DF')
frame.place( relwidth=1, relheight=1)

#create buttons and center them
button = tk.Button(frame, text = "Create a budget", font = ("Arial",15), bg = '#46DBCE', fg='red',command=lambda:budge_mkr_open())
button.place(relx=0.1, rely=0.5,relwidth=0.25,relheight=0.25,)

button2 = tk.Button(frame, text = "Analyze your expenses", font=("Arial",15), bg = '#46DBCE', fg='red',command=lambda : expense_analyzer(totals,tv))
button2.place(relx=0.4, rely=0.5,relwidth=0.25,relheight=0.25)

button3 = tk.Button(frame, text = "Investigate most frequent purchases", font = ("Arial",15), bg = '#46DBCE', fg='red', command=lambda: freq_analyzer(frq))
button3.place(relx=0.7, rely=0.5,relwidth=0.25,relheight=0.25)

#create label
label = tk.Label(frame, text="Welcome to Budgeroo!",bg='#8EC6DF', font=("Courier",44))
label.place(relx=0.3, rely=0, relwidth=0.45,relheight = 0.2)

label2 = tk.Label(frame, text="Select an option below to get started!",bg='#8EC6DF', font="Courier")
label2.place(relx=0.3, rely=0.25, relwidth=0.45,relheight = 0.2)

root.mainloop()

#end






