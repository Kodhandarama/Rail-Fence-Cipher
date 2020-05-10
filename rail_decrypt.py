def RailFenceDecrypt(cipher, key): 
  
    """create the matrix to cipher"""  
    # no of rows = plain text key   
    # no of columns = length(cipher)
     
    # filling the rail matrix to distinguish filled spaces 
    #from blank ones
     
    rail = [['\n' for i in range(len(cipher))]  
                  for j in range(key)] 
      
    # To find the vertical direction in 
    #which to decrypt the cipher
    vertical_direction = None
    row, col = 0, 0
      
    # mark the places with '*' 
    for i in range(len(cipher)): 
        if row == 0: 
            vertical_direction = True
        if row == key - 1: 
            vertical_direction = False
          
        # place the marker because this is a marked space 
        rail[row][col] = '*'
        col += 1
          
        # find the next row using direction flag 
        if vertical_direction: 
            row += 1
        else: 
            row -= 1
              
    """ Now we can construct the rail matrix based on the marked spaces"""
    index = 0
    for i in range(key): 
        for j in range(len(cipher)): 
            if ((rail[i][j] == '*') and (index < len(cipher))): 
                rail[i][j] = cipher[index] 
                index += 1
          
    """ Now, the marked spaces are read to give the decrypted text """
    decrypted_text = [] 
    row, col = 0, 0
    for i in range(len(cipher)): 
          
        # check the direction of flow 
        if row == 0: 
            vertical_direction = True
        if row == key-1: 
            vertical_direction = False
              
        # place the marker 
        if (rail[row][col] != '*'): 
            decrypted_text.append(rail[row][col]) 
            col += 1
              
        # find the next row using 
        # direction flag 
        if vertical_direction: 
            row += 1
        else: 
            row -= 1
    return("".join(decrypted_text)) 

