from random import choice
from experta import *

class reglas(Fact):
    """Info about the traffic light."""
    pass

class Response:
    def __init__(self):
        self.response = []
    pass

    def addResponse(self, response):
        self.response.append(response)
        
    def getResponse(self):
        return self.response

class sistemadereglas(KnowledgeEngine):
    
    def __init__(self, responses):
        super().__init__()
        self.responses = responses
    pass


    @Rule((reglas(estado_academico="si")))
    def m1(self):
        result = 'Usted cuenta con una buena salud a nivel respiratorio.'
        print(result)
        self.responses.addResponse(result) 
        
    @Rule(AND(reglas(first="si")),(reglas(second="no")),(reglas(third="no")),(reglas(fourth="no")),(reglas(fifth="no")))
    def m2(self):
        result = ' Es recomendable tomar reposo, la dificultad a respirar puede deberse a varias causas una de ellas la falta de ejercicio fisico, si los sintomas persisten despues de tomar un descanzo consulte a su medico. '
        print(result)
        self.responses.addResponse(result) 

    @Rule(AND(reglas(first="no")),(reglas(second="si")),(reglas(third="no")),(reglas(fourth="no")),(reglas(fifth="no")))
    def m3(self):
        result = 'Si actualmente no presenta ningun signo de alarma se le recomienda mantener una revision periodica con su medico para el control o terapias.'
        print(result)
        self.responses.addResponse(result) 

    @Rule(AND(reglas(first="no")),(reglas(second="no")),(reglas(third="si")),(reglas(fourth="no")),(reglas(fifth="no")))
    def m4(self):
        result = 'Debe acercarse a su centro de salud mas cercano, realizarce los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result) 
    
    @Rule(AND(reglas(first="no")),(reglas(second="no")),(reglas(third="no")),(reglas(fourth="si")),(reglas(fifth="no")))
    def m5(self):
        result = 'Por favor ser mas claro ya que no seleccionado ningun sintoma.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="no")),(reglas(third="no")),(reglas(fourth="no")),(reglas(fifth="si")))
    def m6(self):
        result = 'Es recomendable siente contar con un control mensual sobre su salud para revisicion periodica y descartar posibles enfermedades hereditarias.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="si")),(reglas(third="no")),(reglas(fourth="no")),(reglas(fifth="no")))
    def m7(self):
        result = 'Si maneja antecedentes se le recomienda seguir al pie de la letra las indicaciones suministradas por el doctor ademas de tomar los medicamentos en sus tiempos.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="no")),(reglas(third="si")),(reglas(fourth="no")),(reglas(fifth="no")))
    def m8(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)
    
    @Rule(AND(reglas(first="si")),(reglas(second="no")),(reglas(third="no")),(reglas(fourth="si")),(reglas(fifth="no")))
    def m9(self):
        result = 'Se recomienda acudir con su medico de cabecera para una valoración a nivel pulmonar.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="no")),(reglas(third="no")),(reglas(fourth="no")),(reglas(fifth="si")))
    def m10(self):
        result = 'Es recomendable siente contar con un control mensual sobre su salud para revisicion periodica y descartar posibles enfermedades hereditarias.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="si")),(reglas(third="si")),(reglas(fourth="no")),(reglas(fifth="no")))
    def m11(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="si")),(reglas(third="no")),(reglas(fourth="si")),(reglas(fifth="no")))
    def m12(self):
        result = 'Si maneja antecedentes se le recomienda seguir al pie de la letra las indicaciones suministradas por el doctor ademas de tomar los medicamentos en sus tiempos.'
        print(result)
        self.responses.addResponse(result)
    
    @Rule(AND(reglas(first="no")),(reglas(second="si")),(reglas(third="no")),(reglas(fourth="no")),(reglas(fifth="si")))
    def m13(self):
        result = 'Es recomendable siente contar con un control mensual sobre su salud para revisicion periodica y descartar posibles enfermedades hereditarias.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="no")),(reglas(third="si")),(reglas(fourth="si")),(reglas(fifth="no")))
    def m14(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="no")),(reglas(third="si")),(reglas(fourth="no")),(reglas(fifth="si")))
    def m15(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="no")),(reglas(third="no")),(reglas(fourth="si")),(reglas(fifth="si")))
    def m16(self):
        result = 'Por favor ser mas claro ya que no seleccionado ningun sintoma.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),AND(reglas(second="si")),AND(reglas(third="si")),AND(reglas(fourth="si")),AND(reglas(fifth="si")))
    def m17(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="no")),(reglas(third="si")),(reglas(fourth="no")),(reglas(fifth="si")))
    def m18(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="si")),(reglas(third="si")),(reglas(fourth="no")),(reglas(fifth="no")))
    def m19(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="no")),(reglas(third="no")),(reglas(fourth="si")),(reglas(fifth="si")))
    def m20(self):
        result = 'Es recomendable siente contar con un control mensual sobre su salud para revisicion periodica y descartar posibles enfermedades hereditarias.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="no")),(reglas(third="si")),(reglas(fourth="si")),(reglas(fifth="no")))
    def m21(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="no")),(reglas(third="si")),(reglas(fourth="si")),(reglas(fifth="si")))
    def m22(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="si")),(reglas(third="si")),(reglas(fourth="si")),(reglas(fifth="no")))
    def m23(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="si")),(reglas(third="si")),(reglas(fourth="no")),(reglas(fifth="si")))
    def m24(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)


    @Rule(AND(reglas(first="si")),(reglas(second="si")),(reglas(third="no")),(reglas(fourth="no")),(reglas(fifth="si")))
    def m25(self):
        result = 'Si maneja antecedentes se le recomienda seguir al pie de la letra las indicaciones suministradas por el doctor ademas de tomar los medicamentos en sus tiempos.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="si")),(reglas(third="si")),(reglas(fourth="si")),(reglas(fifth="no")))
    def m26(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="no")),(reglas(second="si")),(reglas(third="si")),(reglas(fourth="si")),(reglas(fifth="si")))
    def m27(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="no")),(reglas(third="si")),(reglas(fourth="si")),(reglas(fifth="si")))
    def m28(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="si")),(reglas(third="no")),(reglas(fourth="si")),(reglas(fifth="si")))
    def m29(self):
        result = 'Se le comienda tomar reposo si los sintomas continuan aun habiendo consumido medicamentos acercarse a su centro de salud mas cercano.'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="si")),(reglas(third="si")),(reglas(fourth="no")),(reglas(fifth="si")))
    def m30(self):
        result = 'Ante este signo de alarma debe acudir inmediatamente a su centro de salud mas cercano para realizar los examenes pertinentes'
        print(result)
        self.responses.addResponse(result)

    @Rule(AND(reglas(first="si")),(reglas(second="si")),(reglas(third="no")),(reglas(fourth="si")),(reglas(fifth="no")))
    def m31(self):
        result = 'Se recomienda tomar reposo si persisten los sintomas acercase al centro de salud mas cercano'
        print(result)
        self.responses.addResponse(result)
        
    @Rule(AND(reglas(first="no")),(reglas(second="si")),(reglas(third="no")),(reglas(fourth="no")),(reglas(fifth="si")))
    def m32(self):
        result = 'Si tiene una recomendación anterior sugerimos seguir con detenimiento las instrucciones de lo contrario agendar cita medica para valoracion.'
        print(result)
        self.responses.addResponse(result)
        


class SBR():
    def __init__(self, data):
        self.responses = Response()
        self.engine = sistemadereglas(self.responses)
        self.data = data
    pass

    def getDiagnostic(self):
        self.engine.reset()
        self.engine.declare(reglas(first=choice([str(self.data['first'])])))
        self.engine.declare(reglas(second=choice([str(self.data['second'])])))
        self.engine.declare(reglas(third=choice([str(self.data['third'])])))
        self.engine.declare(reglas(fourth=choice([str(self.data['fourth'])])))
        self.engine.declare(reglas(fifth=choice([str(self.data['fifth'])])))
        self.engine.run()
        return self.responses.getResponse()
