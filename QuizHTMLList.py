items = ['first string', 'second string']
html_str = "<ul>\n"	# "\ n" is the character that marks the end of the line, it does
              		# the characters that are after it in html_str are on the next line
for string in items:
    html_str += "<li>" + string + "</li>\n"
html_str += "</ul>"
# write your code here


print(html_str)
