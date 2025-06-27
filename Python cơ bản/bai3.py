def most_frequent_char(text):
    char_count = {}
    for char in text:
        if char != ' ':  
            char_count[char] = char_count.get(char, 0) + 1
    
    if not char_count: 
        return "Không có ký tự hợp lệ"
    
    max_char = max(char_count, key=char_count.get)
    max_count = char_count[max_char]
    
    return f"Ký tự xuất hiện nhiều nhất là '{max_char}' với {max_count} lần"

test_string = "lap trinh bang ngon ngu python"
print(most_frequent_char(test_string)) 
print(most_frequent_char("hello world"))  
print(most_frequent_char("aaa bbb cc")) 
print(most_frequent_char("")) 