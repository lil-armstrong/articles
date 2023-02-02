from sublime import Region
import sublime_plugin

class
CloseTagCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		# Get the cursor position
		cursor_pos = self.view.sel()[0].begin()

		# Get the current line
		region = Region(0, self.view.size())
		region_text = self.view.substr(region)

		# Check if the line ends with an open HTML Tag
		if "</" in region_text:
			return

		# Find the start and end position of the open HTML tag
		tag_start = region_text.rfind("<", 0, cursor_pos)
		tag_end = region_text.find(">", tag_start)

		# Extract the tag name
		tag_name = region_text[tag_start + 1:tag_end]

		# Check if the open tag is a self closing tag
		if tag_name[-1] == "/":
			return

		# Find the position of the closing tag
		close_tag_pos = region_text.find("</" + tag_name + ">", tag_end)

		# Count the number of open and close tags
		open_tags = region_text.count("<" + tag_name + ">")
		close_tags = region_text.count("</" + tag_name + ">")

		# initialize a dictionary to store the number of open and close tags for each tag name
		tag_counts = {}

		# iterate thru the open tags in the document
		start_pos = 0
		while True:
			start_pos = region_text.find("<", start_pos)
			if start_pos == -1:
				break
			end_pos = region_text.find(">", start_pos)
			tag = region_text[start_pos, 1:end_pos]

			if " " in tag:
				tag = tag[:tag.find(" ")]
			if tag not in tag_counts:
				tag_counts[tag] = [1, 0]
			else:
				tag_counts[tag][0] += 1
			start_pos = end_pos

		# Iterate thru the close tags in the document
		start_pos = 0
		while True:
			start_pos = region_text.find("</", start_pos)
			if start_pos == -1:
				break
			end_pos = region_text.find(">", start_pos)
			tag = region_text[start_pos, 2:end_pos]

			if tag not in tag_counts:
				tag_counts[tag] = [0, 1]
			else:
				tag_counts[tag][1] += 1
			start_pos = end_pos


		# Check if the closing tag already exists
		if tag_counts[tag_name][0] > tag_counts[tag_name][1]:
			# insert the closing tag
			self.view.insert(edit, cursor_pos, "</" + tag_name + ">")

