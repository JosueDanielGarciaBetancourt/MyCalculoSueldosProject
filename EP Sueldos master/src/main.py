from logica.Inserts import Insert
from logica.Deletes import Delete
from logica.Updates import Update
from logica.Queries import Queries
from logica.CalculoSueldo import CalculoSueldo
from modelo.Declarative_Base import inicializarBD
from vista.GestorSueldos import GestorSueldos

if __name__ == '__main__':

    # Borrar tablas y crear nuevamente
    inicializarBD()

    print("\n==============INSERTS==============")
    print("\nMESES")

    # Insertar meses
    Insert.insertMes("MES01", "ENERO")
    Insert.insertMes("MES02", "FEBRERO")
    Insert.insertMes("MES03", "MARZO")
    Insert.insertMes("MES04", "ABRIL")
    Insert.insertMes("MES05", "MAYO")
    Insert.insertMes("MES06", "JUNIO")
    Insert.insertMes("MES07", "JULIO")
    Insert.insertMes("MES08", "AGOSTO")
    Insert.insertMes("MES09", "SEPTIEMBRE")
    Insert.insertMes("MES10", "OCTUBRE")
    Insert.insertMes("MES11", "NOVIEMBRE")
    Insert.insertMes("MES12", "DICIEMBRE")

    print("\nBONIFICACIONES")
    # Insertar bonificaciones
    Insert.insertBonificacion("BONI01", "Factor por horas extras", 0.50)
    Insert.insertBonificacion("BONI02", "Movilidad", 1000.00)
    Insert.insertBonificacion("BONI03", "Factor de bonificación suplementaria", 0.03)

    print("\nTRABAJADORES")
    # Insertar trabajador
    Insert.insertTrabajador("TRAB01", "Josué García", 500.00,'CIO')
    Insert.insertTrabajador("TRAB02", "Sergio Ramírez", 700.00,'CIO2')
    Insert.insertTrabajador("TRAB03", "Gian Piere", 1200.00,'CIO3')

    print("\nDETALLE MENSUAL TRABAJADOR")
    # Insertar detalle mensual trabajador
    Insert.insertDetalleMensualTrabajador("TRAB01", "MES11", 3, 60, 30, 1, 1, 2000.00)
    Insert.insertDetalleMensualTrabajador("TRAB01", "MES12", 3, 60, 30, 1, 1, 2000.00)
    Insert.insertDetalleMensualTrabajador("TRAB02", "MES05", 3, 60, 30, 1, 1, 2000.00)

    print("\nBOLETA DE PAGO")
    # Insertar boleta pago
    Insert.insertBoletaPago("BOLE01TRAB01", "TRAB01", 2000.00, 200.00, 1700.00)
    Insert.insertBoletaPago("BOLE01TRAB02", "TRAB02", 2000.00, 200.00, 1700.00)

    print("\nDETALLE BONIFICACIÓN")
    # Insertar detalle de bonificación
    Insert.insertDetalleBonificacion("BONI01", "BOLE01TRAB01", 250.00)
    Insert.insertDetalleBonificacion("BONI02", "BOLE01TRAB01", 1000.00)
    Insert.insertDetalleBonificacion("BONI03", "BOLE01TRAB02", 750.00)

    print("\n==============DELETES==============\n")
    print("\nMES")
    # Eliminando un mes
    Delete.deleteMes("MES12")

    print("\nTRABAJADOR")
    # Eliminando un trabajador (esto borrará registros en boletaPago)
    Delete.deleteTrabajador("TRAB01")

    print("\nBONIFICACIÓN")
    # Eliminando una bonificación (esto borrará registros en detalleBonificacion)
    # Delete.deleteBonificacion("BONI02")

    print("\n==============UPDATES==============\n")

    print("\nSUELDO BASE")
    Update.updateSueldoBase("TRAB02", 100)

    print("\nBONIFICACIÓN")
    Update.updateValorBonificacion("BONI01", 0.6)

    print("\n==============QUERIES==============\n")

    # Ejemplo: Obtener un mes por ID
    print("MES")
    mes = Queries.get_mes_by_id("MES05")
    if mes:
        print("ID del Mes: ", mes.IDMes)
        print("Nombre del Mes: ", mes.mesNombre)
    else:
        print("No se encontró el mes.")

    print()

    # Ejemplo: Obtener una bonificación por ID
    print("BONIFICACIÓN")
    bonificacion = Queries.get_bonificacion_by_id("BONI03")
    if bonificacion:
        print("ID de Bonificación: ", bonificacion.IDBonificacion)
        print("Tipo de Bonificación: ", bonificacion.bonTipo)
        print("Valor de Bonificación: ", bonificacion.bonValor)
    else:
        print("No se encontró la bonificación.")

    print()

    # Ejemplo: Obtener un trabajador por ID
    print("TRABAJADOR")
    trabajador = Queries.get_trabajador_by_id("TRAB02")
    if trabajador:
        print("ID del Trabajador: ", trabajador.IDTrabajador)
        print("Nombre y Apellidos: ", trabajador.trabNombreApellidos)
        print("Sueldo Base: ", trabajador.trabSueldoBase)
        print("Fecha de Creación: ", trabajador.created_at)
    else:
        print("No se encontró el trabajador.")

    print()

    # Ejemplo: Obtener un detalle mensual de trabajador por ID de trabajador y ID de mes
    print("DETALLE MENSUAL")
    detalle_mensual = Queries.get_detalle_mensual_trabajador_by_id("TRAB02", "MES05")
    if detalle_mensual:
        print("ID del Trabajador: ", detalle_mensual.IDTrabajador)
        print("ID del Mes: ", detalle_mensual.IDMes)
        print("Año: ", detalle_mensual.detalleAnio)
        print("Horas extras: ", detalle_mensual.detalleHorasExtras)
        print("Minutos de tardanza: ", detalle_mensual.detalleMinutosTardanzas)
        print("Horas extras: ", detalle_mensual.detalleHorasExtras)
        print("Minutos justificados: ", detalle_mensual.detalleMinutosJustificados)
        print("Días de falta: ", detalle_mensual.detalleDiasFalta)
        print("Días justificados: ", detalle_mensual.detalleDiasJustificados)
        print("Sueldo Neto: ", detalle_mensual.detalleSueldoNeto)
    else:
        print("No se encontró el detalle mensual.")

    print()

    # Ejemplo: Obtener una boleta de pago por ID
    print("BOLETA DE PAGO")
    boleta_pago = Queries.get_boleta_pago_by_id("BOLE01TRAB02")
    if boleta_pago:
        print("ID de Boleta de Pago:", boleta_pago.IDBoletaPago)
        print("ID del Trabajador:", boleta_pago.IDTrabajador)
        print("Sueldo Neto:", boleta_pago.bolSueldoNeto)
        print("Descuento Total:", boleta_pago.bolDescuentoTotal)
        print("Bonificación Total:", boleta_pago.bolBonificacionTotal)
        print("Fecha de Emisión:", boleta_pago.bolFechaEmision)
        print("Hora de Emisión:", boleta_pago.bolHoraEmision)
    else:
        print("No se encontró la boleta de pago.")

    print()

    # Ejemplo: Obtener un detalle de bonificación por ID de bonificación y ID de boleta de pago
    print("DETALLE DE BONIFICACIÓN")
    detalle_bonificacion = Queries.get_detalle_bonificacion_by_id("BONI03", "BOLE01TRAB02")
    if detalle_bonificacion:
        print("ID de Bonificación:", detalle_bonificacion.IDBonificacion)
        print("ID de Boleta de Pago:", detalle_bonificacion.IDBoletaPago)
        print("Monto total de bonificación: ", detalle_bonificacion.detbonMontoTotalPorBonificacion)
    else:
        print("No se encontró el detalle de bonificación.")

    print("\n==============PRUEBA CÁLCULO SUELDO==============\n")

    trab02 = Queries.get_trabajador_by_id("TRAB02")
    detalleTrab02 = Queries.get_detalle_mensual_trabajador_by_id("TRAB02", "MES05")
    Movilidad = Queries.get_bonificacion_by_id("BONI02")
    factSuplementaria = Queries.get_bonificacion_by_id("BONI03")
    print("BONIFICACIONES: \n")
    print("Movilidad: ", Movilidad.bonValor)
    print("Factor de bonif. Suplementaria: ", factSuplementaria.bonValor)
    print("TRAB02: \n")
    print("ID del Trabajador: ", trab02.IDTrabajador)
    print("Nombre y Apellidos: ", trab02.trabNombreApellidos)
    print("Sueldo Base: ", trab02.trabSueldoBase)
    print("Fecha de Creación: ", trab02.created_at)
    print("\nDetalle mensual TRAB02: \n")
    print("ID del Trabajador: ", detalleTrab02.IDTrabajador)
    print("ID del Mes: ", detalleTrab02.IDMes)
    print("Año: ", detalleTrab02.detalleAnio)
    print("Horas extras: ", detalleTrab02.detalleHorasExtras)
    print("Minutos de tardanza: ", detalleTrab02.detalleMinutosTardanzas)
    print("Horas extras: ", detalleTrab02.detalleHorasExtras)
    print("Minutos justificados: ", detalleTrab02.detalleMinutosJustificados)
    print("Días de falta: ", detalleTrab02.detalleDiasFalta)
    print("Días justificados: ", detalleTrab02.detalleDiasJustificados)

    calcularSueldoTrab01 = CalculoSueldo(trab02.trabSueldoBase, detalleTrab02.detalleHorasExtras,
                                         detalleTrab02.detalleDiasFalta, detalleTrab02.detalleMinutosTardanzas,
                                         Movilidad.bonValor, factSuplementaria.bonValor)

    sueldoNetoTrab02 = calcularSueldoTrab01.CalcularSueldoNeto()

    print(f"\nEl SUELDO NETO de TRAB02 es: {sueldoNetoTrab02}")

    print("\nEjecutando app...")

    # Ejecutar App
    App = GestorSueldos()
