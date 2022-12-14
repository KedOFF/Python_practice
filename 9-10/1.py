mac = ["aabb:cc80:7000", "aabb:dd80:7340", "aabb:ee80:7000", "aabb:ff80:7000"]
result = []
for line in mac:
    words = line.split(':')
    line2 = words[0] + '.' + words[1] + '.' + words[2]
    result.append(line2)
print (result)