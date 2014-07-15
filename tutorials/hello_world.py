def hello_world():
    """This is a hello world example function."""
    print('Hello, World!')
    
def find_unique_elements(list_input,sort=True):
    """This method finds the unique elements of a list (or array in PERL), sorts and returns it
    arg list_input:The list from which the unique elements have to be identified. Not optional.
    type list_input:list of integers
    arg sort: Set to true if the unqiue list has to be sorted. False otherwise.
    type sort: Boolean
    rtype:sorted list of unique elements.
    """
    #define the empty list that holds the unique elements
    unique_elements = []
    #Loop through the list
    for element in list_input:
        #If the element is already present in the unique list, then skip. Otherwise add it.
        if element not in unique_elements:
            unique_elements.append(element)
    if sort:
        return sorted(unique_elements)
    else:
        return unique_elements

print "As-is list is", find_unique_elements(list_input = [1,3,12,8,3,4,8,3,], sort = False)
print "Sorted list is", find_unique_elements(list_input = [1,3,12,8,3,4,8,3,], sort = True)