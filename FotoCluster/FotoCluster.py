# Вывод количества кластеров в выборке фотографий по косинусному расстоянию.

# Решение задачи.

# Автор: Хоружий И.Н.
# Дата:  18-19.01.2022


from sklearn.metrics.pairwise import cosine_similarity

# класс учета данных по кластеризации
# вначале количество кластеров рано количеству кластеризуемых объектов
# потом объединяем похожие вызовом cluster_objects
class My_cluster:
    def __init__(self, num_objects):
        self.num_objects = num_objects
        # список с номерами кластеров, куда попали объекты
        # изначально для каждого объекта свой кластер
        self.nums_clustered = [ i for i in range(0, num_objects)]        
        self.count = num_objects

    # объединение объектов с индексами index1, index2 в кластер 
    def cluster_objects(self, index1, index2):
        if self.nums_clustered[index1] == self.nums_clustered[index2]:
            return
        # объединяем кластеры
        for i in range(0, self.num_objects):
            if self.nums_clustered[i] == self.nums_clustered[index2]:
                self.nums_clustered[i] = self.nums_clustered[index1]
        self.count -= 1        
                
    def get_count_clusters(self):        
        return self.count

def main():
    # читаем входные данные из файла input.txt
    in_file = open("input.txt", mode = "r")
    param = in_file.readline().split(" ")
    n_foto = int(param[0])
    metrics = int(param[1])
    treshold = float(param[2])
    print("N = ", n_foto, ", M = ", metrics, ", T = ", treshold)
    fotos = list()
    fotos = [[float(item) for item in line.split(" ")] for line in in_file]
    print(fotos)
    in_file.close()

    # вычисляем матрицу косинусных расстояний между наборами метрик
    # !!! не уверен, что правильно использую cosine_similarity,
    # но результат похож на правду
    # надо будет позже разобраться
    cosine_matrix = cosine_similarity(fotos)
    print('\n', cosine_matrix)

    # оъединение в кластеры
    clasters = My_cluster(n_foto)
    for i in range(0, n_foto):
        for j in range(i+1, n_foto):
            if cosine_matrix[i][j] >= treshold:
                clasters.cluster_objects(i, j)
    #вывод ответа
    print(clasters.get_count_clusters())
    outFile = open("output.txt", mode = "w")        
    outFile.write(str(clasters.get_count_clusters()))
    outFile.close()

    


    
if __name__ == "__main__":
    main()
