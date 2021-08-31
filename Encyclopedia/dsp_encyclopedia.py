##########################################################################
#                                                                        #
#                       DSP Interactive Encyclopedia                     #
#                                                                        #
##########################################################################

#The YAML file to source from
filename="example.yaml"

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
   - Category alphabetical order -> alphabetical order
   - Category alphabetical order -> date modified
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
	Polyphase quadrature filter:
   	category: ["Filters","FIR"]
   	date: "12/12/2021"
   	links: "https://en.wikipedia.org/wiki/Polyphase_quadrature_filter"
   	contents: |-
         A polyphase quadrature filter, or PQF, is a filter bank which splits an input signal into a given number N (mostly a power of 2) of equidistant sub-bands. 
         These sub-bands are subsampled by a factor of N, so they are critically sampled.
         An important application of the polyphase filters (of FIR type) concerns the filtering and decimation of large band (and so high sample rate) input signals, e.g. coming from a high rate ADC, which can not be directly processed by an FPGA or in some case by an ASIC either.

   	
	---
*	Future ideas

'''

import yaml

with open(filename, 'r') as input_data:
   try:
         data=yaml.safe_load(input_data)
         subjects=[]
         subjects=list(data.keys())
         print(data[subjects[1]]["contents"])
         print(subjects)
        
   except yaml.YAMLError as exc:
      print(exc)