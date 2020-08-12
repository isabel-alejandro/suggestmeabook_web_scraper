from textblob import TextBlob
import nltk  # Needed for a few TextBlob methods

#return words and how many times they're used
def data_analytics(sourcefile, floor=0):
    with open(sourcefile, 'r') as file:
        print("Reading file...\n")
        input = file.read().replace('\n', '').replace('.', ' ').replace(',', ' ')
        blob = TextBlob(input)
        output = blob.words

    # Tuples are keywords and how many times they are used.
    returndata = []
    for term in set(output):
        termcount = output.count(term)
        if termcount > floor:
            returndata.append((term, termcount))
        else:
            pass
    return returndata

nltk.download('brown')
nltk.download('punkt')

data = data_analytics('suggestmeabook.txt', 3)

#output to a CSV file
with open('exportdata.csv', 'w') as output:
    for pair in data:
        output.write(f'{pair[0]},{pair[1]}\n')
