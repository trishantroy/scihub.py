from scihub import SciHub
import csv
import time

sh = SciHub()

with open("../../paper_dataset.csv") as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	line_count = 0
	for row in csv_reader:
		if line_count > 2:
			title = row[1]
			url = row[2]
			print(title)
			# print(url)
			# result = sh.download(url, path='../../Magazine Papers/'+title+'.pdf')
			time.sleep(2)
		line_count = line_count + 1


# exactly the same thing as fetch except downloads the articles to disk
# if no path given, a unique name will be used as the file name
