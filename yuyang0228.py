"""
Title: MA676 Python programming mini project
Author: Yuyang Li, Yujia Wang, Yuchen Liu, Biyao Zhang
Date: Feb 28, 2022
"""


### library packages
import numpy as np
import pandas as pd


### function: uniform the format which devide odd lines and even lines
def read_file(file):
    """
    Parameters
    ----------
    def read_file（file : TYPE
            Change the file into two tuples
            Every 2 lines are stored in one tuple.

    Returns
    -------
    first_every_2 : tuple
        Starting from the first line and scan all the odd lines.
    second_every_2 : tuple
        Starting from the second line and scan all the even lines.
    """
    first_every_2 = () # tuple 1
    second_every_2 = () # tuple 2
    line_count = 0
    for line in file:
        stripped_line = line.replace("\n","")
        if line_count%2 == 0:
            first_every_2 += (stripped_line,) # if tuple only has one value we need add one , behind the value like (a,)
        elif line_count%2 == 1:
            second_every_2 += (stripped_line,)
        line_count += 1
    return (first_every_2,second_every_2)
 
    
### read "friends.txt", get "name" and "phone number"
friends_file = open('friends.txt')
(names,phone) = read_file(friends_file)
#print(names)
#print(phone)
 

### read "map_areacodes_states.txt", get "area code" and "place"
map_file = open('map_areacodes_states.txt')
(areacodes,places) = read_file(map_file)

          
### function: replace messy punctuation into " "
def sanitize(some_tuple):
    """
    Parameters
    ----------
    some_tuple : tuple
        Delete some symbols like "-", "(" and space in elements of tuple.

    Returns
    -------
    clean_string : tuple
        A string without the symbols.
    """
    clean_string = () # initialize
    for st in some_tuple:
        st = st.replace(" ","")
        st = st.replace("-","")
        st = st.replace("(","")
        st = st.replace(")","")
        st = st.replace(" ","")
        clean_string += (st,)
    return clean_string


### clean "phone number"into uniform format
clean_phone = sanitize(phone)
#print(clean_phone)
friends_file.close()  # store the changes of file


### function: match "phone number" and "area code"
def get_area_code():
    area_code = ()
    for pf in clean_phone:
        area_code += (pf[0:3],)
    return area_code

area_code = get_area_code()
#print(area_code)


### function: match "area code" and "name:
#print(pd.DataFrame({'names':names,'area_code':area_code}))
def analyze_friends():
    left_df = pd.DataFrame({'names':names,'area_code':area_code})
    right_df = pd.DataFrame({'areacodes':areacodes,'places':places})
    #print(left_df)
    return left_df.merge(right_df , left_on = 'area_code',right_on='areacodes',
                  how = 'left')

analyze = analyze_friends()


### print the result
print(analyze.iloc[:,[0,1,3]])
print("Your friends live in",len(analyze.places.unique()),"different states")
#print(analyze.names,analyze.places)
    

