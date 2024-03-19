#import Translator from googletrans module
from googletrans import Translator
try:
    with open('test.txt', 'r', encoding='utf-8') as my_file:
        translate_content =my_file.read()

    translator = Translator()
    translated_text = translator.translate(translate_content,src ='en',dest='ja')
    print(translated_text.text)

    try:
        with open('translatedtest.txt', 'w', encoding='utf-8') as translated_file:
            translated_file.write(translated_text.text)
            print('File has been translated')

    except FileNotFoundError as err:
        print('Output file does not exist')
        raise err
    except IOError as err:
        print('IO error occurred when writing the file')
        raise err

except FileNotFoundError as err:
    print('Input file does not exist')
    raise err
except IOError as err:
    print('IO error occurred while reading the file')
    raise err
