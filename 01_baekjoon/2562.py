input_array = []
for _ in range(9):
    input_array.append(int(input()))

max_ = max(input_array)
index_ = input_array.index(max_) +1

print(max_)
print(index_)
     