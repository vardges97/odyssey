from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print(self,document):
        pass
    @abstractmethod
    def scan(self,document):
        pass

class OldPrinter(Printer):
    def print(self,document):
        print(f"Printing {document} in black and white")

class NewPrinter(Printer):
    def print(self,document):
        print(f"Printing {document} in color")
    def scan(self,document):
        print(f"Scanning {document}...")

"""isp can be interpreted as a copy of single responsibility with the aditional thought about client 
who should not be forced to use methods they dont need ie a class should not be forced to have/use something
 it has no business using/having """

class Printer(ABC):
    @abstractmethod
    def print(self,document):
        pass
class Scanner(ABC):
    @abstractmethod
    def scan(self,document):
        pass

class Oldprinter(Printer):
    def print(self,document):
        print(f'printing {document}')

class NewPrinter(Printer,Scanner):
    def print(self,document):
        print(f'printing {document} in colour')
    def scan(self,document):
        print(f'scanning {document}')
"""this way print and scan are separate classes which have a single responsibility and each 
class can take whatever responsibility it needs and thus not violate isp(interface segregation principle) """