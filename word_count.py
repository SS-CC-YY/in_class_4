import collections

def word_count(in_put):
    s_list = in_put.split(' ')
    [s_list.remove(item) for item in s_list if item in ',.']
    count = collections.Counter(s_list)
    return count

def main():
    sentence = input("Enter a sentence: ")
    count = word_count(sentence)
    print("The numer of words: ", len(count.keys()))

if __name__ == "__main__":
    main()