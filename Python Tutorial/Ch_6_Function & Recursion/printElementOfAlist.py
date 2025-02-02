#WAF to print the element of a list in a single line.(list is the parameter)

cities = ["delhi","gurgaon","noida","pune","mumbai","chennai"]
heroes = ["thor","ironman","captain america","shaktiman"]

def  print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

print_list(heroes)