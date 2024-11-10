import csv
import os

MAX_RECORDS = 3

class Records:

    # __file__ hace referencia al archvio actual (records.py)
    filename = 'records.csv'
    base_dir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    path = os.path.join(base_dir, 'data', filename)

    def __init__(self):
        # self.game_records = []
        self.check_records_file()
        self.cargar()

    def check_records_file(self):
        data_dir = os.path.dirname(self.path)
        if not os.path.isdir(data_dir):
            os.makedirs(data_dir)
            print('No había directorio para datos, pero lo he creado!')
        if not os.path.exists(self.path):
            self.reset()

    def insertar_record(self, nombre, puntuacion):
        # contador = 0
        # for item in self.game_records:
        #     if puntuacion > item[1]:
        #         self.game_records.insert(contador, [nombre, puntuacion])
        #         break
        #     contador += 1
        self.game_records.append([nombre, puntuacion])
        self.game_records.sort(key=lambda dato: dato[1], reverse=True)
        self.game_records = self.game_records[:MAX_RECORDS]
        self.guardar()

    @property
    def puntuacion_menor(self):
        return self.game_records[-1][1]

    def guardar(self):
        with open(self.path, mode="w") as records_file:
            writer = csv.writer(records_file, lineterminator='\n')
            writer.writerow(['Nombre', 'Puntos'])
            writer.writerows(self.game_records)

    def cargar(self):
        with open(self.path, mode='r') as records_file:
            reader = csv.reader(records_file, lineterminator='\n')
            self.game_records = []
            contador = 0
            for linea in reader:
                contador += 1
                if contador == 1:
                    continue
                self.game_records.append([linea[0], int(linea[1])])

    def reset(self):
        """
        Crea el archivo de records VACÍO.
        """
        # ¿dónde guardo los records?
        # vaciar los records guardados para que no haya ninguno
        # guardar el fichero

        self.game_records = []
        for cont in range(MAX_RECORDS):
            self.game_records.append(['---', 0])
        self.guardar()