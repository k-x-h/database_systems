import csv


results = []
with open("instructor.txt") as csvfile:
    reader = csv.reader(csvfile) 
    for row in reader: # each row becomes a list within the "results" list
        results.append(row)
        
        
        
user_id=1002 #placeholder user input for instructor id

id_list=[] #creating a list that will contain all of the id's




for i in range(len(results)):
    id_list.append(int(results[i][0])) #appends all values from the 0th position in each list (instructor id) to id_list
    
if user_id not in id_list: #checking to see if the user_id does not exist in the id_list list
    print("not in")
    

#writing results list to a csv text file, could potentially be turned into a function and done at the end of each step in the menu to ensure edits are saved
with open ("csv_results.txt", "w", newline="") as f:
    write = csv.writer(f)
    write.writerows(results)