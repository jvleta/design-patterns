from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

PI = 3.14159

class ShapeVisitor(ABC):

    @abstractmethod
    def visit_circle_object(self, element: Circle) -> None:
        pass

    @abstractmethod
    def visit_square_object(self, element: Square) -> None:
        pass
    
class Shape(ABC):

    @abstractmethod
    def accept(self, visitor: ShapeVisitor) -> None:
        pass

@dataclass    
class Circle(Shape):
    radius: float
    
    def accept(self, visitor: ShapeVisitor) -> None:
        visitor.visit_circle_object(self)

    def exclusive_method_of_concrete_component_a(self) -> str:
        return "A"

@dataclass
class Square(Shape):
    length: float
    
    def accept(self, visitor: ShapeVisitor):
        visitor.visit_square_object(self)

    
class ComputeArea(ShapeVisitor):
    def visit_circle_object(self, element) -> None:
        print(f"Area = {pi * element.radius**2}")

    def visit_square_object(self, element) -> None:
        print(f"Area = {element.length**2}")


class ComputePerimeter(ShapeVisitor):
    def visit_circle_object(self, element) -> None:
        print(f"Perimeter = {2.0 * pi * element.radius}")

    def visit_square_object(self, element) -> None:
        print(f"Perimeter = {4.0 * element.length}")


def client_code(components: List[Shape], visitor: ShapeVisitor) -> None:
    for component in components:
        component.accept(visitor)
    

if __name__ == "__main__":
    shapes = [Circle(1.0), Square(1.0)]

    client_code(shapes, ComputeArea())
    client_code(shapes, ComputePerimeter())
    
    