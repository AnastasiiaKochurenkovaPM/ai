import random
from math import exp
import numpy as np
from matplotlib import pyplot as plt
import time
from copy import deepcopy

N_QUEENS = 8
TEMPERATURE = 100

#Формула комбінації. Це вибір двох королев у n королев
def threat_calculate(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    return (n - 1) * n / 2

#Створіть шахову дошку з ферзем у рядку
def create_board(n):
    chess_board = {}
    temp = list(range(n))
    random.shuffle(temp)
    column = 0

    while len(temp) > 0:
        row = random.choice(temp)
        chess_board[column] = row
        temp.remove(row)
        column += 1
    del temp
    print_board(chess_board)
    return chess_board

#обчислення загроз для ферзя
def cost(chess_board):
    threat = 0
    m_chessboard = {}
    a_chessboard = {}

    for column in chess_board:
        temp_m = column - chess_board[column]
        temp_a = column + chess_board[column]
        if temp_m not in m_chessboard:
            m_chessboard[temp_m] = 1
        else:
            m_chessboard[temp_m] += 1
        if temp_a not in a_chessboard:
            a_chessboard[temp_a] = 1
        else:
            a_chessboard[temp_a] += 1

    for i in m_chessboard:
        threat += threat_calculate(m_chessboard[i])
    del m_chessboard

    for i in a_chessboard:
        threat += threat_calculate(a_chessboard[i])
    del a_chessboard

    return threat

#Допоміжна функція випадкової зміни розв'язку
def in_conflict_with_another_queen(row, column, board):
    
    for other_column, other_row in enumerate(board):
        if in_conflict(column, row, other_column, other_row):
            if row != other_row or column != other_column:
                return True
    return False

#Оцінка розв'язку. Перевіряє, чи даний рядок і стовпець відповідають ферзю, який конфліктує з іншим ферзем
def in_conflict(column, row, other_column, other_row):
    
    if column == other_column:
        return True 
    if row == other_row:
        return True
    if abs(column - other_column) == abs(row - other_row):
        return True

    return False

#друк дошки
def print_board(board):
    print("")
    for row in range(len(board)):
        line = ''
        for column in range(len(board)):
            if board[column] == row:
                line += ' Q ' if in_conflict_with_another_queen(row, column, board) else ' q '
            else:
                line += ' . '
        print(line)
    print("")


# метод відпалу
def simulated_annealing():
    solution_found = False
    line = []
    answer = create_board(N_QUEENS)

    cost_answer = cost(answer)

    t = TEMPERATURE
    sch = 0.99

    while t > 0:
        t *= sch
        successor = deepcopy(answer)
        while True:
            index_1 = random.randrange(0, N_QUEENS - 1)
            index_2 = random.randrange(0, N_QUEENS - 1)
            if index_1 != index_2:
                break
        successor[index_1], successor[index_2] = successor[index_2], \
            successor[index_1] 
        line.append(successor[index_2])
        delta = cost(successor) - cost_answer
        if delta < 0 or random.uniform(0, 1) < exp(-delta / t):
            answer = deepcopy(successor)
            cost_answer = cost(answer)
        if cost_answer == 0:
            solution_found = True
            print_result(answer)
            break
    if solution_found is False:
        print("Failed")

    print_board(answer)     


#Друк координат
def print_result(board):
    result = []
    for column, row in board.items():
        result.append(row+1)
        print("{} => {}".format(column+1, row+1))    
    return result             


def main():
    start = time.time()
    simulated_annealing()


if __name__ == "__main__":
    main()