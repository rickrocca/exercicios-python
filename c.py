n = int(input())
matrices = []

for n in range(0, n):
    matrix = input()
    matrices.append(matrix.split(','))

# TODO: Create a function to calculate accuracy and precision metrics
def calculate_accuracy_precision(tp,fp,fn,tn):

    accuracy = (tp + tn) / (tp + fp + fn + tn)
    precision = tp / (tp + fp) 

    return accuracy, precision

# TODO: Create a function to find the matrix index with the best combined accuracy and precision
def best_performance(matrices):
    best_index = 0
    best_accuracy = 0
    best_precision = 0
    # TODO: Define Loop through each matrix to calculate metrics
    for index, matrix in enumerate(matrices):
        # TODO: Define tp, fp fn and tn
        verdadeiros_positivos = int(matrix[0])
        falsos_positivos = int(matrix[1])
        verdadeiros_negativos = int(matrix[2])
        falsos_negativos = int(matrix[3])
        # TODO: Calculate accuracy and precision
        accuracy, precision = calculate_accuracy_precision(verdadeiros_positivos, falsos_positivos, verdadeiros_negativos, falsos_negativos)
        # TODO: Update best metrics if found
        print(index)
        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_precision = precision
            best_index = index + 1
        
    return best_index, best_accuracy, best_precision

# Print the results
best_index, best_accuracy, best_precision = best_performance(matrices)


print(f"Índice: {best_index}")
print(f"Acurácia: {round(best_accuracy, 2)}")
print(f"Precisão: {round(best_precision, 2)}")