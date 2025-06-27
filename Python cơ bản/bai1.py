def format_sentence(text):
    words = text.split()
    if words:
        words[0] = words[0].capitalize()
    
    for i in range(1, len(words)):
        words[i] = words[i].lower()
    
    return ' '.join(words)

test_string = "nGuYen vAN a"
result = format_sentence(test_string)
print(result)
print(format_sentence("tRAN tHI b"))
print(format_sentence("lE vAN cUONG"))