from Dominio import Factura
from datetime import datetime as dt
import main

listadoFacturas = [] #list

formatoConseFact = "FACT#{0}" 
consecutivoFactura = 1


def encabezadoSistema():
    print("----------------------------------")   
    print("Opción #1 : Crear facturas")
    print("Opción #2 : Imprimir facturas")
    print("----------------------------------")

def crearFactura(montofactura, categoriaVenta):

    if (categoriaVenta == 'A' or categoriaVenta == 'a' or categoriaVenta == 'B' or categoriaVenta == 'b' or categoriaVenta == 'C' or categoriaVenta == 'c'):
        try:

            if (categoriaVenta == 'A' or categoriaVenta == 'a'):
                descuento = 0.05
            elif (categoriaVenta == 'B' or categoriaVenta == 'b'):
                descuento = 0.10
            else: #y sino
                descuentoparcial = int(input("Ingrese el porcentaje de descuento aplicado: "))
                descuento = descuentoparcial / 100 

            ofactura = Factura() #instanciar una clase en un objeto (ya existe en memoria)   
            global consecutivoFactura
            numFact = str(consecutivoFactura).rjust(5,'0')
            ofactura.idfactura =  formatoConseFact.format(numFact) #"FACT#0001" #Quemar el dato / HardCode
            ofactura.fechafactura = dt.now()    
            ofactura.categoriaVenta = categoriaVenta
            ofactura.montofactura = montofactura        
            ofactura.calculaImpuesto()
            ofactura.montototal = ofactura.impuestofactura + ofactura.montofactura
            ofactura.descuento = ofactura.montofactura * descuento
            listadoFacturas.append(ofactura) #es el metodo que me permite agregar elementos a la lista
            consecutivoFactura = consecutivoFactura + 1
            #n = 2
            #x = 0
            #resultado = n / x
            #consecutivoFactura += 1 
        except ZeroDivisionError:
            #Mandar registrar el error en bitacoras (Tabla BD / Archivo Txt)
            #Informarle al usuario de error con un mensaje mas amigable
            print("Se esta dando una division entre cero")   
        except BaseException:
            print('Existe un error al crear la factura')
        
    else: #y sino
            print("Categoria invalida")
            main.registrarfactura
    
  
def imprimirfacturas():
    #iterar es saltar de elemento a elemento dentro de la colección
    
    for n in listadoFacturas:
        print("---------------")
        print(n.idfactura, "Factura en colones")
        #casting de dato convirtiendo de numero (int) a cadena de texto (str)
        print("Fecha ",n.fechafactura)
        print("La cateogria de la factura es: ",n.categoriaVenta)
        print("Subtotal ","₡",n.montofactura) 
        print("Descuento ","₡",n.descuento)
        print("Impuesto ","₡",round(n.impuestofactura,5))
        print("Total ","₡",(n.montofactura-n.descuento)+n.impuestofactura)
        