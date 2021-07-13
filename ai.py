from chess import Board
import chess


piece_value = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}


pawn_position_based_eval_for_white = [
    0, 0, 0, 0, 0, 0, 0, 0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5, 5, 10, 25, 25, 10, 5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, -5, -10, 0, 0, -10, -5, 5,
    5, 0, -10, -20, -20, -10, 0, 5,
    0, 0, 0, 0, 0, 0, 0, 0
]
pawn_black = [
    0,  0,  0,  0,  0,  0,  0,  0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
     5,  5, 10, 25, 25, 10,  5,  5,
     0,  0,  0, 20, 20,  0,  0,  0,
     5, -5,-10,  0,  0,-10, -5,  5,
     5, 0, 10,-20,-20, 10, 0,  5,
     0,  0,  0,  0,  0,  0,  0,  0
]
pawn_position_based_eval_for_black = list(reversed(pawn_black))

knight_position_based_eval_for_white = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]
# 89 to win
# knight_black = [
#     -40, -40, -40, -40, -30, -40, -40, -40,
#     -40, -20, 0, 0, 0, 0, -20, -40,
#     -30, 0, 10, 15, 15, 10, 0, -30,
#     -30, 5, 15, 20, 20, 15, 5, -30,
#     -30, 0, 15, 20, 20, 15, 0, -30,
#     -30, 5, 10, 15, 15, 10, 5, -30,
#     -40, -20, -20, 0, 0, 0, -20, -40,
#     -40, -40, -40, -40, -30, -40, -40, -40
# ]

# 99 to win
knight_black = [
    -40, -40, -40, -40, -30, -40, -40, -40,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, 0, -40,
    -40, -40, -40, -40, -30, -40, -40, -40
]

knight_position_based_eval_for_black = list(reversed(knight_black))

# Pawel's suggestion
queen_position_based_eval_for_white = [
    -10, -5, -5, -5, -5, -5, -5, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 0, 0, 5, 0, -10,
    -10, -5, -5, -5, -5, -5, -5, -10
]

# queen_position_based_eval_for_white = [
#     -10, -5, -5, -5, -5, -5, -5, -10,
#     -10, 0, 0, 0, 0, 0, 0, -10,
#     -10, 0, 5, 5, 5, 5, 0, -10,
#     -5, 0, 5, 5, 5, 5, 0, -5,
#     0, 0, 5, 5, 5, 5, 0, -5,
#     -10, 5, 5, 5, 5, 5, 0, -10,
#     -5, 0, 0, 0, 0, 0, 0, -10,
#     -10, -5, -5, -5, -5, -5, -5, -10
# ]


queen_position_temp_for_black = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20,
]
queen_position_based_eval_for_black = list(reversed(queen_position_temp_for_black))


bishop_position_based_eval_for_white = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]
bishop_position_based_eval_for_black = list(reversed(bishop_position_based_eval_for_white))

rook_position_based_eval_for_white = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0,
]
rook_position_based_eval_for_black = list(reversed(rook_position_based_eval_for_white))

king_position_based_eval_for_white = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, 0, 0, 0, 20, 20,
    30, 20, 10, 0, 0, 10, 20, 30
]
king_position_based_eval_for_black = list(reversed(king_position_based_eval_for_white))

king_position_based_eval_for_white_end_game = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10,  0,  0, -10, -20, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -30,  0,  0,  0,  0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50
]

king_position_based_eval_for_black_end_game = list(reversed(king_position_based_eval_for_white_end_game))


def evaluate_position(piece: chess.Piece, square: chess.Square, end_game: bool) -> int:
    piece_type = piece.piece_type
    positions = None
    if piece_type == chess.PAWN:
        if piece.color == chess.WHITE:
            positions = pawn_position_based_eval_for_white
        else:
            positions = pawn_position_based_eval_for_black
    if piece_type == chess.KNIGHT:
        if piece.color == chess.WHITE:
            positions = knight_position_based_eval_for_white
        else:
            if piece.color == chess.BLACK:
                positions = knight_position_based_eval_for_black
    if piece_type == chess.BISHOP:
        if piece.color == chess.WHITE:
            positions = bishop_position_based_eval_for_white
        else:
            positions = bishop_position_based_eval_for_black
    if piece_type == chess.ROOK:
        if piece.color == chess.WHITE:
            positions = rook_position_based_eval_for_white
        else:
            positions = rook_position_based_eval_for_black
    if piece_type == chess.QUEEN:
        if piece.color == chess.WHITE:
            positions = queen_position_based_eval_for_white
        else:
            positions = queen_position_based_eval_for_black
    if piece_type == chess.KING:
        if end_game:
            if piece.color == chess.WHITE:
                positions = king_position_based_eval_for_white_end_game
            else:
                positions = king_position_based_eval_for_black_end_game
        else:
            if piece.color == chess.WHITE:
                positions = king_position_based_eval_for_white
            else:
                positions = king_position_based_eval_for_black

    return positions[square]

def are_we_in_end_game(board: chess.Board) -> bool:
    queens = 0
    bishops_knights = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            if piece.color == chess.WHITE and piece.piece_type == chess.QUEEN:
                queens += 1
            # if piece.piece_type == chess.KNIGHT or piece.piece_type == chess.BISHOP:
            if piece.piece_type == chess.KNIGHT and piece.color == chess.BLACK:
                bishops_knights += 1
    #no one has a queen or no other pieces are on the board
    if queens == 0 or (queens == 2 and bishops_knights <= 1):
        return True
    else:
        return False

def vanilla_eval(board):
    return 0
c = 0
def maximizer(board: chess.Board, depth: int,alpha , beta, evaluate=vanilla_eval) -> float:
    # global c
    if board.is_checkmate():
        return -float("inf")
    if depth == 0 or board.is_game_over():
        return evaluate(board)
    value = -float('inf')
    for move in board.legal_moves:
        board.push(move)
        print(move)
        value = max(value, minimizer(board, depth - 1, alpha, beta, evaluate ))
        board.pop()
        # c = c + 1
    # print(c)
    return value

def minimizer(board: chess.Board, depth: int, alpha , beta , evaluate=vanilla_eval) -> float:
    # global c
    if board.is_checkmate():
        return float("inf")
    if depth == 0 or board.is_game_over():
        return evaluate(board)
    value = float('inf')
    for move in board.legal_moves:
        board.push(move)
        print(move)
        value = min(value, maximizer(board, depth - 1, alpha, beta, evaluate))
        board.pop()
        # c = c + 1
    # print(c)
    return value

def captureHeuristic(board: chess.Board, source, destination):
    souToDest = {}
    notCapture = {}

    for s in source:
        for d in destination:

            square = chess.parse_square(d)
            piece = board.piece_at(square)

            if piece is not None:
                notCapture[d] = False
                if piece.piece_type == chess.KING:
                    souToDest[(s, d)] = piece_value[chess.KING]
                elif piece.piece_type == chess.QUEEN:
                    souToDest[(s, d)] = piece_value[chess.QUEEN]
                elif piece.piece_type == chess.KNIGHT:
                    souToDest[(s, d)] = piece_value[chess.KNIGHT]
                elif piece.piece_type == chess.PAWN:
                    souToDest[(s, d)] = piece_value[chess.PAWN]
                elif piece.piece_type == chess.ROOK:
                    souToDest[(s, d)] = piece_value[chess.ROOK]
                elif piece.piece_type == chess.BISHOP:
                    souToDest[(s, d)] = piece_value[chess.BISHOP]
            else:
                notCapture[d] = True

    return souToDest, notCapture

def RelativeHistoryAndKillerHeuristic(board: chess.Board,source, destination, depth, historyHeuristic, butterflyHeuristic, killerHeuristic):
    souToDest = {}
    for s in source:
        for dest in destination:
            square = chess.parse_square(dest)
            piece = board.piece_at(square)
            if piece is None:
                if butterflyHeuristic[dest] == 0:
                    souToDest[(s,dest)] = 0 + killerHeuristic[depth - 1][dest]
                elif butterflyHeuristic[dest] != 0:
                    # souToDest[(s,dest)] =  killerHeuristic[depth - 1][dest]
                    souToDest[(s,dest)] = (int(historyHeuristic[dest]) / int(butterflyHeuristic[dest])) + killerHeuristic[depth - 1][dest]
    return souToDest



def alphabeta(board: chess.Board, depth: int, alpha , beta, maxORmin,historyHeuristic,butterflyHeuristic, killerHeuristic, evaluate=vanilla_eval) -> float:
    global c
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    moves = list(board.legal_moves)
    destination = []
    source = []
    souToDest1 = {}
    souToDest2 = {}
    notCapture = {}
    souToDest = {}

    for m in moves:
        tempDest = m.__str__()[2:4]
        tempSou = m.__str__()[:2]
        destination.append(tempDest)
        source.append(tempSou)
        souToDest[(tempSou, tempDest)] = 0


    souToDest1,notCapture  = captureHeuristic(board, source, destination)
    souToDest2 = RelativeHistoryAndKillerHeuristic(board, source, destination, depth, historyHeuristic, butterflyHeuristic, killerHeuristic)

    for x in souToDest1:
        souToDest[(x[0], x[1])] = souToDest1[x]

    for y in souToDest2:
        souToDest[(y[0], y[1])] = souToDest2[y]


    firstTime = True
    bestMove = 0
    if maxORmin:
        if board.is_checkmate():
            return -float("inf")
        for child in sorted(souToDest, key=souToDest.get, reverse=True):
            # c = c + 1
            # print(c)
            move = child[0] + child[1]
            board.push(chess.Move.from_uci(move))
            value = -float('inf')
            count = 0
            for i in notCapture:
                if notCapture[i]:
                    count = count + 1
            if count != len(notCapture):
                if not notCapture[child[1]] and firstTime:
                    bestMove = souToDest[child]
                if notCapture[child[1]]:
                    if bestMove > souToDest[child]:
                        break
            firstTime = False

            # another heuristic
            if notCapture[child[1]]:
                historyHeuristic[child[1]] += 1
                for m in sorted(souToDest, key=souToDest.get, reverse=True):
                    if m != child:
                        butterflyHeuristic[child[1]] += 1
                killerHeuristic[depth - 1][child[1]] += 1
            value = max(value,
                        alphabeta(board, depth - 1, alpha, beta, False, historyHeuristic, butterflyHeuristic, killerHeuristic,
                                  evaluate))
            alpha = max(alpha, value)

            if alpha >= beta:
                # historyHeuristic[child[1]] += 1
                # for m in sorted(souToDest, key=souToDest.get, reverse=True):
                #     if m != child:
                #         butterflyHeuristic[child[1]] += 1
                # killerHeuristic[depth - 1][child[1]] += 1
                board.pop()
                break
            else:
                if notCapture[child[1]]:
                    butterflyHeuristic[child[1]] += 1
            board.pop()
            # c = 0
            return value
    else:
        if board.is_checkmate():
            return float("inf")
        for child in sorted(souToDest, key=souToDest.get, reverse=True):
            # c = c + 1
            # print(c)
            move = child[0] + child[1]
            board.push(chess.Move.from_uci(move))
            value = float('inf')
            count = 0
            for i in notCapture:
                if notCapture[i]:
                    count = count + 1
            if count != len(notCapture):
                if not notCapture[child[1]] and firstTime:
                    bestMove = souToDest[child]
                if notCapture[child[1]]:
                    if bestMove > souToDest[child]:
                        break
            firstTime = False


            # another heuristic
            if notCapture[child[1]]:
                historyHeuristic[child[1]] += 1
                for m in sorted(souToDest, key=souToDest.get, reverse=True):
                    if m != child:
                        butterflyHeuristic[child[1]] += 1
                killerHeuristic[depth - 1][child[1]] += 1
            value = min(value,
                        alphabeta(board, depth - 1, alpha, beta, True, historyHeuristic, butterflyHeuristic, killerHeuristic,
                                  evaluate))
            beta = min(beta, value)

            if beta <= alpha:
                # historyHeuristic[child[1]] += 1
                # for m in sorted(souToDest, key=souToDest.get, reverse=True):
                #     if m != child:
                #         butterflyHeuristic[child[1]] += 1
                # killerHeuristic[depth - 1][child[1]] += 1
                board.pop()
                break
            else:
                if notCapture[child[1]]:
                    butterflyHeuristic[child[1]] += 1
            board.pop()
            # c = 0
            return value

