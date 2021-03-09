## import of needed values
# import matplotlib.pyplot as plt
# import pandas as pd

## Open file to get mean service time
with openfile("data/Service_times_good.txt") as file:
    data = file.read()
    values = []
    for value in data:
        values.append(value)
    
    ## calculate mean time
    mean = sum(values)/len(values)
    print(mean)