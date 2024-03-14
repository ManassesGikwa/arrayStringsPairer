def solution(S):
    #BDD
    #Given an array of strings
    #when you find a pair of strings (matching letters at a particular index)
    #then return an array containing the indices of two strings and the position where they share a common letter.
    #Create a dictionary to store indices of letters at each position
    
    #PSEUDOCODE
    # 1. Initialize a dictionary 
    # 2. Iterate through each string in S
    # 3. Iterate a second time through each character in the string 
    # 4. If the character is not in the dictionary, add it else 
    # 5. If the position is not in the dictionary for this character, add it
    # 6. Append the index of the string
    # 7. Iterate through the S_letters_dict dictionary to find pairs
    # 8. If there are at least two indices in this position return the first pair found
    
    #initialize our dictionary to hold characters and track position
    S_letters_dict = {}
    
    #iterating through each string inS
    for i, string in enumerate(S):
            #loop again through each character in the string 
        for j, char in enumerate(string):
            if char not in S_letters_dict:
                S_letters_dict[char] = {}            
            if j not in S_letters_dict[char]:
                S_letters_dict[char][j] = []        
            S_letters_dict[char][j].append(i)
        #Iterate through dictionary  and find pairs
            
        for char, positions in S_letters_dict.items():
            for position, indices in positions.items():
           
              if len(indices) >= 2:
                # any first pair found
                return [indices[0], indices[1], position]
    
    # If no pair is found, return an empty list
    return []


print(solution(["abc","bca","dbe"]))  # Expected: [0, 2, 1]
print(solution(["zzzz","ferz","zdsr","fgtd"]))  # Expected: [0, 1, 3]
print(solution(["gr","sd","rg"]))  # Expected: []
print(solution(["bdafg","ceagi"]))  # Expected: [0, 1, 2]
