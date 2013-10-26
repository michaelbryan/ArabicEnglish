import sys
from openpyxl.reader.excel import load_workbook
import unicodedata
import codecs

def WriteDataToFile(file_name, mylist):
	file_handler = open(file_name, 'w')
	for crap in mylist:
		print "crap:", crap
		try:
			file_handler.write(crap)
		except UnicodeEncodeError:
			file_handler.write(crap.encode('utf8'))

		file_handler.write("\n")
	#file_handler.write("\n".join(list))
	file_handler.close()

def GetData(input_file, begin_range, end_range):
	data = []
	
	workbook = load_workbook(input_file)
	worksheet_names = workbook.get_sheet_names()
	
	worksheet1 = workbook.get_sheet_by_name(worksheet_names[0])
	for index, row in enumerate(worksheet1.range(begin_range + ":" + end_range)):
		data.append([])
		for cell in row:
			data[index].append(cell.value)
	
	#print "data: %s" % data
	return data

def main():
	if(len(sys.argv) != 5):
		print "**************************************************"
		print "Usage  : python %s [excel (.xlsx) input file] [top left cell] [bottom right cell] [text (.txt) output file]" % sys.argv[0]
		print "Example: python %s 0_RecordLinkageInput100Lines.xlsx A1 T101 2_100Lines.txt" % sys.argv[0]
		print "**************************************************"
		return
	
	excel_input_file = sys.argv[1]
	excel_top_left_cell = sys.argv[2]
	excel_bottom_right_cell = sys.argv[3]
	text_output_file = sys.argv[4]
	
	data = GetData(excel_input_file, excel_top_left_cell, excel_bottom_right_cell)
	
	output_txt_list = []
	output_html_list = []
	
	output_html_list.append("<table border=\"4\">\n")
	
	for row_index, row in enumerate(data):
		output_html_list.append("<tr>")
		
		cell_details = []
		for cell_index, cell in enumerate(row):
			print "cell:", cell
			# cell could be unicode ... UnicodeEncodeError:
			if cell is None:
				cell = ""
			elif isinstance(cell, (int, long, float, complex)):
				cell = str(cell)
			else:
				try:
					cell.decode('ascii')
					cell = str(cell)
				except UnicodeEncodeError:
					#import pdb; pdb.set_trace()
					print "it was not a ascii-encoded unicode string"
					#cell = str(cell.encode('utf16'))

			output_html_list.append("<td>")
			output_html_list.append(cell)
			output_html_list.append("</td>")
			cell_details.append(cell)
		output_txt_list.append("|".join(cell_details))
		output_html_list.append("</tr>")
	
	output_html_list.append("</table>")
	
	WriteDataToFile(text_output_file, output_txt_list)
	WriteDataToFile("output.html", output_html_list)

if __name__ == "__main__":
	main()
	