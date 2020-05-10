# Rail Fence Cipher Encryption function

  
# function to encrypt a message
a=15
def RailFenceEncrypt(plain_text, key):
  
    """create the matrix to cipher """
    # no of columns = length of plain text 
    # no of rows = selected key

    """filling the rail matrix initialsing with ‘\n’""" 
    
    rail = [['\n' for i in range(len(plain_text))] 
                  for j in range(key)]
      
    # to find the vertical dircetion in which the text has to be encrypted
    vertical_direction = False
    row, col = 0, 0
      
    for i in range(len(plain_text)):
          
        """ check the vertical direction and reverse it if
         we have reached the top or bottom rail """
         
        if (row == 0) or (row == key - 1):
            vertical_direction = not vertical_direction
          
        # Enter one element of plain_text into the cipher matrix
        
        rail[row][col] = plain_text[i]
        col += 1
          
        """find the next row using direction flag"""
        
        if vertical_direction:
            row += 1
        else:
            row -= 1
    # now we can construct the cipher 
    # using the rail matrix
    encrypted_text = []
    for i in range(key):
        for j in range(len(plain_text)):
            if rail[i][j] != '\n':
                encrypted_text.append(rail[i][j])
    return("" . join(encrypted_text))
 
 #first change for git

#This is on new branch