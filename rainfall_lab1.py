# This file reads the rainfall.txt and sorts the data acourdinf to rainfall measure
# Then the sorted data in written into a not rainfallfmt.txt file
# The city names are witten in upper case centered in field width 25
# The rainfall data is written in one decimal place 

def main():
    
    record_file = open("rainfall.txt", "r")
    new_file = open("rainfallfmt.txt", "w")
    
    category_51_60 = []
    category_61_70 = []
    category_71_80 = []
    category_81_90 = []
    category_91_100 = []
    all_categories = [category_51_60, category_61_70, category_71_80, category_81_90, category_91_100]
    headings = ["[51-60] ", "[61-70] ", "[71-80] ", "[81-90] ", "[91-100] "]
    
    # read and store lines to all_content
    all_content = []
    for line in record_file:
        all_content.append(line)
    
    # split and format data by line    
    for data in all_content:
        city, rain_measure = data.split()
        #city = ("%25s" % (city).center(25)).upper()
        city = city.center(25,' ').upper()
        rain_measure = float(rain_measure)
        formatted_data = "%s  %5.1f" % (city, rain_measure) 
        
        # decide categories 
        if rain_measure>=51.0 and rain_measure<=60.5:
            category_51_60.append(formatted_data)
        elif rain_measure>=60.6 and rain_measure<=70.5:
            category_61_70.append(formatted_data)
        elif rain_measure>=70.6 and rain_measure<=80.5:
            category_71_80.append(formatted_data)
        elif rain_measure>=80.6 and rain_measure<=90.5:
            category_81_90.append(formatted_data)
        elif rain_measure>=90.6 and rain_measure<=100.5:
            category_91_100.append(formatted_data)
        else:
            print("Error: " + formatted_data)
    
    count = 0
    # sort according to rainfall measure
    for category in all_categories: 
        if len(category)>=2:
            category.sort(key=lambda s: s.split()[1])
       
        new_file.write(headings[count])
        new_file.write("\n")
        count += 1
        for data in category:
            new_file.write(data + "\n")
        new_file.write("\n")
            
    new_file.close()   
    record_file.close()
    print(all_categories) 
main()