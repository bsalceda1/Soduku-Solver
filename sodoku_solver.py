sodoku_board = [
	[0,0,2,8,0,0,3,0,0],
	[0,0,0,0,0,9,0,2,0],
	[4,3,7,2,5,6,0,0,0],  
	[1,0,0,0,0,0,0,0,4],
	[3,0,4,0,1,0,6,0,7],
	[5,0,6,4,0,7,0,1,0],
	[6,0,8,1,0,2,4,7,9],
	[0,0,3,5,0,0,0,6,0],
	[0,9,0,7,0,4,0,3,8],
]

def print_board(board):
	for y in range(len(board)):
		#Print horizontal line every 3 elements
		if y % 3 == 0 and y != 0:
			print("----------------------")
		###########################################
		for x in range(len(board[0])):
					#Print vertical line every 3 element
					if x % 3 == 0 and x != 0 :
						print("|", end= " ")
					####################################
					if x < len(board[0]) - 1:
						print(board[y][x], end=" ")
					else:
						print(board[y][x])

#Return position of empty spot
def find_empty_spot(board):
	for y in range(len(board)):
		for x in range(len(board)):
			if board[y][x] == 0:
				return (y, x)

def is_valid(board, pos, val):
	#Check if new val doesnt break sodoku rule
	#check row
	for x in range(len(board[0])):
		if board[pos[0]][x] == val and x != pos[1]:
			return False
	#check column 
	for y in range(len(board)):
		if board[y][pos[1]] == val and y != pos[0]:
			return False

	#check mini box 
	#(8,0)
	y_mini = pos[0] // 3
	x_mini = pos[1] // 3
	#678
	#012
	for y in range(y_mini*3, y_mini*3 + 3):
		for x in range(x_mini*3, x_mini*3 + 3):
			if board[y][x] == val and [y,x] != pos:
				return False

	return True

def solve(board):
	#Return True if no more empty spot
	if not find_empty_spot(board):
		return True

	empty = find_empty_spot(board)
	y,x = empty
	for i in range(1,10):
		#Check 1-9, put in empty spot if valid
		if is_valid(board, (y,x), i):
			board[y][x] = i

			#Call function until all empty boxes have value
			if solve(board):
				return True

		board[y][x] = 0

	return False

if __name__ == "__main__":
	print_board(sodoku_board)
	solve(sodoku_board)
	print("#######################")
	print_board(sodoku_board)
						 
