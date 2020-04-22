from scihub import SciHub
import csv
import time

sh = SciHub()

base_folder = "../../"
path_folder = base_folder + "Magazine Papers/"
with open(base_folder + "paper_dataset.csv") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count > 2:
			title = row[1]
			url = row[2]
			print(title)
			# print(url)
			result = sh.download(url, path = path_folder + title + '.pdf')
			time.sleep(2)
		line_count = line_count + 1