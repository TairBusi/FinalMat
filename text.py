def revword(str):
     return str[::-1].lower()
 
def countword() :
    count=1
    myFile=open("text.txt","r")
    myListedFile=myFile.readlines()
    word=myListedFile[0].lower().strip()
    for line in myListedFile[1:]:
        for myWord in line.split():
            if revword(myWord).strip() == word:
                count+=1
    return count
'''
def revword(word:str) -> str:
    word=list(word)
    new_word=[]

    for letter in reversed(word):
      
        new_word.append(letter.lower())
    
    new_word=''.join(new_word)
    
    return new_word

def countword()->int:
    file = open("text.txt", 'r' )
    text =file.read()
    file.close()
    text=text.split()
    word=(text[0]).lower()
    new_text=[]
    for all_word in text[1:]:
        new_text.append(revword(all_word))     
    count=new_text.count(word)+1     

    return count

print(countword())


def revword(word:str) -> str:
    word=list(word)
    new_word=[]

    for letter in reversed(word):
      
        new_word.append(letter.lower())
    
    new_word=''.join(new_word)
    
    return new_word


def countword()->int:
    file = open("text.txt", 'r' )
    text =file.read()
    file.close()
    text=text.split()
    word=(text[0]).lower()
    new_text=[]
    for all_word in text[1:]:
        new_text.append(revword(all_word))     
    count=new_text.count(word)+1     

    return count

print(countword())

'''

  
    
    



        