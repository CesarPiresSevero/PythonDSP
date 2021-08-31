##########################################################################
#                                                                        #
#                       DSP Interactive Encyclopedia                     #
#                                                                        #
##########################################################################

'''
*	Overview
   Easy way to seach and collect information about pertinent DSP 
   algorithms. This content will be read from a source file that the 
   data can be added in any order. The idea is to summerize and create 
   an encyclopedia with all important DSP concepts in one organized 
   place that can be referenced easier than a single book or a online 
   search. 
   The contents can contain any pure text data. Ideally with link for 
   references.
   The best part is that this data will be stored in the same repo as 
   the demonstration codes. That means only by acessing the repo all the
   resources are there.
   The library application will be entire accesed with the terminal and
   won't use any GUI for usage.

*	Features
   The search engine will sort subjects automatically by:
   - Alphabetical order
   - Date modified
   - Category alphabetical order
   The user can make custom search by:
   - Letters: search any ammount of letters that matches title + contents
   - Keywords: search in title + contents
   - Date modified: using start to end date
   The user can also add aditional chapters inside each subject that will 
   be used as index. The user than can access them individually otherwise
   their contents will be omitted when the main subject is accessed.

*	Data structure
   The data structure used will be YAML due to its similarity to Python
   indexation use. Here is an example of usage:
	---
   #Subject name
	Polyphase quadrature filter:
      #Main category        
   	category: "Filters"
      #Subcategory field
      subcategory: "FIR"
      #YYYY/MM/DD   
   	date: "2021/05/04"
      #List or single string
   	links: "https://en.wikipedia.org/wiki/Polyphase_quadrature_filter" 
      # |- added to keep the newlines
   	contents: |-
         A polyphase quadrature filter, or PQF, is a filter bank which 
         splits an input signal into a given number N (mostly a 
         power of 2) of equidistant sub-bands. 
      # Can have any size of components
      subcontents:
         Applications: Compression, decimation and interpolation
         Comercial Usage: MP3	
	---
   General rules:
   - The names "category","date","links","contents" and "subcontents" 
   are mandatory and other names will be ignored
   - No field is mandatory for the code to work. Non complete fields will 
   be set as "Null" in the search
   - Only contents will be displayed, the other fields will be used as
   metadata unless user requestes more info

*	Future ideas
   - Add pictures from "assets" automatically showing in the terminal or
   externally as set by the user
   - Add MSDOS aesthetic to the tool 

'''

#Texts used in the application
logo_text='''
################################################################################
#                                                                              #
#                       DSP Interactive Encyclopedia                           #
#                                                                              #
################################################################################
'''
intro_text='''
Easy way to seach and collect information about pertinent DSP algorithms. 
This content will be read from a source file that the data can be added in 
any order. The idea is to summerize and create an encyclopedia with all 
important DSP concepts in one organized place that can be referenced easier 
than a single book or a online search. 
'''
options_text='''
----------------------------------------   ------------   ----------
| Sort by (N)ame, (D)ate or (C)ategory |   | (S)earch |   | (E)xit |
----------------------------------------   ------------   ----------
'''
searc_text='''
----------------   ------------   ----------
| (N)ew search |   | (R)eturn |   | (E)xit |
----------------   ------------   ----------
'''
return_text='''
------------   ----------
| (R)eturn |   | (E)xit |
------------   ----------
'''
sort_by_name_text="""SORT BY NAME

Select the subject:\n"""

sort_by_date_text="""SORT BY DATE

Select the subject:\n"""

sort_by_category_text="""SORT BY CATEGORY 

Select the subject:\n"""

#Importing libs
import os
import yaml
import time

#The YAML file to source from
filename="example.yaml"

#The application class
class application:
   def __init__(self):
      self.clear_screen()
      self.keypress="" #user input
      self.data={} #YAML file dictionary
      self.status=0 #0-> Main menu, 1-> Sort menu, 2-> Search Menu, 3-> Subject menu, 4-> Subcontent menu
      self.sort=""
      self.subject=""
      self.read_file()
      self.menus()

   def clear_screen(self):
      os.system('cls' if os.name == 'nt' else 'clear')  

   def read_file(self):
      with open(filename, 'r') as input_data:
         try:
            self.data=yaml.safe_load(input_data)  
         except yaml.YAMLError as exc:
            print("Error reading the YAML file:"+filename)
            raise
   def print_main_screen(self):
      self.clear_screen()
      print(logo_text,intro_text,options_text)

   def print_sort_screen(self):
      self.clear_screen()
      print(logo_text)

   def get_user_input(self):
      self.keypress=input()

   def print_list_of_options(self,inlist,extralist=None):
      if(extralist==None):
         for index, val in enumerate(inlist):
            print("("+str(index)+")",val)
      else:
         for index, val in enumerate(inlist):
            try:
               if(extralist[index-1]!=extralist[index]): print("*",extralist[index])
            except:
               print("*",extralist[index])
            print("("+str(index)+")",val)

   def menus(self):
      while True:
         #Main menu
         if(self.status==0): 
            #Showing main screen
            self.print_main_screen()
            while True:
               self.get_user_input()
               self.print_main_screen()
               if(self.keypress=="e"): return
               if(self.keypress not in "ndcs") or self.keypress=="" or len(self.keypress)>1:
                  pass
               else:
                  if(self.keypress in "ndc"): #Sort
                     self.status=1
                     self.sort=self.keypress
                     break
                  else:                  #Search
                     self.status=2
                     break
               time.sleep(0.1)
         #Sort menu
         elif(self.status==1):   
            if(self.sort=="n"):                          #Sort by name
               while(True):
                  subjects=sorted(list(self.data.keys()))
                  self.print_sort_screen()
                  print(sort_by_name_text)
                  self.print_list_of_options(subjects)
                  print(return_text)
                  self.get_user_input()
                  if(self.keypress=="r"): 
                     self.status=0
                     self.print_main_screen()
                     break
                  elif(self.keypress=="e"): 
                     self.print_sort_screen()
                     print(sort_by_name_text)
                     self.print_list_of_options(subjects)
                     print(return_text)
                     return
                  elif not self.keypress.isnumeric() or self.keypress=="" or len(self.keypress)>1 or (len(subjects)-1<int(self.keypress)):
                     pass
                  else:
                     self.status=3
                     self.subject=subjects[int(self.keypress)]
                     break
                  time.sleep(0.1)
            elif(self.sort=="d"):                        #Sort by date
               while(True):
                  subjects=sorted(list(self.data.keys()))
                  date={}
                  for sub in subjects:
                     try:
                        date[sub]=self.data[sub]["date"]
                     except:
                        date[sub] = "Null"
                  for val in date: 
                     if(date[val]=="Null"): date[val]=date.pop(val)  
                  subjects=list(date.keys())
                  self.print_sort_screen()
                  print(sort_by_date_text)
                  self.print_list_of_options(subjects,list(date.values()))
                  print(return_text)
                  self.get_user_input()
                  if(self.keypress=="r"):
                     self.print_main_screen() 
                     self.status=0
                     break
                  elif(self.keypress=="e"): 
                     self.print_sort_screen()
                     print(sort_by_date_text)
                     self.print_list_of_options(subjects,list(date.values()))
                     print(return_text)
                     return
                  elif not self.keypress.isnumeric() or self.keypress=="" or len(self.keypress)>1 or (len(subjects)-1<int(self.keypress)):
                     pass
                  else:
                     self.status=3
                     self.subject=subjects[int(self.keypress)]
                     break
                  time.sleep(0.1)
            elif(self.sort=="c"):                        #Sort by category
               while(True):
                  subjects=sorted(list(self.data.keys()))
                  category={}
                  for sub in subjects:
                     try:
                        category[sub]=self.data[sub]["category"]
                     except:
                        category[sub] = "Null"
                  #Separating category in alphabetical order
                  category=dict(sorted(category.items(), key=lambda item: item[1]))
                  #Sending subjects with no category to the end of list
                  for val in list(category): 
                     if(category[val]=="Null"): category[val]=category.pop(val)  
                  subjects=list(category.keys())
                  self.print_sort_screen()
                  print(sort_by_category_text)
                  self.print_list_of_options(subjects,list(category.values()))
                  print(return_text)
                  self.get_user_input()
                  if(self.keypress=="r"):
                     self.print_main_screen() 
                     self.status=0
                     break
                  elif(self.keypress=="e"): 
                     self.print_sort_screen()
                     print(sort_by_category_text)
                     self.print_list_of_options(subjects,list(category.values()))
                     print(return_text)
                     return
                  elif not self.keypress.isnumeric() or self.keypress=="" or len(self.keypress)>1 or (len(subjects)-1<int(self.keypress)):
                     pass
                  else:
                     self.status=3
                     self.subject=subjects[int(self.keypress)]
                     break
                  time.sleep(0.1)
         #Search menu
         elif(self.status==2):
            break
         #Contents menu
         elif(self.status==3):
            self.clear_screen()
            print(self.subject,"\n")
            print(self.data[self.subject]["contents"])
            return
         #Subcontents menu
         elif(self.status==4):
            self.clear_screen()
            print(self.data[self.subject]["subcontents"])
            return
         time.sleep(0.1)


if __name__ == '__main__':
   app_obj=application()
