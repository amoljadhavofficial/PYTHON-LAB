while True:
    print("\n--- STRING MANIPULATION MENU ---")
    print("1. Count vowels, consonants, digits, special characters")
    print("2. Check palindrome")
    print("3. Character frequency")
    print("4. Convert lowercase to uppercase and vice versa")
    print("5. Remove spaces")
    print("6. Count number of words")
    print("7. Check if string contains only digits")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 8:
        print("Program Terminated")
        break

    s = input("Enter a string: ")

    # 1. Count vowels, consonants, digits, special characters
    if choice == 1:
        v = c = d = sp = 0
        for ch in s:
            if ch.isalpha():
                if ch.lower() in 'aeiou':
                    v += 1
                else:
                    c += 1
            elif ch.isdigit():
                d += 1
            else:
                sp += 1

        print("Vowels:", v)
        print("Consonants:", c)
        print("Digits:", d)
        print("Special Characters:", sp)

    # 2. Palindrome check
    elif choice == 2:
        rev = ""
        for ch in s:
            rev = ch + rev

        if s == rev:
            print("Palindrome String")
        else:
            print("Not a Palindrome")

    # 3. Character frequency
    elif choice == 3:
        temp = s
        for ch in temp:
            if temp.count(ch) > 0:
                print(ch, ":", temp.count(ch))
                temp = temp.replace(ch, "")

    # 4. Convert lowercase to uppercase and vice versa
    elif choice == 4:
        result = ""
        for ch in s:
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            elif 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch
        print("Converted String:", result)

    # 5. Remove spaces
    elif choice == 5:
        result = ""
        for ch in s:
            if ch != ' ':
                result += ch
        print("String without spaces:", result)

    # 6. Count words
    elif choice == 6:
        count = 1
        for ch in s:
            if ch == ' ':
                count += 1
        print("Number of words:", count)

    # 7. Check if only digits
    elif choice == 7:
        flag = True
        for ch in s:
            if ch < '0' or ch > '9':
                flag = False
                break

        if flag:
            print("String contains only digits")
        else:
            print("String contains non-digit characters")

    else:
        print("Invalid choice")
