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
      #List or single string          
   	category: ["Filters","FIR"]   
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
intro_text='''
################################################################################
#                                                                              #
#                       DSP Interactive Encyclopedia                           #
#                                                                              #
################################################################################
   
   Easy way to seach and collect information about pertinent DSP algorithms. 
   This content will be read from a source file that the data can be added in 
   any order. The idea is to summerize and create an encyclopedia with all 
   important DSP concepts in one organized place that can be referenced easier 
   than a single book or a online search. 
'''
options_text='''
----------------------------------------   -------------------   ----------
| Sort by (N)ame, (D)ate or (C)ategory |   | Custom (S)earch |   | (E)xit |
----------------------------------------   -------------------   ----------
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
      self.data={} #YAML file dictionary
      self.status=0 #0-> Main menu, 1-> Sort menu, 2-> Search Menu, 3-> Subject menu, 4-> Subcontent menu
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
      print(intro_text,options_text)

   def get_user_input(self):
      return(input())

   def menus(self):
      while True:
         if(self.status==0): #Main menu
            #Showing main screen
            print(intro_text,options_text)
            while True:
               keypress=self.get_user_input()
               if(keypress=="e"): return
               if(keypress not in "ndcs") or keypress=="" or len(keypress)>1:
                  self.print_main_screen()
               else:
                  if(keypress in "ndc"): #Sort
                     self.status=1
                     break
                  else:                  #Search
                     self.status=2
                     break
               time.sleep(0.1)
         elif(self.status==1):
            subjects=list(self.data.keys())
            print(self.data[subjects[1]]["contents"])
            break
         elif(self.status==2):
            break
         elif(self.status==3):
            break
         elif(self.status==4):
            break
         time.sleep(0.1)


if __name__ == '__main__':
   app_obj=application()




# dictv=dict(data.values())
# print(dictv["category"])
# print(data)
# subjects=[]
# subjects=list(data.keys())
# print(app_obj.data[subjects[1]]["contents"])
# print(app_obj.data[subjects[1]]["subcontents"])
# print(subjects)