import re
import pyperclip
from pymystem3 import Mystem


from bad_words.bad_words_file import bad_words_from_file

from keyworder.remove_doubles import no_doubles
from keyworder.write_keywords import write_keywords
from notific import notification
from check_file_exist import create_file_if_no


keyword_file = create_file_if_no('keywords','keywords in work.txt')
bad_word_file = create_file_if_no('keywords','bad_words.txt')


# def bad_words_from_file(bad_word_file):  # извлекаю слова исключения из текстового файла
#     with open(bad_word_file, 'r') as text_file:
#         lines = text_file.readlines()
#     bad_words = ''
#     for i in lines:
#         bad_words += '|' + i.strip()
#     return f"\\b({bad_words.lstrip('|')})\\b"


# def write_keywords(keyword_file, final):
#     with open(keyword_file, 'a') as text_file:
#         text_file.write('\n')
#         text_file.write(datetime.now().strftime("%Y-%m-%d") + '\n')
#         text_file.write(final)


def words_optimization():
    durty_words = pyperclip.paste().lower()
    bad_words = bad_words_from_file(bad_word_file)
    optimization = re.findall(r'\w{3,}', durty_words)  # оставляю только слова длиннее трех букв
    optimization = (' '.join(optimization))
    lemmatized_words = "".join(Mystem().lemmatize(optimization))
    no_bad_words = re.sub(bad_words, '', lemmatized_words)  # удаляю слова паразиты
    final = no_doubles(no_bad_words)    #str
    write_keywords(final,keyword_file)
    pyperclip.copy(final)
    notification(final, 'Обработаны ключевые слова:')
    return final


if __name__ == '__main__':
    words_optimization()
    # write_keywords("")
    # assert words_optimization() is not None
    # assert type(words_optimization()) == str

