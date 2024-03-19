class Zoologico():
    _zonas = []

    def __init__(self, nombre, ubicacion):
        self._nombre = nombre
        self._ubicacion = ubicacion

    def agregarZonas(self, zonas):
        self._zonas.append(zonas)

    def cantidadTotalAnimales(self):
        cantidadAnimales = 0
        for zona in self._zonas:
            cantidadAnimales += zona.cantidadAnimales()
        return cantidadAnimales

    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getUbicacion(self):
        return self._ubicacion

    def setUbicacion(self, ubicacion):
        self._ubicacion = ubicacion

    @classmethod
    def getZona(cls):
        return cls._zonas

    @classmethod
    def setZona(cls, zonas):
        cls._zonas=zonas