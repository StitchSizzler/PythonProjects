"""
This program reads input_lab8.txt and processes
the marks (ave, min, max, histogram) into an html page
"""

import webbrowser

def main():
    input_file = open("input_lab8.txt", "r")
    html_file = open("marks_lab8.htm", "w")
    all_marks = []
    
    # read every line and add marks to list all_marks
    for line in input_file:
        student_id, marks = line.split(" ")
        all_marks.append(int(marks))
    
    # calculate average, min and max
    total_marks = 0
    total_students = len(all_marks)
    minimum = 100
    maximum = 0  
    bins = [0,0,0,0,0,0,0,0,0,0] # will hold frequency of marks for each interval 
    # e.g bin[3] will hold freq of marks from 30-39
    for mark in all_marks:
        # calculate min and max
        if mark >= maximum:
            maximum = mark
        if mark <= minimum:
            minimum = mark
        # sum for average
        total_marks += mark
        # enter value to bin
        if len(str(mark)) ==2:
            interval = str(mark)[0]
        else:
            interval = 0            
        bins[int(interval)] += 1    # update frequency at bin
    average = total_marks/total_students
    
    # write ave, min, max to html file
    html_file.write("<html> \n"    # header html tag
                    "\t<body> \n"    # header body tag
                    "\t\t<h1>Welcome to statistics page!</h1> \n"   # heading
                    "\t\t<br /> \n"  # add blank line
                    "\t\t<p>Average is: %0.4f \n" 
                    "\t\t<br />Minimum is: %d \n" 
                    "\t\t<br />Maximum is: %d </p> \n" % (average, minimum, maximum))
                    
                    # make the histogram
    html_file.write("\t\t<table> \n"   # start table
                    "\t\t\t<tr> \n")    # start row
                    # make bins(columns/bars) inside row using loop
    for frequency in bins:                
        html_file.write("\t\t\t\t<td valign='bottom'> \n"   # make column
                        "\t\t\t\t\t<div style='width:30px;height:%dpx;background:blue;border:1px solid red;'></div> \n"    # set divident style 
                        "\t\t\t\t</td> \n" %(frequency*20))   # end column tag
    html_file.write("\t\t\t<tr> \n")    # start row 
    for i in range(len(bins)):
        if i == 0:
            interval = "[0-9]&nbsp&nbsp&nbsp&nbsp"
        else:
            interval = "[%d0-%d9]" % (i, i)
        html_file.write("\t\t\t\t<td>%s</ts> \n" %(interval))    # write bin interval
                        
    html_file.write("\t\t\t</tr> \n"      # end row tag
                    "\t\t</table> \n"   # end table tag                    
                    "\t</body> \n"   # close body tag
                    "</html> \n" ) # close html tag  
    
    input_file.close()
    html_file.close()
    webbrowser.open("file:///C:/Users/eahme/Documents/CMPUT_175/Python/marks_lab8.htm")   # open html link

main()