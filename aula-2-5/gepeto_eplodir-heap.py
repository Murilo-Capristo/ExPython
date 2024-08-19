
contador = 1
class LargeObject:
    def __init__(self, size_mb):
        # Inicializa o objeto com um bytearray que consome memória
        self.data = bytearray(10**6 * size_mb)  # `size_mb` MB por objeto

def allocate_large_memory(size_mb_per_object):
    large_objects = []
    while True:
        global contador 
        contador += 1
        print(contador)
        large_objects.append(LargeObject(size_mb_per_object))
   

# Ajuste o tamanho do bloco de memória por objeto em megabytes
allocate_large_memory(size_mb_per_object=10)  # 10 MB por objeto