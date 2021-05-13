def check_pal(in_put):
    sentence = list(in_put)
    sentence.reverse()
    if list(in_put) == sentence:
        return True
    else:
        return False

def main():
    sentence = input("Please enter the sentence that you want check: ")
    if check_pal(sentence):
        print("%s is palindrome" % sentence)
    else:
        print("%s is not palindrome" % sentence)

if __name__ == '__main__':
    main()