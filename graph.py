import matplotlib.pyplot as plt
import numpy as np

f = open('results-trans.csv', 'r')
comp = "/"
first = False
temp = ""
current_size = 0
line_num = 0
ops_per_s = []
rel = []
ops = []
num_threads = []
lock_taken = []
list_size = []
percent_lock_taken = []
for index in range(0, 7):
	new_opsps = []
	new_ops = []
	new_rel = []
	new_list = []
	new_threads = []
	new_lock_taken = []
	new_percent_lock_taken = []
	ops_per_s.append(new_opsps)
	ops.append(new_ops)
	num_threads.append(new_threads)
	list_size.append(new_list)
	rel.append(new_rel)
	lock_taken.append(new_lock_taken)
	percent_lock_taken.append(new_percent_lock_taken)

for line in f:
	slashes = 0
	for c in line:
		if c == "/" or c == "\n":
			if slashes == 0:
				list_size[current_size].append(temp)
			elif slashes == 1:
				num_threads[current_size].append(temp)
			elif slashes == 2:
				rel[current_size].append(temp)
			elif slashes == 3:
				ops[current_size].append(temp)
			elif slashes == 4:
				ops_per_s[current_size].append(temp)
			elif slashes == 5:
				lock_taken[current_size].append(temp)
			elif slashes == 6:
				percent_lock_taken[current_size].append(temp)
			slashes = slashes + 1
			temp = ""
		else:
			temp = temp + c

	line_num = line_num + 1
	if line_num == 6:
		current_size = current_size + 1
		line_num = 0

print current_size
f.close()
for i in range(0, current_size):
	t = num_threads[i]
	s = ops_per_s[i]
	plt.plot(t, s)
	plt.xlabel('Number of Threads')
	plt.ylabel('Operations Per Second')
	plt.title('Restricted Transactional Memory and a List size of ' + list_size[i][0])
	plt.grid(True)
	plt.savefig(list_size[i][0] + ".png")
	plt.show()

#Tree Size/nt/rt/ops/ops-per-s/Lock Taken/%Lock Taken