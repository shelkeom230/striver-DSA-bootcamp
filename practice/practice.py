# default args 
def append_items(item,my_list=[]):
    my_list.append(item)
    return my_list 

if __name__=="__main__":
    print(append_items(10))
    