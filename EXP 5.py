# Experiment Execution Code

text = "  Python is Very Powerful for Data Science!!!  "

print("The Original Text:", text)
print("-" * 70)

# 1. strip() - removes extra spaces
clean_text = text.strip()
print("The text after strip():", clean_text)
print("The Number of characters:", len(clean_text))
print("-" * 70)

# 2. lower() - convert to lowercase
lower_text = clean_text.lower()
print("The text after lower():", lower_text)
print("-" * 70)

# 3. upper() - convert to uppercase
upper_text = clean_text.upper()
print("The text after upper():", upper_text)
print("-" * 70)

# 4. replace() - remove special characters
replaced_text = clean_text.replace("!!!", "")
print("The text after replace():", replaced_text)
print("-" * 70)

# 5. split() - split sentence into words
words = replaced_text.split()
print("The text after the split():", words)
print("-" * 70)

# 6. len() - count number of characters
print("The number of characters:", len(replaced_text))
print("-" * 70)

# 7. count() - count the occurrence of a word
print("Count of word data:", clean_text.count("Python"))
print("-" * 70)

# 8. find() - find the position of a word
print("The position of word 'Python':", replaced_text.find("Python"))
print("-" * 70)

# 9. startswith() - check sentence start
print("Starts with 'Python':", clean_text.startswith("Python"))
print("-" * 70)

# 10. endswith() - check sentence end
print("Ends with 'Science':", replaced_text.endswith("Science"))
print("-" * 70)

# 11. isalpha() - check alphabet data
sample_word = "datascience"
print("Is 'datascience':", sample_word.isalpha())

# 12. isdigit() - check numeric data
sample_numeric = "2026"
print("Is '2026':", sample_numeric.isdigit())

print("\nString (Text) processing completed successfully!")
