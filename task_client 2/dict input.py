

## #Sample dictionary
##my_dict = {
##    "key1": "This is the value containing apple.",
##    "key2": "Another value with banana.",
##    "key3": "A value that doesn't have the input."
##}
##
## #Taking user input
##user_input = input("Enter a search term: ")
##
## Loop through dictionary items
##user=False
##for key, value in my_dict.items():
##    #print(value)
##    if user_input in value:
##          print(f"Key: {key}\nValue: {value}\n")
##          user_input=True
##    else:
##        print(user+user_input)
##      
##    if re.search(user_input, value):
##        print(f"Key: {key}\nValue: {value}\n")


##
### Sample string
##my_string = "This is a sample string containing the word apple."
##
### User input
##user_input = input("Enter a word to search: ")
##
##if user_input in my_string:
##    print(f"The word '{user_input}' was found in the string.")
##else:
##    print(f"The word '{user_input}' was not found in the string.")


data_collection = [
    {"language": "python", "id": "1000", "name": "vijay"},
    {"language": "python", "id": "1001", "name": "mani"},
    {"language": "sql", "id": "1002", "name": "jagadesh"},
    {"language": "java,python,sql", "id": "1003", "name": "jagadesh"},
    {"language": "java", "id": "1004", "name": "vicky"}
]

user_input = input("Enter a language: ")

found_names = [entry["name"] for entry in data_collection if user_input in entry["language"]]

if found_names:
    print("Names found for the given language:")
    for name in found_names:
        print(name)
else:
    print("No names found for the given language.")









