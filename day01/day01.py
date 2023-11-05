from typing import List;
import os;
import time;
import matplotlib.pyplot as plt
import numpy as np

def read_input(file_name):
    current_path = os.path.dirname(__file__)
    lines : List[int] = []
    try:
        with open(os.path.join(current_path, file_name), 'r') as file:
            for line in file:
                lines.append(int(line.strip()))  
    except Exception as e:
        print(f"An error occurred: {e}")
    return lines


class Frequency:
    def __init__(self):
        self.currentFrequency = 0

    def calibrate(self, num):
        self.currentFrequency += num;


# put your inputs file next to this file!
lines = read_input('input.txt');
# solve the problem here!
f = Frequency();
g = Frequency();

for line in lines:
    f.calibrate(line)
print(f.currentFrequency); 


seen_frequencies = set()
repeat_frequency = None
times = []
start_time = time.time()
i = 0 


while repeat_frequency is None:
    for line in lines:
        i += 1
        g.calibrate(line)

        ret_val = g.currentFrequency in seen_frequencies
        if i % 100 == 0:
            times.append((time.time() - start_time) * 1_000_000)
            start_time = time.time() 

        if ret_val:
            repeat_frequency = g.currentFrequency
            break
        #print(f"added {g.currentFrequency} at {len(seen_frequencies)}")
        seen_frequencies.add(g.currentFrequency)

print(f"first repeated result: {repeat_frequency}")


y = times
x = np.linspace(1, len(times),len(times))

plt.plot(x, y, label='Data Points', color='blue', linestyle='--')
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Sample Plot')
plt.legend()

plt.savefig('plot.png', dpi=300, bbox_inches='tight')

plt.show()

