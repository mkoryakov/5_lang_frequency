import argparse
import os
from collections import Counter
from re import findall


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as file_handler:
        return file_handler.read()


def get_most_frequent_words(text, count_print_words=10):
    text = text.lower()
    words_from_text = findall('[a-zа-я]+', text)
    most_frequent_words = Counter(words_from_text).most_common(count_print_words)
    return most_frequent_words


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''Скрипт выводит в консоль 10 самых популярных
        слов из файла, поданного на вход''')
    parser.add_argument('--file_name', '-f', default='lang_frequency.py',
                        help='''Имя файла, в котором необходимо подсчитать
                        количество употреблений каждого слова слова''')
    args = parser.parse_args()
    text = load_data(args.file_name)
    most_frequent_words = get_most_frequent_words(text)
    for word in most_frequent_words:
        print('%s: %d' % (word[0], word[1]))
