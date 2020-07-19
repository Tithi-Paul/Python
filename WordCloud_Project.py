def generate_from_frequencies(Mp):
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    cloud.to_file("myfile.jpg")


def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]
    
    # LEARNER CODE START HERE

    all_words = file_contents.split()
    print(all_words)

    Mp = {}
    for i in all_words:
        if i.isalpha() == True and uninteresting_words.count(i) == 0:
            if i not in Mp:
                Mp[i] = 1
            else:
                Mp[i] += 1

    generate_from_frequencies(Mp)        
    
    #wordcloud
    #cloud = wordcloud.WordCloud()
    #cloud.generate_from_frequencies()
    #return cloud.to_array()

Input = "i am not Hridoy roy who loved coding"
calculate_frequencies(Input)