# src/services/biblioteca_service.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from src.models.libro import Libro
from utils.validadores.comunes import validar_id
from utils.validadores.biblioteca.validaciones_biblioteca import (
    validar_titulo, validar_autor, validar_precio, validar_cantidad
)

class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []
        self.ingresos = 0.0

    def buscar_libro(self, titulo):
        for libro in self.catalogo:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None

    def agregar_libro(self, libro):
        self.catalogo.append(libro)
        return f"✅ '{libro.titulo}' añadido al catálogo."

    def prestar_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if not libro:
            return "❌ Libro no encontrado."
        if libro.prestado:
            return "⚠️ El libro ya está prestado."
        libro.prestado = True
        return f"📖 Libro '{titulo}' prestado con éxito."

    def devolver_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if not libro:
            return "❌ Libro no encontrado."
        if not libro.prestado:
            return "⚠️ El libro no estaba prestado."
        libro.prestado = False
        return f"🔄 Libro '{titulo}' devuelto. ¡Gracias!"

    def comprar_libro(self, titulo, autor, precio, cantidad=1):
        # Primero validamos
        ok_titulo, resultado_titulo = validar_titulo(titulo)
        if not ok_titulo:
            return False, f"❌ {resultado_titulo}"
        
        ok_autor, resultado_autor = validar_autor(autor)
        if not ok_autor:
            return False, f"❌ {resultado_autor}"
        
        ok_precio, resultado_precio = validar_precio(precio)
        if not ok_precio:
            return False, f"❌ {resultado_precio}"
        
        ok_cant, resultado_cant = validar_cantidad(cantidad)
        if not ok_cant:
            return False, f"❌ {resultado_cant}"

        # Si pasa validaciones, procedemos
        existente = self.buscar_libro(resultado_titulo)
        if existente:
            existente.cantidad += resultado_cant
            return True, f"📦 Stock de '{resultado_titulo}' actualizado a {existente.cantidad} unidades."
        else:
            nuevo = Libro(resultado_titulo, resultado_autor, resultado_precio, resultado_cant)
            mensaje = self.agregar_libro(nuevo)
            return True, mensaje

    def vender_libro(self, titulo):
        libro = self.buscar_libro(titulo)
        if not libro:
            return "❌ Libro no encontrado."
        if libro.cantidad <= 0:
            return "⚠️ Sin stock disponible."
        if libro.prestado:
            return "⚠️ El libro está prestado, no se puede vender."
        
        libro.cantidad -= 1
        self.ingresos += libro.precio
        return f"💰 Vendido '{libro.titulo}' por ${libro.precio:.2f}. Ingresos totales: ${self.ingresos:.2f}"

    def mostrar_catalogo(self):
        if not self.catalogo:
            return "📭 Catálogo vacío."
        
        resultado = [f"\n📚 Catálogo de '{self.nombre}':"]
        for libro in self.catalogo:
            resultado.append(f"   {libro}")
        return "\n".join(resultado)