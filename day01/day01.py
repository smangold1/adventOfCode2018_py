from typing import List;
import os;
import time;

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

while repeat_frequency is None:
    for line in lines:
        g.calibrate(line)
        if g.currentFrequency in seen_frequencies:
            repeat_frequency = g.currentFrequency
            break
        print(f"added {g.currentFrequency} at {len(seen_frequencies)}")
        seen_frequencies.add(g.currentFrequency)

print(f"first repeated result: {repeat_frequency}")
