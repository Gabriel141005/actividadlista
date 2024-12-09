class NodoArbol:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.hijos = []
        self.pareja = None

def añadir_pareja(nodo, etiqueta_pareja):
    if nodo.pareja is None:
        pareja = NodoArbol(etiqueta_pareja)
        nodo.pareja = pareja
        pareja.pareja = nodo
        return f"Pareja {etiqueta_pareja} añadida a {nodo.etiqueta}"
    else:
        return f"{nodo.etiqueta} ya tiene pareja ({nodo.pareja.etiqueta})"

def añadir_descendiente(progenitor, etiqueta_hijo):
    hijo = NodoArbol(etiqueta_hijo)
    progenitor.hijos.append(hijo)
    if progenitor.pareja:
        progenitor.pareja.hijos.append(hijo)  # Compartir hijos entre pareja
    return f"Descendiente {etiqueta_hijo} añadido a {progenitor.etiqueta}"

def desplegar_arbol(nodo, nivel=0):
    if nodo is not None:
        print("    " * nivel + "- " + nodo.etiqueta)
        if nodo.pareja:
            print("    " * nivel + "  (Pareja: " + nodo.pareja.etiqueta + ")")
        for hijo in nodo.hijos:
            desplegar_arbol(hijo, nivel + 1)

def localizar_nodo(nodo, etiqueta):
    if nodo is None:
        return None
    if nodo.etiqueta == etiqueta:
        return nodo
    for hijo in nodo.hijos:
        resultado = localizar_nodo(hijo, etiqueta)
        if resultado:
            return resultado
    return None

def actualizar_nodo(nodo, etiqueta_actual, etiqueta_nueva):
    nodo_objetivo = localizar_nodo(nodo, etiqueta_actual)
    if nodo_objetivo:
        nodo_objetivo.etiqueta = etiqueta_nueva
        return f"Nodo {etiqueta_actual} actualizado a {etiqueta_nueva}"
    else:
        return "Nodo no encontrado"

def listar_descendientes(nodo):
    if not nodo.hijos:
        return f"{nodo.etiqueta} no tiene descendientes"
    return "Descendientes de " + nodo.etiqueta + ": " + ", ".join(h.etiqueta for h in nodo.hijos)

# Menú interactivo
arbol_raiz = None

while True:
    print("\n🌳 ARBOL 🌳")
    print("1. Nueva raíz")
    print("2. Añadir pareja")
    print("3. Añadir descendiente")
    print("4. Mostrar árbol completo")
    print("5. Actualizar nodo/nombress")
    print("6. Listar descendientes de un nodo")
    print("7. Salir")
    opcion = input("OPCIÓN: ")

    if opcion == "1":
        if arbol_raiz is None:
            etiqueta_raiz = input("Introduce el nombre de la raíz: ")
            arbol_raiz = NodoArbol(etiqueta_raiz)
            print(f"Raíz {etiqueta_raiz} creada.")
        else:
            print("Ya existe ese")

    elif opcion == "2":
        if arbol_raiz is None:
            print("Primero debes crear la raíz")
        else:
            etiqueta_nodo = input("Introduce el nombre del quien tendra pareja: ")
            nodo = localizar_nodo(arbol_raiz, etiqueta_nodo)
            if nodo:
                etiqueta_pareja = input("Introduce el nombre de la pareja: ")
                print(añadir_pareja(nodo, etiqueta_pareja))
            else:
                print("nombre no encontrado")

    elif opcion == "3":
        if arbol_raiz is None:
            print("Primero debes crear la raiz")
        else:
            etiqueta_nodo = input("Introduce nombre del padre/madre: ")
            nodo = localizar_nodo(arbol_raiz, etiqueta_nodo)
            if nodo:
                etiqueta_hijo = input("Introduce el nombre del nuevo descendiente: ")
                print(añadir_descendiente(nodo, etiqueta_hijo))
            else:
                print("no encontrado")

    elif opcion == "4":
        if arbol_raiz is None:
            print("Árbol vacio")
        else:
            desplegar_arbol(arbol_raiz)

    elif opcion == "5":
        if arbol_raiz is None:
            print("Primero debes crear la raiz")
        else:
            etiqueta_actual = input("Nombre del nodo a cambiar: ")
            etiqueta_nueva = input("Nuevo nombre: ")
            print(actualizar_nodo(arbol_raiz, etiqueta_actual, etiqueta_nueva))

    elif opcion == "6":
        if arbol_raiz is None:
            print("Primero debes crear la raiz")
        else:
            etiqueta_nodo = input("Introduce la etiqueta del nodo: ")
            nodo = localizar_nodo(arbol_raiz, etiqueta_nodo)
            if nodo:
                print(listar_descendientes(nodo))
            else:
                print("Nodo no encontrado")

    elif opcion == "7":
        print("Saliendo...")
        break

    else:
        print("Opción no válida.")
