def bubble(x, Reversed=False):
    for j in range(len(x)):
        for i in range(len(x)):
            try:
                if not Reversed:
                    if (x[i] <= x[i+1]): #if val1 is smaller than val 2
                        pass
                    else:
                        temp = x[i+1]
                        x[i+1] = x[i] #swaps the values
                        x[i] = temp
                else: #the non reversed section, see original
                    if (x[i] >= x[i+1]):
                        pass    
                    else:
                        temp = x[i]
                        x[i] = x[i+1]
                        x[i+1] = temp
            except:
                pass
    return x

def insertSort(x, Reversed = False):
    for i in range(1, len(x)):
        y = x[i] #temporary value
        j = i-1  #iterator i+1
        while y < x[j] and j>=0:
            x[j+1] = x[j] #inserts the item
            j-=1
        x[j+1] = y #temp allocation

    if Reversed:
        new = [] 
        for i in range(len(x), 0, -1):
            try:
                new.append(x[i-1]) #reverses the list
            except:
                pass
        x = new
    return x

def partition(x,low,high):
    i = (low - 1)
    pivot = x[high] #gettting the pivot (last item of the list)
    for j in range(low, high): 
        if x[j] <= pivot: #moving items smalelr than the pivot to before the pivot
            i = i + 1
            x[i], x[j] =  x[j], x[i] #swapping values
    x[i+1],x[high] = x[high],x[i+1] 
    return (i+1)

def quickSort(x, low, high):
    if low < high:
        y = partition(x,low,high)
        quickSort(x, low, y - 1)
        quickSort(x, y + 1, high) #sorting the two partitions

def binSearch(x, target):
    pointer = len(x) // 2 #midway point
    loops = 2 #i just couldnt think of another way to do it
    while True:
        if x[pointer] == target: #if the index is correct
            return pointer
        elif x[pointer] > target: #if its in the left half
            pointer -= pointer // loops
        elif x[pointer] < target: #if its in the right half
            pointer += pointer // loops
        else:
            return -1 #if its not in the list
        if pointer > len(x) -1: #had an error where it was pointing to the 17th value (index 16)
            pointer = len(x) -1
        loops +=2

def linSearch(x, target):
    i = 0
    while x[i] != target: #runs through each item
        i+=1
    return i

        
