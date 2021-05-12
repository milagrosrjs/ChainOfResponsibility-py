from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional


class Handler(ABC):
    """
    La interfaz Handler declara un método para construir la cadena de controladores.
    También declara un método para ejecutar una solicitud.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler: #setea el handler siguiente
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]: #le define una solicitud al handle
        pass


class AbstractHandler(Handler):
    

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Devolver un controlador desde aquí nos permitirá vincular los controladores en una
        # forma conveniente como esta:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


"""
Todos los Handlers manejan una solicitud o la pasan al siguiente Handler en
la cadena.
"""


class MonkeyHandler(AbstractHandler): #handler que responde a la solicitud "Banana"
    def handle(self, request: Any) -> str:
        if request == "Banana":
            return f"Monkey: I'll eat the {request}"
        else:
            return super().handle(request)


class SquirrelHandler(AbstractHandler): #handler que responde a la solicitud "Nut"
    def handle(self, request: Any) -> str:
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}"
        else:
            return super().handle(request)


class DogHandler(AbstractHandler): #handler que responde a la solicitud "MeatBall"
    def handle(self, request: Any) -> str:
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}"
        else:
            return super().handle(request)


def client_code(handler: Handler) -> None: #función que solo recibe un handler en específico
    """
     El código de cliente trabaja con un solo controlador.
    """

    for food in ["Nut", "Banana", "MeatBall"]: #for para general enviar solicitudes a Handlers
        print(f"\nClient: Who wants a {food}?")
        result = handler.handle(food)
        if result:
            print(f"  {result}", end="") #si el handler actual puede responder a esa solicitud dice que comió food 
        else:
            print(f"  {food} was left untouched.", end="") #si no puede responder a la solicitud dice que no tocó food


if __name__ == "__main__":
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()

    monkey.set_next(squirrel).set_next(dog) #setea el orden de la cadena

    # El cliente debe poder enviar una solicitud a cualquier controlador, no solo al
    # primero en la cadena.
    print("Chain: Monkey > Squirrel > Dog")
    client_code(monkey) #empieza por mono
    print("\n")

    print("Subchain: Squirrel > Dog")
    client_code(squirrel) #empieza por squirrel
    print("\n")

    print("Subsubchain: Squirrel")
    client_code(dog) #empieza por perro

