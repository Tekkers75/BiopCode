import matplotlib.pyplot as plt

def rz_encoding(data):
    encoded_data = []

    consecutive_ones = 0  

    for bit in data:
        if bit == 0:
            
            encoded_data.append(0)  
            
        else:
            if consecutive_ones % 2 == 0:
                encoded_data.append(1)  
            else:
                encoded_data.append(-1)  

            
            consecutive_ones += 1  

    return encoded_data

data = [0,1,1,0,1,0,0,0, 0,1,1,0,0,1,0,1, 0,1,1,0,1,1,0,0, 0,1,1,0,1,1,0,0, 0,1,1,0,1,1,1,1, 0,0,1,0,0,0,0,0, 0,1,1,1,0,1,1,1, 0,1,1,0,1,1,1,1, 0,1,1,1,0,0,1,0, 0,1,1,0,1,1,0,0, 0,1,1,0,0,1,0,0]
encoded_data = rz_encoding(data)


for item in encoded_data:
    print(item, end=" ")
print()


import matplotlib.pyplot as plt
def plot_dependency_graph(data):

    plt.plot(range(1, len(data) + 1), data, marker='o')


    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('RZ Encoding')


    plt.show()

plot_dependency_graph(encoded_data)
