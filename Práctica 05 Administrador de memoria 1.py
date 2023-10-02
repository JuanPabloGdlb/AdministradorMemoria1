# Definición de la clase MemoryBlock para representar un bloque de memoria con capacidad y nombre de proceso
class MemoryBlock:
    #Este es el constructor de la clase MemoryBlock. 
    def __init__(self, capacity):
        #Almacena la capacidad del bloque de memoria.
        self.capacity = capacity
        #El bloque de memoria está vacío y no contiene ningún proceso.
        self.process_name = None
#allocate: Este método se utiliza para asignar un proceso a un bloque de memoria.
    def allocate(self, process_name):
        self.process_name = process_name

    def deallocate(self):
        self.process_name = None

# Función para mostrar el estado de los bloques de memoria (ocupados o libres)
def display_memory_blocks(memory_blocks):
    for i, block in enumerate(memory_blocks):
        status = "Occupied" if block.process_name else "Free"
        print(f"Block {i+1} ({block.capacity} KB): {status} - Process: {block.process_name}")

# Algoritmo de asignación de memoria: Primer ajuste
def first_fit(memory_blocks, process_name, size):
    for block in memory_blocks:
        #Verifica si el bloque de memoria está libre, es decir, si no tiene ningún proceso asignado.
        #Esto verifica si la capacidad del bloque de memoria es igual o mayor que el tamaño del proceso que se desea asignar
        if not block.process_name and block.capacity >= size:
            block.allocate(process_name)
            return True
        #Si la función devuelve True para indicar que la asignación se realizó con éxito.
        #Si no se encuentra ningún bloque adecuado después de revisar todos los bloques de memoria, la función devuelve False para indicar que no se pudo asignar el proceso en ningún bloque.
    return False

# Algoritmo de asignación de memoria: Mejor ajuste
def best_fit(memory_blocks, process_name, size):
    # Esta variable se utilizará para realizar un seguimiento del bloque de memoria que mejor se ajuste al proceso.
    best_fit_block = None
    for block in memory_blocks:
    #Verifica si el bloque de memoria está libre, es decir, si no tiene ningún proceso asignado.
        #Esto verifica si la capacidad del bloque de memoria es igual o mayor que el tamaño del proceso que se desea asignar
        if not block.process_name and block.capacity >= size:
            if best_fit_block is None or block.capacity < best_fit_block.capacity:
                best_fit_block = block
    # Busca el bloque de memoria que mejor se adapte al tamaño del proceso y lo utiliza para asignar el proceso si cumple con los requisitos de tamaño.
    if best_fit_block:
        best_fit_block.allocate(process_name)
        return True
    return False

# Algoritmo de asignación de memoria: Peor ajuste
def worst_fit(memory_blocks, process_name, size):
    # Esta variable se utilizará para realizar un seguimiento del bloque de memoria que mejor se ajuste al proceso.
    worst_fit_block = None
    for block in memory_blocks:
        #Verifica si el bloque de memoria está libre, es decir, si no tiene ningún proceso asignado.
            #Esto verifica si la capacidad del bloque de memoria es igual o mayor que el tamaño del proceso que se desea asignar
        if not block.process_name and block.capacity >= size:
            if worst_fit_block is None or block.capacity > worst_fit_block.capacity:
                worst_fit_block = block
    # Busca el bloque de memoria que peor se adapte al tamaño del proceso y lo utiliza para asignar el proceso si cumple con los requisitos de tamaño.
    if worst_fit_block:
        worst_fit_block.allocate(process_name)
        return True
    return False

# Algoritmo de asignación de memoria: Siguiente ajuste
def next_fit(memory_blocks, process_name, size, last_allocated_index):
# Se obtiene el número total de bloques de memoria en la lista memory_blocks
# y se almacena en la variable n.
    n = len(memory_blocks)
    for i in range(n):
        # El bucle comienza desde el último bloque asignado
        index = (last_allocated_index + i) % n
        block = memory_blocks[index]
        # verifica si el bloque de memoria está libre
        if not block.process_name and block.capacity >= size:
            block.allocate(process_name)
            return index
    return -1

# Función principal del programa
def main():
    num_blocks = int(input("Ingrese el número de bloques de memoria: "))
    memory_blocks = []
    # Ingresar la capacidad de cada bloque de memoria
    for _ in range(num_blocks):
    # Busca el próximo bloque disponible a partir del último bloque asignado y lo utiliza para asignar el proceso si cumple con los requisitos de tamaño.
        capacity = int(input(f"Ingrese la capacidad del bloque {len(memory_blocks)+1} en KB: "))
        memory_blocks.append(MemoryBlock(capacity))

    while True:
        print("\nElija un algoritmo\n 1: Primer ajuste\n 2: Mejor ajuste\n 3: Peor ajuste\n 4: Siguiente ajuste\n 0: Salir\n ")
        algorithm_choice = input("Opción: ")

        if algorithm_choice == "0":
            break

        if algorithm_choice not in ["1", "2", "3", "4"]:
            print("Opción no válida. Por favor, ingrese un número válido.")
            continue
# Leer el archivo "archivos.txt" que contiene los nombres y tamaños de los procesos
        try:
            with open("archivos.txt", "r") as file:
                lines = file.readlines()
                for line in lines:
                    process_name, size_str = line.strip().split(", ")
                    size = int(size_str[:-2])  # Eliminar "kb" y convertir a entero

                    allocated = False
                    if algorithm_choice == "1":
                        allocated = first_fit(memory_blocks, process_name, size)
                    elif algorithm_choice == "2":
                        allocated = best_fit(memory_blocks, process_name, size)
                    elif algorithm_choice == "3":
                        allocated = worst_fit(memory_blocks, process_name, size)
                    elif algorithm_choice == "4":
                        last_allocated_index = -1
                        while True:
                            last_allocated_index = next_fit(memory_blocks, process_name, size, last_allocated_index)
                            if last_allocated_index == -1:
                                break
                            allocated = True
                            break

                    if allocated:
                        print(f"Archivo {process_name} asignado con éxito usando el algoritmo seleccionado.")
                    else:
                        print(f"No se pudo asignar el archivo {process_name} usando el algoritmo seleccionado. No hay suficiente espacio.")

                    display_memory_blocks(memory_blocks)

        except FileNotFoundError:
            print("El archivo 'archivos.txt' no se encuentra.")

if __name__ == "__main__":
    main()
