# -*- coding: utf-8 -*-
"""DocxtoTxt.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BY3-pFnLqbD-VErewGQp9g8EBzM8-Km1

Docx To Text Using Python
"""

##Install the Library First
#pip install docx2txt

Doc_List = ["Doc1.docx","Doc2.docx"]

import docx2txt

for Doc in Doc_List:
  # replace following line with location of your .docx file
  MY_TEXT = docx2txt.process(Doc)
  with open("Output.txt", "a") as text_file:
      print(MY_TEXT, file=text_file)