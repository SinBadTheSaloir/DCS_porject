chap1_names = ["Alice", "White Rabbit"]
chap1_data = [
    # Alice's feelings towards all, White Rabbit
    [
        [0]*14, # Alice towards herself
        [5, 0, 0, 1, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0] # Alice towards White Rabbit
    ],
    # White Rabbit's feelings towards Alice, all
    [
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Alice
        [0]*14 # White Rabbit towards himself
    ]
]

chap2_names = ["Alice", "White Rabbit", "Mouse"]
chap2_data = [
    # Alice's feelings towards herself, White Rabbit, Mouse
    [
        [0]*14, # Alice towards herself
        [5, 0, 0, 1, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0], # Alice towards White Rabbit
        [5, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0] # Alice towards Mouse
    ],
    # White Rabbit's feelings towards Alice, himself, Mouse
    [
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Alice
        [0]*14, # White Rabbit towards himself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # White Rabbit towards Mouse (no interaction)
    ],
    # Mouse's feelings towards Alice, White Rabbit, himself
    [
        [4, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Mouse towards Alice
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Mouse towards White Rabbit (no interaction)
        [0]*14 # Mouse towards himself
    ]
]

chap3_names = ["Alice", "Mouse", "Lory", "Dodo", "Duck"]
chap3_data = [
    # Alice's feelings towards herself, Mouse, Lory, Dodo, Duck
    [
        [0]*14, # Alice towards herself
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Alice towards Mouse
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards Lory
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Alice towards Dodo
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0]  # Alice towards Duck
    ],
    # Mouse's feelings towards Alice, himself, Lory, Dodo, Duck
    [
        [4, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Mouse towards Alice
        [0]*14, # Mouse towards himself
        [0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Mouse towards Lory
        [0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Mouse towards Dodo
        [0, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0]  # Mouse towards Duck
    ],
    # Lory's feelings towards Alice, Mouse, himself, Dodo, Duck
    [
        [3, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Lory towards Alice
        [2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Lory towards Mouse
        [0]*14, # Lory towards himself
        [2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Lory towards Dodo
        [2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0]  # Lory towards Duck
    ],
    # Dodo's feelings towards Alice, Mouse, Lory, himself, Duck
    [
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Dodo towards Alice
        [2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Dodo towards Mouse
        [2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Dodo towards Lory
        [0]*14, # Dodo towards himself
        [2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0]  # Dodo towards Duck
    ],
    # Duck's feelings towards Alice, Mouse, Lory, Dodo, himself
    [
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Duck towards Alice
        [2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Duck towards Mouse
        [2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Duck towards Lory
        [2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Duck towards Dodo
        [0]*14  # Duck towards himself
    ]
]

chap4_names = ["Alice", "White Rabbit"]
chap4_data = [
    # Alice's feelings towards herself, White Rabbit
    [
        [0]*14, # Alice towards herself
        [5, 0, 0, 1, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0] # Alice towards White Rabbit
    ],
    # White Rabbit's feelings towards Alice, himself
    [
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Alice
        [0]*14 # White Rabbit towards himself
    ]
]

chap5_names = ["Alice", "Caterpillar"]
chap5_data = [
    # Alice's feelings towards herself, Caterpillar
    [
        [0]*14, # Alice towards herself
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0] # Alice towards Caterpillar
    ],
    # Caterpillar's feelings towards Alice, himself
    [
        [4, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Caterpillar towards Alice
        [0]*14 # Caterpillar towards himself
    ]
]

chap6_names = ["Alice", "Pigeon"]
chap6_data = [
    # Alice's feelings towards herself, Pigeon
    [
        [0]*14, # Alice towards herself
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0] # Alice towards Pigeon
    ],
    # Pigeon's feelings towards Alice, himself
    [
        [2, 0, 0, 8, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0], # Pigeon towards Alice
        [0]*14 # Pigeon towards himself
    ]
]

chap7_names = ["Alice", "March Hare", "Hatter", "Dormouse"]
chap7_data = [
    # Alice's feelings towards herself, March Hare, Hatter, Dormouse
    [
        [0]*14, # Alice towards herself
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards March Hare
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards Hatter
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0]  # Alice towards Dormouse
    ],
    # March Hare's feelings towards Alice, Hatter, Dormouse, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # March Hare towards Alice
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # March Hare towards Hatter
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # March Hare towards Dormouse
        [0]*14 # March Hare towards himself
    ],
    # Hatter's feelings towards Alice, March Hare, Dormouse, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Hatter towards Alice
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Hatter towards March Hare
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Hatter towards Dormouse
        [0]*14 # Hatter towards himself
    ],
    # Dormouse's feelings towards Alice, March Hare, Hatter, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Dormouse towards Alice
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Dormouse towards March Hare
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Dormouse towards Hatter
        [0]*14 # Dormouse towards himself
    ]
]

chap8_names = ["Alice", "Queen of Hearts", "King of Hearts", "Cheshire Cat"]
chap8_data = [
    # Alice's feelings towards herself, Queen of Hearts, King of Hearts, Cheshire Cat
    [
        [0]*14, # Alice towards herself
        [3, 0, 0, 4, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards King of Hearts
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0] # Alice towards Cheshire Cat
    ],
    # Queen of Hearts' feelings towards Alice, King of Hearts, Cheshire Cat, herself
    [
        [5, 0, 0, 5, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0], # Queen of Hearts towards Alice
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Queen of Hearts towards King of Hearts
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Queen of Hearts towards Cheshire Cat
        [0]*14 # Queen of Hearts towards herself
    ],
    # King of Hearts' feelings towards Alice, Queen of Hearts, Cheshire Cat, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Alice
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # King of Hearts towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Cheshire Cat
        [0]*14 # King of Hearts towards himself
    ],
    # Cheshire Cat's feelings towards Alice, Queen of Hearts, King of Hearts, himself
    [
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Cheshire Cat towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Cheshire Cat towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Cheshire Cat towards King of Hearts
        [0]*14 # Cheshire Cat towards himself
    ]
]

chap9_names = ["Alice", "Duchess", "Queen of Hearts"]
chap9_data = [
    # Alice's feelings towards herself, Duchess, Queen of Hearts
    [
        [0]*14, # Alice towards herself
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards Duchess
        [4, 0, 0, 4, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0] # Alice towards Queen of Hearts
    ],
    # Duchess's feelings towards Alice, herself, Queen of Hearts
    [
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Duchess towards Alice
        [0]*14, # Duchess towards herself
        [4, 0, 0, 3, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0] # Duchess towards Queen of Hearts
    ],
    # Queen of Hearts' feelings towards Alice, Duchess, herself
    [
        [5, 0, 0, 5, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0], # Queen of Hearts towards Alice
        [4, 0, 0, 3, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Queen of Hearts towards Duchess
        [0]*14 # Queen of Hearts towards herself
    ]
]

chap10_names = ["Alice", "Mock Turtle", "Gryphon"]
chap10_data = [
    # Alice's feelings towards herself, Mock Turtle, Gryphon
    [
        [0]*14, # Alice towards herself
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards Mock Turtle
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0] # Alice towards Gryphon
    ],
    # Mock Turtle's feelings towards Alice, himself, Gryphon
    [
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Mock Turtle towards Alice
        [0]*14, # Mock Turtle towards himself
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0] # Mock Turtle towards Gryphon
    ],
    # Gryphon's feelings towards Alice, Mock Turtle, himself
    [
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Gryphon towards Alice
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Gryphon towards Mock Turtle
        [0]*14 # Gryphon towards himself
    ]
]

chap11_names = ["Alice", "King of Hearts", "Queen of Hearts", "Knave of Hearts", "White Rabbit", "Hatter", "March Hare", "Dormouse"]
chap11_data = [
    [
        [0]*14, # Alice towards herself
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards King of Hearts
        [4, 0, 0, 4, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Alice towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards White Rabbit
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards Hatter
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards March Hare
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0]  # Alice towards Dormouse
    ],
    # King of Hearts' feelings towards Alice, Queen of Hearts, Knave of Hearts, White Rabbit, Hatter, March Hare, Dormouse, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Alice
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # King of Hearts towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards White Rabbit
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Hatter
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards March Hare
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Dormouse
        [0]*14 # King of Hearts towards himself
    ],
    # Queen of Hearts' feelings towards Alice, King of Hearts, Knave of Hearts, White Rabbit, Hatter, March Hare, Dormouse, herself
    [
        [5, 0, 0, 5, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0], # Queen of Hearts towards Alice
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Queen of Hearts towards King of Hearts
        [4, 0, 0, 3, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Queen of Hearts towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Queen of Hearts towards White Rabbit
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Queen of Hearts towards Hatter
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Queen of Hearts towards March Hare
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Queen of Hearts towards Dormouse
        [0]*14 # Queen of Hearts towards herself
    ],
    # Knave of Hearts' feelings towards Alice, King of Hearts, Queen of Hearts, White Rabbit, Hatter, March Hare, Dormouse, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards King of Hearts
        [4, 0, 0, 3, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Knave of Hearts towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards White Rabbit
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards Hatter
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards March Hare
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards Dormouse
        [0]*14 # Knave of Hearts towards himself
    ],
    # White Rabbit's feelings towards Alice, King of Hearts, Queen of Hearts, Knave of Hearts, Hatter, March Hare, Dormouse, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards King of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Hatter
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards March Hare
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Dormouse
        [0]*14 # White Rabbit towards himself
    ],
    # Hatter's feelings towards Alice, King of Hearts, Queen of Hearts, Knave of Hearts, White Rabbit, March Hare, Dormouse, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Hatter towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Hatter towards King of Hearts
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Hatter towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Hatter towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Hatter towards White Rabbit
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Hatter towards March Hare
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Hatter towards Dormouse
        [0]*14 # Hatter towards himself
    ],
    # March Hare's feelings towards Alice, King of Hearts, Queen of Hearts, Knave of Hearts, White Rabbit, Hatter, Dormouse, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # March Hare towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # March Hare towards King of Hearts
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # March Hare towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # March Hare towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # March Hare towards White Rabbit
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # March Hare towards Hatter
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # March Hare towards Dormouse
        [0]*14 # March Hare towards himself
    ],
    # Dormouse's feelings towards Alice, King of Hearts, Queen of Hearts, Knave of Hearts, White Rabbit, Hatter, March Hare, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Dormouse towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Dormouse towards King of Hearts
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Dormouse towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Dormouse towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Dormouse towards White Rabbit
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Dormouse towards Hatter
        [3, 0, 0, 1, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Dormouse towards March Hare
        [0]*14 # Dormouse towards himself
    ]
]

chap12_names = ["Alice", "King of Hearts", "Queen of Hearts", "Knave of Hearts", "White Rabbit", "Gryphon", "Mock Turtle"]
chap12_data = [
    # Alice's feelings towards herself, King of Hearts, Queen of Hearts, Knave of Hearts, White Rabbit, Gryphon, Mock Turtle
    [
        [0]*14, # Alice towards herself
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards King of Hearts
        [4, 0, 0, 4, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Alice towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Alice towards White Rabbit
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Alice towards Gryphon
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0]  # Alice towards Mock Turtle
    ],
    # King of Hearts' feelings towards Alice, Queen of Hearts, Knave of Hearts, White Rabbit, Gryphon, Mock Turtle, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Alice
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # King of Hearts towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards White Rabbit
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Gryphon
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # King of Hearts towards Mock Turtle
        [0]*14 # King of Hearts towards himself
    ],
    # Queen of Hearts' feelings towards Alice, King of Hearts, Knave of Hearts, White Rabbit, Gryphon, Mock Turtle, herself
    [
        [5, 0, 0, 5, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0], # Queen of Hearts towards Alice
        [4, 0, 0, 1, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Queen of Hearts towards King of Hearts
        [4, 0, 0, 3, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Queen of Hearts towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Queen of Hearts towards White Rabbit
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Queen of Hearts towards Gryphon
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Queen of Hearts towards Mock Turtle
        [0]*14 # Queen of Hearts towards herself
    ],
    # Knave of Hearts' feelings towards Alice, King of Hearts, Queen of Hearts, White Rabbit, Gryphon, Mock Turtle, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards King of Hearts
        [4, 0, 0, 3, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Knave of Hearts towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards White Rabbit
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards Gryphon
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Knave of Hearts towards Mock Turtle
        [0]*14 # Knave of Hearts towards himself
    ],
    # White Rabbit's feelings towards Alice, King of Hearts, Queen of Hearts, Knave of Hearts, Gryphon, Mock Turtle, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards King of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Gryphon
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # White Rabbit towards Mock Turtle
        [0]*14 # White Rabbit towards himself
    ],
    # Gryphon's feelings towards Alice, King of Hearts, Queen of Hearts, Knave of Hearts, White Rabbit, Mock Turtle, himself
    [
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Gryphon towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Gryphon towards King of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Gryphon towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Gryphon towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Gryphon towards White Rabbit
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Gryphon towards Mock Turtle
        [0]*14 # Gryphon towards himself
    ],
    # Mock Turtle's feelings towards Alice, King of Hearts, Queen of Hearts, Knave of Hearts, White Rabbit, Gryphon, himself
    [
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Mock Turtle towards Alice
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Mock Turtle towards King of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Mock Turtle towards Queen of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Mock Turtle towards Knave of Hearts
        [3, 0, 0, 2, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0], # Mock Turtle towards White Rabbit
        [4, 0, 0, 2, 0, 0, 4, 4, 4, 0, 0, 0, 0, 0], # Mock Turtle towards Gryphon
        [0]*14 # Mock Turtle towards himself
    ]
]

#1 ,12
global start , end 
start = 1
end = 12
def collect_chapter_data_AW():
    a,b = aggregate_chapter_data()
    return a,b
def aggregate_chapter_data(chapter_count =end):
    global start , end 

    aggregated_names = []
    aggregated_data = []
    
    for n in range(start, end + 1):
        chap_names = globals().get(f'chap{n}_names')
        chap_data = globals().get(f'chap{n}_data')
        
        if chap_names is not None and chap_data is not None:
            aggregated_names.append(chap_names)
            aggregated_data.append(chap_data)
    
    return aggregated_names, aggregated_data
    