
def read_file(file_path:str)->list:
    with open(file_path,'r') as file:
        word_list = [_.strip() for _ in file.readlines()]
    return word_list
    

def wagner_fiesher(word1:str,word2:str)->int:
    len1,len2 = len(word1)+1,len(word2)+1

    #Initializing zeros based on the length of both the words
    d = [[0] *len2 for _ in range(len1)]

    # Targetting the first row and column, then make an initialization [0,...len(word)]
    for i in range(len1):
        d[i][0] = i
    for j in range(len2):
        d[0][j] = j

    for i in range(1,len1):
        for j in range(1,len2):
            if word1[i-1] == word2[j-1]:
                s = 0
            else:
                s = 1
            
            d[i][j] = min(d[i-1][j]+1, #deletion
                        d[i][j-1]+1, #insertion
                        d[i-1][j-1]+s #subtitution
                        )
    return d[len1-1][len2-1]

def calculate_distance(word:str,word_list:list)->dict:
    word_dictionary = {}
    for words in word_list:
        calculate_distance = wagner_fiesher(word,words)
        word_dictionary[words] = calculate_distance #storing the word and distance
    
    return word_dictionary

if __name__=='__main__':
    word = 'bellytish'
    word_list = read_file(file_path = "words.txt")
    word_dictionary = calculate_distance(word,word_list)
    sorted_words = sorted(word_dictionary.items(),key = lambda item:item[1])
    print('The Top Five closest match is :')
    for i in range(len(sorted_words)):
        print(f'{sorted_words[i][0]} : {sorted_words[i][1]}')
        if i ==5:
            break
    
        
    