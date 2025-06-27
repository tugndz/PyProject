def reverse_words(text):
    words = text.split()
    words = words[::-1]
    return ' '.join(words)

test_string = "lap trinh bang ngon ngu python"
result = reverse_words(test_string)
print(result)

print(reverse_words("hello world")) 
print(reverse_words("python la ngon ngu tuyet voi")) 