import sys  # so that it can take system argumnets
import urllib.request
import bs4 as bs
from PyQt4.QtGui import QApplication  # pyQT4 is an asynchronous library
from PyQt4.QtCore import QUrl  # this is how we can read the url
from PyQt4.QtWebKit import QWebPage
import csv


class Client(QWebPage):

    def __init__(self, url):
        self.app = QApplication(sys.argv)  # finding the application not
        # initialinzing it otherwise it must have anathor self argument
        QWebPage.__init__(self)       # initialinzing the q webpage
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

	def on_page_load(self):
		self.app.quit()  # run until the page loads after loading we are done

url = "https://techolution.app.param.ai/jobs/"
client_response= Client(url)
source = client_response.mainFrame().toHtml()

soup = bs.BeautifulSoup(source, 'lxml')

csv_file=open('techolution.csv', 'w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Category',
'Job Positions', 'Job Type', 'Locations', 'Experience', 'Date Posted'])



for require in soup.find_all('div', class_='ui segments'):
		catg = require.h2.text
		print(catg)



		job_position = require.find_all('h3').text
		print(job_position)



		opening_types = require.find('p').text
		opening_types = opening_types.split('·')

		job_type=opening_types[0].replace('\n','')
		job_type=job_type.strip()

		locations=opening_types[1].replace('\n','')
		locations=locations.strip()

		experience=opening_types[2].replace('\n','')
		experience=experience.strip()
		
		print(job_type)
		print(locations)
		print(experience)



		date_posted=require.find('div',
        class_='four wide right aligned computer tablet only column').text
		print(date_posted)

	
	
	csv_writer.writerow([catg,job_position,job_type,
    locations,experience,date_posted])

csv_file.close()