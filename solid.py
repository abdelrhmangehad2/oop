from abc import ABC, abstractmethod

class InvoiceOutput(ABC):
    @abstractmethod
    def output(self, invoice):
        pass

class ConsolePrinter(InvoiceOutput):
    def output(self, invoice):
        print("Invoice Details:")
        for item in invoice.items:
            print(f"{item['name']} - {item['quantity']} x {item['price']}")

class JsonPrinter(InvoiceOutput):
    def output(self, invoice):
        import json
        print(json.dumps(invoice.items, indent=2))


printer=  ConsolePrinter()
printer = JsonPrinter()

