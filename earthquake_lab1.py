# This program reads the earthquake.txt 
# and prints sorted date/magnitudes 
# according to the region

def main():
    
    earthquake_file = open("earthquake.txt", "r")  
    all_regions = []
    
    # read and store lines to all_content
    all_content = []
    for line in earthquake_file:
        all_content.append(line)
    
    # get date, magnitude, and place of each entry 
    for entry in all_content:
        magnitude, date, other_info = entry.split(" ", 2)
        place = entry.split().pop()
        # add data to all_regions
        # check if place already exist
        place_exist = False
        place_exist = add_region(all_regions, place, date, magnitude, place_exist)      
        if place_exist == False or place_exist == None:
            all_regions.append([place])
            add_region(all_regions, place, date, magnitude, place_exist)
    
    # print out all data by list  
    for data in all_regions:
        print(data)
    earthquake_file.close()
 
'''  
    # Optional code to print the lists of lists
    # without quotation marks on individual items
    # BUT this part will convert lists into strings
    strings_list = []
    for region_entry in all_regions:
        new_string = "["    # Note: every change to new_string returns a NEW new_string
        for item in region_entry:
            new_string += str(item) + ", "
        new_string = new_string[:-2]    # Remove ", " from end
        new_string += "]"
        new_string = new_string.replace("'", "")
        print(new_string)
'''

def add_region(all_regions, place, date, magnitude, place_exist):
# decides if place(list) exist in all_regions
# add date, magnitude and return if it does
    for region in all_regions:
        if place in region:
            region.append([date, magnitude]) 
            place_exist = True
            return place_exist
        
main()

