import os
import time
import subprocess
import matplotlib.pyplot as plt

data_dir = "data"
files = [f for f in os.listdir(data_dir) if f.startswith("example") and f.endswith(".in") and f != "example1.in"]

results = []
for file in files:
    filepath = os.path.join(data_dir, file)
    
    try:
        with open(filepath, 'r') as f:
            lines = f.read().strip().split('\n')
            if len(lines) < 2: continue
            n = len(lines[-1].strip())
    except Exception as e:
        print(f"Error reading {file}: {e}")
        continue
    
    start_time = time.perf_counter()
    try:
        with open(filepath, 'r') as f:
            subprocess.run(["python3", "src/main.py"], stdin=f, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception as e:
        print(f"Error running {file}: {e}")
        continue
    end_time = time.perf_counter()
    
    runtime = end_time - start_time
    results.append((n, runtime, file))
    print(f"File: {file} | Length: {n} | Runtime: {runtime:.4f} seconds")


results.sort(key=lambda x: x[0])

lengths = [r[0] for r in results]
times = [r[1] for r in results]


plt.figure(figsize=(10, 6))
plt.plot(lengths, times, marker='o', linestyle='-', color='b')


for (n, t, file) in results:
    plt.annotate(file.replace('.in', ''), (n, t), textcoords="offset points", xytext=(0,10), ha='center', fontsize=8)

plt.title('Sequence Length vs. Runtime for HVLCS Algorithm')
plt.xlabel('Length of Input String')
plt.ylabel('Runtime (seconds)')
plt.grid(True)
plt.tight_layout()

output_file = 'runtime_graph.png'
plt.savefig(output_file)
print(f"\nSuccess! Graph saved to {output_file}")
