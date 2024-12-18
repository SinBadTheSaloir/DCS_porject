# Data


chapter_names = [
    ["Morrel", "Edmond", "Danglars"],
    ["Edmond", "Old_man_dantes", "Caderousse", "Danglars"],
    ['Mercédès', 'Fernand', 'Edmond', 'Danglars', 'Caderousse'],
    ["Danglars", "Caderousse", "Fernand"],
    ["Edmond", "Morrel", "Danglars", "Caderousse", "Fernand", "Mercédès"],
    ["Marquise de Saint-Méran", "M. de Villefort", "Renée", "Noirtier"],
    ["Villefort", "Edmond"]
]




relationships_data = [
    # Chapter 1 - Morrel, Edmond, Danglars
    [
        # Morrel's relationships (towards himself, Edmond, Danglars)
        [[0]*14, [8,0,0,0,0,10,7,8,8,6,0,0,8,0], [5,0,0,0,5,10,7,6,6,0,0,0,0,0]],
        # Edmond's relationships (towards Morrel, himself, Danglars)
        [[8,0,0,0,5,4,4,8,9,10,0,0,8,0], [0]*14, [3,0,0,6,0,5,5,4,6,0,7,10,1,0]],
        # Danglars' relationships (towards Morrel, Edmond, himself)
        [[5,0,0,0,5,4,4,5,5,4,0,0,0,0], [1,0,0,10,0,5,5,1,1,1,10,10,1,10], [0]*14]
    ],
    # Chapter 2 - Edmond, Old_man_dantes, Caderousse, Danglars
    [
        # Edmond's relationships (towards himself, Old_man_dantes, Caderousse, Danglars)
        [[0]*14, [10,10,0,0,0,10,10,10,10,10,0,0,0,0], [5,0,0,0,0,0,10,4,5,0,0,7,0,0], [3,0,0,6,0,5,5,4,6,0,7,10,1,0]],
        # Old_man_dantes' relationships (towards Edmond, himself, Caderousse, Danglars)
        [[10,10,0,0,0,10,10,10,10,10,0,0,0,0], [0]*14, [5,0,0,0,0,0,10,4,5,0,0,7,0,0], [0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
        # Caderousse's relationships (towards Edmond, Old_man_dantes, himself, Danglars)
        [[4,0,0,5,0,0,5,5,4,0,7,0,0,8], [4,0,0,5,0,0,5,5,4,0,7,0,0,8], [0]*14, [6,0,0,0,0,0,5,6,6,8,0,0,10,0]],
        # Danglars' relationships (towards Edmond, Old_man_dantes, Caderousse, himself)
        [[1,0,0,10,0,5,5,1,1,1,10,10,1,10], [0,0,0,0,0,0,0,0,0,0,0,0,0,0], [6,0,0,0,0,0,5,6,6,8,0,0,10,0], [0]*14]
    ],
    # Chapter 3 - Mercédès, Fernand, Edmond, Danglars, Caderousse
    [
        # Mercédès' relationships (towards herself, Fernand, Edmond, Danglars, Caderousse)
        [[0]*14, [8,7,1,0,0,0,5,10,8,0,10,0,1,10], [10,0,10,0,0,0,10,10,10,10,10,0,10,0], [1,2,3,4,5,6,7,8,9,10,11,12,13,14], [0]*14],
        # Fernand's relationships (towards Mercédès, himself, Edmond, Danglars, Caderousse)
        [[8,7,10,0,0,0,10,8,0,10,10,0,1,10], [0]*14, [1,0,0,10,0,0,4,1,1,1,0,0,1,10], [6,0,0,0,0,0,4,7,5,8,0,0,10,1], [6,0,0,0,0,0,4,7,5,8,0,0,10,1]],
        # Edmond's relationships (towards Mercédès, Fernand, himself, Danglars, Caderousse)
        [[10,0,10,0,0,0,10,10,10,10,10,0,10,0], [3,0,0,1,0,0,6,5,5,0,0,0,3,7], [0]*14, [3,0,0,6,0,5,5,4,6,0,7,10,1,0], [5,0,0,0,0,0,10,4,5,0,0,7,0,0]],
        # Danglars' relationships (towards Mercédès, Fernand, Edmond, himself, Caderousse)
        [[0]*14, [6,0,0,0,0,0,4,7,5,8,0,0,10,1], [1,0,0,10,0,5,5,1,1,1,10,10,1,10], [0]*14, [6,0,0,0,0,0,5,6,6,8,0,0,10,0]],
        # Caderousse's relationships (towards Mercédès, Fernand, Edmond, Danglars, himself)
        [[0]*14, [5,0,0,0,0,0,5,5,5,5,0,0,10,0], [4,0,0,5,0,0,5,5,4,0,7,0,0,8], [6,0,0,0,0,0,5,6,6,8,0,0,10,0], [0]*14]
    ],
    [
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[6,0,0,0,0,0,5,6,6,8,0,0,10,6],[6,0,0,0,0,0,4,7,5,8,0,0,10,0]],
    [[6,0,0,0,0,0,5,6,6,8,0,0,5,10],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,0,0,0,0,0,5,5,5,5,0,0,5,10]],
    [[7,0,0,0,0,0,4,7,5,8,0,0,10,1],[4,0,0,0,0,0,4,7,5,8,0,0,5,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    ],
    [
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[8,0,0,0,5,4,4,8,9,10,0,0,8,0],[4,0,0,6,0,5,5,5,6,0,7,10,1,0],[6,0,0,0,0,0,10,4,5,0,5,0,0,0],[6,0,0,1,0,0,6,5,5,0,0,0,3,7],[10,0,10,0,0,0,10,10,10,10,10,0,10,0]],

    [[9,0,0,0,0,10,7,8,8,6,0,0,8,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,0,0,0,5,10,7,6,6,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0]],

    [[1,0,0,10,0,5,5,1,1,1,10,10,1,10],[5,0,0,0,5,4,4,5,5,4,0,0,0,10],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,0,0,0,0,0,5,6,6,8,0,0,10,5],[6,0,0,0,0,0,4,8,5,8,0,0,10,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    [[7,0,0,5,0,0,5,5,4,1,7,0,0,8],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[4,0,0,0,0,0,5,4,4,4,0,0,5,4],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[2,0,0,0,0,0,5,4,4,4,0,0,5,4],[0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    [[1,0,0,10,0,0,4,1,1,1,0,0,1,10],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[6,0,0,0,0,0,4,7,5,8,0,0,10,0],[4,0,0,0,0,0,4,7,5,8,0,0,5,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[8,7,10,0,0,0,10,8,0,10,10,0,1,10]],
    [[10,0,10,0,0,0,10,10,10,10,10,0,10,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[8,7,1,0,0,0,5,10,8,0,10,0,1,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
],
[
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,0,0,0,10,0,10,7,7,5,0,0,8,0],[0,10,0,0,10,0,10,6,6,0,0,0,8,0],[0,0,0,10,1,0,1,1,1,0,0,10,1,10]],
    [[6,0,0,0,10,0,10,6,6,6,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,10,0,10,0,10,8,8,7,0,0,0,0],[1,10,0,5,1,0,7,0,1,0,0,0,0,10]],
    [[0,10,0,0,10,0,10,6,6,0,0,0,8,0],[0,0,10,0,10,0,10,8,8,7,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0]],
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

],
[
    [[0,0,0,0,0,0,0,0,0,0,0,0,0,0],[5,0,0,0,10,0,10,7,6,3,0,0,1,10]],
    [[6,0,0,0,0,0,4,10,10,10,0,0,10,1],[0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

],

]

# chap 10
chap10_names = ["Marquise de Saint-Méran", "M. de Villefort", "Renée", "Mercédès", "Dantès"]
chap10_data = [
    # Marquise de Saint-Méran
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [6, 0, 0, 0, 5, 0, 10, 6, 6, 0, 0, 0, 0, 0],  # Towards M. de Villefort
        [0, 0, 10, 0, 5, 0, 10, 6, 6, 0, 0, 0, 0, 0], # Towards Renée
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Mercédès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards Dantès
    ],
    # M. de Villefort
    [
        [5, 0, 0, 0, 5, 0, 10, 7, 7, 5, 0, 0, 8, 0], # Towards Marquise de Saint-Méran
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 0, 10, 7, 7, 0, 0, 0, 8, 0], # Towards Renée
        [2, 0, 0, 0, 2, 0, 3, 3, 3, 0, 0, 0, 3, 0],  # Towards Mercédès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards Dantès
    ],
    # Renée
    [
        [0, 10, 0, 0, 5, 0, 10, 6, 6, 0, 0, 0, 0, 0], # Towards Marquise de Saint-Méran
        [7, 0, 0, 0, 7, 0, 10, 7, 7, 0, 0, 0, 8, 0],  # Towards M. de Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards herself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards Mercédès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # Towards Dantès
    ],
    # Mercédès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Marquise de Saint-Méran
        [2, 0, 0, 0, 2, 0, 3, 3, 3, 0, 0, 0, 3, 0],  # Towards M. de Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Renée
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [0, 9, 0, 0, 9, 0, 9, 9, 9, 0, 0, 0, 9, 0]   # Towards Dantès
    ],
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Marquise de Saint-Méran
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards M. de Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Renée
        [9, 0, 0, 0, 9, 0, 9, 9, 9, 0, 0, 0, 9, 0],  # Towards Mercédès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]


# Chap 11
chap11_names = ["Louis XVIII", "Villefort", "M. de Blacas"]

chap11_data = [
    # Louis XVIII
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 2, 10, 8, 8, 7, 7, 0, 8, 0, 7, 0],  # Towards Villefort
        [7, 0, 0, 1, 10, 8, 7, 7, 6, 0, 7, 0, 6, 0]   # Towards M. de Blacas
    ],
    # Villefort
    [
        [9, 0, 0, 0, 10, 10, 9, 9, 8, 0, 9, 0, 9, 0],  # Towards Louis XVIII
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards himself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # Towards M. de Blacas (no direct interaction rated)
    ],
    # M. de Blacas
    [
        [0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Louis XVIII (no direct interaction rated)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Villefort (no direct interaction rated)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]


chap12_names = ["Louis XVIII", "Villefort", "M. de Blacas", "Minister of Police (Dandré)"]

chap12_data = [
    # Louis XVIII
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards himself
        [8, 0, 0, 3, 10, 9, 9, 8, 8, 0, 9, 0, 8, 0],   # Towards Villefort
        [6, 0, 0, 4, 10, 7, 6, 5, 4, 0, 5, 0, 4, 0],   # Towards M. de Blacas
        [6, 0, 0, 4, 10, 7, 6, 5, 4, 0, 5, 0, 4, 0]    # Towards Minister of Police (Dandré)
    ],
    # Villefort
    [
        [9, 0, 0, 0, 10, 10, 9, 9, 9, 0, 10, 0, 10, 0], # Towards Louis XVIII
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    # Towards himself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],    # Towards M. de Blacas (no direct interaction rated)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]     # Towards Minister of Police (Dandré) (no direct interaction rated)
    ],
    # M. de Blacas
    [
        [0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards Louis XVIII (no direct interaction rated)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards Villefort (no direct interaction rated)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards himself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # Towards Minister of Police (Dandré) (no direct interaction rated)
    ],
    # Minister of Police (Dandré)
    [
        [0, 0, 0, 0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards Louis XVIII (no direct interaction rated)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards Villefort (no direct interaction rated)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],   # Towards M. de Blacas (no direct interaction rated)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # Towards himself
    ]
]


chap13_names = ["Villefort", "M. Noirtier"]

chap13_data = [
    # Villefort
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 10, 0, 10, 6, 7, 0, 8, 0, 9, 0]  # Towards M. Noirtier
    ],
    # M. Noirtier
    [
        [8, 0, 0, 0, 10, 0, 10, 7, 8, 0, 9, 0, 10, 0], # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # Towards himself
    ]
]

chap14_names = ["Villefort", "M. Morrel", "Dantès", "Napoleon"]

chap14_data = [
    # Villefort
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 0, 7, 6, 5, 0, 6, 0, 4, 0],  # Towards M. Morrel
        [3, 0, 0, 0, 3, 0, 10, 1, 2, 0, 1, 0, 0, 0], # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards Napoleon (no interaction)
    ],
    # M. Morrel
    [
        [6, 0, 0, 0, 10, 0, 8, 7, 8, 0, 7, 0, 7, 0], # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Dantès (no direct interaction)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards Napoleon (no interaction)
    ],
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Villefort (no direct interaction, unaware of his fate)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards M. Morrel (no direct interaction)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards Napoleon (no interaction)
    ],
    # Napoleon
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Villefort (no direct interaction)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards M. Morrel (no interaction)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Dantès (no interaction)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap15_names = ["Dantès", "Inspector", "Abbé Faria"]

chap15_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [0, 10, 0, 0, 10, 0, 9, 9, 9, 0, 9, 0, 10, 0], # Towards Inspector
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards Abbé Faria (no direct interaction in this chapter)
    ],
    # Inspector
    [
        [0, 0, 0, 0, 10, 0, 8, 8, 8, 0, 8, 0, 9, 0], # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards Abbé Faria (no interaction noted)
    ],
    # Abbé Faria
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Dantès (no direct interaction in this chapter)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards Inspector (no interaction)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]


chap16_names = ["Dantès", "Jailer"]

chap16_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 0, 10, 3, 4, 0, 5, 0, 6, 0]  # Towards Jailer
    ],
    # Jailer
    [
        [4, 0, 0, 0, 4, 0, 7, 2, 3, 0, 4, 0, 5, 0],  # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap17_names = ["Dantès", "Abbé Faria"]

chap17_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Abbé Faria
    ],
    # Abbé Faria
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0], # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]        # Towards himself
    ]
]

chap18_names = ["Dantès", "Abbé Faria"]

chap18_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Abbé Faria
    ],
    # Abbé Faria
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0], # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]        # Towards himself
    ]
]
chap19_names = ["Dantès", "Abbé Faria", "Governor"]

chap19_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Abbé Faria
        [2, 0, 0, 0, 2, 0, 3, 2, 2, 0, 2, 0, 1, 0]       # Towards Governor
    ],
    # Abbé Faria
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0], # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],       # Towards himself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]        # Towards Governor (no direct interaction)
    ],
    # Governor
    [
        [3, 0, 0, 0, 3, 0, 4, 3, 3, 0, 3, 0, 2, 0],       # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],       # Towards Abbé Faria (no direct interaction)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]        # Towards himself
    ]
]

chap20_names = ["Dantès", "Abbé Faria"]

chap20_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Abbé Faria
    ],
    # Abbé Faria
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0], # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]        # Towards himself
    ]
]

chap21_names = ["Dantès"]

chap21_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Towards himself
    ]
]

chap22_names = ["Dantès"]

chap22_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Towards himself
    ]
]

chap23_names = ["Dantès", "Smuggler Captain", "Smuggler Crew"]

chap23_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 8, 8, 0, 8, 0, 9, 0],  # Towards Smuggler Captain
        [7, 0, 0, 0, 7, 0, 8, 8, 8, 0, 8, 0, 9, 0]   # Towards Smuggler Crew
    ],
    # Smuggler Captain
    [
        [7, 0, 0, 0, 7, 0, 8, 8, 8, 0, 8, 0, 9, 0], # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards Smuggler Crew (no direct interaction)
    ],
    # Smuggler Crew
    [
        [7, 0, 0, 0, 7, 0, 8, 8, 8, 0, 8, 0, 9, 0], # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # Towards Smuggler Captain (no direct interaction)
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Towards themselves
    ]
]
chap25_names = ["Dantès"]

chap25_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Towards himself
    ]
]
chap26_names = ["Dantès", "Smugglers"]

chap26_data = [
    # Dantès
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 0, 10, 9, 8, 0, 9, 0, 10, 0]  # Towards Smugglers
    ],
    # Smugglers
    [
        [7, 0, 0, 0, 7, 0, 10, 9, 8, 0, 9, 0, 10, 0],  # Towards Dantès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]    # Towards themselves
    ]
]

chap27_names = ["Fernand", "Danglars", "Caderousse", "Villefort", "La Carconte"]

chap27_data = [
    # Fernand
    [
        [0]*14,  # Towards himself
        [3, 0, 0, 0, 3, 0, 4, 3, 3, 0, 3, 0, 4, 0],  # Towards Danglars (collusion and shared goals but also tension)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 6, 0],  # Towards Caderousse (manipulation and dominance)
        [0]*14,  # Towards Villefort (no direct interaction in this context)
        [0]*14   # Towards La Carconte (no interaction)
    ],
    # Danglars
    [
        [3, 0, 0, 0, 3, 0, 4, 3, 3, 0, 3, 0, 4, 0],  # Towards Fernand (shared manipulation but mutual distrust)
        [0]*14,  # Towards himself
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 6, 0],  # Towards Caderousse (utilitarian relationship)
        [0]*14,  # Towards Villefort (no direct interaction in this context)
        [0]*14   # Towards La Carconte (no interaction)
    ],
    # Caderousse
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 6, 0],  # Towards Fernand (subservience and fear)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 6, 0],  # Towards Danglars (reluctant partnership)
        [0]*14,  # Towards himself
        [0]*14,  # Towards Villefort (no interaction)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 7, 0]   # Towards La Carconte (marital relationship with its complexities)
    ],
    # Villefort
    [
        [0]*14,  # Towards Fernand (no interaction)
        [0]*14,  # Towards Danglars (no interaction)
        [0]*14,  # Towards Caderousse (no interaction)
        [0]*14,  # Towards himself
        [0]*14   # Towards La Carconte (no interaction)
    ],
    # La Carconte
    [
        [0]*14,  # Towards Fernand (no interaction)
        [0]*14,  # Towards Danglars (no interaction)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 7, 0],  # Towards Caderousse (complex marital dynamics)
        [0]*14,  # Towards Villefort (no interaction)
        [0]*14   # Towards herself
    ]
]

chap28_names = ["Caderousse", "Abbé Busoni"]

chap28_data = [
    # Caderousse
    [
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 5, 0, 7, 6, 6, 0, 6, 0, 7, 0]  # Towards Abbé Busoni (apprehensive but also hopeful of gaining something)
    ],
    # Abbé Busoni
    [
        [7, 0, 0, 0, 7, 0, 8, 8, 8, 0, 8, 0, 9, 0],  # Towards Caderousse (manipulative and probing, seeking truth and justice)
        [0]*14  # Towards himself (no self-evaluation in this context)
    ]
]



chap30_names = ["Englishman", "M. de Boville"]

chap30_data = [
    # Englishman
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 8, 0, 9, 9, 8, 0, 8, 0, 9, 0]  # Towards M. de Boville (practical and somewhat opportunistic in offering to buy the debt)
    ],
    # M. de Boville
    [
        [6, 0, 0, 0, 7, 0, 8, 8, 7, 0, 7, 0, 8, 0],  # Towards Englishman (desperate but cautious, relieved by the offer but aware of potential consequences)
        [0]*14  # Towards himself
    ]
]

chap31_names = ["M. Morrel", "Englishman", "Emmanuel"]

chap31_data = [
    # M. Morrel
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 9, 9, 0, 9, 0, 10, 0],  # Towards Englishman (grateful for the support and possibility of a solution)
        [0]*14   # Towards Emmanuel (no significant direct financial interaction in this context)
    ],
    # Englishman
    [
        [8, 0, 0, 0, 8, 0, 9, 9, 9, 0, 9, 0, 10, 0],  # Towards M. Morrel (sympathetic and supportive, offering a financial lifeline)
        [0]*14,  # Towards himself
        [0]*14   # Towards Emmanuel (no direct interaction in financial discussions)
    ],
    # Emmanuel
    [
        [0]*14,  # Towards M. Morrel (primarily an assistant, not involved in the debt negotiation)
        [0]*14,  # Towards Englishman (no direct interaction)
        [0]*14   # Towards himself
    ]
]

chap32_names = ["M. Morrel", "Julie Morrel", "Maximilian Morrel", "Cocles", "Emmanuel"]

chap32_data = [
    # M. Morrel
    [
        [0]*14,  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Julie Morrel (receiving unexpected aid through her)
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Maximilian Morrel (emotional support)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Cocles (dependability in crisis)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]   # Towards Emmanuel (trust and reliance in managing financial crisis)
    ],
    # Julie Morrel
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards M. Morrel (delivering crucial help)
        [0]*14,  # Towards herself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (sisterly concern and support)
        [0]*14,  # Towards Cocles (no direct interaction)
        [0]*14   # Towards Emmanuel (no direct interaction)
    ],
    # Maximilian Morrel
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards M. Morrel (supportive and concerned)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Julie Morrel (caring and supportive)
        [0]*14,  # Towards himself
        [0]*14,  # Towards Cocles (no direct interaction)
        [0]*14   # Towards Emmanuel (no direct interaction)
    ],
    # Cocles
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards M. Morrel (loyalty in financial handling)
        [0]*14,  # Towards Julie Morrel (no direct interaction)
        [0]*14,  # Towards Maximilian Morrel (no direct interaction)
        [0]*14,  # Towards himself
        [0]*14   # Towards Emmanuel (no direct interaction)
    ],
    # Emmanuel
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards M. Morrel (assisting in managing the crisis)
        [0]*14,  # Towards Julie Morrel (no direct interaction)
        [0]*14,  # Towards Maximilian Morrel (no direct interaction)
        [0]*14,  # Towards Cocles (no direct interaction)
        [0]*14   # Towards himself
    ]
]


chap33_names = ["Franz d'Épinay", "Gaetano", "Sailors", "Sinbad the Sailor"]

chap33_data = [
    # Franz d'Épinay
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 7, 7, 0, 8, 0, 8, 0],  # Towards Gaetano (trust and dependency for guidance)
        [7, 0, 0, 0, 7, 0, 8, 6, 6, 0, 7, 0, 7, 0],  # Towards Sailors (general trust but cautious)
        [9, 0, 0, 0, 9, 0, 10, 8, 8, 0, 9, 0, 9, 0]  # Towards Sinbad the Sailor (fascination and respect for the mysterious host)
    ],
    # Gaetano
    [
        [8, 0, 0, 0, 8, 0, 9, 7, 7, 0, 8, 0, 8, 0],  # Towards Franz d'Épinay (professional responsibility and care)
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 7, 7, 0, 8, 0, 8, 0],  # Towards Sailors (leadership and command)
        [8, 0, 0, 0, 8, 0, 9, 7, 7, 0, 8, 0, 8, 0]  # Towards Sinbad the Sailor (respect and cautious interaction)
    ],
    # Sailors
    [
        [7, 0, 0, 0, 7, 0, 8, 6, 6, 0, 7, 0, 7, 0],  # Towards Franz d'Épinay (compliance and general neutral behavior)
        [8, 0, 0, 0, 8, 0, 9, 7, 7, 0, 8, 0, 8, 0],  # Towards Gaetano (obedience and following orders)
        [0]*14,  # Towards themselves
        [7, 0, 0, 0, 7, 0, 8, 6, 6, 0, 7, 0, 7, 0]  # Towards Sinbad the Sailor (neutral, doing as commanded)
    ],
    # Sinbad the Sailor
    [
        [9, 0, 0, 0, 9, 0, 10, 8, 8, 0, 9, 0, 9, 0],  # Towards Franz d'Épinay (welcoming and intriguing)
        [8, 0, 0, 0, 8, 0, 9, 7, 7, 0, 8, 0, 8, 0],  # Towards Gaetano (commanding but fair)
        [7, 0, 0, 0, 7, 0, 8, 6, 6, 0, 7, 0, 7, 0],  # Towards Sailors (authoritative and distant)
        [0]*14  # Towards himself
    ]
]

chap34_names = ["Franz d'Épinay", "Sinbad the Sailor", "Gaetano", "Sailors"]

chap34_data = [
    # Franz d'Épinay
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Sinbad the Sailor (fascinated and intrigued by his host)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Gaetano (relying on his guidance and expertise)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0]   # Towards Sailors (general trust but cautious)
    ],
    # Sinbad the Sailor
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Franz d'Épinay (enjoys sharing his wealth and mysteries)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Gaetano (commands with respect)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards Sailors (authoritative but fair)
    ],
    # Gaetano
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Franz d'Épinay (helpful and loyal)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Sinbad the Sailor (respectful and obedient)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards Sailors (leadership and command)
    ],
    # Sailors
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Franz d'Épinay (neutral, follow orders)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Sinbad the Sailor (obedience and respect)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Gaetano (follow his command)
        [0]*14  # Towards themselves
    ]
]
chap34_names = ["Franz d'Épinay", "Sinbad the Sailor", "Gaetano", "Sailors"]

chap34_data = [
    # Franz d'Épinay
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Sinbad the Sailor (fascinated and intrigued by his host)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Gaetano (relying on his guidance and expertise)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0]   # Towards Sailors (general trust but cautious)
    ],
    # Sinbad the Sailor
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Franz d'Épinay (enjoys sharing his wealth and mysteries)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Gaetano (commands with respect)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards Sailors (authoritative but fair)
    ],
    # Gaetano
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Franz d'Épinay (helpful and loyal)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Sinbad the Sailor (respectful and obedient)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards Sailors (leadership and command)
    ],
    # Sailors
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Franz d'Épinay (neutral, follow orders)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Sinbad the Sailor (obedience and respect)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Gaetano (follow his command)
        [0]*14  # Towards themselves
    ]
]

chap35_names = ["Franz d'Épinay", "Albert de Morcerf"]

chap35_data = [
    # Franz d'Épinay
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 8, 8, 0, 8, 0, 9, 0]  # Towards Albert de Morcerf (partners in adventure and exploration)
    ],
    # Albert de Morcerf
    [
        [7, 0, 0, 0, 7, 0, 8, 8, 8, 0, 8, 0, 9, 0],  # Towards Franz d'Épinay (mutual enjoyment of their journey and mishaps)
        [0]*14  # Towards himself
    ]
]

chap36_names = ["Franz d'Épinay", "Sinbad the Sailor", "Gaetano", "Cicerone"]

chap36_data = [
    # Franz d'Épinay
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 7, 0, 8, 0],  # Towards Sinbad the Sailor (interest and intrigue)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 7, 0],  # Towards Gaetano (dependence for guidance)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 6, 0]   # Towards Cicerone (usual guide interaction)
    ],
    # Sinbad the Sailor
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 7, 0, 8, 0],  # Towards Franz d'Épinay (enigmatic guidance)
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 7, 0],  # Towards Gaetano (commanding presence)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 6, 0]   # Towards Cicerone (minimal direct interaction)
    ],
    # Gaetano
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 7, 0],  # Towards Franz d'Épinay (providing service)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 7, 0],  # Towards Sinbad the Sailor (respect and obedience)
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 7, 0]   # Towards Cicerone (colleague interaction)
    ],
    # Cicerone
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 6, 0],  # Towards Franz d'Épinay (usual service)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 6, 0],  # Towards Sinbad the Sailor (minimal interaction)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 7, 0],  # Towards Gaetano (professional relation)
        [0]*14  # Towards himself
    ]
]

chap37_names = ["Franz d'Épinay", "Albert de Morcerf", "The Count of Edmond"]

chap37_data = [
    # Franz d'Épinay
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 7, 0, 8, 0],  # Towards Albert de Morcerf (friendship and shared experiences)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards The Count of Edmond (fascination and some trepidation)
    ],
    # Albert de Morcerf
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 7, 0, 8, 0],  # Towards Franz d'Épinay (close friendship)
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards The Count of Edmond (admiration and intrigue)
    ],
    # The Count of Edmond
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Franz d'Épinay (mysterious guidance and manipulation)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Albert de Morcerf (intrigue and underlying motives)
        [0]*14  # Towards himself
    ]
]

chap38_names = ["The Count of Edmond", "Albert de Morcerf", "Franz d'Épinay"]

chap38_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Albert de Morcerf (gratitude and manipulation)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]   # Towards Franz d'Épinay (suspicion and curiosity)
    ],
    # Albert de Morcerf
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (trust and admiration)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards Franz d'Épinay (friendship and reliance)
    ],
    # Franz d'Épinay
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (wariness and intrigue)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Albert de Morcerf (close friendship)
        [0]*14   # Towards himself
    ]
]

chap39_names = ["Franz d'Épinay", "Albert de Morcerf"]

chap39_data = [
    # Franz d'Épinay
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Albert de Morcerf (protective and concerned)
    ],
    # Albert de Morcerf
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Franz d'Épinay (trust and dependence)
        [0]*14  # Towards himself
    ]
]

chap40_names = ["The Count of Edmond", "Maximilian Morrel", "Valentine de Villefort", "Noirtier"]

chap40_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Maximilian Morrel (deep intrigue and strategic alliance)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Valentine de Villefort (interest in her wellbeing and role in plans)
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0]  # Towards Noirtier (respect and recognition of his position within the Villefort family)
    ],
    # Maximilian Morrel
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (admiration and loyalty)
        [0]*14,  # Towards himself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Valentine de Villefort (love and deep affection)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Noirtier (respect due to his connection with Valentine)
    ],
    # Valentine de Villefort
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (curiosity and mild apprehension)
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Maximilian Morrel (reciprocated love and trust)
        [0]*14,  # Towards herself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Noirtier (deep familial love and dependence)
    ],
    # Noirtier
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (acknowledgment of his influence)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (favorable view due to Valentine)
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Valentine de Villefort (protective and loving grandfather)
        [0]*14  # Towards himself
    ]
]

chap40_names = ["The Count of Edmond", "Maximilian Morrel", "Valentine de Villefort", "Noirtier"]

chap40_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Maximilian Morrel (deep intrigue and strategic alliance)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Valentine de Villefort (interest in her wellbeing and role in plans)
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0]  # Towards Noirtier (respect and recognition of his position within the Villefort family)
    ],
    # Maximilian Morrel
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (admiration and loyalty)
        [0]*14,  # Towards himself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Valentine de Villefort (love and deep affection)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Noirtier (respect due to his connection with Valentine)
    ],
    # Valentine de Villefort
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (curiosity and mild apprehension)
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Maximilian Morrel (reciprocated love and trust)
        [0]*14,  # Towards herself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Noirtier (deep familial love and dependence)
    ],
    # Noirtier
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (acknowledgment of his influence)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (favorable view due to Valentine)
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Valentine de Villefort (protective and loving grandfather)
        [0]*14  # Towards himself
    ]
]
chap41_names = ["The Count of Edmond", "Villefort"]

chap41_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0]  # Towards Villefort (complex manipulation and psychological play)
    ],
    # Villefort
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (intrigue, fear, and respect)
        [0]*14  # Towards himself
    ]
]


chap42_names = ["Albert de Morcerf", "Beauchamp", "Debray", "Château-Renaud", "Maximilian Morrel"]

chap42_data = [
    # Albert de Morcerf
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Beauchamp (friend and occasional confidant)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray (social acquaintance, somewhat distant)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Château-Renaud (close friend and confidant)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]   # Towards Maximilian Morrel (admiration and respect)
    ],
    # Beauchamp
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Albert de Morcerf
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray (colleague and competitor)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Château-Renaud
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0]   # Towards Maximilian Morrel (slightly formal respect)
    ],
    # Debray
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Albert de Morcerf
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Beauchamp
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Château-Renaud
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0]   # Towards Maximilian Morrel
    ],
    # Château-Renaud
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Albert de Morcerf
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Beauchamp
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]   # Towards Maximilian Morrel (respect for his heroic deeds)
    ],
    # Maximilian Morrel
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Albert de Morcerf
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Debray
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Château-Renaud
        [0]*14   # Towards himself
    ]
]

chap43_names = ["Albert de Morcerf", "The Count of Edmond", "Various guests"]

chap43_data = [
    # Albert de Morcerf
    [
        [0]*14,  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (admiration and dependency)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards Various guests (general sociability)
    ],
    # The Count of Edmond
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Albert de Morcerf (fondness and manipulation)
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]   # Towards Various guests (polite but distant)
    ],
    # Various guests
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Albert de Morcerf (respect for the host)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (curiosity and admiration)
        [0]*14   # Towards themselves
    ]
]

chap44_names = ["The Count of Edmond", "Bertuccio", "The Notary"]

chap44_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Bertuccio (master and servant relationship with some tension)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards The Notary (professional and transactional interaction)
    ],
    # Bertuccio
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (fear and respect)
        [0]*14,  # Towards himself
        [0]*14   # Towards The Notary (no significant interaction)
    ],
    # The Notary
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (professional courtesy and service)
        [0]*14,  # Towards Bertuccio (no significant interaction)
        [0]*14   # Towards himself
    ]
]

chap45_names = ["The Count of Edmond", "Bertuccio", "Concierge"]

chap45_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Bertuccio (deeply involved in uncovering Bertuccio's past)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Concierge (functional and authoritative interaction)
    ],
    # Bertuccio
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (conflicted emotions due to past events)
        [0]*14,  # Towards himself
        [0]*14   # Towards Concierge (no significant interaction)
    ],
    # Concierge
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (respect and compliance)
        [0]*14,  # Towards Bertuccio (no significant interaction)
        [0]*14   # Towards himself
    ]
]

chap46_names = ["Bertuccio", "The Count of Edmond"]

chap46_data = [
    # Bertuccio
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards The Count of Edmond (respect and fear due to the Count's power and knowledge)
    ],
    # The Count of Edmond
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Bertuccio (curiosity and utilitarian interest in Bertuccio's knowledge and abilities)
        [0]*14  # Towards himself
    ]
]

chap47_names = ["Caderousse", "La Carconte", "The Jeweller"]

chap47_data = [
    # Caderousse
    [
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards La Carconte (distrust and manipulation in their relationship)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards The Jeweller (greed and deceit in their interaction)
    ],
    # La Carconte
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Caderousse (complicity and unease)
        [0]*14,  # Towards herself
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0]  # Towards The Jeweller (guarded and opportunistic)
    ],
    # The Jeweller
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Caderousse (suspicion and caution)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards La Carconte (wary and calculating)
        [0]*14  # Towards himself
    ]
]

chap48_names = ["The Count of Edmond", "Baron Danglars"]

chap48_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Baron Danglars (manipulative and strategic interactions)
    ],
    # Baron Danglars
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (wary and somewhat intimidated)
        [0]*14  # Towards himself
    ]
]

chap49_names = ["Madame Danglars", "Lucien Debray", "The Count of Edmond"]

chap49_data = [
    # Madame Danglars
    [
        [0]*14,  # Towards herself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Lucien Debray (close and confidential relationship)
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0]  # Towards The Count of Edmond (impressed and intrigued)
    ],
    # Lucien Debray
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Madame Danglars (mutually beneficial relationship)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards The Count of Edmond (respectful and cautious)
    ],
    # The Count of Edmond
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Madame Danglars (charming and manipulative)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Lucien Debray (cordial with underlying motives)
        [0]*14  # Towards himself
    ]
]

chap50_names = ["The Count of Edmond", "Haydée"]

chap50_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Haydée (deep connection, paternal and protective feelings)
    ],
    # Haydée
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (devotion and deep respect)
        [0]*14  # Towards herself
    ]
]

chap50_names = ["The Count of Edmond", "Haydée"]

chap50_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Haydée (deep connection, paternal and protective feelings)
    ],
    # Haydée
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (devotion and deep respect)
        [0]*14  # Towards herself
    ]
]

chap51_names = ["Albert de Morcerf", "Mercédès"]

chap51_data = [
    # Albert de Morcerf
    [
        [0]*14,  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0]  # Towards Mercédès (mother, deep love and respect)
    ],
    # Mercédès
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Albert de Morcerf (son, profound love and protective feelings)
        [0]*14  # Towards herself
    ]
]

chap52_names = ["The Count of Edmond", "Haydée", "Maximilian Morrel", "Julie", "Emmanuel"]

chap52_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Haydée (paternal affection, deep care)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (mentorship, respect)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Julie (benevolence, kindness)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Emmanuel (respectful and formal relationship)
    ],
    # Haydée
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (devotion, gratitude)
        [0]*14,  # Towards herself
        [0]*14,  # Towards Maximilian Morrel (no significant interaction)
        [0]*14,  # Towards Julie (no significant interaction)
        [0]*14   # Towards Emmanuel (no significant interaction)
    ],
    # Maximilian Morrel
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (admiration, loyalty)
        [0]*14,  # Towards Haydée (no significant interaction)
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Julie (sibling affection and care)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]   # Towards Emmanuel (brotherly relationship)
    ],
    # Julie
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (gratitude, respect)
        [0]*14,  # Towards Haydée (no significant interaction)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (sisterly love and care)
        [0]*14,  # Towards herself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0]  # Towards Emmanuel (deep love as a spouse)
    ],
    # Emmanuel
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (respect, gratitude)
        [0]*14,  # Towards Haydée (no significant interaction)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (brotherly bond)
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Julie (love, marital bond)
        [0]*14  # Towards himself
    ]
]
chap53_names = ["The Count of Edmond", "Maximilian Morrel", "Julie", "Emmanuel", "Cocles"]

chap53_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (mentorship and deep care)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Julie (fondness and respect)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Emmanuel (professional respect)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0]  # Towards Cocles (respect for his loyalty and service)
    ],
    # Maximilian Morrel
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (admiration, gratitude)
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Julie (sisterly affection)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Emmanuel (brother-in-law and friend)
        [0]*14  # Towards Cocles (limited interaction)
    ],
    # Julie
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (grateful and respectful)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (sibling love and care)
        [0]*14,  # Towards herself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Emmanuel (devoted wife)
        [0]*14  # Towards Cocles (no significant interaction)
    ],
    # Emmanuel
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (respectful and professional)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (close family bond)
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Julie (loving husband)
        [0]*14,  # Towards himself
        [0]*14  # Towards Cocles (limited interaction)
    ],
    # Cocles
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards The Count of Edmond (respect for the Count's status and authority)
        [0]*14,  # Towards Maximilian Morrel (limited interaction)
        [0]*14,  # Towards Julie (limited interaction)
        [0]*14,  # Towards Emmanuel (limited interaction)
        [0]*14  # Towards himself
    ]
]
chap54_names = ["Valentine", "Maximilian"]

chap54_data = [
    # Valentine
    [
        [0]*14,  # Towards herself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Maximilian (deep affection and emotional reliance)
    ],
    # Maximilian
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Valentine (devoted love and commitment to protect)
        [0]*14  # Towards himself
    ]
]

chap55_names = ["Madame de Villefort", "Edward", "The Count of Edmond", "Valentine"]

chap55_data = [
    # Madame de Villefort
    [
        [0]*14,  # Towards herself
        [5, 0, 0, 0, 5, 0, 5, 5, 5, 0, 5, 0, 5, 0],  # Towards Edward (frustration but affection for her mischievous son)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (fascination and intrigue)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards Valentine (concern mixed with detachment)
    ],
    # Edward
    [
        [5, 0, 0, 0, 5, 0, 5, 5, 5, 0, 5, 0, 5, 0],  # Towards Madame de Villefort (playful indifference)
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards The Count of Edmond (childish curiosity)
        [0]*14   # Towards Valentine (typical sibling unawareness)
    ],
    # The Count of Edmond
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Madame de Villefort (calculative engagement)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Edward (amused tolerance)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards Valentine (sympathetic protector)
    ],
    # Valentine
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Madame de Villefort (resigned tolerance)
        [0]*14,  # Towards Edward (sibling neutrality)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (respect and trust)
        [0]*14  # Towards herself
    ]
]

chap56_names = ["The Count of Edmond", "Albert de Morcerf", "Bertuccio", "Lucien Debray", "Baptistin"]

chap56_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Albert de Morcerf (complex mentor-like relationship)
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Bertuccio (loyalty and service)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Lucien Debray (social interaction, not close)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Baptistin (faithful servant)
    ],
    # Albert de Morcerf
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (admiration, intrigue)
        [0]*14,  # Towards himself
        [0]*14,  # Towards Bertuccio (minimal interaction)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Lucien Debray (friend)
        [0]*14  # Towards Baptistin (no significant interaction)
    ],
    # Bertuccio
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (devotion, gratitude)
        [0]*14,  # Towards Albert de Morcerf (minimal interaction)
        [0]*14,  # Towards himself
        [0]*14,  # Towards Lucien Debray (no interaction)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Baptistin (work-related interactions)
    ],
    # Lucien Debray
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (social acquaintance)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Albert de Morcerf (friendship)
        [0]*14,  # Towards Bertuccio (no interaction)
        [0]*14,  # Towards himself
        [0]*14  # Towards Baptistin (no interaction)
    ],
    # Baptistin
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (loyal servant)
        [0]*14,  # Towards Albert de Morcerf (no significant interaction)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Bertuccio (colleague, similar roles)
        [0]*14,  # Towards Lucien Debray (no interaction)
        [0]*14  # Towards himself
    ]
]
chap57_names = ["The Count of Edmond", "Albert de Morcerf", "Madame Danglars", "Eugénie Danglars", "Lucien Debray"]

chap57_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Albert de Morcerf (mentor-like, with complexity due to Albert's family history)
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Madame Danglars (manipulative, strategic interests)
        [0]*14,  # Towards Eugénie Danglars (indirect influence, no direct interaction)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Lucien Debray (social acquaintance, nuanced through political connections)
    ],
    # Albert de Morcerf
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards The Count of Edmond (admiration mixed with emerging suspicion)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Madame Danglars (social interaction, mutual respect in society)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Eugénie Danglars (acquaintance, little personal connection)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Lucien Debray (friendship through social and familial ties)
    ],
    # Madame Danglars
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (fascination and intrigue)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Albert de Morcerf (social politeness, acquaintance)
        [0]*14,  # Towards herself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Eugénie Danglars (maternal relationship with formal interactions)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0]  # Towards Lucien Debray (acquaintance through political and social interactions)
    ],
    # Eugénie Danglars
    [
        [0]*14,  # Towards The Count of Edmond (no direct interaction)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Albert de Morcerf (formal acquaintance, lack of personal connection)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Madame Danglars (complex maternal relationship)
        [0]*14,  # Towards herself
        [0]*14  # Towards Lucien Debray (no significant interaction)
    ],
    # Lucien Debray
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (acquaintance with reserved curiosity)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Albert de Morcerf (social and familial friendship)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Madame Danglars (political and social connection)
        [0]*14,  # Towards Eugénie Danglars (limited to no interaction)
        [0]*14  # Towards himself
    ]
]
chap58_names = ["The Count of Edmond", "Major Cavalcanti", "Baptistin"]

chap58_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Major Cavalcanti (manipulative and authoritative)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]   # Towards Baptistin (loyal servant, responsible)
    ],
    # Major Cavalcanti
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (reliant and manipulated)
        [0]*14,  # Towards himself
        [0]*14   # Towards Baptistin (minimal interaction)
    ],
    # Baptistin
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (servitude and loyalty)
        [0]*14,  # Towards Major Cavalcanti (no significant interaction)
        [0]*14   # Towards himself
    ]
]

chap59_names = ["The Count of Edmond", "Andrea Cavalcanti", "Baptistin"]

chap59_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards Andrea Cavalcanti (scheming, manipulative support)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Baptistin (servitude, reliable execution of duties)
    ],
    # Andrea Cavalcanti
    [
        [9, 0, 0, 0, 9, 0, 10, 9, 9, 0, 10, 0, 10, 0],  # Towards The Count of Edmond (manipulated, reliant on his support)
        [0]*14,  # Towards himself
        [0]*14   # Towards Baptistin (no significant interaction)
    ],
    # Baptistin
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (loyal and obedient)
        [0]*14,  # Towards Andrea Cavalcanti (no significant interaction)
        [0]*14   # Towards himself
    ]
]




chap60_names = ["Valentine", "Madame Danglars", "Eugénie Danglars", "Maximilian"]

chap60_data = [
    # Valentine
    [
        [0]*14,  # Towards herself
        [0]*14,  # Towards Madame Danglars (no significant direct interaction mentioned)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Eugénie Danglars (sympathy and mutual confidences)
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Maximilian (deep love and affection)
    ],
    # Madame Danglars
    [
        [0]*14,  # Towards Valentine (no significant direct interaction mentioned)
        [0]*14,  # Towards herself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Eugénie Danglars (complex mother-daughter relationship)
        [0]*14  # Towards Maximilian (no interaction)
    ],
    # Eugénie Danglars
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Valentine (shared confidences and understanding)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Madame Danglars (strained relationship)
        [0]*14,  # Towards herself
        [0]*14  # Towards Maximilian (no interaction)
    ],
    # Maximilian
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Valentine (deep love and affection)
        [0]*14,  # Towards Madame Danglars (no interaction)
        [0]*14,  # Towards Eugénie Danglars (no interaction)
        [0]*14  # Towards himself
    ]
]

chap61_names = ["Valentine", "Villefort", "Madame de Villefort", "Noirtier"]

chap61_data = [
    # Valentine
    [
        [0]*14,  # Towards herself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Villefort (tension and disagreement over marriage plans)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Madame de Villefort (discomfort and disagreement)
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Noirtier (deep affection and mutual understanding)
    ],
    # Villefort
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Valentine (authoritative and imposing decisions)
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Madame de Villefort (partner in decision-making)
        [0]*14  # Towards Noirtier (minimal direct interaction described)
    ],
    # Madame de Villefort
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Valentine (manipulative and controlling behavior)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Villefort (supportive and complicit in plans)
        [0]*14,  # Towards herself
        [0]*14  # Towards Noirtier (no significant interaction)
    ],
    # Noirtier
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Valentine (deep affection and protective)
        [0]*14,  # Towards Villefort (strained relationship, no direct interaction mentioned)
        [0]*14,  # Towards Madame de Villefort (no interaction)
        [0]*14  # Towards himself
    ]
]

chap62_names = ["Villefort", "Edmond", "Valentine", "Épinay", "Noirtier"]

chap62_data = [
    # Villefort
    [
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Edmond (professional respect but underlying tension)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Valentine (paternal affection but conflicting interests)
        [0]*14,  # Towards Épinay (no significant interaction)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0]   # Towards Noirtier (strained familial relationships)
    ],
    # Edmond
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Villefort (curiosity and manipulative interest)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Valentine (sympathetic observer)
        [0]*14,  # Towards Épinay (no significant interaction)
        [0]*14  # Towards Noirtier (interest in his condition and actions)
    ],
    # Valentine
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Villefort (mixed feelings due to familial conflict)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Edmond (trust and reliance)
        [0]*14,  # Towards herself
        [0]*14,  # Towards Épinay (engaged but conflicted)
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0]  # Towards Noirtier (deep affection and alliance)
    ],
    # Épinay
    [
        [0]*14,  # Towards Villefort (no significant interaction)
        [0]*14,  # Towards Edmond (no significant interaction)
        [0]*14,  # Towards Valentine (fiancé but emotionally distant)
        [0]*14,  # Towards himself
        [0]*14  # Towards Noirtier (no direct interaction)
    ],
    # Noirtier
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Villefort (disapproval and opposition)
        [0]*14,  # Towards Edmond (no significant interaction)
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Valentine (love and protective intentions)
        [0]*14,  # Towards Épinay (opposition to his involvement with Valentine)
        [0]*14  # Towards himself
    ]
]
chap63_names = ["Villefort", "Edmond", "Danglars"]

chap63_data = [
    # Villefort
    [
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Edmond (underlying distrust and caution)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Danglars (professional courtesy but competitive)
    ],
    # Edmond
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Villefort (manipulative, probing for weaknesses)
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Danglars (disguised antagonism, seeking leverage)
    ],
    # Danglars
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Villefort (rivalry under the guise of professionalism)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Edmond (wary respect and fear)
        [0]*14  # Towards himself
    ]
]

chap64_names = ["The Count of Edmond", "Bertuccio", "Maximilian Morrel", "Château-Renaud", "Debray", "Danglars", "Cavalcanti"]

chap64_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Bertuccio (trusted servant, intricate relationship)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Maximilian Morrel (protective, mentor-like role)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Château-Renaud (acquaintance, social interactions)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray (social, wary interactions)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Danglars (complex, often antagonistic)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]   # Towards Cavalcanti (manipulative, part of a larger scheme)
    ],
    # Bertuccio
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (loyalty and obedience)
        [0]*14,  # Towards himself
        [0]*14,  # Towards Maximilian Morrel (no significant interaction)
        [0]*14,  # Towards Château-Renaud (no interaction)
        [0]*14,  # Towards Debray (no interaction)
        [0]*14,  # Towards Danglars (no interaction)
        [0]*14  # Towards Cavalcanti (no interaction)
    ],
    # Maximilian Morrel
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (admiration, loyalty)
        [0]*14,  # Towards Bertuccio (no significant interaction)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Château-Renaud (friendship, social ties)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray (acquaintance, social)
        [0]*14,  # Towards Danglars (no direct interaction)
        [0]*14  # Towards Cavalcanti (no interaction)
    ],
    # Château-Renaud
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (social acquaintance)
        [0]*14,  # Towards Bertuccio (no interaction)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Maximilian Morrel (friendship, social circle)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray (friends, social circle)
        [0]*14,  # Towards Danglars (no significant interaction)
        [0]*14  # Towards Cavalcanti (no significant interaction)
    ],
    # Debray
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (social, cautious interactions)
        [0]*14,  # Towards Bertuccio (no interaction)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Maximilian Morrel (acquaintance, social)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Château-Renaud (friends, social circle)
        [0]*14,  # Towards himself
        [0]*14,  # Towards Danglars (no significant interaction)
        [0]*14  # Towards Cavalcanti (no significant interaction)
    ],
    # Danglars
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (antagonistic, wary)
        [0]*14,  # Towards Bertuccio (no interaction)
        [0]*14,  # Towards Maximilian Morrel (no interaction)
        [0]*14,  # Towards Château-Renaud (no significant interaction)
        [0]*14,  # Towards Debray (no significant interaction)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Cavalcanti (complex, financial and social ties)
    ],
    # Cavalcanti
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (manipulated, dependent)
        [0]*14,  # Towards Bertuccio (no interaction)
        [0]*14,  # Towards Maximilian Morrel (no interaction)
        [0]*14,  # Towards Château-Renaud (no significant interaction)
        [0]*14,  # Towards Debray (no significant interaction)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Danglars (complex, part of financial schemes)
        [0]*14  # Towards himself
    ]
]
chap65_names = ["The Count of Edmond", "Villefort", "Danglars", "Debray", "Château-Renaud", "Cavalcanti", "Bertuccio"]

chap65_data = [
    # The Count of Edmond
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Villefort (complex, manipulative intent)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Danglars (antagonistic, financial manipulation)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray (social and strategic interactions)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Château-Renaud (social acquaintance)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Cavalcanti (manipulative, controlled interaction)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]   # Towards Bertuccio (trusted servant, integral to schemes)
    ],
    # Villefort
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (wary, under manipulation)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Danglars (professional, competitive)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray (professional ties)
        [0]*14,  # Towards Château-Renaud (no significant interaction)
        [0]*14,  # Towards Cavalcanti (no significant interaction)
        [0]*14  # Towards Bertuccio (no interaction)
    ],
    # Danglars
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (antagonism, financial fears)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Villefort (professional rivalry)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray (social and financial connections)
        [0]*14,  # Towards Château-Renaud (no significant interaction)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Cavalcanti (financial schemes)
        [0]*14  # Towards Bertuccio (no interaction)
    ],
    # Debray
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (social interactions, wary)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Villefort (professional interactions)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Danglars (social acquaintance)
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Château-Renaud (friendship)
        [0]*14,  # Towards Cavalcanti (no significant interaction)
        [0]*14  # Towards Bertuccio (no interaction)
    ],
    # Château-Renaud
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (social acquaintance)
        [0]*14,  # Towards Villefort (no interaction)
        [0]*14,  # Towards Danglars (no significant interaction)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Debray (friends, social circle)
        [0]*14,  # Towards himself
        [0]*14,  # Towards Cavalcanti (no significant interaction)
        [0]*14  # Towards Bertuccio (no interaction)
    ],
    # Cavalcanti
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards The Count of Edmond (manipulated, part of schemes)
        [0]*14,  # Towards Villefort (no interaction)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Danglars (financial connections, part of schemes)
        [0]*14,  # Towards Debray (no significant interaction)
        [0]*14,  # Towards Château-Renaud (no interaction)
        [0]*14,  # Towards himself
        [0]*14  # Towards Bertuccio (no interaction)
    ],
    # Bertuccio
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards The Count of Edmond (deep loyalty and service)
        [0]*14,  # Towards Villefort (no significant interaction)
        [0]*14,  # Towards Danglars (no interaction)
        [0]*14,  # Towards Debray (no interaction)
        [0]*14,  # Towards Château-Renaud (no interaction)
        [0]*14,  # Towards Cavalcanti (no interaction)
        [0]*14  # Towards himself
    ]
]

chap66_names = ["Danglars", "Cavalcanti", "Andrea Cavalcanti", "Caderousse"]

chap66_data = [
    # Danglars
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Cavalcanti (financial interest, superficial cordiality)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Andrea Cavalcanti (similar motivations as with Cavalcanti)
        [3, 0, 0, 0, 3, 0, 4, 3, 3, 0, 4, 0, 4, 0]   # Towards Caderousse (distrust, unease)
    ],
    # Cavalcanti
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Danglars (allied for mutual benefit)
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Andrea Cavalcanti (paternal yet formal relationship)
        [0]*14  # Towards Caderousse (no direct interaction)
    ],
    # Andrea Cavalcanti
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Danglars (utilitarian, seeking advantage)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Cavalcanti (formal, somewhat distant)
        [0]*14,  # Towards himself
        [0]*14  # Towards Caderousse (no significant interaction)
    ],
    # Caderousse
    [
        [3, 0, 0, 0, 3, 0, 4, 3, 3, 0, 4, 0, 4, 0],  # Towards Danglars (animosity, past grievances)
        [0]*14,  # Towards Cavalcanti (no interaction)
        [0]*14,  # Towards Andrea Cavalcanti (no interaction)
        [0]*14  # Towards himself
    ]
]

chap67_names = ["Danglars", "Lucien Debray", "Madame Danglars"]

chap67_data = [
    # Danglars
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Lucien Debray (professional, connected through financial and social ties)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0]  # Towards Madame Danglars (strained, underlying tensions and conflicts)
    ],
    # Lucien Debray
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Danglars (mutual respect, financial interests)
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Madame Danglars (intimate, possibly more than just friends)
    ],
    # Madame Danglars
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Danglars (marital discord, lack of harmony)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Lucien Debray (complex emotional and possibly romantic involvement)
        [0]*14  # Towards herself
    ]
]

chap68_names = ["Danglars", "Cavalcanti", "Edmond", "Andrea", "Morcerf", "Fernand"]

chap68_data = [
    # Danglars
    [
        [0]*14,
        [7, 0, 0, 0, 7, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Cavalcanti (financial and social collaboration)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Edmond (suspicious and cautious)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Andrea (professional connection)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Morcerf (societal relations)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0]  # Towards Fernand (tense and competitive)
    ],
    # Cavalcanti
    [
        [7, 0, 0, 0, 7, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Danglars
        [0]*14,
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 6, 0],  # Towards Edmond
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Andrea (family ties)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Morcerf
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0]  # Towards Fernand
    ],
    # Edmond
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Danglars
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 6, 0],  # Towards Cavalcanti
        [0]*14,
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 7, 0, 7, 0],  # Towards Andrea (manipulative)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Morcerf
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 7, 0, 7, 0]  # Towards Fernand (vengeful)
    ],
    # Andrea
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Danglars
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Cavalcanti
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 7, 0, 7, 0],  # Towards Edmond
        [0]*14,
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Morcerf
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0]  # Towards Fernand
    ],
    # Morcerf
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Danglars
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Cavalcanti
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Edmond
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Andrea
        [0]*14,
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Fernand (intense rivalry)
    ],
    # Fernand
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Danglars
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Cavalcanti
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 7, 0, 7, 0],  # Towards Edmond
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Andrea
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Morcerf
        [0]*14
    ]
]

chap69_names = ["Danglars", "Villefort", "Edmond"]

chap69_data = [
    # Danglars
    [
        [0]*14,
        [6, 0, 0, 0, 6, 0, 6, 6, 6, 0, 6, 0, 6, 0],  # Towards Villefort (strained legal and social interactions)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 5, 0]  # Towards Edmond (distrust and fear)
    ],
    # Villefort
    [
        [6, 0, 0, 0, 6, 0, 6, 6, 6, 0, 6, 0, 6, 0],  # Towards Danglars
        [0]*14,
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 5, 0]  # Towards Edmond (wary of potential exposure)
    ],
    # Edmond
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 5, 0],  # Towards Danglars
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 5, 0],  # Towards Villefort
        [0]*14
    ]
]

chap70_names = ["Danglars", "Albert", "Edmond", "Villefort"]

chap70_data = [
    # Danglars
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Albert (strained familial relationship)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Edmond (tense, distrust)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0]  # Towards Villefort (complex legal entanglements)
    ],
    # Albert
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Danglars
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Edmond (friendship and admiration)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0]  # Towards Villefort (formal societal interactions)
    ],
    # Edmond
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Danglars
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Albert
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 6, 5, 5, 0, 6, 0, 6, 0]  # Towards Villefort (mysterious and probing interactions)
    ],
    # Villefort
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Danglars
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Albert
        [6, 0, 0, 0, 6, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Edmond
        [0]*14  # Towards himself
    ]
]

chap71_names = ["Villefort", "Edmond", "Count Wilmore", "Abbé"]

chap71_data = [
    # Villefort
    [
        [0]*14,  # Towards himself
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Edmond (suspicion and fear)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Count Wilmore (respect due to assumed social standing)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Abbé (reverence and reliance on spiritual guidance)
    ],
    # Edmond
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Villefort
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Count Wilmore (mutual respect)
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Abbé (deep respect and trust)
    ],
    # Count Wilmore
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Villefort
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Edmond
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Abbé (respectful interactions)
    ],
    # Abbé
    [
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Villefort
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Edmond
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Count Wilmore
        [0]*14  # Towards himself
    ]
]

chap72_names = ["Morcerf", "Mercédès", "Danglars", "Villefort", "Albert", "Edmond"]

chap72_data = [
    # Morcerf
    [
        [0]*14,  # Towards himself
        [4, 0, 0, 0, 4, 0, 5, 4, 4, 0, 5, 0, 5, 0],  # Towards Mercédès (strained, familial tension)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Danglars (political rivalry)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Villefort (formal and distant)
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Albert (father-son relationship with underlying issues)
        [3, 0, 0, 0, 3, 0, 4, 3, 3, 0, 4, 0, 4, 0]  # Towards Edmond (hostile due to unfolding revenge)
    ],
    # Mercédès
    [
        [4, 0, 0, 0, 4, 0, 5, 4, 4, 0, 5, 0, 5, 0],  # Towards Morcerf
        [0]*14,  # Towards herself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Danglars (social acquaintance)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Villefort
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Albert (protective and loving mother)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0]  # Towards Edmond (complex past relationship)
    ],
    # Danglars
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Morcerf
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Mercédès
        [0]*14,  # Towards himself
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Villefort (professional connections)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Albert
        [4, 0, 0, 0, 4, 0, 5, 4, 4, 0, 5, 0, 5, 0]  # Towards Edmond (financial and personal animosity)
    ],
    # Villefort
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Morcerf
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Mercédès
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 6, 0, 6, 0],  # Towards Danglars
        [0]*14,  # Towards himself
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Albert
        [4, 0, 0, 0, 4, 0, 5, 4, 4, 0, 5, 0, 5, 0]  # Towards Edmond (legal and personal conflicts)
    ],
    # Albert
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Morcerf
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Mercédès
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Danglars
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Villefort
        [0]*14,  # Towards himself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Edmond (friendship and mentorship)
    ],
    # Edmond
    [
        [3, 0, 0, 0, 3, 0, 4, 3, 3, 0, 4, 0, 4, 0],  # Towards Morcerf
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 7, 0, 7, 0],  # Towards Mercédès
        [4, 0, 0, 0, 4, 0, 5, 4, 4, 0, 5, 0, 5, 0],  # Towards Danglars
        [4, 0, 0, 0, 4, 0, 5, 4, 4, 0, 5, 0, 5, 0],  # Towards Villefort
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Albert
        [0]*14  # Towards himself
    ]
]
chap73_names = ["Edmond", "Mercédès"]

chap73_data = [
    # Edmond
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Mercédès (complex emotions of past love and current conflicts)
    ],
    # Mercédès
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Edmond
        [0]*14  # Towards herself
    ]
]

chap74_names = ["Villefort", "Valentine", "Barrois"]

chap74_data = [
    # Villefort
    [
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Valentine (paternal concern mixed with professional detachment)
        [6, 0, 0, 0, 6, 0, 6, 6, 6, 0, 6, 0, 6, 0]  # Towards Barrois (employer to servant relationship)
    ],
    # Valentine
    [
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Villefort
        [0]*14,  # Towards herself
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0]  # Towards Barrois (familial affection)
    ],
    # Barrois
    [
        [6, 0, 0, 0, 6, 0, 6, 6, 6, 0, 6, 0, 6, 0],  # Towards Villefort
        [8, 0, 0, 0, 8, 0, 9, 8, 8, 0, 9, 0, 9, 0],  # Towards Valentine
        [0]*14  # Towards himself
    ]
]

chap76_names = ["Valentine", "Morrel", "Villefort", "Madame de Villefort"]

chap76_data = [
    # Valentine
    [
        [0]*14,  # Towards herself
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Morrel (deep love and devotion)
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Villefort (conflicted feelings due to family loyalty)
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 5, 0]  # Towards Madame de Villefort (distant and strained relationship)
    ],
    # Morrel
    [
        [10, 0, 0, 0, 10, 0, 10, 10, 10, 0, 10, 0, 10, 0],  # Towards Valentine
        [0]*14,  # Towards himself
        [4, 0, 0, 0, 4, 0, 5, 4, 4, 0, 4, 0, 4, 0],  # Towards Villefort (antagonistic due to obstacles)
        [3, 0, 0, 0, 3, 0, 4, 3, 3, 0, 3, 0, 3, 0]  # Towards Madame de Villefort (mistrust and disdain)
    ],
    # Villefort
    [
        [6, 0, 0, 0, 6, 0, 7, 6, 6, 0, 6, 0, 6, 0],  # Towards Valentine
        [4, 0, 0, 0, 4, 0, 5, 4, 4, 0, 4, 0, 4, 0],  # Towards Morrel
        [0]*14,  # Towards himself
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0]  # Towards Madame de Villefort (complex relationship with moments of alliance and opposition)
    ],
    # Madame de Villefort
    [
        [5, 0, 0, 0, 5, 0, 6, 5, 5, 0, 5, 0, 5, 0],  # Towards Valentine
        [3, 0, 0, 0, 3, 0, 4, 3, 3, 0, 3, 0, 3, 0],  # Towards Morrel
        [7, 0, 0, 0, 7, 0, 8, 7, 7, 0, 8, 0, 8, 0],  # Towards Villefort
        [0]*14  # Towards herself
    ]
]

chap114_names = ["Danglars", "Edmond", "Benedetto", "Villefort", "Eugénie Danglars"]
chap114_data = [
    # Danglars
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Benedetto
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Eugénie Danglars
    ],
    # Edmond
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Benedetto
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Eugénie Danglars
    ],
    # Benedetto
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Villefort
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Eugénie Danglars
    ],
    # Villefort
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Benedetto
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Eugénie Danglars
    ],
    # Eugénie Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Benedetto
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards herself
    ]
]

chap115_names = ["Danglars", "Edmond", "Villefort", "Madame Danglars"]
chap115_data = [
    # Danglars
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Edmond
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Madame Danglars
    ],
    # Edmond
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Madame Danglars
    ],
    # Villefort
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Madame Danglars
    ],
    # Madame Danglars
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards herself
    ]
]

chap113_names = ["Danglars", "Edmond", "Benedetto", "Villefort"]
chap113_data = [
    # Danglars
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Benedetto
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4]   # Towards Villefort
    ],
    # Edmond
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Benedetto
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Villefort
    ],
    # Benedetto
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Villefort
    ],
    # Villefort
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Benedetto
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap111_names = ["Villefort", "Benedetto", "President", "Lawyer", "Jury"]
chap111_data = [
    # Villefort
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Benedetto
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards President
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Lawyer
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Jury
    ],
    # Benedetto
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards President
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Lawyer
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Jury
    ],
    # President
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Benedetto
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Lawyer
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Jury
    ],
    # Lawyer
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Benedetto
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards President
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Jury
    ],
    # Jury
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Villefort
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Benedetto
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards President
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Lawyer
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap112_names = ["Danglars", "Benedetto", "Jury", "Villefort"]
chap112_data = [
    # Danglars
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Benedetto
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Jury
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4]   # Towards Villefort
    ],
    # Benedetto
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Jury
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Villefort
    ],
    # Jury
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Benedetto
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Villefort
    ],
    # Villefort
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Benedetto
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Jury
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap110_names = ["Valentine", "Villefort", "Morrel", "Edmond"]
chap110_data = [
    # Valentine
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Villefort
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6], # Towards Morrel
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5]   # Towards Edmond
    ],
    # Villefort
    [
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Edmond
    ],
    # Morrel
    [
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5]   # Towards Edmond
    ],
    # Edmond
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap110_names = ["Valentine", "Villefort", "Morrel", "Edmond"]
chap110_data = [
    # Valentine
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Villefort
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6], # Towards Morrel
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5]   # Towards Edmond
    ],
    # Villefort
    [
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Edmond
    ],
    # Morrel
    [
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5]   # Towards Edmond
    ],
    # Edmond
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap109_names = ["Danglars", "Edmond", "M. de Boville"]
chap109_data = [
    # Danglars
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards M. de Boville
    ],
    # Edmond
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards M. de Boville
    ],
    # M. de Boville
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]
chap108_names = ["Villefort", "Morrel", "Noirtier", "d’Avrigny"]
chap108_data = [
    # Villefort
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Noirtier
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4]   # Towards d’Avrigny
    ],
    # Morrel
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6], # Towards Noirtier
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4]   # Towards d’Avrigny
    ],
    # Noirtier
    [
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Villefort
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5]   # Towards d’Avrigny
    ],
    # d’Avrigny
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Morrel
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Noirtier
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap107_names = ["Valentine", "Madame de Villefort", "Villefort", "d’Avrigny", "Morrel"]
chap107_data = [
    # Valentine
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Towards Madame de Villefort
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards d’Avrigny
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6] # Towards Morrel
    ],
    # Madame de Villefort
    [
        [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards d’Avrigny
        [4, 0, 0, 0, 4, 4, 4, 4, 4, 3, 4, 3, 4, 3]   # Towards Morrel
    ],
    # Villefort
    [
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Madame de Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards d’Avrigny
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Morrel
    ],
    # d’Avrigny
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Madame de Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4]   # Towards Morrel
    ],
    # Morrel
    [
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Valentine
        [4, 0, 0, 0, 4, 4, 4, 4, 4, 3, 4, 3, 4, 3],  # Towards Madame de Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards d’Avrigny
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]
chap106_names = ["Valentine", "Madame de Villefort", "Edmond"]
chap106_data = [
    # Valentine
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2],  # Towards Madame de Villefort
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5]   # Towards Edmond
    ],
    # Madame de Villefort
    [
        [3, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 2, 3, 2],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Edmond
    ],
    # Edmond
    [
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Madame de Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]
chap105_names = ["Edmond", "Valentine", "Villefort", "Noirtier", "Morrel"]
chap105_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Noirtier
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4]   # Towards Morrel
    ],
    # Valentine
    [
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Noirtier
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6]   # Towards Morrel
    ],
    # Villefort
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Noirtier
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Morrel
    ],
    # Noirtier
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4]   # Towards Morrel
    ],
    # Morrel
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Edmond
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Noirtier
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap104_names = ["Danglars", "Madame Danglars", "Villefort", "Andrea Cavalcanti"]
chap104_data = [
    # Danglars
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Madame Danglars
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Villefort
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Andrea Cavalcanti
    ],
    # Madame Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Andrea Cavalcanti
    ],
    # Villefort
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Madame Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Andrea Cavalcanti
    ],
    # Andrea Cavalcanti
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Madame Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap103_names = ["Valentine", "Noirtier", "Villefort", "Morrel", "Edmond"]
chap103_data = [
    # Valentine
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Noirtier
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Morrel
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5]   # Towards Edmond
    ],
    # Noirtier
    [
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Morrel
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Edmond
    ],
    # Villefort
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Noirtier
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Edmond
    ],
    # Morrel
    [
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Valentine
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Noirtier
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5]   # Towards Edmond
    ],
    # Edmond
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Noirtier
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap102_names = ["Eugénie Danglars", "Louise d’Armilly", "Madame Danglars", "Porter"]
chap102_data = [
    # Eugénie Danglars
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Louise d’Armilly
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Madame Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Porter
    ],
    # Louise d’Armilly
    [
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Eugénie Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Madame Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Porter
    ],
    # Madame Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Eugénie Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Louise d’Armilly
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Porter
    ],
    # Porter
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Eugénie Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Louise d’Armilly
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Madame Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap101_names = ["Edmond", "Andrea Cavalcanti", "Danglars", "Eugénie Danglars", "Madame Danglars"]
chap101_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Andrea Cavalcanti
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Eugénie Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Madame Danglars
    ],
    # Andrea Cavalcanti
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Eugénie Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Madame Danglars
    ],
    # Danglars
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Edmond
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Andrea Cavalcanti
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Eugénie Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Madame Danglars
    ],
    # Eugénie Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Andrea Cavalcanti
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Madame Danglars
    ],
    # Madame Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Andrea Cavalcanti
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Eugénie Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards herself
    ]
]

chap100_names = ["Edmond", "Mercedes", "Albert", "Villefort"]
chap100_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6],  # Towards Mercedes
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Villefort
    ],
    # Mercedes
    [
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Villefort
    ],
    # Albert
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Mercedes
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Villefort
    ],
    # Villefort
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Mercedes
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap99_names = ["Danglars", "Eugénie Danglars", "Andrea Cavalcanti"]
chap99_data = [
    # Danglars
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Eugénie Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Andrea Cavalcanti
    ],
    # Eugénie Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Andrea Cavalcanti
    ],
    # Andrea Cavalcanti
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Eugénie Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap98_names = ["Villefort", "Morrel", "Noirtier", "Valentine", "D'Avrigny"]
chap98_data = [
    # Villefort
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Noirtier
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards D'Avrigny
    ],
    # Morrel
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Noirtier
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards D'Avrigny
    ],
    # Noirtier
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Villefort
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards D'Avrigny
    ],
    # Valentine
    [
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Villefort
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Morrel
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Noirtier
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards D'Avrigny
    ],
    # D'Avrigny
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Noirtier
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap97_names = ["Morrel", "Valentine", "Noirtier", "Madame Danglars", "Eugénie Danglars"]
chap97_data = [
    # Morrel
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Valentine
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Noirtier
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Madame Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Eugénie Danglars
    ],
    # Valentine
    [
        [10, 0, 0, 0, 10, 10, 10, 9, 9, 8, 9, 7, 9, 6],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Noirtier
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Madame Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Eugénie Danglars
    ],
    # Noirtier
    [
        [8, 0, 0, 0, 8, 8, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Morrel
        [9, 0, 0, 0, 9, 9, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Madame Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Eugénie Danglars
    ],
    # Madame Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Noirtier
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Eugénie Danglars
    ],
    # Eugénie Danglars
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Morrel
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Valentine
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Noirtier
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Madame Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards herself
    ]
]

chap96_names = ["Edmond", "Morcerf", "Mercedes", "Albert"]
chap96_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6],  # Towards Mercedes
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5]   # Towards Albert
    ],
    # Morcerf
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Mercedes
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Albert
    ],
    # Mercedes
    [
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morcerf
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5]   # Towards Albert
    ],
    # Albert
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Morcerf
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Mercedes
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]
chap95_names = ["Edmond", "Mercedes", "Albert", "Morrel", "Emmanuel"]
chap95_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6],  # Towards Mercedes
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Emmanuel
    ],
    # Mercedes
    [
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morrel
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Emmanuel
    ],
    # Albert
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Mercedes
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Emmanuel
    ],
    # Morrel
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Mercedes
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Emmanuel
    ],
    # Emmanuel
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Mercedes
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Albert
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap94_names = ["Edmond", "Maximilian Morrel", "Haydée"]
chap94_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Maximilian Morrel
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6]   # Towards Haydée
    ],
    # Maximilian Morrel
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Haydée
    ],
    # Haydée
    [
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Maximilian Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards herself
    ]
]

chap93_names = ["Edmond", "Ali", "Mercedes", "Edmond"]
chap93_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Ali
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6],  # Towards Mercedes
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Edmond
    ],
    # Ali
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Mercedes
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Edmond
    ],
    # Mercedes
    [
        [9, 0, 0, 0, 9, 9, 9, 9, 8, 9, 8, 7, 8, 6],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Ali
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5]   # Towards Edmond
    ],
    # Edmond
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Ali
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Mercedes
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap92_names = ["Edmond", "Edmond", "Mercédès", "Fernand"]
chap92_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Mercédès
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Fernand
    ],
    # Edmond
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Mercédès
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Fernand
    ],
    # Mercédès
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Fernand
    ],
    # Fernand
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Mercédès
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]


chap91_names = ["Beauchamp", "Morcerf", "Edmond", "Albert", "Château-Renaud", "Morrel", "Mercédès"]
chap91_data = [
    # Beauchamp
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Château-Renaud
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Mercédès
    ],
    # Morcerf
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Château-Renaud
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Mercédès
    ],
    # Edmond
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morcerf
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Château-Renaud
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Mercédès
    ],
    # Albert
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Beauchamp
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Château-Renaud
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Mercédès
    ],
    # Château-Renaud
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Beauchamp
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Morcerf
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Edmond
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Albert
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Morrel
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Mercédès
    ],
    # Morrel
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Albert
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Château-Renaud
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Mercédès
    ],
    # Mercédès
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Albert
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Château-Renaud
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards herself
    ]
]
chap90_names = ["Beauchamp", "Albert", "Morcerf", "Danglars", "Cavalcanti", "Edmond"]
chap90_data = [
    # Beauchamp
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Cavalcanti
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Edmond
    ],
    # Albert
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Beauchamp
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Cavalcanti
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Edmond
    ],
    # Morcerf
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Cavalcanti
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Edmond
    ],
    # Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Albert
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morcerf
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Cavalcanti
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Edmond
    ],
    # Cavalcanti
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Beauchamp
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Albert
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Morcerf
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Edmond
    ],
    # Edmond
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Albert
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Cavalcanti
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]
chap89_names = ["Edmond", "Albert", "Beauchamp"]
chap89_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Beauchamp
    ],
    # Albert
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Beauchamp
    ],
    # Beauchamp
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap88_names = ["Beauchamp", "Albert", "Edmond", "Danglars", "Eugénie Danglars"]
chap88_data = [
    # Beauchamp
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Eugénie Danglars
    ],
    # Albert
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Beauchamp
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Eugénie Danglars
    ],
    # Edmond
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Eugénie Danglars
    ],
    # Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Albert
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Eugénie Danglars
    ],
    # Eugénie Danglars
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Beauchamp
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Albert
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Edmond
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards herself
    ]
]
chap87_names = ["Edmond", "Ali", "Caderousse", "Benedetto", "Villefort"]
chap87_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Ali
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Caderousse
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Benedetto
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4]   # Towards Villefort
    ],
    # Ali
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Caderousse
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Benedetto
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Villefort
    ],
    # Caderousse
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Ali
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 7, 6, 7, 5, 7, 4],  # Towards Benedetto
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Villefort
    ],
    # Benedetto
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Edmond
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Ali
        [7, 0, 0, 0, 7, 7, 7, 7, 7, 6, 7, 5, 7, 4],  # Towards Caderousse
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Villefort
    ],
    # Villefort
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Ali
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Caderousse
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Benedetto
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap86_names = ["Edmond", "Ali", "Bertuccio", "Baptistin", "Caderousse"]
chap86_data = [
    # Edmond
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Ali
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Bertuccio
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Baptistin
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Caderousse
    ],
    # Ali
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Bertuccio
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Baptistin
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2]   # Towards Caderousse
    ],
    # Bertuccio
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Ali
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Baptistin
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2]   # Towards Caderousse
    ],
    # Baptistin
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Ali
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Bertuccio
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2]   # Towards Caderousse
    ],
    # Caderousse
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Edmond
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2],  # Towards Ali
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2],  # Towards Bertuccio
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2],  # Towards Baptistin
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap85_names = ["Andrea Cavalcanti", "Danglars", "Caderousse"]
chap85_data = [
    # Andrea Cavalcanti
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2]   # Towards Caderousse
    ],
    # Danglars
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Andrea Cavalcanti
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2]   # Towards Caderousse
    ],
    # Caderousse
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2],  # Towards Andrea Cavalcanti
        [5, 0, 0, 0, 5, 5, 5, 5, 4, 5, 4, 3, 4, 2],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap84_names = ["Danglars", "Andrea", "Caderousse", "Benedetto"]
chap84_data = [
    # Danglars
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Andrea
        [4, 0, 0, 0, 4, 4, 4, 4, 4, 3, 4, 2, 4, 2],  # Towards Caderousse
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Benedetto
    ],
    # Andrea
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Caderousse
        [7, 0, 0, 0, 7, 7, 7, 7, 7, 6, 7, 5, 7, 4]   # Towards Benedetto
    ],
    # Caderousse
    [
        [4, 0, 0, 0, 4, 4, 4, 4, 4, 3, 4, 2, 4, 2],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Andrea
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Benedetto
    ],
    # Benedetto
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 7, 6, 7, 5, 7, 4],  # Towards Andrea
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Caderousse
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap83_names = ["Morrel", "Noirtier", "Valentine", "Barrois", "Villefort", "D'Avrigny"]
chap83_data = [
    # Morrel
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Noirtier
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Barrois
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards D'Avrigny
    ],
    # Noirtier
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Barrois
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards D'Avrigny
    ],
    # Valentine
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Morrel
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Noirtier
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Barrois
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards D'Avrigny
    ],
    # Barrois
    [
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Noirtier
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards D'Avrigny
    ],
    # Villefort
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Noirtier
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Barrois
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards D'Avrigny
    ],
    # D'Avrigny
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Noirtier
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Barrois
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap82_names = ["Morrel", "Barrois", "Valentine", "Villefort", "Avrigny"]
chap82_data = [
    # Morrel
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 6, 6, 7, 7, 7, 6, 6, 5, 6, 4],  # Towards Barrois
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Avrigny
    ],
    # Barrois
    [
        [7, 0, 0, 0, 6, 6, 7, 7, 7, 6, 6, 5, 6, 4],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Avrigny
    ],
    # Valentine
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Morrel
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Barrois
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Avrigny
    ],
    # Villefort
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Barrois
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Avrigny
    ],
    # Avrigny
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Barrois
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap81_names = ["Valentine", "Franz", "Villefort", "Épinay", "Morrel", "Albert", "Edmond", "Morcerf", "Danglars", "Beauchamp", "Fernand"]
chap81_data = [
    # Valentine
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [8, 8, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Franz
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [7, 8, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Épinay
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Morrel
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Franz
    [
        [8, 8, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [7, 8, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Épinay
        [8, 8, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Morrel
        [8, 8, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Albert
        [8, 8, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Edmond
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 6, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [6, 6, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Villefort
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Franz
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 8, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Épinay
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 6, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [6, 6, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Épinay
    [
        [7, 8, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [7, 8, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Franz
        [7, 8, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 6, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [7, 7, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [6, 6, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Morrel
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Franz
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Épinay
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Albert
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Franz
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Épinay
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Edmond
    [
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Valentine
        [8, 0, 0, 0, 8, 8, 8, 8, 7, 8, 7, 6, 7, 5],  # Towards Franz
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Épinay
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Morcerf
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Franz
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Épinay
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Danglars
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Franz
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Épinay
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Albert
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Morcerf
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Beauchamp
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Beauchamp
    [
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Valentine
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Franz
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Villefort
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Épinay
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morrel
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Albert
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Edmond
        [7, 0, 0, 0, 7, 7, 7, 7, 6, 7, 6, 5, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4]   # Towards Fernand
    ],
    # Fernand
    [
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Valentine
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Franz
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Épinay
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Morrel
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Albert
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 5, 6, 4],  # Towards Beauchamp
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap80_names = ["Albert", "Edmond", "Morcerf", "Haydée"]
chap80_data = [
    # Albert
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 1, 8, 8, 8, 8, 8, 7, 8, 6, 8, 5],  # Towards Edmond
        [6, 0, 0, 1, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Morcerf
        [5, 0, 0, 0, 5, 5, 6, 5, 5, 4, 5, 3, 5, 3]   # Towards Haydée
    ],
    # Edmond
    [
        [8, 0, 0, 1, 8, 8, 8, 8, 8, 7, 8, 6, 8, 5],  # Towards Albert
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 1, 7, 7, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Morcerf
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4]   # Towards Haydée
    ],
    # Morcerf
    [
        [6, 0, 0, 1, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Albert
        [7, 0, 0, 1, 7, 7, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 1, 5, 5, 6, 5, 5, 4, 5, 3, 5, 3]   # Towards Haydée
    ],
    # Haydée
    [
        [5, 0, 0, 0, 5, 5, 6, 5, 5, 4, 5, 3, 5, 3],  # Towards Albert
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [5, 0, 0, 1, 5, 5, 6, 5, 5, 4, 5, 3, 5, 3],  # Towards Morcerf
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards herself
    ]
]

chap79_names = ["Cavalcanti", "Andrea", "Edmond", "Danglars", "Eugénie", "Morcerf"]
chap79_data = [
    # Cavalcanti
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 6, 5, 5, 4, 5, 3, 5, 3],  # Towards Andrea
        [6, 0, 0, 1, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [4, 0, 0, 1, 4, 4, 5, 4, 4, 3, 4, 2, 4, 2],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Eugénie
        [5, 0, 0, 1, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3]   # Towards Morcerf
    ],
    # Andrea
    [
        [5, 0, 0, 0, 5, 5, 6, 5, 5, 4, 5, 3, 5, 3],  # Towards Cavalcanti
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [7, 0, 0, 0, 7, 7, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Edmond
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Eugénie
        [4, 0, 0, 1, 4, 4, 5, 4, 4, 3, 4, 2, 4, 2]   # Towards Morcerf
    ],
    # Edmond
    [
        [6, 0, 0, 1, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Cavalcanti
        [7, 0, 0, 0, 7, 7, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Andrea
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 0, 0, 0, 8, 8, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Danglars
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Eugénie
        [7, 0, 0, 1, 7, 7, 8, 7, 7, 6, 7, 5, 7, 4]   # Towards Morcerf
    ],
    # Danglars
    [
        [4, 0, 0, 1, 4, 4, 5, 4, 4, 3, 4, 2, 4, 2],  # Towards Cavalcanti
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Andrea
        [8, 0, 0, 0, 8, 8, 9, 8, 8, 7, 8, 6, 8, 5],  # Towards Edmond
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Eugénie
        [6, 0, 0, 1, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4]   # Towards Morcerf
    ],
    # Eugénie
    [
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Cavalcanti
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Andrea
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 5, 6, 4, 6, 4],  # Towards Edmond
        [5, 0, 0, 0, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Danglars
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4]   # Towards Morcerf
    ],
    # Morcerf
    [
        [5, 0, 0, 1, 5, 5, 5, 5, 5, 4, 5, 3, 5, 3],  # Towards Cavalcanti
        [4, 0, 0, 1, 4, 4, 5, 4, 4, 3, 4, 2, 4, 2],  # Towards Andrea
        [7, 0, 0, 1, 7, 7, 8, 7, 7, 6, 7, 5, 7, 4],  # Towards Edmond
        [6, 0, 0, 1, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Danglars
        [6, 0, 0, 0, 6, 6, 7, 6, 6, 5, 6, 4, 6, 4],  # Towards Eugénie
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]

chap78_names = ["Villefort", "Valentine", "Franz", "Épinay", "Barrois"]
chap78_data = [
    # Villefort
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 8, 0, 0, 9, 9, 9, 8, 7, 8, 6, 4, 6, 3],  # Towards Valentine
        [6, 0, 0, 1, 7, 6, 8, 5, 4, 5, 5, 3, 5, 4],  # Towards Franz
        [7, 8, 0, 0, 8, 7, 7, 8, 8, 7, 7, 5, 6, 2],  # Towards Épinay
        [5, 0, 0, 1, 5, 5, 5, 4, 4, 4, 4, 2, 3, 2]   # Towards Barrois
    ],
    # Valentine
    [
        [8, 8, 0, 0, 9, 9, 9, 8, 7, 8, 6, 4, 6, 3],  # Towards Villefort
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards herself
        [7, 7, 7, 0, 6, 6, 8, 7, 7, 7, 6, 5, 6, 4],  # Towards Franz
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 3, 5, 3],  # Towards Épinay
        [7, 0, 0, 0, 7, 7, 7, 6, 7, 7, 7, 5, 6, 3]   # Towards Barrois
    ],
    # Franz
    [
        [6, 0, 0, 1, 7, 6, 8, 5, 4, 5, 5, 3, 5, 4],  # Towards Villefort
        [7, 7, 7, 0, 6, 6, 8, 7, 7, 7, 6, 5, 6, 4],  # Towards Valentine
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [8, 8, 0, 0, 7, 8, 8, 7, 8, 8, 7, 6, 7, 4],  # Towards Épinay
        [6, 0, 0, 0, 5, 5, 6, 5, 5, 5, 5, 4, 5, 3]   # Towards Barrois
    ],
    # Épinay
    [
        [7, 8, 0, 0, 8, 7, 7, 8, 8, 7, 7, 5, 6, 2],  # Towards Villefort
        [6, 0, 0, 0, 6, 6, 6, 6, 6, 6, 6, 3, 5, 3],  # Towards Valentine
        [8, 8, 0, 0, 7, 8, 8, 7, 8, 8, 7, 6, 7, 4],  # Towards Franz
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Towards himself
        [5, 0, 0, 1, 5, 5, 5, 4, 4, 4, 4, 2, 3, 2]   # Towards Barrois
    ],
    # Barrois
    [
        [5, 0, 0, 1, 5, 5, 5, 4, 4, 4, 4, 2, 3, 2],  # Towards Villefort
        [7, 0, 0, 0, 7, 7, 7, 6, 7, 7, 7, 5, 6, 3],  # Towards Valentine
        [6, 0, 0, 0, 5, 5, 6, 5, 5, 5, 5, 4, 5, 3],  # Towards Franz
        [5, 0, 0, 1, 5, 5, 5, 4, 4, 4, 4, 2, 3, 2],  # Towards Épinay
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]   # Towards himself
    ]
]



chapter_names

relationships_data
# 115 max

def get_data():
    for i in range(10, 115):
        number = str(i)
        name_array = "chap" + number + "_names"
        data_array = "chap" + number + "_data"
        print(name_array, data_array)
        # Accessing dynamically named variables
        if name_array in globals():
            names = globals()[name_array]
            data = globals()[data_array]
            chapter_names.append(names)
            relationships_data.append(data)

        else:
            print(f"{name_array} does not exist.")
    
    return chapter_names,relationships_data

