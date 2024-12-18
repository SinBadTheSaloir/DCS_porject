chap1_names = ["The artist", "The critic", "The cultivated"]
chap1_data = [
    [
        [0]*14,  # The artist towards himself
        [3, 0, 0, 4, 5, 5, 5, 3, 3, 4, 5, 4, 4, 3],  # The artist towards The critic
        [5, 0, 0, 3, 4, 5, 4, 3, 4, 3, 5, 4, 4, 3],  # The artist towards The cultivated
    ],
    [
        [3, 0, 0, 4, 5, 5, 5, 3, 3, 4, 5, 4, 4, 3],  # The critic towards The artist
        [0]*14,  # The critic towards himself
        [2, 0, 0, 4, 4, 4, 4, 2, 3, 3, 4, 3, 3, 2],  # The critic towards The cultivated
    ],
    [
        [5, 0, 0, 3, 4, 5, 4, 3, 4, 3, 5, 4, 4, 3],  # The cultivated towards The artist
        [2, 0, 0, 4, 4, 4, 4, 2, 3, 3, 4, 3, 3, 2],  # The cultivated towards The critic
        [0]*14,  # The cultivated towards himself
    ]
]

chap2_names = ["Basil Hallward", "Lord Henry Wotton", "Dorian Gray"]
chap2_data = [
    [
        [0]*14,  # Basil Hallward towards himself
        [6, 0, 0, 5, 5, 4, 5, 6, 6, 4, 5, 5, 5, 5],  # Basil Hallward towards Lord Henry Wotton
        [9, 0, 0, 3, 4, 7, 6, 5, 9, 8, 7, 9, 9, 3],  # Basil Hallward towards Dorian Gray
    ],
    [
        [6, 0, 0, 5, 5, 4, 5, 6, 6, 4, 5, 5, 5, 5],  # Lord Henry Wotton towards Basil Hallward
        [0]*14,  # Lord Henry Wotton towards himself
        [7, 0, 0, 3, 4, 6, 6, 6, 7, 6, 7, 6, 7, 3],  # Lord Henry Wotton towards Dorian Gray
    ],
    [
        [9, 0, 0, 3, 4, 7, 6, 5, 9, 8, 7, 9, 9, 3],  # Dorian Gray towards Basil Hallward
        [7, 0, 0, 3, 4, 6, 6, 6, 7, 6, 7, 6, 7, 3],  # Dorian Gray towards Lord Henry Wotton
        [0]*14,  # Dorian Gray towards himself
    ]
]

chap3_names = ["Lord Henry Wotton", "Lord Fermor", "Dorian Gray"]
chap3_data = [
    [
        [0]*14,  # Lord Henry Wotton towards himself
        [4, 0, 0, 6, 4, 5, 6, 4, 4, 4, 5, 4, 4, 6],  # Lord Henry Wotton towards Lord Fermor
        [6, 0, 0, 3, 5, 6, 7, 6, 6, 5, 6, 6, 6, 3],  # Lord Henry Wotton towards Dorian Gray
    ],
    [
        [4, 0, 0, 6, 4, 5, 6, 4, 4, 4, 5, 4, 4, 6],  # Lord Fermor towards Lord Henry Wotton
        [0]*14,  # Lord Fermor towards himself
        [3, 0, 0, 4, 4, 4, 4, 3, 3, 3, 4, 3, 3, 4],  # Lord Fermor towards Dorian Gray
    ],
    [
        [6, 0, 0, 3, 5, 6, 7, 6, 6, 5, 6, 6, 6, 3],  # Dorian Gray towards Lord Henry Wotton
        [3, 0, 0, 4, 4, 4, 4, 3, 3, 3, 4, 3, 3, 4],  # Dorian Gray towards Lord Fermor
        [0]*14,  # Dorian Gray towards himself
    ]
]

chap4_names = ["Lord Henry Wotton", "Aunt Agatha", "Mr. Erskine"]
chap4_data = [
    [
        [0]*14,  # Lord Henry Wotton towards himself
        [7, 0, 0, 2, 5, 6, 7, 7, 7, 6, 7, 6, 7, 2],  # Lord Henry Wotton towards Aunt Agatha
        [8, 0, 0, 3, 6, 7, 8, 8, 8, 7, 8, 7, 8, 3],  # Lord Henry Wotton towards Mr. Erskine
    ],
    [
        [7, 0, 0, 2, 5, 6, 7, 7, 7, 6, 7, 6, 7, 2],  # Aunt Agatha towards Lord Henry Wotton
        [0]*14,  # Aunt Agatha towards herself
        [6, 0, 0, 4, 5, 6, 6, 6, 6, 5, 6, 5, 6, 4],  # Aunt Agatha towards Mr. Erskine
    ],
    [
        [8, 0, 0, 3, 6, 7, 8, 8, 8, 7, 8, 7, 8, 3],  # Mr. Erskine towards Lord Henry Wotton
        [6, 0, 0, 4, 5, 6, 6, 6, 6, 5, 6, 5, 6, 4],  # Mr. Erskine towards Aunt Agatha
        [0]*14,  # Mr. Erskine towards himself
    ]
]

chap5_names = ["Sibyl Vane", "Mrs. Vane", "Jim Vane"]
chap5_data = [
    [
        [0]*14,  # Sibyl Vane towards herself
        [5, 0, 0, 4, 5, 4, 5, 3, 5, 4, 5, 4, 5, 3],  # Sibyl Vane towards Mrs. Vane
        [6, 0, 0, 3, 6, 4, 5, 4, 6, 5, 6, 4, 6, 3],  # Sibyl Vane towards Jim Vane
    ],
    [
        [5, 0, 0, 4, 5, 4, 5, 3, 5, 4, 5, 4, 5, 3],  # Mrs. Vane towards Sibyl Vane
        [0]*14,  # Mrs. Vane towards herself
        [4, 0, 0, 3, 4, 3, 4, 3, 4, 4, 4, 3, 4, 3],  # Mrs. Vane towards Jim Vane
    ],
    [
        [6, 0, 0, 3, 6, 4, 5, 4, 6, 5, 6, 4, 6, 3],  # Jim Vane towards Sibyl Vane
        [4, 0, 0, 3, 4, 3, 4, 3, 4, 4, 4, 3, 4, 3],  # Jim Vane towards Mrs. Vane
        [0]*14,  # Jim Vane towards himself
    ]
]

chap6_names = ["Dorian Gray", "Lord Henry Wotton", "Basil Hallward"]
chap6_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [7, 0, 0, 5, 7, 6, 7, 5, 7, 6, 7, 6, 7, 5],  # Dorian Gray towards Lord Henry Wotton
        [8, 0, 0, 4, 8, 7, 8, 6, 8, 7, 8, 7, 8, 4],  # Dorian Gray towards Basil Hallward
    ],
    [
        [7, 0, 0, 5, 7, 6, 7, 5, 7, 6, 7, 6, 7, 5],  # Lord Henry Wotton towards Dorian Gray
        [0]*14,  # Lord Henry Wotton towards himself
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Lord Henry Wotton towards Basil Hallward
    ],
    [
        [8, 0, 0, 4, 8, 7, 8, 6, 8, 7, 8, 7, 8, 4],  # Basil Hallward towards Dorian Gray
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Basil Hallward towards Lord Henry Wotton
        [0]*14,  # Basil Hallward towards himself
    ]
]

chap7_names = ["Dorian Gray", "Lord Henry Wotton", "Sibyl Vane"]
chap7_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Dorian Gray towards Lord Henry Wotton
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Sibyl Vane
    ],
    [
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Lord Henry Wotton towards Dorian Gray
        [0]*14,  # Lord Henry Wotton towards himself
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Lord Henry Wotton towards Sibyl Vane
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Sibyl Vane towards Dorian Gray
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Sibyl Vane towards Lord Henry Wotton
        [0]*14,  # Sibyl Vane towards herself
    ]
]

chap8_names = ["Dorian Gray", "James Vane", "Mrs. Vane"]
chap8_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [5, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # Dorian Gray towards James Vane
        [6, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],  # Dorian Gray towards Mrs. Vane
    ],
    [
        [5, 0, 0, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # James Vane towards Dorian Gray
        [0]*14,  # James Vane towards himself
        [4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # James Vane towards Mrs. Vane
    ],
    [
        [6, 0, 0, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],  # Mrs. Vane towards Dorian Gray
        [4, 0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # Mrs. Vane towards James Vane
        [0]*14,  # Mrs. Vane towards herself
    ]
]

chap9_names = ["Dorian Gray", "Basil Hallward", "Lord Henry Wotton"]
chap9_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [7, 0, 0, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6],  # Dorian Gray towards Basil Hallward
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Dorian Gray towards Lord Henry Wotton
    ],
    [
        [7, 0, 0, 6, 7, 6, 7, 6, 7, 6, 7, 6, 7, 6],  # Basil Hallward towards Dorian Gray
        [0]*14,  # Basil Hallward towards himself
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Basil Hallward towards Lord Henry Wotton
    ],
    [
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Lord Henry Wotton towards Dorian Gray
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Lord Henry Wotton towards Basil Hallward
        [0]*14,  # Lord Henry Wotton towards himself
    ]
]

chap10_names = ["Dorian Gray", "Basil Hallward", "Lord Henry Wotton"]
chap10_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [7, 0, 0, 5, 7, 6, 7, 5, 7, 6, 7, 6, 7, 5],  # Dorian Gray towards Basil Hallward
        [8, 0, 0, 4, 8, 7, 8, 6, 8, 7, 8, 7, 8, 4],  # Dorian Gray towards Lord Henry Wotton
    ],
    [
        [7, 0, 0, 5, 7, 6, 7, 5, 7, 6, 7, 6, 7, 5],  # Basil Hallward towards Dorian Gray
        [0]*14,  # Basil Hallward towards himself
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Basil Hallward towards Lord Henry Wotton
    ],
    [
        [8, 0, 0, 4, 8, 7, 8, 6, 8, 7, 8, 7, 8, 4],  # Lord Henry Wotton towards Dorian Gray
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Lord Henry Wotton towards Basil Hallward
        [0]*14,  # Lord Henry Wotton towards himself
    ]
]

chap11_names = ["Dorian Gray", "Basil Hallward", "Victor"]
chap11_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [7, 0, 0, 5, 7, 6, 7, 5, 7, 6, 7, 6, 7, 5],  # Dorian Gray towards Basil Hallward
        [3, 0, 0, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3],  # Dorian Gray towards Victor
    ],
    [
        [7, 0, 0, 5, 7, 6, 7, 5, 7, 6, 7, 6, 7, 5],  # Basil Hallward towards Dorian Gray
        [0]*14,  # Basil Hallward towards himself
        [4, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # Basil Hallward towards Victor
    ],
    [
        [3, 0, 0, 3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3],  # Victor towards Dorian Gray
        [4, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # Victor towards Basil Hallward
        [0]*14,  # Victor towards himself
    ]
]

chap12_names = ["Dorian Gray", "Lord Henry Wotton", "Basil Hallward"]
chap12_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Dorian Gray towards Lord Henry Wotton
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Basil Hallward
    ],
    [
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Lord Henry Wotton towards Dorian Gray
        [0]*14,  # Lord Henry Wotton towards himself
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Lord Henry Wotton towards Basil Hallward
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Basil Hallward towards Dorian Gray
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Basil Hallward towards Lord Henry Wotton
        [0]*14,  # Basil Hallward towards himself
    ]
]

chap13_names = ["Dorian Gray", "Basil Hallward", "Lord Henry Wotton"]
chap13_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [6, 0, 0, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],  # Dorian Gray towards Basil Hallward
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Lord Henry Wotton
    ],
    [
        [6, 0, 0, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],  # Basil Hallward towards Dorian Gray
        [0]*14,  # Basil Hallward towards himself
        [5, 0, 0, 3, 5, 4, 5, 4, 5, 4, 5, 4, 5, 3],  # Basil Hallward towards Lord Henry Wotton
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Lord Henry Wotton towards Dorian Gray
        [5, 0, 0, 3, 5, 4, 5, 4, 5, 4, 5, 4, 5, 3],  # Lord Henry Wotton towards Basil Hallward
        [0]*14,  # Lord Henry Wotton towards himself
    ]
]

chap14_names = ["Dorian Gray", "Basil Hallward", "James Vane"]
chap14_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [6, 0, 0, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],  # Dorian Gray towards Basil Hallward
        [5, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # Dorian Gray towards James Vane
    ],
    [
        [6, 0, 0, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],  # Basil Hallward towards Dorian Gray
        [0]*14,  # Basil Hallward towards himself
        [4, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # Basil Hallward towards James Vane
    ],
    [
        [5, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # James Vane towards Dorian Gray
        [4, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # James Vane towards Basil Hallward
        [0]*14,  # James Vane towards himself
    ]
]

chap15_names = ["Dorian Gray", "Alan Campbell", "Lord Henry Wotton"]
chap15_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Dorian Gray towards Alan Campbell
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Lord Henry Wotton
    ],
    [
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Alan Campbell towards Dorian Gray
        [0]*14,  # Alan Campbell towards himself
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Alan Campbell towards Lord Henry Wotton
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Lord Henry Wotton towards Dorian Gray
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Lord Henry Wotton towards Alan Campbell
        [0]*14,  # Lord Henry Wotton towards himself
    ]
]

chap16_names = ["Dorian Gray", "Lady Narborough", "Lord Henry Wotton"]
chap16_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [6, 0, 0, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],  # Dorian Gray towards Lady Narborough
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Lord Henry Wotton
    ],
    [
        [6, 0, 0, 5, 6, 5, 6, 5, 6, 5, 6, 5, 6, 5],  # Lady Narborough towards Dorian Gray
        [0]*14,  # Lady Narborough towards herself
        [5, 0, 0, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4],  # Lady Narborough towards Lord Henry Wotton
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Lord Henry Wotton towards Dorian Gray
        [5, 0, 0, 4, 5, 4, 5, 4, 5, 4, 5, 4, 5, 4],  # Lord Henry Wotton towards Lady Narborough
        [0]*14,  # Lord Henry Wotton towards himself
    ]
]

chap17_names = ["Dorian Gray", "Lady Monmouth", "Lord Henry Wotton"]
chap17_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Dorian Gray towards Lady Monmouth
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Lord Henry Wotton
    ],
    [
        [8, 0, 0, 5, 8, 7, 8, 6, 8, 7, 8, 7, 8, 5],  # Lady Monmouth towards Dorian Gray
        [0]*14,  # Lady Monmouth towards herself
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Lady Monmouth towards Lord Henry Wotton
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Lord Henry Wotton towards Dorian Gray
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Lord Henry Wotton towards Lady Monmouth
        [0]*14,  # Lord Henry Wotton towards himself
    ]
]

chap18_names = ["Dorian Gray", "Duchess of Monmouth", "Lord Henry Wotton"]
chap18_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [9, 0, 0, 5, 9, 7, 9, 6, 9, 7, 9, 7, 9, 5],  # Dorian Gray towards Duchess of Monmouth
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Lord Henry Wotton
    ],
    [
        [9, 0, 0, 5, 9, 7, 9, 6, 9, 7, 9, 7, 9, 5],  # Duchess of Monmouth towards Dorian Gray
        [0]*14,  # Duchess of Monmouth towards herself
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Duchess of Monmouth towards Lord Henry Wotton
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Lord Henry Wotton towards Dorian Gray
        [6, 0, 0, 4, 6, 5, 6, 5, 6, 5, 6, 5, 6, 4],  # Lord Henry Wotton towards Duchess of Monmouth
        [0]*14,  # Lord Henry Wotton towards himself
    ]
]

chap19_names = ["Dorian Gray", "James Vane", "Lord Henry Wotton"]
chap19_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [5, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # Dorian Gray towards James Vane
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Lord Henry Wotton
    ],
    [
        [5, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # James Vane towards Dorian Gray
        [0]*14,  # James Vane towards himself
        [4, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # James Vane towards Lord Henry Wotton
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Lord Henry Wotton towards Dorian Gray
        [4, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # Lord Henry Wotton towards James Vane
        [0]*14,  # Lord Henry Wotton towards himself
    ]
]

chap20_names = ["Dorian Gray", "Lord Henry Wotton", "Hetty Merton"]
chap20_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Lord Henry Wotton
        [6, 0, 0, 3, 6, 5, 6, 4, 6, 5, 6, 5, 6, 3],  # Dorian Gray towards Hetty Merton
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Lord Henry Wotton towards Dorian Gray
        [0]*14,  # Lord Henry Wotton towards himself
        [5, 0, 0, 3, 5, 4, 5, 4, 5, 4, 5, 4, 5, 3],  # Lord Henry Wotton towards Hetty Merton
    ],
    [
        [6, 0, 0, 3, 6, 5, 6, 4, 6, 5, 6, 5, 6, 3],  # Hetty Merton towards Dorian Gray
        [5, 0, 0, 3, 5, 4, 5, 4, 5, 4, 5, 4, 5, 3],  # Hetty Merton towards Lord Henry Wotton
        [0]*14,  # Hetty Merton towards herself
    ]
]

chap21_names = ["Dorian Gray", "Lord Henry Wotton", "James Vane"]
chap21_data = [
    [
        [0]*14,  # Dorian Gray towards himself
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Dorian Gray towards Lord Henry Wotton
        [5, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # Dorian Gray towards James Vane
    ],
    [
        [7, 0, 0, 4, 7, 6, 7, 5, 7, 6, 7, 6, 7, 4],  # Lord Henry Wotton towards Dorian Gray
        [0]*14,  # Lord Henry Wotton towards himself
        [4, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # Lord Henry Wotton towards James Vane
    ],
    [
        [5, 0, 0, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],  # James Vane towards Dorian Gray
        [4, 0, 0, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4],  # James Vane towards Lord Henry Wotton
        [0]*14,  # James Vane towards himself
    ]
]

global start , end 
start = 1
end = 21
def collect_chapter_data_PDG():
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

collect_chapter_data_PDG()