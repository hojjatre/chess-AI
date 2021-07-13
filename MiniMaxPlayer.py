import chess
from Player import Player
from ai import *

class MiniMaxPlayer(Player):
    max_depth = 2
    move_count = 0

    def initHeuristics(self):
        self.historyHeuristic = {}
        self.killerHeuristic = {}
        self.butterflyHeuristic = {}
        for square in chess.SQUARES:
            self.historyHeuristic[chess.square_name(square)] = 0
            self.butterflyHeuristic[chess.square_name(square)] = 0
        for i in range(0, self.max_depth):
            self.killerHeuristic[i] = {}
            for square in chess.SQUARES:
                self.killerHeuristic[i][chess.square_name(square)] = 0

    def evaluate(self, board: chess.Board) -> float:
        total = 0
        end_game = are_we_in_end_game(board)

        value = 0
        for square in chess.SQUARES:
            piece = board.piece_at(square)
            if not piece:
                continue


            value = piece_value[piece.piece_type] + evaluate_position(piece, square, end_game)

            if piece.color == chess.WHITE:
                total += value
            else:
                total -= value

        return total


    def move(self, board: chess.Board) -> chess.Move:
        self.initHeuristics()
        # c = 0
        value = -float('inf') if self.player_color else float('inf')
        alpha = -float('inf')
        beta = float('inf')
        best_move = None
        temp = 0
        legal_moves = list(board.legal_moves)

        for move in legal_moves:
            board.push(move)
            if board.is_checkmate():
                board.pop()
                return move

            if board.is_game_over():

                value = max(value, self.evaluate(board)) if self.player_color else min(value, self.evaluate(board))
                

                if self.player_color:
                    if temp >= value:
                        value = temp
                        best_move = move
                else:
                    if temp <= value:
                        value = temp
                        best_move = move

                board.pop()

                continue
            if board.can_claim_draw():
                temp = 0
            else:
                # temp = minimizer(board, self.max_depth, alpha, beta, self.evaluate) if self.player_color else maximizer(board, self.max_depth, alpha, beta, self.evaluate)
                temp = alphabeta(board, self.max_depth, alpha, beta,False, self.historyHeuristic, self.butterflyHeuristic, self.killerHeuristic, self.evaluate) if self.player_color else alphabeta(board, self.max_depth, alpha, beta, True, self.historyHeuristic, self.butterflyHeuristic, self.killerHeuristic, self.evaluate)
                # c = c + 1
                # print(c)
            if self.player_color:
                if temp >= value:
                    value = temp
                    best_move = move
            else:
                if temp <= value:
                    value = temp
                    best_move = move
            board.pop()

        self.move_count += 1

        return best_move

