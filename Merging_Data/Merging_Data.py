import csv

dataset1 = []
dataset2 = []

with open("bright_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset1.append(row)

with open("dwarf_stars.csv", "r") as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        dataset2.append(row)

header_1 = dataset1[0]
stars_data1 = dataset1[1:]

header_2 = dataset2[0]
stars_data2 = dataset2[1:]

print(header_1, header_2)

header = header_1+header_2

stars_data = []

for index, data_row in enumerate(stars_data1):
    stars_data.append(stars_data1[index]+stars_data2[index])

with open("merged_dataset.csv", "a+") as f:
    csv_writer = csv.writer(f)
    csv_writer.writerow(header)
    csv_writer.writerows(stars_data)

    