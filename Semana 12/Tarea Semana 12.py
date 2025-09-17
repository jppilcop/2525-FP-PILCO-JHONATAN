# Lista de nombres de ciudades
ciudades = ["Quito", "Riobamba", "Ibarra"]

# Matriz 3D de temperaturas en °C
temperaturas = [
    [  # Ciudad 1 - Quito (9 a 19 °C)
        [  # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 14},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 17},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ]
    ],
    [  # Ciudad 2 - Riobamba (9 a 19 °C)
        [  # Semana 1
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 18},
           {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 12},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 18}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ]
    ],
    [  # Ciudad 3 - Ibarra (10 a 19 °C)
        [  # Semana 1
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 14},
            {"day": "Jueves", "temp": 13},
            {"day": "Viernes", "temp": 15},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 10},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 13},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 19}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 13},
            {"day": "Miércoles", "temp": 15},
            {"day": "Jueves", "temp": 14},
            {"day": "Viernes", "temp": 16},
            {"day": "Sábado", "temp": 17},
            {"day": "Domingo", "temp": 19}
        ]
    ]
]

# Iteración con bucles anidados para promedios
for i in range(len(temperaturas)):  # Ciudades
    print(f"\nPromedios de {ciudades[i]}:")

    for j in range(len(temperaturas[i])):  # Semanas
        suma = 0
        for k in range(len(temperaturas[i][j])):  # Días
            suma += temperaturas[i][j][k]['temp']

        promedio = suma / len(temperaturas[i][j])
        print(f"  Semana {j + 1}: {promedio:.2f} °C")