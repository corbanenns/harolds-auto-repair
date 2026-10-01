#!/usr/bin/env python3
"""Generates src/pages/services/*.html and src/pages/es/services/*.html plus the
two overview pages from the data below. Run before build.py when service copy changes."""
import json, pathlib
HERE = pathlib.Path(__file__).parent / "pages"

S = [
 dict(slug="oil-change-maintenance", img="oil-change.jpg", book="oil-change",
  en=dict(name="Oil Change & Scheduled Maintenance", short="Oil Change & Maintenance",
   title="Oil Change & Scheduled Maintenance in West Salem | Harold's",
   desc="Full-synthetic oil changes with a digital inspection every time, plus factory 30/60/90k scheduled maintenance for all makes. Book online at Harold's in West Salem.",
   h1="Oil changes with a second set of eyes.",
   lead="Every oil change at Harold's includes a digital multi-point inspection with photos texted to you. It's the cheapest insurance your car can get.",
   points=["Full-synthetic, synthetic blend and conventional oil to manufacturer spec","OEM-quality filters, drain plug gasket and reset of the maintenance light","Digital inspection: brakes, tires, fluids, belts, battery, with photos","Fluid top-offs and tire pressure set","30k / 60k / 90k factory-schedule services for Subaru, Toyota, Honda, Ford, GM, Nissan, Mazda, Hyundai/Kia and European makes","Timing belts, spark plugs, transmission and coolant services done on schedule, not by guesswork"],
   faq=[("How long does an oil change take?","Usually 45 minutes to an hour including the inspection. You're welcome to wait, or drop off and we'll text you when it's ready."),("Do you use the oil my manufacturer specifies?","Yes. We match the viscosity and spec in your owner's manual, including European long-life oils."),("What's a 60k service?","The bundle of items your manufacturer calls for around 60,000 miles: typically fluids, filters, spark plugs on some engines, and a thorough inspection. We quote it from the factory schedule for your exact vehicle and skip anything already done.")]),
  es=dict(name="Cambio de aceite y mantenimiento programado", short="Cambio de aceite y mantenimiento",
   title="Cambio de aceite y mantenimiento en West Salem | Harold's",
   desc="Cambios de aceite sintético con inspección digital en cada visita, más el mantenimiento de fábrica de 30/60/90 mil millas para todas las marcas. Reserve en línea en Harold's, West Salem.",
   h1="Cambios de aceite con un segundo par de ojos.",
   lead="Cada cambio de aceite en Harold's incluye una inspección digital multipunto con fotos enviadas a su teléfono. Es el seguro más barato que su auto puede tener.",
   points=["Aceite sintético, semisintético o convencional según la especificación del fabricante","Filtros de calidad OEM, empaque del tapón y reinicio de la luz de mantenimiento","Inspección digital: frenos, llantas, fluidos, bandas, batería, con fotos","Relleno de fluidos y ajuste de presión de llantas","Servicios de 30 / 60 / 90 mil millas según el programa de fábrica para Subaru, Toyota, Honda, Ford, GM, Nissan, Mazda, Hyundai/Kia y marcas europeas","Bandas de tiempo, bujías, transmisión y refrigerante a tiempo, no a ojo"],
   faq=[("¿Cuánto tarda un cambio de aceite?","Normalmente de 45 minutos a una hora, incluida la inspección. Puede esperar o dejar el auto y le enviamos un texto cuando esté listo."),("¿Usan el aceite que indica mi fabricante?","Sí. Usamos la viscosidad y especificación de su manual, incluidos los aceites europeos de larga duración."),("¿Qué es el servicio de 60 mil?","El conjunto de trabajos que su fabricante indica alrededor de las 60,000 millas: fluidos, filtros, bujías en algunos motores y una inspección completa. Lo cotizamos según el programa de fábrica de su vehículo y omitimos lo que ya se hizo.")])),
 dict(slug="brakes", img="brakes.jpg", book="brakes",
  en=dict(name="Brake Repair & Service", short="Brake Service",
   title="Brake Repair in West Salem | Pads, Rotors, Calipers | Harold's",
   desc="Brake pads, rotors, calipers, fluid flushes and ABS repair in West Salem. Measured in millimeters, shown in photos, backed by a 1 year / 12,000 mile warranty.",
   h1="Brakes, measured and shown. Not guessed.",
   lead="We measure your pads in millimeters and photograph the rotors, so you can see exactly why we're recommending what we're recommending. Or why we're telling you it can wait.",
   points=["Pads, rotors, calipers, hoses and hardware","Brake fluid flush and bleed","ABS and brake warning light diagnosis","Grinding, squealing, pulsing pedal and pulling to one side","Parking brake repair","Quality parts with a 1 year / 12,000 mile warranty"],
   faq=[("How do I know if I need brakes?","Squealing, grinding, a pulsing pedal, a longer stop or a brake warning light. Or ask us at your next oil change; pad thickness is on every inspection."),("Pads only, or pads and rotors?","It depends on rotor thickness and condition, which we measure. If the rotors are within spec and true, we'll tell you pads alone are fine."),("Can I bring my own parts?","We install parts we source so we can warranty the job. We'll match quality to your budget.")]),
  es=dict(name="Reparación y servicio de frenos", short="Frenos",
   title="Reparación de frenos en West Salem | Balatas, discos, calipers | Harold's",
   desc="Balatas, discos, calipers, purga de líquido y reparación de ABS en West Salem. Medido en milímetros, mostrado en fotos, con garantía de 1 año / 12,000 millas.",
   h1="Frenos medidos y mostrados. No adivinados.",
   lead="Medimos sus balatas en milímetros y fotografiamos los discos, para que vea exactamente por qué recomendamos lo que recomendamos. O por qué le decimos que puede esperar.",
   points=["Balatas, discos, calipers, mangueras y herrajes","Purga y cambio de líquido de frenos","Diagnóstico de ABS y luz de advertencia de frenos","Rechinidos, vibración en el pedal y jalón hacia un lado","Reparación del freno de mano","Refacciones de calidad con garantía de 1 año / 12,000 millas"],
   faq=[("¿Cómo sé si necesito frenos?","Rechinidos, pedal que vibra, frenado más largo o una luz de advertencia. O pregúntenos en su próximo cambio de aceite; el grosor de las balatas está en cada inspección."),("¿Solo balatas, o balatas y discos?","Depende del grosor y estado de los discos, que medimos. Si están dentro de especificación, le diremos que con balatas basta."),("¿Puedo traer mis propias refacciones?","Instalamos refacciones que nosotros conseguimos para poder garantizar el trabajo. Ajustamos la calidad a su presupuesto.")])),
 dict(slug="tires-alignment", img="tires.jpg", book="tires",
  en=dict(name="Tires & Wheel Alignment", short="Tires & Alignment",
   title="Tires & Wheel Alignment in West Salem | Harold's Quality Auto Repair",
   desc="New tires, rotation, balancing, flat repair, TPMS and computerized four-wheel alignment in West Salem. Tread depth photographed on every inspection.",
   h1="Tires and alignment, with the numbers to back it up.",
   lead="Tread depth on all four tires is part of every inspection, so you'll never be surprised by a bald tire. When it's time, we'll quote tires that fit how and where you drive.",
   points=["New tires for cars, SUVs, light trucks and vans, most major brands","Mounting, balancing and TPMS sensor service","Rotation and flat repair","Computerized four-wheel alignment with before/after printout","Pulling, uneven wear, vibration and steering-wheel-off-center diagnosis","Suspension and steering repair that often goes with alignment"],
   faq=[("How often should I align?","Any time you install new tires, after hitting a serious pothole or curb, or if the car pulls or the wheel sits off-center. Annually is a good habit in Oregon."),("Do you sell tires?","Yes. Tell us how you drive and we'll quote options at a few price points. We can usually have them the next day."),("Do you fix flats?","Yes, if the puncture is in the repairable area of the tread. We'll show you a photo if it isn't.")]),
  es=dict(name="Llantas y alineación", short="Llantas y alineación",
   title="Llantas y alineación en West Salem | Harold's Quality Auto Repair",
   desc="Llantas nuevas, rotación, balanceo, reparación de ponchaduras, TPMS y alineación computarizada de cuatro ruedas en West Salem.",
   h1="Llantas y alineación, con números que lo respaldan.",
   lead="La profundidad del dibujo de las cuatro llantas es parte de cada inspección, así que nunca le sorprenderá una llanta lisa. Cuando sea el momento, le cotizamos llantas según cómo y dónde maneja.",
   points=["Llantas nuevas para autos, SUV, camionetas y vans, de las principales marcas","Montaje, balanceo y servicio de sensores TPMS","Rotación y reparación de ponchaduras","Alineación computarizada de cuatro ruedas con impresión de antes y después","Diagnóstico de jalón, desgaste disparejo, vibración y volante descentrado","Reparación de suspensión y dirección, que suele ir con la alineación"],
   faq=[("¿Cada cuánto debo alinear?","Cada vez que instale llantas nuevas, después de un bache o banqueta fuerte, o si el auto jala o el volante queda chueco. Una vez al año es buena costumbre en Oregón."),("¿Venden llantas?","Sí. Díganos cómo maneja y le cotizamos opciones en varios precios. Normalmente las tenemos al día siguiente."),("¿Reparan ponchaduras?","Sí, si la perforación está en la zona reparable del dibujo. Si no, le mostramos una foto.")])),
 dict(slug="diagnostics", img="inspection.jpg", book="check-engine",
  en=dict(name="Check Engine Light & Diagnostics", short="Check Engine & Diagnostics",
   title="Check Engine Light Diagnostics in West Salem | Harold's",
   desc="Check engine light, electrical, drivability and no-start diagnostics in West Salem with factory-level scan tools and ASE Master technicians who read the data, not just the code.",
   h1="A code tells you where to look. We find out why.",
   lead="Anyone can read a trouble code. Diagnosing the actual cause takes factory-level tools, wiring diagrams and a technician who's seen it before. That's what you're paying for, and it's cheaper than replacing parts on a guess.",
   points=["Check engine, ABS, airbag, traction and transmission warning lights","Factory-level scan tools for domestic, Asian and European makes","Drivability: misfires, stalling, rough idle, poor mileage, hesitation","No-start and intermittent electrical problems","Oil, coolant and vacuum leak pinpointing","Pre-purchase inspections before you buy a used car"],
   faq=[("How much is a diagnostic?","We charge a flat diagnostic fee that covers the testing time to find the cause. You'll get the result, the evidence and a written estimate before any repair."),("My light is on but the car drives fine. Is it urgent?","A steady light usually isn't an emergency but shouldn't be ignored; a flashing light means stop driving and call us. Either way, we'll tell you straight."),("Can you just clear the code?","We can, but it will come back if the cause isn't fixed, and clearing it erases the data we need to diagnose it.")]),
  es=dict(name="Luz de check engine y diagnóstico", short="Check engine y diagnóstico",
   title="Diagnóstico de check engine en West Salem | Harold's",
   desc="Diagnóstico de check engine, sistema eléctrico, fallas de manejo y no arranque en West Salem, con escáneres de nivel de fábrica y técnicos ASE Master que leen los datos, no solo el código.",
   h1="Un código dice dónde buscar. Nosotros averiguamos por qué.",
   lead="Cualquiera puede leer un código de falla. Diagnosticar la causa real requiere herramientas de nivel de fábrica, diagramas eléctricos y un técnico que ya lo ha visto antes. Eso es lo que paga, y sale más barato que cambiar piezas a ciegas.",
   points=["Luces de check engine, ABS, bolsas de aire, tracción y transmisión","Escáneres de nivel de fábrica para marcas americanas, asiáticas y europeas","Fallas de manejo: fallos de encendido, se apaga, ralentí irregular, mal rendimiento, titubeo","Problemas de no arranque y eléctricos intermitentes","Localización de fugas de aceite, refrigerante y vacío","Inspección antes de comprar un auto usado"],
   faq=[("¿Cuánto cuesta el diagnóstico?","Cobramos una tarifa fija de diagnóstico que cubre el tiempo de pruebas para encontrar la causa. Recibe el resultado, la evidencia y un presupuesto por escrito antes de cualquier reparación."),("La luz está encendida pero el auto anda bien. ¿Es urgente?","Una luz fija normalmente no es emergencia pero no debe ignorarse; una luz parpadeando significa deje de manejar y llámenos. En cualquier caso, le hablamos claro."),("¿Pueden solo borrar el código?","Podemos, pero volverá si no se corrige la causa, y borrarlo elimina los datos que necesitamos para el diagnóstico.")])),
 dict(slug="engine-transmission", img="engine-belts.jpg", book="diagnostic",
  en=dict(name="Engine & Transmission Repair", short="Engine & Transmission",
   title="Engine & Transmission Repair in West Salem | Harold's Quality Auto Repair",
   desc="Engine repair, head gaskets, timing, engine replacement and automatic/manual transmission service and replacement in West Salem. 11 bays, ASE Master technicians, 1 year / 12,000 mile warranty.",
   h1="The big jobs, done right the first time.",
   lead="Head gaskets, timing chains, transmission rebuilds and full engine replacements. We diagnose before we quote, show you what we found, and back the work with our warranty.",
   points=["Head gaskets, timing belts and chains, valve cover and oil leaks","Engine replacement with new, remanufactured or quality used engines","Automatic transmission service, repair and replacement","Manual transmission and clutch replacement","Transfer case, differential and CV axle service","Cooling system: radiators, water pumps, thermostats, hoses"],
   faq=[("Is it worth fixing, or should I replace the car?","We'll give you an honest answer with the numbers: repair cost, the rest of the car's condition from the inspection, and what it's likely worth. Sometimes the answer is no, and we'll say so."),("Do you offer financing on big repairs?","Yes, through our payment partner. Ask before you approve the estimate. See <a href='/about#financing'>financing</a>."),("How long will my car be down?","Depends on parts availability. We'll give you a realistic timeline up front and text you if it changes.")]),
  es=dict(name="Reparación de motor y transmisión", short="Motor y transmisión",
   title="Reparación de motor y transmisión en West Salem | Harold's",
   desc="Reparación de motor, juntas de cabeza, tiempo, reemplazo de motor y servicio o reemplazo de transmisión automática y manual en West Salem. 11 bahías, técnicos ASE Master, garantía de 1 año / 12,000 millas.",
   h1="Los trabajos grandes, bien hechos a la primera.",
   lead="Juntas de cabeza, cadenas de tiempo, reconstrucción de transmisiones y reemplazo completo de motor. Diagnosticamos antes de cotizar, le mostramos lo que encontramos y respaldamos el trabajo con nuestra garantía.",
   points=["Juntas de cabeza, bandas y cadenas de tiempo, fugas de aceite y tapa de válvulas","Reemplazo de motor con motores nuevos, remanufacturados o usados de calidad","Servicio, reparación y reemplazo de transmisión automática","Transmisión manual y reemplazo de clutch","Caja de transferencia, diferencial y flechas CV","Sistema de enfriamiento: radiadores, bombas de agua, termostatos, mangueras"],
   faq=[("¿Vale la pena repararlo o mejor cambio de auto?","Le damos una respuesta honesta con números: costo de la reparación, el estado del resto del auto según la inspección y su valor aproximado. A veces la respuesta es no, y se lo diremos."),("¿Ofrecen financiamiento en reparaciones grandes?","Sí, a través de nuestro socio de pagos. Pregunte antes de aprobar el presupuesto. Vea <a href='/es/about#financing'>financiamiento</a>."),("¿Cuánto tiempo estará mi auto en el taller?","Depende de la disponibilidad de refacciones. Le damos un plazo realista desde el principio y le avisamos por texto si cambia.")])),
 dict(slug="ac-heating", img="engine-bay.jpg", book="ac",
  en=dict(name="A/C & Heating Service", short="A/C & Heating",
   title="Car A/C Repair & Heating Service in West Salem | Harold's",
   desc="Air conditioning recharge, leak detection, compressor and heater core repair in West Salem. R-134a and R-1234yf systems. Book online at Harold's.",
   h1="Cold in August. Warm in January.",
   lead="A/C that blows warm usually means a leak, and recharging without finding it just means paying again next summer. We find the leak, fix it, then recharge to spec.",
   points=["A/C performance test and refrigerant leak detection with dye and electronic sniffer","Evacuate and recharge, R-134a and newer R-1234yf systems","Compressors, condensers, evaporators, expansion valves and hoses","Heater cores, blower motors, blend doors and climate control electronics","Cabin air filter replacement","Cooling system service that keeps the heater working"],
   faq=[("Can you just top off my A/C?","We can recharge, but we'll test for leaks first and tell you what we find. A system that's low has a leak somewhere."),("Why does my heater only work when I'm driving?","Often low coolant or a failing water pump or thermostat. It's worth checking soon, since the same problem can overheat the engine."),("Do you service the new refrigerant?","Yes. We're equipped for R-1234yf, which most vehicles built after about 2017 use.")]),
  es=dict(name="Aire acondicionado y calefacción", short="Aire acondicionado y calefacción",
   title="Reparación de aire acondicionado y calefacción en West Salem | Harold's",
   desc="Recarga de aire acondicionado, detección de fugas, compresores y radiador de calefacción en West Salem. Sistemas R-134a y R-1234yf. Reserve en línea en Harold's.",
   h1="Frío en agosto. Calor en enero.",
   lead="Un aire acondicionado que sopla caliente casi siempre tiene una fuga, y recargarlo sin encontrarla solo significa volver a pagar el próximo verano. Encontramos la fuga, la reparamos y recargamos a especificación.",
   points=["Prueba de rendimiento del A/C y detección de fugas con tinte y detector electrónico","Vacío y recarga, sistemas R-134a y los nuevos R-1234yf","Compresores, condensadores, evaporadores, válvulas de expansión y mangueras","Radiadores de calefacción, motores de ventilador, compuertas y electrónica del clima","Cambio de filtro de cabina","Servicio del sistema de enfriamiento que mantiene la calefacción funcionando"],
   faq=[("¿Pueden solo rellenar el gas del A/C?","Podemos recargar, pero primero probamos fugas y le decimos qué encontramos. Un sistema bajo de gas tiene una fuga en algún lado."),("¿Por qué mi calefacción solo funciona cuando voy manejando?","Suele ser refrigerante bajo, o una bomba de agua o termostato fallando. Conviene revisarlo pronto, porque el mismo problema puede sobrecalentar el motor."),("¿Dan servicio al refrigerante nuevo?","Sí. Estamos equipados para R-1234yf, que usan la mayoría de los vehículos fabricados después de 2017.")])),
 dict(slug="exhaust", img="exhaust.jpg", book="exhaust",
  en=dict(name="Custom Exhaust & Muffler Repair", short="Custom Exhaust",
   title="Custom Exhaust & Muffler Repair in West Salem | Harold's",
   desc="In-house exhaust bending and welding in West Salem. Muffler and pipe repair, catalytic converters, cat-back systems and custom exhaust for cars and trucks.",
   h1="Bent and welded in-house.",
   lead="Most shops bolt on whatever fits. We have our own pipe bender and welding bay, which means repairs that fit right and custom systems built for your vehicle.",
   points=["Muffler, resonator and pipe repair and replacement","Catalytic converter replacement, including Oregon-compliant units","Custom-bent cat-back and dual exhaust systems","Exhaust leaks, rattles and heat shield repair","Manifold and flex pipe repair","Lifted trucks, classic cars and project vehicles welcome"],
   faq=[("Why does my car sound louder all of a sudden?","Usually a rusted-through pipe or a cracked flex joint. It's often a small weld repair rather than a whole new system. We'll show you a photo."),("Can you make it sound a certain way?","Yes. Tell us what you're after, deeper tone, quieter, or a specific muffler brand, and we'll build it."),("Catalytic converter was stolen. Can you help?","Yes, and we can add a shield to make it harder next time. We'll help with the insurance paperwork.")]),
  es=dict(name="Escape a medida y reparación de mofles", short="Escape a medida",
   title="Escape a medida y reparación de mofles en West Salem | Harold's",
   desc="Doblado y soldadura de escape en nuestro propio taller en West Salem. Reparación de mofles y tubos, convertidores catalíticos, sistemas cat-back y escapes a medida para autos y camionetas.",
   h1="Doblado y soldado en nuestro taller.",
   lead="Muchos talleres atornillan lo que quede. Nosotros tenemos nuestra propia dobladora de tubo y bahía de soldadura, lo que significa reparaciones que ajustan bien y sistemas a medida para su vehículo.",
   points=["Reparación y reemplazo de mofles, resonadores y tubos","Reemplazo de convertidor catalítico, incluidas unidades aprobadas para Oregón","Sistemas cat-back y escapes dobles doblados a medida","Fugas de escape, ruidos y reparación de protectores de calor","Reparación de múltiple y tubo flexible","Bienvenidas las camionetas levantadas, autos clásicos y proyectos"],
   faq=[("¿Por qué mi auto suena más fuerte de repente?","Normalmente un tubo oxidado o una junta flexible rota. Suele ser una soldadura pequeña y no un sistema nuevo. Le mostramos una foto."),("¿Pueden hacer que suene de cierta forma?","Sí. Díganos qué busca, un tono más grave, más silencioso o una marca de mofle en particular, y lo construimos."),("Me robaron el convertidor catalítico. ¿Pueden ayudar?","Sí, y podemos agregar una protección para que sea más difícil la próxima vez. Le ayudamos con el papeleo del seguro.")])),
 dict(slug="marine", img="shop-interior.jpg", book="marine",
  en=dict(name="Marine & Boat Motor Service", short="Marine & Boat Motors",
   title="Boat Motor & Marine Engine Service in Salem, OR | Harold's",
   desc="Inboard and outboard boat motor service, winterization and repair in West Salem. Trailer your boat to Harold's and get the same digital inspection and warranty.",
   h1="Boat motors, too.",
   lead="One of the few shops in the Salem area that works on marine engines. Trailer it in and get the same photo inspection, straight answers and warranty as your truck.",
   points=["Inboard and sterndrive engine service and repair","Outboard motor tune-ups and repair","Winterization and spring de-winterization","Fuel system, cooling system and electrical diagnosis","Impellers, belts, plugs and lower-unit service","Trailer bearings and lights while it's here"],
   faq=[("Do I bring the boat on the trailer?","Yes. We work on trailered boats in the shop. Call ahead so we can plan the space."),("When should I winterize?","Before the first hard freeze, usually by late October in the valley. Book early; spots fill fast."),("Do you work on jet skis or ATVs?","Ask. We take some powersports work depending on the engine and season.")]),
  es=dict(name="Motores marinos y de lancha", short="Motores marinos",
   title="Servicio de motores de lancha y marinos en Salem, OR | Harold's",
   desc="Servicio, invernaje y reparación de motores de lancha fuera de borda e interiores en West Salem. Traiga su lancha en remolque a Harold's y reciba la misma inspección digital y garantía.",
   h1="También motores de lancha.",
   lead="Uno de los pocos talleres de la zona de Salem que trabaja motores marinos. Tráigala en remolque y reciba la misma inspección con fotos, respuestas claras y garantía que su camioneta.",
   points=["Servicio y reparación de motores interiores y sterndrive","Afinación y reparación de motores fuera de borda","Invernaje y preparación de primavera","Diagnóstico de sistema de combustible, enfriamiento y eléctrico","Impulsores, bandas, bujías y servicio de unidad inferior","Baleros y luces del remolque mientras está aquí"],
   faq=[("¿Traigo la lancha en el remolque?","Sí. Trabajamos lanchas en remolque dentro del taller. Llame antes para planear el espacio."),("¿Cuándo debo hacer el invernaje?","Antes de la primera helada fuerte, normalmente a finales de octubre en el valle. Reserve con tiempo; los lugares se llenan rápido."),("¿Trabajan motos acuáticas o cuatrimotos?","Pregunte. Tomamos algunos trabajos de powersports según el motor y la temporada.")])),
]

TXT = {
 "en": dict(services="Services", what="What we do", all="All makes and models, import and domestic. Every job backed by our 1 year / 12,000 mile warranty.",
   dvi_h="Included: digital inspection", dvi_p='Your technician photographs anything worn and texts you the report. You approve each item from your phone. <a href="/inspections">See how it works</a>.',
   txt_h="Text updates, pay by phone", txt_p='We text when the car is checked in, when the report is ready and when it\'s done, with a secure pay link. <a href="/pay">After-hours pickup</a> available.',
   faq="Common questions", book="Book", call="Call", p="",
   ov_title="Auto Repair Services in West Salem | Harold's Quality Auto Repair", ov_desc="Full-service auto repair in West Salem: oil changes, brakes, tires and alignment, check engine diagnostics, engine and transmission, A/C, custom exhaust, fleet and marine. All makes and models.",
   ov_eyebrow="Services", ov_h1="Everything your vehicle needs, under one roof.", ov_lead="Import and domestic cars, light trucks, SUVs, fleet vehicles and boat motors. 11 bays, ASE Master Certified technicians, and a digital inspection with every visit.",
   fleet_h="Fleet & Corporate", fleet_p="Priority turnaround, inspection logs per vehicle and monthly invoicing for West Salem businesses.", more="Learn more →",
   makes_h="Makes we see most", makes_p1="Subaru, Toyota, Honda, Ford, Chevrolet and GMC, Ram and Jeep, Nissan, Mazda, Hyundai and Kia, plus BMW, Audi, Volkswagen, Mercedes and Volvo. If it's not on the list, call; it probably is.", makes_p2="Diesel pickups, hybrids and classic cars welcome. We'll tell you up front if a job is outside what we do.",
   unsure_h="Not sure what you need?", unsure_p="Describe the symptom and we'll start with a diagnosis. You'll get the cause, the evidence and a written estimate before anything is repaired.", unsure_btn="Book a diagnostic"),
 "es": dict(services="Servicios", what="Lo que hacemos", all="Todas las marcas y modelos, importados y americanos. Cada trabajo respaldado por nuestra garantía de 1 año / 12,000 millas.",
   dvi_h="Incluido: inspección digital", dvi_p='Su técnico fotografía cualquier desgaste y le envía el reporte por texto. Usted aprueba cada punto desde su teléfono. <a href="/es/inspections">Vea cómo funciona</a>.',
   txt_h="Avisos por texto, pago desde el teléfono", txt_p='Le enviamos un texto cuando recibimos el auto, cuando el reporte está listo y cuando terminamos, con un enlace de pago seguro. <a href="/es/pay">Recogida fuera de horario</a> disponible.',
   faq="Preguntas frecuentes", book="Reservar", call="Llamar", p="/es",
   ov_title="Servicios de taller mecánico en West Salem | Harold's Quality Auto Repair", ov_desc="Taller mecánico completo en West Salem: cambios de aceite, frenos, llantas y alineación, diagnóstico de check engine, motor y transmisión, aire acondicionado, escape a medida, flotillas y motores marinos. Todas las marcas.",
   ov_eyebrow="Servicios", ov_h1="Todo lo que su vehículo necesita, bajo un mismo techo.", ov_lead="Autos importados y americanos, camionetas, SUV, vehículos de flotilla y motores de lancha. 11 bahías, técnicos con certificación ASE Master y una inspección digital en cada visita.",
   fleet_h="Flotillas y empresas", fleet_p="Prioridad en los tiempos, registro de inspecciones por vehículo y facturación mensual para negocios de West Salem.", more="Más información →",
   makes_h="Las marcas que más vemos", makes_p1="Subaru, Toyota, Honda, Ford, Chevrolet y GMC, Ram y Jeep, Nissan, Mazda, Hyundai y Kia, además de BMW, Audi, Volkswagen, Mercedes y Volvo. Si no está en la lista, llame; seguramente sí la trabajamos.", makes_p2="Bienvenidas las pickups diésel, híbridos y autos clásicos. Le decimos desde el principio si un trabajo está fuera de lo que hacemos.",
   unsure_h="¿No sabe qué necesita?", unsure_p="Describa el síntoma y empezamos con un diagnóstico. Recibe la causa, la evidencia y un presupuesto por escrito antes de reparar nada.", unsure_btn="Reservar un diagnóstico"),
}

def write(lang):
    t = TXT[lang]; P = t["p"]
    out = HERE / ("es/services" if lang == "es" else "services"); out.mkdir(parents=True, exist_ok=True)
    for s in S:
        d = s[lang]
        meta = {"title": d["title"], "description": d["desc"], "path": f"{P}/services/{s['slug']}",
                "jsonld": {"@context": "https://schema.org", "@type": "Service", "serviceType": s["en"]["name"], "areaServed": "West Salem, OR",
                           "provider": {"@type": "AutoRepair", "name": "Harold's Quality Auto Repair Inc", "telephone": "+1-503-365-9702",
                                        "address": {"@type": "PostalAddress", "streetAddress": "675 Bartell Dr NW", "addressLocality": "Salem", "addressRegion": "OR", "postalCode": "97304"}}}}
        points = "\n".join(f"        <li>{x}</li>" for x in d["points"])
        faq = "\n".join(f"    <details><summary>{q}</summary><p>{a}</p></details>" for q, a in d["faq"])
        html = f"""<!-- {json.dumps(meta, ensure_ascii=False)} -->
<section class="page-hero has-photo">
  <div class="bg" style="background-image:url(/assets/img/{s['img']})" role="img" aria-label="{d['short']}"></div>
  <div class="container">
    <p class="breadcrumb"><a href="{P}/services">{t['services']}</a> / {d['short']}</p>
    <h1>{d['h1']}</h1>
    <p class="lead">{d['lead']}</p>
    <div class="btn-row" style="margin-top:1.2rem"><a class="btn btn-yellow btn-lg" data-book href="/book?service={s['book']}">{t['book']}: {d['short']}</a><a class="btn btn-outline-light btn-lg" data-tel href="#">{t['call']} <span data-phone></span></a></div>
  </div>
</section>

<section class="section">
  <div class="container split" style="align-items:flex-start">
    <div>
      <h2>{t['what']}</h2>
      <ul class="checks">
{points}
      </ul>
      <p class="muted">{t['all']}</p>
    </div>
    <div>
      <div class="card"><h3>{t['dvi_h']}</h3><p>{t['dvi_p']}</p></div>
      <div class="card" style="margin-top:16px"><h3>{t['txt_h']}</h3><p>{t['txt_p']}</p></div>
    </div>
  </div>
</section>

<section class="section alt">
  <div class="container" style="max-width:820px">
    <h2>{t['faq']}</h2>
{faq}
  </div>
</section>
"""
        (out / f"{s['slug']}.html").write_text(html)
    cards = "\n".join(f"""      <a class="card photo-card" href="{P}/services/{s['slug']}"><img src="/assets/img/{s['img']}" alt="" loading="lazy"><div class="body"><h3>{s[lang]['name']}</h3><p>{s[lang]['lead'].split('. ')[0]}.</p><span class="more">{t['more']}</span></div></a>""" for s in S)
    ov = f"""<!-- {json.dumps({"title": t['ov_title'], "description": t['ov_desc'], "path": f"{P}/services"}, ensure_ascii=False)} -->
<section class="page-hero has-photo">
  <div class="bg" style="background-image:url(/assets/img/lift-work.jpg)" role="img" aria-label=""></div>
  <div class="container">
    <p class="eyebrow">{t['ov_eyebrow']}</p>
    <h1>{t['ov_h1']}</h1>
    <p class="lead">{t['ov_lead']}</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid grid-3">
{cards}
      <a class="card photo-card" href="{P}/fleet"><img src="/assets/img/under-car.jpg" alt="" loading="lazy"><div class="body"><h3>{t['fleet_h']}</h3><p>{t['fleet_p']}</p><span class="more">{t['more']}</span></div></a>
    </div>
  </div>
</section>
<section class="section alt">
  <div class="container split">
    <div>
      <h2>{t['makes_h']}</h2>
      <p>{t['makes_p1']}</p>
      <p>{t['makes_p2']}</p>
    </div>
    <div class="card">
      <h3>{t['unsure_h']}</h3>
      <p>{t['unsure_p']}</p>
      <a class="btn btn-primary" data-book href="/book?service=diagnostic" style="margin-top:1rem">{t['unsure_btn']}</a>
    </div>
  </div>
</section>
"""
    (HERE / ("es/services.html" if lang == "es" else "services.html")).write_text(ov)

for lang in ("en", "es"):
    write(lang)
print("service pages generated (en + es)")
