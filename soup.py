#import libraries
from bs4 import BeautifulSoup
from urllib2 import urlopen

#This range relates to the url. Each page has 10 results and there is a total of over 4828 contacts, so it will stop at result page 4830
count = range(0, 4830, 10)

#This is the url that has all the data. Where it says counter is the result the page starts on
url="http://www.unilag.edu.ng/staffdirectory.php?page=about_staffdirectory&param=a&paramcat=staff&counter={0}&move=front"

#This text begins the writing the file process
with open('final_lagos3.txt', 'wb') as ifile:
	#For loop that goes through counters so page starting with result 0, 10, 20, etc
	for x in count:
		#opens and reads html page
		html = urlopen(url.format(x))
		soup = BeautifulSoup(html)
		#specifically gets each table with the class "tbl_right_left_bottom_top2"
		tables = soup.find_all('table', {"class": "tbl_right_left_bottom_top2"})
		#final list that will be a list of each staff member with their contact information
		final_list = []
		#Will go through each table and take out text and clean up spaces, extra commas, and other weird characters. Then these results are split into a list.
		# Since each option ends with a View Full Profile and Publications, I use this as a breaker for the lsit
		for items in tables:
			item=items.get_text().replace(u'\xa0','').replace(',','').replace('\n', ' ').replace(u'\x95', '').split('View Full Profile and Publications.')
			final_list.extend(item)

		#write into the file
		for items in final_list:
			ifile.write('{0}\n'.format(items));
			
		print x
