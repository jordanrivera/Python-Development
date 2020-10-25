file = open('csv_data.txt', 'r')
lines = file.readlines()
file.close()

lines = [line.strip() for line in lines[1:]]
