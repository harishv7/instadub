with open('lang.txt') as f:
    lines = f.readlines()

write_file = open('myfile.txt', 'w')

for lang in lines:
    lang = lang.replace("\n", "")
    str_w = "<li><a href=\"#\">" + lang + "</a></li>\n"
    str_w = "<option>" + lang + "</option>\n"
    print(str_w)
    write_file.write(str_w)
    write_file.write("")
    
