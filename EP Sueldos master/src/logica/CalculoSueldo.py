
class CalculoSueldo():
    def __init__(self, sueldoBase, horasExtra, diasFalta, minutosTardanza, montoMovilidad, factorSuplementaria):
        self.horasExtra = horasExtra
        self.sueldo = sueldoBase
        self.diasFalta = diasFalta
        self.minutosTardanza = minutosTardanza
        self.Movilidad = montoMovilidad
        self.Suplementaria = factorSuplementaria

    def CalcularSueldoNeto(self):
        sueldoBasico = self.sueldo
        bonificaciones = self.CalculoBonificaciones()
        descuentos = self.CalculoDescuentos()
        sueldoNeto = sueldoBasico+bonificaciones-descuentos
        sueldoNeto = round(sueldoNeto, 2)
        return sueldoNeto

    def CalculoBonificaciones(self):
        self.PagoHorasExtra = 1.50*self.horasExtra*((self.sueldo/30)/8)
        self.BonificacionSumplementaria = self.Suplementaria*self.sueldo
        self.Bonificaciones = self.Movilidad+self.BonificacionSumplementaria+self.PagoHorasExtra
        self.remuneracionComputable = self.sueldo+self.Movilidad+self.BonificacionSumplementaria
        return self.Bonificaciones

    def CalculoDescuentos(self):
        self.remuneracionMinima = self.sueldo+self.Bonificaciones
        self.DescuentoFaltas = self.remuneracionComputable/30*self.diasFalta
        self.DescuentoTardanza = (((self.remuneracionComputable/30)/8)/60)*self.minutosTardanza
        self.descuentos = self.DescuentoFaltas+self.DescuentoTardanza
        return self.descuentos

