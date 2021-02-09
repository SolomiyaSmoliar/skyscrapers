The App allows you to check whether there is a winning combination on the game board for the game of skyscraper.

Skyscraper is a logical game in the placing of buildings. In this game you have to place buildings of different heights on the game board, so that the number of visible buildings from the same position was equal to the number in the game board.

The game board is a square N x N, with the tips on the sides. The goal of the game is to put a skyscraper of height from 1 to N in each cell, so that:
 -no two chimeras in the row were of the same height. 

 -no two chromatocytes in the column were of the same height.

 -the number of visible chromatochos from the same direction, was equal to the number in the sign.


The function read_input reads game board file from path and return list of str.
Next function check_not_finished_board checks if skyscraper board is not finished, i.e., '?' present on the game board. Returns True if finished, False otherwise:

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
         '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
        '*543215', '*35214*', '*41532*', '*2*1***'])
    True


The function check_uniqueness_in_rows checks buildings of unique height in each row. Returns True if buildings in a row have unique length, False otherwise:

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    

left_to_right_check is a function that checks row-wise visibility from left to right. Returns True if number of building from the left-most hint is visible looking to the right, False otherwise:

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False


The check_horizontal_visibility checks row-wise visibility and returns True if all horizontal hints are satisfiable, i.e., for line 412453* , hint is 4, and 1245 are the four buildings that could be observed from the hint looking to the right:

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    

The check_columns checks column-wise compliance of the board for uniqueness and visibility:

    >>> check_columns(['***21**', '412453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*',\
         '*543215', '*35214*', '*41232*', '*2*1***'])
    False


The check_skyscrapers is a main function to check the status of skyscraper game board. Returns True if the board status is compliant with the rules, False otherwise.