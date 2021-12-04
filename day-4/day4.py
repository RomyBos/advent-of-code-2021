inputfile_boards = open('day-4/day4_input_board.txt', 'r')
inputfile_numbers = open('day-4/day4_input_num.txt', 'r')

BOARD_SIZE = 5

boards = []
with open('day-4/day4_input_board.txt', 'r') as f:
    board = []
    for line in f.readlines():
        row = []
        if line == '\n':
            boards.append(board)
            board = []
        else:
            for num in line.split():
                row.append({'number': num, 'marked': False})
            board.append(row)            
        
numbers = inputfile_numbers.read().split(',')

def play(boards, numbers):
    # Draw a number:
    for number in numbers:
        print("Next Number drawn:")
        print(number)
        # Mark number on all boards:
        boards = markBoards(boards, number)
        # Check if there is a winner
        winnerBoardNumbers = getWinner(boards)
        if winnerBoardNumbers != []:
            for winner in winnerBoardNumbers:
                winnerBoard = boards[winner]
                print('Score of winning board:')
                print(getBoardScore(winnerBoard, int(number)))
            winnerBoardNumbers = list(sorted(set(winnerBoardNumbers)))
            winnerBoardNumbers = winnerBoardNumbers[::-1]
            for winner in winnerBoardNumbers:
                del boards[winner]
        if boards == []:
            break
            

def markBoards(boards, num):
    marked_boards = boards.copy()
    for board in marked_boards:
        for row in board:
            for place in row:
                if place['number'] == num:
                    place['marked'] = True
    return marked_boards

def getWinner(boards):
    list_of_winners = []
    for b in range(len(boards)):
        board = boards[b]
        for i in range(BOARD_SIZE):
            row_win = True
            column_win = True
            for j in range(BOARD_SIZE):
                place = board[i][j]
                if place['marked'] == False:
                    row_win = False
                place = board[j][i]
                if place['marked'] == False:
                    column_win = False
            if (row_win or column_win) == True:
                list_of_winners.append(b)
    return list_of_winners

def getBoardScore(board, num):
    sum = 0
    for row in board:
        for place in row:
            if place['marked'] == False:
                sum += int(place['number'])
    score = sum * num
    return score

play(boards, numbers)