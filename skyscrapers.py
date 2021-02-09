'''
Skyscrapers
'''
def read_input(path: str):
    '''
    Read game board file from path.
    Return list of str.
    '''
    positions = []
    file_ = open(path, 'r')
    contents = file_.readlines()
    for line in contents:
        positions.append(line.replace('\n', ''))
    return positions


def check_not_finished_board(board: list):
    """
    Check if skyscraper board is not finished, i.e., '?' present on the game board.

    Return True if finished, False otherwise.

    >>> check_not_finished_board(['***21**', '4?????*', '4?????*',\
         '*?????5', '*?????*', '*?????*', '*2*1***'])
    False
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
        '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_not_finished_board(['***21**', '412453*', '423145*',\
         '*5?3215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for line in board:
        if '?' in line:
            result = False
            break
        else:
            result = True
    return result


def check_uniqueness_in_rows(board: list):
    """
    Check buildings of unique height in each row.

    Return True if buildings in a row have unique length, False otherwise.

    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_uniqueness_in_rows(['***21**', '452453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_uniqueness_in_rows(['***21**', '412453*', '423145*',\
         '*553215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(1, len(board) - 1):
        if len(board[i][1:-1]) != len(set(board[i][1:-1])):
            result = False
            break
        else:
            result = True
    return result


def left_to_right_check(input_line: str, pivot: int):
    """
    Check row-wise visibility from left to right.
    Return True if number of building from the left-most hint is
    visible looking to the right,
    False otherwise.

    input_line - representing board row.
    pivot - number on the left-most hint of the input_line.

    >>> left_to_right_check("412453*", 4)
    True
    >>> left_to_right_check("452453*", 5)
    False
    """
    visibility = 1
    max_ = int(input_line[1])
    for i in range(2, len(input_line) - 1):
        number = int(input_line[i])
        if max_ < number:
            max_ = number
            visibility += 1
    return True if visibility == pivot else False


def check_horizontal_visibility(board: list):
    """
    Check row-wise visibility (left-right and vice versa)

    Return True if all horizontal hints are satisfiable,
     i.e., for line 412453* , hint is 4, and 1245 are the four buildings
      that could be observed from the hint looking to the right.

    >>> check_horizontal_visibility(['***21**', '412453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_horizontal_visibility(['***21**', '452453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    >>> check_horizontal_visibility(['***21**', '452413*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    for i in range(1, len(board) - 1):
        if board[i][0] != '*':
            result_1 = left_to_right_check(board[i], int(board[i][0]))
        else:
            result_1 = True
        # ------------------
        if board[i][-1] != '*':
            result_2 = left_to_right_check(board[i][::-1], int(board[i][-1]))
        else:
            result_2 = True
        # ------------------
        if result_1 == False or result_2 == False:
            result = False
            break
        else:
            result = True
    return result


def check_columns(board: list):
    """
    Check column-wise compliance of the board for uniqueness
    (buildings of unique height) and visibility
    (top-bottom and vice versa).

    Same as for horizontal cases, but aggregated in
    one function for vertical case, i.e. columns.

    >>> check_columns(['***21**', '412453*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    True
    >>> check_columns(['***21**', '412453*', '423145*',\
         '*543215', '*35214*', '*41232*', '*2*1***'])
    False
    >>> check_columns(['***21**', '412553*', '423145*',\
         '*543215', '*35214*', '*41532*', '*2*1***'])
    False
    """
    new_board = []
    for i in range(0, len(board) - 1):
        new_list = ''.join(list(map(lambda x: x[i], board)))
        new_board.append(new_list)
    # ----------------------------
    result_uniq = check_uniqueness_in_rows(new_board)
    if result_uniq == False:
        result = False
    else:
        result_visib = check_horizontal_visibility(new_board)
        if result_visib == False:
            result = False
        else:
            result = True
    return result


def check_skyscrapers(input_path: str):
    """
    Main function to check the status of skyscraper game board.
    Return True if the board status is compliant with the rules,
    False otherwise.
    """
    board = read_input(input_path)
    result_finished = check_not_finished_board(board)
    if result_finished == False:
        result = False
    else:
        result_uniq = check_uniqueness_in_rows(board)
        if result_uniq == False:
            result = False
        else:
            result_horizontal = check_horizontal_visibility(board)
            if result_horizontal == False:
                result = False
            else:
                result_column = check_columns(board)
                if result_column == False:
                    result = False
                else:
                    result = True
    return result


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(check_skyscrapers('C:/Users/Solomiya/Desktop/skyscrapers_state.txt'))
