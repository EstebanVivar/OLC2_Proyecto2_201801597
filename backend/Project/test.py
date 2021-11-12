def compile(self, environment):
        genAux = Generator()
        generator = genAux.getInstance()
    
        continueLbl = generator.newLabel()
        generator.putLabel(continueLbl)

        condition = self.cond.compile(environment)
        newEnv = Environment(environment)

        newEnv.breakLbl = condition.falseLbl
        newEnv.continueLbl = continueLbl

        generator.putLabel(condition.trueLbl)

        self.instr.compile(newEnv)
        generator.addGoto(continueLbl)

        generator.putLabel(condition.falseLbl)


        #     ///////////BACKUP IF////////////

        #      cond =self.condicion.compilar(entorno)
        # etiquetaTrue = cond.etiquetaTrue
        # etiquetaFalse = cond.etiquetaFalse

        # generator.agregarComentario("INSTRUCCIONES SI IF VERDADERO")
        # generator.agregarEtiqueta(etiquetaTrue)
        # if self.instruccionesElse != None:

        #     etiquetaSalida = generator.nuevaEtiqueta()
        #     for instruccion in self.instruccionesIf:
        #         instruccion.compilar(entorno)
        #     generator.agregarGoto(etiquetaSalida)
        # else:
        #     for instruccion in self.instruccionesIf:
        #         instruccion.compilar(entorno)
        # generator.agregarComentario("INSTRUCCIONES SI IF FALSO")

        # generator.agregarEtiqueta(etiquetaFalse)
        # if self.instruccionesElse != None:
        #     if isinstance(self.instruccionesElse, If):
        #         self.instruccionesElse.compilar(entorno)
        #     else:
                # for instruccion in self.instruccionesElse:
                #     instruccion.compilar(entorno)

        #     generator.agregarGoto(etiquetaSalida)
        #     generator.agregarEtiqueta(etiquetaSalida)



struct Persona
    nombre::String;
    edad::Int64;
    numeroFamiliares::Int64;
end;

function RegistrarPersona(nombre::String, edad::Int64, numeroFamiliares::Int64)::Persona
    return Persona(nombre, edad, numeroFamiliares);
end;

function AgregarFamiliar(persona::Persona)::Nothing
    persona.numeroFamiliares = persona.numeroFamiliares + 1;
end;

function ImprimirDatosPersona(persona::Persona)::Nothing
    print("Nombre: ");
    println(persona.nombre);
    print("Edad: ");
    println(persona.edad);
    print("Numero de familiares: ");
    println(persona.numeroFamiliares);
end;

manuel = RegistrarPersona("Manuel", 22, 4);
ImprimirDatosPersona(manuel);
AgregarFamiliar(manuel);
ImprimirDatosPersona(manuel);