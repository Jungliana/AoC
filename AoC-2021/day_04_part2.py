import numpy as np


def loadNumberList():
    numberList = []
    with open('day_04_input_01') as file:
        for line in file:
            splittedLine = line.split(',')
            for element in splittedLine:
                numberList.append(int(element))
    return numberList


def readBingoBoards():
    numberList = []
    with open('day_04_input_02') as file:
        for line in file:
            if line != '\n':
                row = line.rstrip('\n').split()
                row = [int(element) for element in row]
                numberList.append(row)
    return numberList


def cutBingoBoards(numberList):
    return [numberList[x:x+5] for x in range(0, len(numberList), 5)]


class BingoBoard():
    def __init__(self, board) -> None:
        self.board = np.array(board)
        self.boardState = self.generateEmptyBoardState()
        self.winning = False
        self.whenWinning = None

    def generateEmptyBoardState(self) -> np.ndarray:
        emptyState = np.zeros((5, 5))
        return emptyState

    def update(self, number):
        numberPosition = np.where(self.board == number)
        for coord in zip(numberPosition[0], numberPosition[1]):
            self.boardState[coord] = 1

    def checkIfWinning(self, i) -> bool:
        numbersColumns = self.boardState.sum(axis=0)
        numbersRows = self.boardState.sum(axis=1)
        if (5. in numbersColumns) or (5. in numbersRows):
            self.winning = True
            if self.whenWinning is None:
                self.whenWinning = i

    def sumUnmarked(self):
        markedValues = np.multiply(self.board, self.boardState)
        unmarkedValues = self.board - markedValues
        return np.sum(unmarkedValues, axis=None)

    def __str__(self) -> str:
        return f'{self.board}'


class BingoGame():
    def __init__(self) -> None:
        self.boards = self.loadBingoBoards()
        self.numbers = loadNumberList()
        self.winner = None
        self.currentNumber = None

    def loadBingoBoards(self):
        allBoards = readBingoBoards()
        listOfBoards = cutBingoBoards(allBoards)
        return [BingoBoard(board) for board in listOfBoards]

    def updateBoards(self):
        for board in self.boards:
            board.update(self.currentNumber)

    def checkForWinner(self, i):
        for board in self.boards:
            board.checkIfWinning(i)
            if board.winning is True:
                self.winner = board

    def allWinning(self):
        for board in self.boards:
            if not board.winning:
                return False
        return True

    def __str__(self) -> str:
        return f'Current number: {self.currentNumber}, winner: {self.winner}'

    def play(self):
        for i in range(len(self.numbers)):
            self.currentNumber = self.numbers[i]
            self.updateBoards()
            self.checkForWinner(i)
            if self.allWinning():
                break

    def findLastWinning(self):
        currentLast = None
        for board in self.boards:
            if (currentLast is None) or (board.whenWinning > currentLast.whenWinning):
                currentLast = board
        return currentLast.sumUnmarked() * self.currentNumber

    def finalScore(self):
        return self.winner.sumUnmarked() * self.currentNumber


if __name__ == "__main__":
    bingo = BingoGame()
    bingo.play()
    print(bingo.findLastWinning())
