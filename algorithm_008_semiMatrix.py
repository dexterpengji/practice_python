# nesting

# vector ===========================
vec_h = [2, 4, 6]

vec_h_sq = [x**x for x in vec_h]
print(vec_h_sq)

vec_v = [[2],[4],[6]]

vec_v_sq = [[x**x] for x in vec_h]
print(vec_v_sq)

# matrix ===========================
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[9,10,11,12]
]

def semy(mat):
	if type(mat[0]) == int:
		return [[ele] for ele in mat]
	else:
		if len(mat[0]) == 1:
			return [x[0] for x in mat]
		else:
			return [[row[i] for row in mat] for i in range(len(mat)+1)]

print(semy(vec_h))
print(semy(vec_v))
print(semy(matrix))
