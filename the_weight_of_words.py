# utilizes a recursive approach with memoization
def find_word(length, weight, word_list, char_memory):

    # BASE CASE
    # only insert a character as a word to the first last element in the list
    if length == 1:
        if 1 <= weight <= 26:

            # Unicode code value is converted from character to int, then converted to character
            word_list[-1] = chr(ord('a') + weight - 1)    
            return True
        else:
            return False

    # already calculated before
    if(length, weight) in char_memory:
        return False

    for i in range(25, -1, -1):   # decrease the weight from 26 to 0.

        # look up characters with remaining lenght and weight
        if find_word(length - 1, weight - i - 1, word_list, char_memory):  

            word_list[-length] = chr(ord('a') + i)  #the length last element = element from first to the end in the list
            return True
    
    char_memory.add((length, weight))
    return False


# Tne result
def get_word(length, weight):

    word_list = [''] * length
    
    char_memory = set()       # store previously calculated results

    if find_word(length, weight, word_list, char_memory):
        return ''.join(word_list)

    else:
        return 'impossible' 

if __name__ == "__main__": ## main change to be "get_word"
    try:
        length, weight = map(int, input().split())

        if length <= 0 or length > 40 or weight <= 0 or weight > 1000:
            raise ValueError("out of the range of l or w")
    
        result = get_word(length, weight)
        print(result)

    except ValueError as e:
        print("input error", str(e))