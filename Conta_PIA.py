print("**"*50)
print("PRESUPUESTO MAESTRO")
print("**"*50)
print("\t"*4,"Presupuesto de Operación")
print("**"*50)
print("-"*30,"1. Presupuesto de ventas","-"*40)
print("--"*50)
enero= int(input("Ingresa la cantidad de ventas esperadas en Enero: "))
febrero= int(input("Ingresa la cantidad de ventas esperadas en Febrero: "))
marzo= int(input("Ingresa la cantidad de ventas esperadas en Marzo: "))
precioUD= int(input("Ingresa el precio por unidad: "))
print("**"*50)
print("\t"*4,"Primer trimestre")
print("--"*50)
print("\t"*4,"Enero \t\t Febrero \t Marzo \t\t Total Trimestre")
print("--"*50)
Venero= enero*precioUD
Vfebrero= febrero*precioUD
Vmarzo= marzo*precioUD
print(f"Pronostico de ventas \t\t {enero} \t\t {febrero} \t\t {marzo}")
print(f"Precio unitario \t\t ${precioUD} \t\t ${precioUD} \t\t ${precioUD} ")
print(f"Ventas presupuestadas \t\t ${Venero} \t\t ${Vfebrero} \t\t ${Vmarzo} \t\t ${Venero+Vfebrero+Vmarzo}")
print("**"*50)
print("**"*50)
print("-"*30,"2. Presupuesto de producción","-"*40)
print("--"*50)
meses= ["Enero","Febrero","Marzo"]
invenF=list()
invenI=list()
for nombre in meses:
    inF= int(input(f"Ingresa la cantidad del inventario final del producto terminado de {nombre}: "))
    invenF.append(inF)
    print("\n")
for nombre in meses:
    inI= int(input(f"Ingresa la cantidad del inventario inicial del producto terminado de {nombre}: "))
    invenI.append(inI)
    print("\n")
prodENE= enero+invenF[0]-invenI[0]
prodFEB= febrero+invenF[0]-invenI[0]
prodMAR= marzo+invenF[0]-invenI[0]
print("\t"*6,"Enero \t\t Febrero \t Marzo \t\t Total Trimestre")
print("--"*50)
print(f"Pronostico de ventas \t\t\t\t {enero} \t\t {febrero} \t\t {marzo}")
print(f"(+)Inventario final deseado del producto terminado {invenF[0]} \t\t {invenF[1]} \t\t {invenF[2]}")
print(f"(-)Inventario inicial de producto terminado \t {invenI[0]} \t\t {invenI[1]} \t\t {invenI[2]}")
print(f"(=)Producción requerida \t\t\t {prodENE} \t\t {prodFEB} \t\t {prodMAR}")
print("**"*50)
print("**"*50)
print("-"*30,"3. Presupuesto de materias primas","-"*40)
print("--"*50)
print("\t\t\t ENERO")
mpud= int(input("Ingresa la materia prima por unidad: "))
invimp= int(input("Ingresa la cantidad de inventario inicial de materia prima: "))
costomp= int(input("Ingresa el costo de la materia prima: "))
mp= prodENE*mpud
invfmp= mp*0.10
mpreq= mp+invfmp-invimp
comprasENE= mpreq*costomp
invImpres= invimp*costomp
invfinal= invfmp*costomp
print("\n")
print(f"Producción requerida \t\t\t\t\t {prodENE}")
print(f"(X) materia prima X unidad \t\t\t\t {mpud}")
print(f"Materia prima para la producción \t\t\t {mp}")
print(f"(+) Inventario final deseado de materia prima (10%) \t {invfmp}")
print(f"(-)Inventario inicial de materia prima \t\t\t {invimp}")
print(f"(=)Materias primas requeridas \t\t\t\t {mpreq}")
print(f"(X) Costo de materia prima \t\t\t\t {costomp}")
print(f"(=)Compras presupuestadas \t\t\t\t {comprasENE}")
print(f"(=)Inventario inicial de materia prima \t\t\t {invImpres}")
print(f"(=)Inventario final de materia prima \t\t\t {invfinal}")

print("\n")
print("\t\t\t FEBRERO")
mpud= int(input("Ingresa la materia prima por unidad: "))
invimp= int(input("Ingresa la cantidad de inventario inicial de materia prima: "))
costomp= int(input("Ingresa el costo de la materia prima: "))
mp= prodFEB*mpud
invfmp= mp*0.10
mpreq= mp+invfmp-invimp
comprasFEB= mpreq*costomp
invImpres= invimp*costomp
invfinal= invfmp*costomp
print("\n")
print(f"Producción requerida \t\t\t\t\t {prodFEB}")
print(f"(X) materia prima X unidad \t\t\t\t {mpud}")
print(f"Materia prima para la producción \t\t\t {mp}")
print(f"(+) Inventario final deseado de materia prima (10%) \t {invfmp}")
print(f"(-)Inventario inicial de materia prima \t\t\t {invimp}")
print(f"(=)Materias primas requeridas \t\t\t\t {mpreq}")
print(f"(X) Costo de materia prima \t\t\t\t {costomp}")
print(f"(=)Compras presupuestadas \t\t\t\t {comprasFEB}")
print(f"(=)Inventario inicial de materia prima \t\t\t {invImpres}")
print(f"(=)Inventario final de materia prima \t\t\t {invfinal}")

print("\n")
print("\t\t\t MARZO")
mpud= int(input("Ingresa la materia prima por unidad: "))
invimp= int(input("Ingresa la cantidad de inventario inicial de materia prima: "))
costomp= int(input("Ingresa el costo de la materia prima: "))
mp= prodMAR*mpud
invfmp= mp*0.10
mpreq= mp+invfmp-invimp
comprasMAR= mpreq*costomp
invImpres= invimp*costomp
invfinal= invfmp*costomp
print("\n")
print(f"Producción requerida \t\t\t\t\t {prodMAR}")
print(f"(X) materia prima X unidad \t\t\t\t {mpud}")
print(f"Materia prima para la producción \t\t\t {mp}")
print(f"(+) Inventario final deseado de materia prima (10%) \t {invfmp}")
print(f"(-)Inventario inicial de materia prima \t\t\t {invimp}")
print(f"(=)Materias primas requeridas \t\t\t\t {mpreq}")
print(f"(X) Costo de materia prima \t\t\t\t {costomp}")
print(f"(=)Compras presupuestadas \t\t\t\t {comprasMAR}")
print(f"(=)Inventario inicial de materia prima \t\t\t {invImpres}")
print(f"(=)Inventario final de materia prima \t\t\t {invfinal}")
print("**"*50)
print("**"*50)
print("-"*30,"4. Presupuesto de obra de mano directa","-"*40)
print("--"*50)
saldiurno= list()
salvesp= list()
for nombre in meses:
    sal1= int(input(f"Ingresa el salario personal diurno de {nombre}: "))
    saldiurno.append(sal1)
    print("\n")
for nombre in meses:
    sal2= int(input(f"Ingresa el salario personal vespertino de {nombre}: "))
    salvesp.append(sal2)
    print("\n")
saltotal= list()
for n in range(0,3):
    salario= saldiurno[n]+salvesp[n]
    saltotal.append(salario)

print("--"*50)
print("\t"*4,"Enero \t\t Febrero \t Marzo")
print("--"*50)
print(f"Salario personal diurno \t\t {saldiurno[0]} \t\t {saldiurno[1]} \t\t {saldiurno[2]}")
print(f"Salario personal vespertino \t\t {salvesp[0]} \t\t {salvesp[1]} \t\t {salvesp[2]}")
print(f"Total de mano de obra \t\t {saltotal[0]} \t\t {saltotal[1]} \t\t {saltotal[2]}")
print("**"*50)
print("**"*50)
print("-"*30,"5. Presupuesto de gastos indirectos de fabricación","-"*40)
print("--"*50)
dep= int(input("Ingresa cantidad $ de la depreciación: "))
superv= int(input("Ingresa la cantidad $ de la supervisión:"))
seguro= int(input("Ingresa la cantidad $ del seguro: "))
mante= int(input("Ingresa la cantidad $ de mantenimiento: "))
acces= int(input("Ingresa la cantidad $ de accesorios: "))
servicios= int(input("Ingresa la cantidad $ de servicios: "))
horasmaq= int(input("Ingresa la cantidad de horas maquina por unidad: "))
tasagif= int(input("Ingresa la tasa de GIF variable: "))
totalGIF= dep+superv+seguro+mante+acces+servicios

print("--"*50)
print("\t"*4,"Enero \t\t Febrero \t Marzo")
print("--"*50)
print("Gastos indirectos de fabricación fijos:")
print(f"Depreciación \t\t\t {dep} \t\t\t {dep} \t\t\t {dep}")
print(f"Supervisión \t\t\t {superv} \t\t\t {superv} \t\t\t {superv}")
print(f"Seguro \t\t\t {seguro} \t\t\t {seguro} \t\t\t {seguro}")
print(f"Mantenimiento \t\t\t {mante} \t\t\t {mante} \t\t\t {mante}")
print(f"Accesorios \t\t\t {acces} \t\t\t {acces} \t\t\t {acces}")
print(f"Servicios \t\t\t {servicios} \t\t\t {servicios} \t\t\t {servicios}")
print(f"Total de GIF fijos \t\t\t {totalGIF} \t\t\t {totalGIF} \t\t\t {totalGIF}")
horasENE= prodENE*horasmaq
horasFEB= prodFEB*horasmaq
horasMAR= prodMAR*horasmaq
gifV1= horasENE*tasagif
gifV2= horasFEB*tasagif
gifV3= horasMAR*tasagif
giftotal1= totalGIF+gifV1
giftotal2= totalGIF+gifV2
giftotal3= totalGIF+gifV3
print("GIF variables: ")
print(f"Producción requerida \t\t\t {prodENE} \t\t\t {prodFEB} \t\t\t {prodMAR}")
print(f"Horas maquinas por unidad \t\t\t {horasmaq} \t\t\t {horasmaq} \t\t\t {horasmaq}")
print(f"Horas maquinas para la producción \t\t\t {horasENE} \t\t\t {horasFEB} \t\t\t {horasMAR}")
print(f"(X) Tasas de GIF variables \t\t\t {tasagif} \t\t\t {tasagif} \t\t\t {tasagif}")
print(f"(=) GIF variable \t\t\t {gifV1} \t\t\t {gifV2} \t\t\t {gifV3}")
print(f"Total de GIF \t\t\t {giftotal1} \t\t\t {giftotal2} \t\t\t {giftotal3}")
print("**"*50)
print("**"*50)
print("-"*30,"6. Presupuesto de gastos de operación","-"*40)
print("--"*50)
sueldo= int(input("Ingresa el sueldo: "))
publicidad= int(input("Ingresa la cantidad $ en publicidad: "))
accesorio= int(input("Ingresa la cantidad $ en accesorios: "))
depre= int(input("Ingresa la cantidad $ de depreciación: "))
varios= int(input("Ingresa la cantidad $ de varios: "))
porcentaje= int(input("Ingresa el porcentaje sobre ventas: "))
gtsadmin= int(input("Ingresa la cantidad de gastos de admin: "))
gtsvts= int(input("Ingresa la cantidad de gastos de vts: "))
impuesto= int(input("Ingresa el porcentaje de impuestos: "))
total= sueldo+publicidad+accesorio+depre+varios
gastoene= Venero*0.05
gastofeb= Vfebrero*0.05
gastomar= Vmarzo*0.05
gasene= total+gastoene
gasfeb= total+gastofeb
gasmar= total+gastomar
print("--"*50)
print("\t"*4,"Enero \t\t Febrero \t Marzo")
print("--"*50)
print("Gastos de operación fijos: ")
print(f"Sueldo \t\t\t {sueldo} \t\t\t {sueldo} \t\t\t {sueldo}")
print(f"Publicidad \t\t\t {publicidad} \t\t\t {publicidad} \t\t\t {publicidad}")
print(f"Accesorios \t\t\t {accesorio} \t\t\t {accesorio} \t\t\t {accesorio}")
print(f"Depreciación \t\t\t {depre} \t\t\t {depre} \t\t\t {depre}")
print(f"Varios \t\t\t {varios} \t\t\t {varios} \t\t\t {varios}")
print(f"Total \t\t\t {total} \t\t\t {total} \t\t\t {total}")

print("Gastos variables de operación: ")
print(f"Ventas \t\t ${Venero} \t\t ${Vfebrero} \t\t ${Vmarzo} \t\t ${Venero+Vfebrero+Vmarzo}")
print(f"(X) porcentaje sobre ventas \t\t\t {porcentaje} \t\t\t {porcentaje} \t\t\t {porcentaje}")
print(f"Gastos variables de operación \t\t\t {gastoene} \t\t\t {gastofeb} \t\t\t {gastomar}")
print(f"Gastos de operación presupuestado \t\t\t {gasene} \t\t\t {gasfeb} \t\t\t {gasmar}")

print("**"*50)
print("\t"*4,"Presupuesto financiero")
print("**"*50)
print("**"*50)
print("-"*30,"1. Estado de resultado","-"*40)
print("--"*50)
print("--"*50)
print("\t"*4,"Enero \t\t Febrero \t Marzo")
print("--"*50)
print(f"Ventas \t\t ${Venero} \t\t ${Vfebrero} \t\t ${Vmarzo} \t\t ${Venero+Vfebrero+Vmarzo}")
print(f"(-)costos de vts \t\t\t {comprasENE} \t\t\t {comprasFEB} \t\t\t {comprasMAR}")
utbruta1= Venero-comprasENE
utbruta2= Vfebrero-comprasFEB
utbruta3= Vmarzo-comprasMAR
print(f"(=)ut. bruta \t\t\t {utbruta1} \t\t\t {utbruta2} \t\t\t {utbruta3}")
print(f"(-)gts adm \t\t\t {gtsadmin} \t\t\t {gtsadmin} \t\t\t {gtsadmin}")
print(f"(-)gts vts \t\t\t {gtsvts} \t\t\t {gtsvts} \t\t\t {gtsvts}")
depreciacion= depre+dep
print(f"(-)depreciación \t\t\t {depreciacion} \t\t\t {depreciacion} \t\t\t {depreciacion}")
utop1= utbruta1-gtsadmin-gtsvts-depreciacion
utop2= utbruta2-gtsadmin-gtsvts-depreciacion
utop3= utbruta3-gtsadmin-gtsvts-depreciacion
print(f"(=)ut.op \t\t\t {utop1} \t\t\t {utop2} \t\t\t {utop3}")
print(f"(=)ut.antes impts \t\t\t {utop1} \t\t\t {utop2} \t\t\t {utop3}")
imp1= utop1*(impuesto/100)
imp2= utop2*(impuesto/100)
imp3= utop3*(impuesto/100)
print(f"(-)impts \t\t\t {imp1}% \t\t\t {imp2}% \t\t\t {imp3}%")
utneta1= utop1-imp1
utneta2= utop2-imp2
utneta3= utop3-imp3
print(f"(=)ut.neta \t\t\t {utneta1} \t\t\t {utneta2} \t\t\t {utneta3}")
print("**"*50)
print("**"*50)
print("-"*30,"2. Flujo efectivo","-"*40)
print("--"*50)
print("--"*50)
saldoinicial= int(input("Ingresa el saldo inicial de efectivo: "))
cobranza= int(input("Ingresa la cantidad cobrada: "))
print(f"Saldo Inicial de efectivo \t\t\t {saldoinicial}")
print("Entradas: ")
print(f"Cobranza \t\t\t {cobranza}")
totalentrada= saldoinicial+cobranza
print(f"Total entradas \t\t\t {totalentrada}")

print("Salidas: ")
manoobra= saltotal[0]+saltotal[1]+saltotal[2]
print(f"Mano de obra \t\t\t {manoobra}")
gtsop= gasene+gasfeb+gasmar
print(f"Gts op \t\t\t {gtsop}")
GIF= giftotal1+giftotal2+giftotal3
print(f"GIF \t\t\t {GIF}")
totalsalida= manoobra+gtsop+GIF
print(f"Total salidas \t\t\t {totalsalida}")
flujo= totalentrada-totalsalida
print(f"Flujo efectivo \t\t\t {flujo}")

print("**"*50)
print("**"*50)
print("-"*30,"3. Balance General","-"*40)
print("--"*50)
print("--"*50)
efec= int(input("Ingresa la cantidad $ de efectivo: "))
cliente= int(input("Ingresa la cantidad $ de clientes: "))
Invmaterial= int(input("Ingresa la cantidad $ de inv. material: "))
prodterminado= int(input("Ingresa la cantidad $ de inv. prod terminado: "))
prodterminado= int(input("Ingresa la cantidad $ de inv. prod terminado: "))
terreno= int(input("Ingresa la cantidad $ de terreno: "))
planta= int(input("Ingresa la cantidad $ de planta: "))
depp= int(input("Ingresa la cantidad $ de depreciación: ")) 
prove= int(input("Ingresa la cantidad $ de proveedores: ")) 
docpagar= int(input("Ingresa la cantidad $ de documentos por pagar: ")) 
obli= int(input("Ingresa la cantidad $ de obligaciones por pagar: ")) 
capital= int(input("Ingresa la cantidad $ de capital contable: ")) 
totalactivo= efec+cliente+Invmaterial+prodterminado
totalnocirculante= terreno+planta+depp
totales= totalactivo+totalnocirculante
pasivocircu= prove+docpagar
totalpasivo= pasivocircu+obli
capitaltotal= capital+totalpasivo
print("Activos circulantes: ")
print(f"Efectivo \t\t {efec}")
print(f"Clientes \t\t {cliente}")
print(f"Inv. material \t\t {Invmaterial}")
print(f"Inv. producto terminado \t\t {prodterminado}")
print(f"Total activos \t\t {totalactivo}")

print("Activo no circulante")
print(f"Terreno \t\t {terreno}")
print(f"Planta \t\t {planta}")
print(f"Depreciación \t\t {depp}")
print(f"Total activo no circulante \t\t {totalnocirculante}")
print(f"Total de activo \t\t {totales}")

print("Pasivo circulante")
print(f"Proveedores \t\t {prove}")
print(f"Documentos por pagar \t\t {docpagar}")
print(f"Total pasivo circulante \t\t {pasivocircu}")
print(f"Obligaciones por pagar \t\t {obli}")
print(f"Total pasivo \t\t {totalpasivo}")

print(f"Capital contable \t\t {capital}")
print("Pasivo + capital")
print(f"Total capital contable \t\t {capitaltotal} = {totales}")
