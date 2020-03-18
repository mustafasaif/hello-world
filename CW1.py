import matplotlib.pyplot as plt

m_path_1=[]
m_path_2=[]

def convert(val):
    if val.endswith('Kb'):
        return float(val[:-2])/1000
    elif val.endswith('Mb'):
        return float(val[:-2])
    elif val.endswith('b'):
        return float(val[:-1])/1000000
    else:
        return 0

with open("network_analysis_data.txt", "r") as file:
    count=0
    for line in file:
        count+= 1
         count%2== 0:
            line1=line.split()[8]
            m_path_2.append(convert(line1))
        else:
            line2=line.split()[8]
            m_path_1.append(convert(line2))
plt.fiure(1)
plt.xlabel('Data Row')
plt.ylabel('Data Rate[Mb/s]')
plt.plot(m_path_1,'blue', label='Path 1')
plt.plot(m_path_2,'red', label='Path 2')
plt.title('Path 1&2')
plt.legend()
plt.grid()

plt.figure(2)
plt.plot(m_path_1,'blue', label='Path 1')
plt.xlabel('Data Row')
plt.ylabel('Data Rate[Mb/s]')
plt.title('Path 1')
plt.grid()
plt.legend()

plt.figure(3)
plt.plot(m_path_2,'red', label='Path 2')
plt.xlabel('Data Row')
plt.ylabel('Data Rate[Mb/s]')
plt.title('Path 2')
plt.legend()
plt.grid()
plt.show()
