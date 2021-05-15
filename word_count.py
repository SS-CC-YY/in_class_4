import collections

def word_count(in_put):
    s_list = in_put.split(' ')
    [s_list.remove(item) for item in s_list if item in ",."]
    count = collections.Counter(s_list)
    return len(count.keys())

def main():
    sentence = input("Enter a sentence: ")
    count = word_count(sentence)
    print("The numer of words: ", count)

if __name__ == "__main__":
    main()