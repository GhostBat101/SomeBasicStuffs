def search_string_in_file(file_name, string_to_search):
    line_number = 0
    list_of_results = []
    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            line_number += 1
            if string_to_search in line:
                list_of_results.append((line_number, line.rstrip()))
                return list_of_results
            else:
                strout = "Not found."
                return strout

location = 'lookingfor_a_line.py'
line = input("what do you want to search in this program? Type it here: ", )
try:
    print(search_string_in_file(location, line))
except:
    print("Something went wrong. Plz input the line you want to search")