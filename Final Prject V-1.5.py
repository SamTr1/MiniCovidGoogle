import csv
import tkinter

"""
Name: Samuel Trujillo
Date: 14 Decemeber 2021

Description:
The program takes in a csv file of covid related data of countries such as their population, number of covid cases
that week, and number of deaths that week. A window appears where the user can click a button to the sort the data and
then download the file as a csv file. As well there is a search bar where the user may ask a question or ask how they
would like there data to be sorted.

Sample runs:
I have emailed you my smaple runs becaue i se GUI's in my poject,
the email was sent 12/9/21

Sources:
Data from Kaggle "Covid-19 Weekly Trends In Asia - Latest Data" by Anadhu H
https://www.kaggle.com/anandhuh/covid19-weekly-trends-in-asia-latest-data

Functions:
Class: Sort_Covid_Data_Window()
Methods: __init__(), if_Word_Found(), sort_By_Question(), search_By_Question(), breakdown_Question(),reset_Button_Color(),
        download(), sort_Pop(), sort_MostCases(), sort_MostCasesProceding(), sort_MostDeaths(), sort_MostDeathsProceding()
Functions: import_File(), export_File(), sort_Info(), sort_Info_LtoG(), search_MostOfData(), search_LeastOfData()

Data Structures:
List, Files, Variables

Recent Topics:
GUI
File Input/Output
Insertion Sort
Word Search

"""

class Sort_Covid_Data_Window:
    
    def __init__(self):
        
        # ------------------
        # ------------------
        # Create Window
        self.main_Window = tkinter.Tk()
        self.main_Window.title("Final Project")
        self.main_Window.geometry("700x500")
        
        self.message = 0
        
        # ------------------
        # ------------------
        # Create Labels
        self.intro_Label = tkinter.Label(self.main_Window,
                                         text="Welcome! Here I have provided covid information from Asia") 
        self.question_Label = tkinter.Label(self.main_Window,
                                          text="Click a button below, to have the covid data sorted to your liking")
        
        # ------------------
        # ------------------
        # Create Buttons
        
        self.sort_Pop_Button = tkinter.Button(self.main_Window, text="Sort by Population",command=self.sort_Pop)
        self.download_Data_Button = tkinter.Button(self.main_Window, text="Download Data",command=self.download)
        
        # ++++++++++++
        # Buttons Related to Most Cases
        self.sort_MostCases_Button = tkinter.Button(self.main_Window, text="Sort by the most cases in the last 7 days",command=self.sort_MostCases)                                     
        self.sort_MostCasesProceding_Button = tkinter.Button(self.main_Window, text="Sort by the most cases in the proceding 7 days",command=self.sort_MostCasesProceding)
        
        # ++++++++++++
        # Buttons Related to Most Deaths
        self.sort_MostDeaths_Button = tkinter.Button(self.main_Window, text="Sort by the most deaths in the last 7 dyas",command=self.sort_MostDeaths)
        self.sort_MostDeathsProceding_Button = tkinter.Button(self.main_Window, text="Sort by the most deaths in the proceding 7 days",command=self.sort_MostDeathsProceding)
        
        self.question_Entry = tkinter.Entry(self.main_Window, width=25)
        self.search_Button = tkinter.Button(self.main_Window,text="Search",command=self.breakdown_Question)
        
        # ------------------
        # ------------------
        # Package Labels 
        self.intro_Label.pack()
        self.question_Label.pack()
        
        # ------------------
        # ------------------
        # Package Buttons
        
        # ++++++++++++
        # Most Cases Related Packages
        self.sort_MostCases_Button.pack()
        self.sort_MostCasesProceding_Button.pack()
        
        # ++++++++++++
        # Most Deaths Related Packages
        self.sort_MostDeaths_Button.pack()
        self.sort_MostDeathsProceding_Button.pack()
        
        # ++++++++++++
        # Other Packages
        self.sort_Pop_Button.pack()
        self.download_Data_Button.pack()
        
        self.question_Entry.pack()
        self.search_Button.pack()
        
        tkinter.mainloop()
    
    # =======================
    # Takes in a List of strings and a word to search for to see if the given word is in the list
    def if_Word_Found(self,search_For):
        
        for index in range(0, len(self.message)):
            
            if self.message[index].lower() == search_For:
                return True
            
        return False
    
    
    # =======================
    def sort_By_Question(self,column_Num):
        if self.if_Word_Found("greatest") or self.if_Word_Found("most"):
            sort_Info_LtoG(covid, column_Num)
            #sort_Info(covid, column_Num)
            self.download()
            
            answer = tkinter.Label(text= "The Information has been saved to Sort_Covid_Data.csv")
            answer.pack()
            
        elif self.if_Word_Found("least") or self.if_Word_Found("fewest"):
            sort_Info(covid, column_Num)
            #sort_Info_LtoG(covid, column_Num)
            self.download()
            
            answer = tkinter.Label(text= "The Information has been saved to Sort_Covid_Data.csv")
            answer.pack()
            
        else:
            answer = tkinter.Label(text= "Sorry your question could not be understood")
            answer.pack()
    
    # =======================
    def search_By_Question(self,column_Num):
        
        if self.if_Word_Found("greatest") or self.if_Word_Found("most"):
            
            answer = tkinter.Label(text=search_MostofData(covid,column_Num))
            answer.pack()
            
        elif self.if_Word_Found("least") or self.if_Word_Found("fewest"):
            
            answer = tkinter.Label(text=search_LeastofData(covid,column_Num))
            answer.pack()
            
        else:
            answer = tkinter.Label(text= "Sorry your question could not be understood")
            answer.pack()
    
    # =======================
    def breakdown_Question(self):
        
        self.message = self.question_Entry.get()
        self.message = self.message.split(" ")
        
        if self.if_Word_Found("from") or self.if_Word_Found("by"):
            
            if self.if_Word_Found("cases"):
                self.sort_By_Question(1)
                
            elif self.if_Word_Found("deaths"):
                self.sort_By_Question(5)
            else:
                answer = tkinter.Label(text= "Sorry your question could not be understood")
                answer.pack()
        
        elif self.if_Word_Found("which") or self.if_Word_Found("what"):
            
            if self.if_Word_Found("cases"):
                self.search_By_Question(1)
                
            elif self.if_Word_Found("deaths"):
                self.search_By_Question(5)
            else:
                answer = tkinter.Label(text= "Sorry your question could not be understood")
                answer.pack()
        
        else:
            answer = tkinter.Label(text= "Sorry your question could not be understood")
            answer.pack()
    
    
    # =======================
    # All Sorts are done from greatest to least
    def reset_Button_Colors(self):
        self.sort_Pop_Button.config(fg="black")
        
        self.sort_MostCases_Button.config(fg="black")
        self.sort_MostCasesProceding_Button.config(fg="black")
        
        self.sort_MostDeaths_Button.config(fg="black")
        self.sort_MostDeathsProceding_Button.config(fg="black")
        
        self.download_Data_Button.config(fg="black")
    
    # =======================
    def sort_Pop(self):
        sort_Info(covid,9)
        self.reset_Button_Colors()
        self.sort_Pop_Button.config(fg="blue")
    
    # =======================
    def sort_MostCases(self):
        sort_Info(covid,1)
        self.reset_Button_Colors()
        self.sort_MostCases_Button.config(fg="blue")        
    
    # =======================
    def sort_MostCasesProceding(self):
        sort_Info(covid,2)
        self.reset_Button_Colors()
        self.sort_MostCasesProceding_Button.config(fg="blue")
    
    # =======================
    def sort_MostDeaths(self):
        sort_Info(covid,5)
        self.reset_Button_Colors()
        self.sort_MostDeaths_Button.config(fg="blue")
        
    # =======================
    def sort_MostDeathsProceding(self):
        sort_Info(covid,6)
        self.reset_Button_Colors()
        self.sort_MostDeathsProceding_Button.config(fg="blue")
        
    # =======================
    def download(self):
        export_File(covid,"Sort_Covid_Data.csv")
        self.download_Data_Button.config(fg="red")

# =======================
# =======================
# =======================
def import_File(csv_File):
    
    with open(csv_File) as get_From:
        c_data = csv.reader(get_From)
        c_data = list(c_data)
    
    return c_data

# =======================
def export_File(c_info, destination_File):
    
    with open(destination_File,"w") as save_To:
        covid_writer = csv.writer(save_To)
        covid_writer.writerows(c_info)

# =======================
def sort_Info(c_info,column):
    
    # ------------------
    # inc the current number 
    for current in range(1,len(c_info)):
        # ------------------
        # Goes through all the indexs before the current number
        for previous in range(1,current):
            # ------------------
            if int(c_info[current][column]) > int(c_info[previous][column]):
                value = c_info.pop(current)
                c_info.insert(previous,value)
# =======================
def sort_Info_LtoG(c_info,column):
    
    # ------------------
    # inc the current number 
    for current in range(1,len(c_info)):
        # ------------------
        # Goes through all the indexs before the current number
        for previous in range(1,current):
            # ------------------
            if int(c_info[current][column]) < int(c_info[previous][column]):
                value = c_info.pop(current)
                c_info.insert(previous,value)

# =======================
# Finds the Country with the most amount of death or covid-19 cases
def search_MostofData(c_info,column_Num):
    
    max = int(c_info[1][column_Num])
    index_Of_Max = 1
    
    for index in range(2, len(c_info)):
        
        if int(c_info[index][column_Num]) > max:
            max = int(c_info[index][column_Num])
            index_Of_Max = index
            
    answer = "The Country with the most covid " + c_info[0][column_Num] + " is: " + str(c_info[index_Of_Max][0]) + " With a total of " + str(max) + " cases"
    return answer

# =======================
# Finds the Country with the least amount of death or covid-19 cases
def search_LeastofData(c_info,column_Num):
    
    min = int(c_info[1][column_Num])
    index_Of_Min = 1
    
    for index in range(2, len(c_info)):
        
        if int(c_info[index][column_Num]) < min:
            min = int(c_info[index][column_Num])
            index_Of_Max = index
            
    answer = "The Country with the least covid " + c_info[0][column_Num] + " is: " + str(c_info[index_Of_Max][0]) + " With a total of " + str(min) + " cases"
    return answer



covid = import_File("covid_data.csv")
gui = Sort_Covid_Data_Window()

        
    
















