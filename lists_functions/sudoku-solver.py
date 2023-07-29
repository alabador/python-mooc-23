
def row_correct(sudoku: list, row_no: int):
    selected_row =  sudoku[row_no]
    for elem in selected_row:
        if elem != 0 and selected_row.count(elem) > 1:
            return False
    return True

def column_correct(sudoku: list, column_no: int):
    selected_column =  []
    for row in sudoku:
        selected_column.append(row[column_no])
    print(selected_column)
    
    for elem in selected_column:
        if elem != 0 and selected_column.count(elem) > 1:
            return False
    return True

def block_correct(sudoku: list, row_no: int, column_no: int):
    block = []
    row_iter = 0
    while row_iter < 3:
        block.append(sudoku[row_no + row_iter][column_no:column_no+3])
        row_iter += 1
    print(block)
    spread = []
    for row in block:
        for elem in row:
            spread.append(elem)
    print(spread)
    for elem in spread:
        if elem != 0 and spread.count(elem) > 1:
            return False
    return True