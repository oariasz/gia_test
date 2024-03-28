
Tasks = [
    {
        'Task': 'Task 1', 
        'Section': 'Reasoning',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you3 have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },
    {
        'Task': 'Task 2', 
        'Section': 'Perceptual Speed',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },    
    {
        'Task': 'Task 3', 
        'Section': 'Number Speed and Accuracy',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },
    {
        'Task': 'Task 43', 
        'Section': 'Word Meaning',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },    
    {
        'Task': 'Task 5', 
        'Section': 'Spatial Visualization',
        'Header1': 'Each question in this section consists of a short statement and a following question.',
        'Header2': 'After you have memorized the statement, click the right arrow [or slied] to reveal the question itself.'
     },    
]

Line2 = 'Work as quickly and accurately ass possible.'
Line3 = 'Good luck!'

# TASK 1
reasoning_pairs = [
    {'Statement': 'Jack es más alto que James', 'Question': '¿Quién es más bajo?', 'Choices': ['Jack', 'James'], 'Answer': 'James'},
    {'Statement': 'Ruth no es tan mayor como Lily', 'Question': '¿Quién es mayor?', 'Choices': ['Ruth', 'Lily'], 'Answer': 'Lily'},
    {'Statement': 'Mark pesa más que David', 'Question': '¿Quién pesa más?', 'Choices': ['David', 'Mark'], 'Answer': 'Mark'},
    {'Statement': 'Emma es más pobre que Bruce', 'Question': '¿Quién es más rico?', 'Choices': ['Bruce', 'Emma'], 'Answer': 'Bruce'},
    {'Statement': 'Lee es más fuerte que Josh', 'Question': '¿Quién es más débil?', 'Choices': ['Josh', 'Lee'], 'Answer': 'Josh'},
    {'Statement': 'Todd no es tan divertido como Matt', 'Question': '¿Quién es más divertido?', 'Choices': ['Todd', 'Matt'], 'Answer': 'Matt'},
    {'Statement': 'Mike no está tan triste como Stacy', 'Question': '¿Quién está más feliz?', 'Choices': ['Stacy', 'Mike'], 'Answer': 'Mike'},
    {'Statement': 'Ron es más inteligente que Joe', 'Question': '¿Quién es menos inteligente?', 'Choices': ['Joe', 'Ron'], 'Answer': 'Joe'},
    {'Statement': 'Alice es más alta que Bob', 'Question': '¿Quién es más bajo?', 'Choices': ['Alice', 'Bob'], 'Answer': 'Bob'},
    {'Statement': 'Sara es mayor que Emily', 'Question': '¿Quién es más joven?', 'Choices': ['Emily', 'Sara'], 'Answer': 'Emily'},
    {'Statement': 'John pesa más que Michael', 'Question': '¿Quién pesa menos?', 'Choices': ['Michael', 'John'], 'Answer': 'Michael'},
    {'Statement': 'Anna es más rica que Kate', 'Question': '¿Quién es más pobre?', 'Choices': ['Kate', 'Anna'], 'Answer': 'Kate'},
    {'Statement': 'Chris es más fuerte que Peter', 'Question': '¿Quién es más débil?', 'Choices': ['Peter', 'Chris'], 'Answer': 'Peter'},
    {'Statement': 'Linda es más divertida que Carol', 'Question': '¿Quién es menos divertida?', 'Choices': ['Carol', 'Linda'], 'Answer': 'Carol'},
    {'Statement': 'Greg está más feliz que Paul', 'Question': '¿Quién está más triste?', 'Choices': ['Paul', 'Greg'], 'Answer': 'Paul'},
    {'Statement': 'Mary es más inteligente que Lisa', 'Question': '¿Quién es menos inteligente?', 'Choices': ['Lisa', 'Mary'], 'Answer': 'Lisa'},
    {'Statement': 'Tom es más alto que Tim', 'Question': '¿Quién es más bajo?', 'Choices': ['Tom', 'Tim'], 'Answer': 'Tim'},
    {'Statement': 'Hannah es mayor que Emma', 'Question': '¿Quién es más joven?', 'Choices': ['Emma', 'Hannah'], 'Answer': 'Emma'},
    {'Statement': 'Richard pesa más que Daniel', 'Question': '¿Quién pesa menos?', 'Choices': ['Daniel', 'Richard'], 'Answer': 'Daniel'},
    {'Statement': 'Sophia es más rica que Olivia', 'Question': '¿Quién es más pobre?', 'Choices': ['Olivia', 'Sophia'], 'Answer': 'Olivia'},
    {'Statement': 'Lucas es más fuerte que Ethan', 'Question': '¿Quién es más débil?', 'Choices': ['Ethan', 'Lucas'], 'Answer': 'Ethan'},
    {'Statement': 'Rachel es más divertida que Jessica', 'Question': '¿Quién es menos divertida?', 'Choices': ['Jessica', 'Rachel'], 'Answer': 'Jessica'},
    {'Statement': 'Ben está más feliz que Andrew', 'Question': '¿Quién está más triste?', 'Choices': ['Andrew', 'Ben'], 'Answer': 'Andrew'},
    {'Statement': 'Grace es más inteligente que Emily', 'Question': '¿Quién es menos inteligente?', 'Choices': ['Emily', 'Grace'], 'Answer': 'Emily'},
    {'Statement': 'Dylan es más alto que Logan', 'Question': '¿Quién es más bajo?', 'Choices': ['Logan', 'Dylan'], 'Answer': 'Logan'},
    {'Statement': 'Madison es mayor que Chloe', 'Question': '¿Quién es más joven?', 'Choices': ['Chloe', 'Madison'], 'Answer': 'Chloe'},
    {'Statement': 'Nathan pesa más que Ethan', 'Question': '¿Quién pesa menos?', 'Choices': ['Ethan', 'Nathan'], 'Answer': 'Ethan'},
    {'Statement': 'Ava es más rica que Mia', 'Question': '¿Quién es más pobre?', 'Choices': ['Mia', 'Ava'], 'Answer': 'Mia'},
    {'Statement': 'Peter no es tan grande como John', 'Question': '¿Quién es más pequeño?', 'Choices': ['Peter', 'John'], 'Answer': 'Peter'},
    {'Statement': 'Alice no es tan alta como Bob', 'Question': '¿Quién es más bajo?', 'Choices': ['Alice', 'Bob'], 'Answer': 'Alice'},
    {'Statement': 'Sara no es tan rápida como Emily', 'Question': '¿Quién es más lenta?', 'Choices': ['Sara', 'Emily'], 'Answer': 'Sara'},
    {'Statement': 'Michael no es tan fuerte como David', 'Question': '¿Quién es más débil?', 'Choices': ['Michael', 'David'], 'Answer': 'Michael'},
    {'Statement': 'Sophia no es tan inteligente como Olivia', 'Question': '¿Quién es menos inteligente?', 'Choices': ['Sophia', 'Olivia'], 'Answer': 'Sophia'},
    {'Statement': 'Ethan no canta tan bien como Lucas', 'Question': '¿Quién canta peor?', 'Choices': ['Ethan', 'Lucas'], 'Answer': 'Ethan'},
    {'Statement': 'Lily no dibuja tan bien como Emma', 'Question': '¿Quién dibuja peor?', 'Choices': ['Lily', 'Emma'], 'Answer': 'Lily'},
    {'Statement': 'Chloe no tiene tanto talento como Madison', 'Question': '¿Quién es más hábil?', 'Choices': ['Madison', 'Chloe'], 'Answer': 'Madison'},
    {'Statement': 'Juan corre más rápido que Tim', 'Question': '¿Quién probablemente ganará la carrera?', 'Choices': ['Juan', 'Tim'], 'Answer': 'Juan'},
    {'Statement': 'Lucia no toca el piano tan bien como Emma', 'Question': '¿Quién es la profesora de piano?', 'Choices': ['Emma', 'Lucia'], 'Answer': 'Emma'},
    {'Statement': 'Peter es más sabio que Daniel', 'Question': '¿Quién es el más tonto?', 'Choices': ['Daniel', 'Peter'], 'Answer': 'Daniel'},
    {'Statement': 'Ernesto es más hablador que Olivia', 'Question': '¿Quién es más reservado?', 'Choices': ['Olivia', 'Ernesto'], 'Answer': 'Olivia'},
    {'Statement': 'Melania baila mejor que Silvia', 'Question': '¿Quién es mala bailarina?', 'Choices': ['Silvia', 'Melania'], 'Answer': 'Silvia'},
]

# TASK 2
perceptual_top = ['E', 'Q', 'D', 'K', 'R', 'P']

synonym_pairs = [
    ['feliz', 'alegre'], ['triste', 'melancólico'], ['grande', 'largo'], ['pequeño', 'diminuto'], ['caliente', 'ardiente'], ['frío', 'congelado'], ['enseñar', 'educar'], ['aprender', 'estudiar'],
    ['romper', 'destrozar'], ['arreglar', 'reparar'], ['día', 'mañana'], ['noche', 'tarde'], ['dar', 'donar'], ['tomar', 'recibir'], ['afilado', 'penetrante'], ['romo', 'despuntado'],
    ['alto', 'talludo'], ['bajo', 'corto'], ['rojo', 'carmesí'], ['azul', 'azul celeste'], ['verde', 'esmeralda'], ['amarillo', 'dorado'], ['negro', 'oscuro'], ['blanco', 'pálido'],
    ['caminar', 'correr'], ['hablar', 'gritar'], ['escribir', 'dibujar'], ['leer', 'mirar'], ['comer', 'beber'], ['pensar', 'reflexionar'], ['perro', 'cachorro'], ['pájaro', 'volar'],
    ['caballo', 'yegua'], ['serpiente', 'víbora'], ['elefante', 'gigante'], ['mono', 'simio'], ['casa', 'edificio'], ['coche', 'vehículo'], ['libro', 'revista'],
    ['mesa', 'escritorio'], ['ordenador', 'computadora portátil'], ['puerta', 'portal'], ['pan', 'barra'], ['queso', 'lácteo'], ['carne', 'carne'], ['verduras', 'vegetales'],
    ['pasta', 'fideos'], ['caramelo', 'dulces'], ['enfadado', 'furioso'], ['asustado', 'aterrado'], ['cansado', 'exhausto'], ['aburrido', 'monótono'], ['orgulloso', 'eufórico'],
    ['celoso', 'envidioso'], ['hablar', 'conversar'], ['susurrar', 'murmurar'], ['brillante', 'luminoso'], ['opaco', 'sin vida'], ['alto', 'escandaloso'], ['tranquilo', 'silencioso'],
    ['fragante', 'aromático'], ['fétido', 'pútrido'], ['pesado', 'pesado'], ['ligero', 'aireado'], ['abundante', 'abundante'], ['escaso', 'raro'], ['victoria', 'triunfo'],
    ['derrota', 'pérdida'], ['esperanza', 'optimismo'], ['desesperación', 'abatimiento'], ['amor', 'afecto'], ['odio', 'aversión'], ['confianza', 'confianza'], ['traición', 'traición']
]

antonym_pairs = [
    ['feliz', 'triste'], ['grande', 'pequeño'], ['caliente', 'frío'], ['largo', 'corto'], ['ancho', 'estrecho'], ['brillante', 'oscuro'], ['áspero', 'suave'], ['mojado', 'seco'],
    ['alto', 'tranquilo'], ['rápido', 'lento'], ['profundo', 'superficial'], ['grueso', 'delgado'], ['pesado', 'ligero'], ['lleno', 'vacío'], ['abierto', 'cerrado'], ['limpio', 'sucio'],
    ['fuerte', 'débil'], ['hermoso', 'feo'], ['rico', 'pobre'], ['joven', 'viejo'], ['activo', 'pasivo'], ['amable', 'cruel'], ['honesto', 'deshonesto'], ['valiente', 'cobarde'],
    ['cuidadoso', 'descuidado'], ['optimista', 'pesimista'], ['generoso', 'egoísta'], ['educado', 'grosero'], ['calmado', 'enfadado'], ['pacífico', 'caótico'], ['saludable', 'enfermo'], ['fresco', 'viejo'],
    ['dulce', 'ácido'], ['amargo', 'dulce'], ['suave', 'duro'], ['liso', 'áspero'], ['flexible', 'rígido'], ['opaco', 'afilado'], ['alto', 'tranquilo'], ['ruidoso', 'silencioso'], ['fragante', 'maloliente'],
    ['atractivo', 'poco atractivo'], ['exitoso', 'fracasado'], ['ganador', 'perdedor'], ['ganar', 'perder'], ['comienzo', 'final'], ['cima', 'fondo'], ['frente', 'espalda'],  ['dentro', 'fuera'],
    ['arriba', 'abajo'], ['hablar', 'escuchar'], ['dar', 'tomar'], ['comprar', 'vender'], ['mostrar', 'ocultar'], ['abrir', 'cerrar'], ['construir', 'destruir'], ['crear', 'destruir'],
    ['empezar', 'terminar'], ['llegar', 'irse'], ['venir', 'ir'], ['día', 'noche'], ['verano', 'invierno'], ['caliente', 'frío'], ['seco', 'húmedo'], ['luz', 'oscuridad'],
    ['amor', 'odio'], ['confianza', 'duda'], ['amigo', 'enemigo'], ['verdad', 'mentira'], ['justicia', 'injusticia'],['libertad', 'encarcelamiento'], ['paz', 'guerra'], ['orden', 'caos'], 
    ['éxito', 'fracaso'], ['victoria', 'derrota'], ['conocimiento', 'ignorancia'], ['sabiduría', 'necedad'], ['lógica', 'emoción'], ['ciencia', 'fe'], ['realidad', 'fantasía'],  ['simple', 'complejo'],
    ['fácil', 'difícil'], ['familiar', 'extraño'], ['famoso', 'desconocido'], ['público', 'privado'], ['abierto', 'secreto'], ['honesto', 'engañoso'], ['claro', 'confuso'], ['confiado', 'inseguro'], 
    ['valiente', 'cobarde'], ['generoso', 'egoísta'], ['activo', 'perezoso'], ['calmado', 'emocionado'], ['paciente', 'impaciente'], ['organizado', 'desordenado'], ['esperanzado', 'desesperado'], ['seguro', 'dubitativo'], 
    ['realista', 'idealista'], ['extrovertido', 'tímido'], ['hablador', 'callado'],
]

analog_pairs = [
    ['feliz', 'alegre'], ['grande', 'grande'], ['caliente', 'ardiente'], ['largo', 'extenso'], ['ancho', 'amplio'], ['brillante', 'brillante'], ['áspero', 'desigual'], ['mojado', 'húmedo'],
    ['alto', 'estruendoso'], ['rápido', 'veloz'], ['profundo', 'profundo'], ['grueso', 'denso'], ['pesado', 'pesado'], ['lleno', 'rebosante'], ['abierto', 'descubierto'], ['limpio', 'impecable'],
    ['fuerte', 'poderoso'], ['hermoso', 'magnífico'], ['rico', 'adinerado'], ['joven', 'jovenil'], ['activo', 'enérgico'], ['amable', 'benevolente'], ['honesto', 'veraz'], ['valiente', 'corajudo'],
    ['cuidadoso', 'cauteloso'], ['optimista', 'esperanzado'], ['generoso', 'desinteresado'], ['educado', 'cortés'], ['calmado', 'sereno'], ['pacífico', 'tranquilo'], ['saludable', 'en forma'], ['fresco', 'nuevo'],
    ['dulce', 'delicioso'], ['amargo', 'acre'], ['suave', 'gentil'], ['liso', 'elegante'], ['flexible', 'flexible'], ['opaco', 'romo'], ['ruidoso', 'estridente'], ['fragante', 'aromático'],
    ['atractivo', 'atractivo'], ['exitoso', 'victorioso'], ['ganador', 'campeón'], ['ganar', 'adquirir'], ['comienzo', 'comienzo'], ['cima', 'cúspide'], ['frente', 'vanguardia'], ['dentro', 'interior'],
    ['arriba', 'superior'], ['hablar', 'conversar'], ['dar', 'otorgar'], ['comprar', 'adquirir'], ['mostrar', 'exhibir'], ['abrir', 'desplegar'], ['construir', 'construir'], ['crear', 'modelar'],
    ['empezar', 'iniciar'], ['llegar', 'alcanzar'], ['venir', 'acercarse'], ['día', 'amanecer'], ['verano', 'estivo'], ['amor', 'adoración'], ['confianza', 'fe'], ['amigo', 'compañero'],
    ['verdad', 'veracidad'], ['justicia', 'equidad'], ['libertad', 'libertad'], ['paz', 'armonía'], ['orden', 'método'], ['éxito', 'logro'], ['victoria', 'triunfo'], ['conocimiento', 'erudición'],
    ['sabiduría', 'sagacidad'], ['lógica', 'razón'], ['ciencia', 'investigación'], ['realidad', 'actualidad'], ['simple', 'básico'], ['fácil', 'sin esfuerzo'], ['familiar', 'conocido'], ['famoso', 'renombrado'],
    ['público', 'abierto'], ['abierto', 'franco'], ['honesto', 'sincero'], ['claro', 'inequívoco'], ['confiado', 'seguro'], ['valiente', 'valeroso'], ['generoso', 'benéfico'], ['activo', 'dinámico'],
    ['calmado', 'compuesto'], ['paciente', 'tolerante'], ['organizado', 'sistemático'], ['esperanzado', 'optimista'], ['seguro', 'seguro de sí mismo'], ['realista', 'pragmático'], ['extrovertido', 'extrovertido'],
    ['hablador', 'locuaz'],
]

unrelated_words = [
    'manzana', 'silla', 'océano', 'montaña', 'paraguas', 'piano', 'nube', 'cámara', 'guitarra', 'bicicleta',
    'flor', 'río', 'sombrero', 'luna', 'estrella', 'vela', 'isla', 'espejo', 'sol', 'tren',
    'zapato', 'llave', 'ventana', 'barco', 'mariposa', 'billetera', 'globo terráqueo', 'reloj', 'mapa', 'pastel',
    'cuadro', 'teléfono', 'moneda', 'martillo', 'silla', 'bolso', 'gafas', 'guitarra', 'tijeras', 'toalla',
    'canasta', 'almohada', 'espejo', 'cojín', 'botella', 'guantes', 'libro', 'paraguas', 'baloncesto', 'guitarra',
    'cepillo', 'control remoto', 'bolígrafo', 'lámpara', 'ventilador', 'cepillo de dientes', 'bandera', 'taza', 'silla', 'borrador',
    'calculadora', 'engrapadora', 'imán', 'refrigerador', 'calendario', 'reloj', 'cinta adhesiva', 'billetera', 'esponja', 'microscopio',
    'alma', 'tomografía computarizada', 'enfriar', 'vodka'
]

word_pairs = synonym_pairs + antonym_pairs + analog_pairs