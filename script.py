with open('Workbook4.csv', 'rb') as ifile:
	data_rows = ifile.read().splitlines()


with open('final_nig_3.csv', 'wb') as finalfile:
	finalfile.write('name, title, department, university, email, poc, my_name, url, category, country\n')
	for index, items in enumerate(data_rows):
		while index%3 ==0:
			finalfile.write("{0}, {1}, Art and Sciences, American University Nigeria, {2}, none , Sonia , {3}, University, Nigeria\n".format( data_rows[index], data_rows[index+1], data_rows[index+2],"None", "http://www.americanuniversitynigeria.org/about/administration/faculty/27-school-of-arts-and-sciences?start=40"));
			index+=1
		while index == 0:
			finalfile.write("{0}, {1}, Art and Sciences, American University Nigeria, {2}, none , Sonia , {3}, University, Nigeria\n".format( data_rows[index], data_rows[index+1], data_rows[index+2],"None", "http://www.americanuniversitynigeria.org/about/administration/faculty/27-school-of-arts-and-sciences?start=40"));
			index+=1 
		else:
			pass
	
	
