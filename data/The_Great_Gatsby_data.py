chap1_names = ["Nick Carraway", "Tom Buchanan", "Daisy Buchanan", "Jordan Baker", "Jay Gatsby"]

chap1_chapter_values = [
    # Nick Carraway's relationships
    [
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        # Towards Tom Buchanan
        [3, 0, 0, 6, 1, 7, 6, 6, 5, 6, 3, 0, 3, 5], 
        # Towards Daisy Buchanan
        [7, 6, 0, 1, 0, 7, 7, 7, 7, 8, 6, 1, 4, 1], 
        # Towards Jordan Baker
        [5, 0, 0, 1, 0, 6, 6, 6, 7, 7, 4, 1, 2, 3], 
        # Towards Jay Gatsby
        [8, 0, 0, 1, 0, 6, 6, 7, 8, 8, 7, 1, 6, 0]
    ],
    # Tom Buchanan's relationships
    [
        # Towards Nick Carraway
        [6, 0, 0, 1, 1, 7, 6, 7, 5, 6, 5, 1, 3, 4], 
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        # Towards Daisy Buchanan
        [8, 9, 0, 1, 0, 7, 7, 7, 7, 8, 8, 1, 4, 1], 
        # Towards Jordan Baker
        [5, 0, 0, 1, 0, 6, 6, 6, 5, 7, 4, 1, 2, 3], 
        # Towards Jay Gatsby
        [1, 0, 0, 1, 1, 6, 6, 7, 2, 1, 1, 1, 3, 10]
    ],
    # Daisy Buchanan's relationships
    [
        # Towards Nick Carraway
        [8, 0, 0, 1, 1, 8, 7, 7, 7, 8, 8, 1, 6, 1], 
        # Towards Tom Buchanan
        [6, 6, 0, 1, 1, 7, 7, 7, 7, 8, 7, 1, 5, 1], 
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        # Towards Jordan Baker
        [6, 0, 0, 1, 0, 7, 7, 7, 7, 7, 6, 1, 4, 1], 
        # Towards Jay Gatsby
        [9, 0, 0, 9, 0, 8, 8, 8, 9, 9, 9, 1, 7, 0]
    ],
    # Jordan Baker's relationships
    [
        # Towards Nick Carraway
        [6, 0, 0, 1, 1, 6, 6, 6, 7, 7, 5, 1, 4, 3], 
        # Towards Tom Buchanan
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 6, 4, 1, 3, 4], 
        # Towards Daisy Buchanan
        [7, 6, 0, 1, 0, 7, 7, 7, 7, 7, 6, 1, 5, 1], 
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        # Towards Jay Gatsby
        [5, 0, 0, 1, 0, 6, 6, 6, 6, 7, 5, 1, 4, 2]
    ],
    # Jay Gatsby's relationships
    [
        # Towards Nick Carraway
        [7, 0, 0, 1, 0, 8, 8, 7, 8, 8, 8, 1, 6, 0], 
        # Towards Tom Buchanan
        [2, 0, 0, 9, 0, 6, 6, 6, 3, 2, 2, 1, 3, 10], 
        # Towards Daisy Buchanan
        [9, 0, 0, 9, 0, 9, 9, 9, 9, 9, 9, 1, 8, 0], 
        # Towards Jordan Baker
        [4, 0, 0, 1, 0, 6, 6, 6, 6, 6, 5, 1, 4, 2], 
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]


chap2_names = ["Nick Carraway", "Tom Buchanan", "Myrtle Wilson", "George Wilson", "Catherine", "Mr. McKee", "Mrs. McKee"]
chap2_chapter_values = [
    # Nick Carraway's relationships
    [
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        # Towards Tom Buchanan
        [3, 0, 0, 6, 1, 7, 6, 6, 5, 6, 3, 0, 3, 5], 
        # Towards Myrtle Wilson
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4], 
        # Towards George Wilson
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3], 
        # Towards Catherine
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4], 
        # Towards Mr. McKee
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4], 
        # Towards Mrs. McKee
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4]
    ],
    # Tom Buchanan's relationships
    [
        # Towards Nick Carraway
        [6, 0, 0, 1, 1, 7, 6, 7, 5, 6, 5, 1, 3, 4], 
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        # Towards Myrtle Wilson
        [7, 0, 0, 8, 0, 6, 6, 6, 6, 7, 7, 1, 5, 2], 
        # Towards George Wilson
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10], 
        # Towards Catherine
        [3, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 1, 3, 4], 
        # Towards Mr. McKee
        [2, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 1, 2, 3], 
        # Towards Mrs. McKee
        [2, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 1, 2, 3]
    ],
    # Myrtle Wilson's relationships
    [
        # Towards Nick Carraway
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4], 
        # Towards Tom Buchanan
        [8, 0, 0, 9, 0, 7, 7, 7, 7, 8, 8, 1, 6, 1], 
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        # Towards George Wilson
        [2, 0, 0, 8, 0, 3, 3, 3, 2, 2, 2, 1, 2, 8], 
        # Towards Catherine
        [6, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 1, 4, 3], 
        # Towards Mr. McKee
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3], 
        # Towards Mrs. McKee
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    # George Wilson's relationships
    [
        # Towards Nick Carraway
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3], 
        # Towards Tom Buchanan
        [1, 0, 0, 9, 0, 3, 3, 3, 2, 1, 2, 1, 3, 10], 
        # Towards Myrtle Wilson
        [6, 0, 0, 1, 0, 5, 5, 5, 5, 6, 5, 0, 4, 2], 
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        # Towards Catherine
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3], 
        # Towards Mr. McKee
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3], 
        # Towards Mrs. McKee
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3]
    ],
    # Catherine's relationships
    [
        # Towards Nick Carraway
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4], 
        # Towards Tom Buchanan
        [3, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 1, 3, 4], 
        # Towards Myrtle Wilson
        [6, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 1, 4, 3], 
        # Towards George Wilson
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3], 
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        # Towards Mr. McKee
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 4], 
        # Towards Mrs. McKee
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 4]
    ],
    # Mr. McKee's relationships
[
    # Towards Nick Carraway
    [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4], 
    # Towards Tom Buchanan
    [2, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 1, 2, 3], 
    # Towards Myrtle Wilson
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3], 
    # Towards George Wilson
    [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3], 
    # Towards Catherine
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 4], 
    # Self
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
    # Towards Mrs. McKee
    [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 4, 5]
],
[
    # Towards Nick Carraway
    [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4], 
    # Towards Tom Buchanan
    [2, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 1, 2, 3], 
    # Towards Myrtle Wilson
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3], 
    # Towards George Wilson
    [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3], 
    # Towards Catherine
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 4], 
    # Towards Mr. McKee
    [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 4, 5], 
    # Self
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
]


chap3_names = ["Nick Carraway", "Jay Gatsby", "Jordan Baker", "Owl Eyes", "Lucille", "Various Guests"]
chap3_chapter_values = [
    # Nick Carraway's relationships
    [
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jay Gatsby
        [8, 0, 0, 7, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        # Towards Jordan Baker
        [6, 0, 0, 6, 0, 7, 7, 6, 7, 7, 6, 0, 4, 6],
        # Towards Owl Eyes
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Lucille
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Various Guests
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    # Jay Gatsby's relationships
    [
        # Towards Nick Carraway
        [8, 0, 0, 7, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jordan Baker
        [7, 0, 0, 6, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Owl Eyes
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Lucille
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Various Guests
        [7, 0, 0, 1, 0, 7, 7, 7, 7, 7, 7, 0, 6, 7]
    ],
    # Jordan Baker's relationships
    [
        # Towards Nick Carraway
        [6, 0, 0, 6, 0, 7, 7, 6, 7, 7, 6, 0, 4, 6],
        # Towards Jay Gatsby
        [7, 0, 0, 6, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Owl Eyes
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Lucille
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Various Guests
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5]
    ],
    # Owl Eyes' relationships
    [
        # Towards Nick Carraway
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Jay Gatsby
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Jordan Baker
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Lucille
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Various Guests
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    # Lucille's relationships
    [
        # Towards Nick Carraway
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Jay Gatsby
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Jordan Baker
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Owl Eyes
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Various Guests
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    # Various Guests' relationships
    [
        # Towards Nick Carraway
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Jay Gatsby
        [7, 0, 0, 1, 0, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Jordan Baker
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5],
        # Towards Owl Eyes
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Lucille
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]



chap4_names = ["Nick Carraway", "Jay Gatsby", "Jordan Baker", "Meyer Wolfshiem", "Daisy Buchanan", "Tom Buchanan"]
chap4_chapter_values = [
    # Nick Carraway's relationships
    [
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jay Gatsby
        [8, 0, 0, 7, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        # Towards Jordan Baker
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Meyer Wolfshiem
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Daisy Buchanan
        [6, 0, 0, 1, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Tom Buchanan
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4]
    ],
    # Jay Gatsby's relationships
    [
        # Towards Nick Carraway
        [8, 0, 0, 7, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jordan Baker
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Meyer Wolfshiem
        [7, 0, 0, 1, 0, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Daisy Buchanan
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        # Towards Tom Buchanan
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10]
    ],
    # Jordan Baker's relationships
    [
        # Towards Nick Carraway
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Jay Gatsby
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Meyer Wolfshiem
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Daisy Buchanan
        [6, 0, 0, 1, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Tom Buchanan
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5]
    ],
    # Meyer Wolfshiem's relationships
    [
        # Towards Nick Carraway
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Jay Gatsby
        [7, 0, 0, 1, 0, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Jordan Baker
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Daisy Buchanan
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Tom Buchanan
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    # Daisy Buchanan's relationships
    [
        # Towards Nick Carraway
        [6, 0, 0, 1, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Jay Gatsby
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        # Towards Jordan Baker
        [6, 0, 0, 1, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Meyer Wolfshiem
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Tom Buchanan
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4]
    ],
    # Tom Buchanan's relationships
    [
        # Towards Nick Carraway
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Jay Gatsby
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        # Towards Jordan Baker
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5],
        # Towards Meyer Wolfshiem
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Daisy Buchanan
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]


chap5_names = ["Nick Carraway", "Jay Gatsby", "Daisy Buchanan"]
chap5_chapter_values = [
    # Nick Carraway's relationships
    [
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jay Gatsby
        [7, 0, 0, 8, 1, 8, 7, 8, 7, 8, 7, 0, 6, 8],
        # Towards Daisy Buchanan
        [8, 6, 0, 7, 0, 8, 8, 7, 8, 8, 7, 0, 6, 7]
    ],
    # Jay Gatsby's relationships
    [
        # Towards Nick Carraway
        [7, 0, 0, 8, 1, 8, 7, 8, 7, 8, 7, 0, 6, 8],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Daisy Buchanan
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10]
    ],
    # Daisy Buchanan's relationships
    [
        # Towards Nick Carraway
        [8, 6, 0, 7, 0, 8, 8, 7, 8, 8, 7, 0, 6, 7],
        # Towards Jay Gatsby
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]


chap6_names = ["Nick Carraway", "Jay Gatsby", "Tom Buchanan", "Daisy Buchanan", "Dan Cody"]
chap6_chapter_values = [
    # Nick Carraway's relationships
    [
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jay Gatsby
        [8, 0, 0, 7, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        # Towards Tom Buchanan
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Daisy Buchanan
        [6, 0, 0, 1, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Dan Cody
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4]
    ],
    # Jay Gatsby's relationships
    [
        # Towards Nick Carraway
        [8, 0, 0, 7, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Tom Buchanan
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        # Towards Daisy Buchanan
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        # Towards Dan Cody
        [9, 0, 0, 8, 1, 9, 9, 8, 9, 9, 9, 0, 8, 9]
    ],
    # Tom Buchanan's relationships
    [
        # Towards Nick Carraway
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Jay Gatsby
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Daisy Buchanan
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Dan Cody
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4]
    ],
    # Daisy Buchanan's relationships
    [
        # Towards Nick Carraway
        [6, 0, 0, 1, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Jay Gatsby
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        # Towards Tom Buchanan
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Dan Cody
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4]
    ],
    # Dan Cody's relationships
    [
        # Towards Nick Carraway
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Jay Gatsby
        [9, 0, 0, 8, 1, 9, 9, 8, 9, 9, 9, 0, 8, 9],
        # Towards Tom Buchanan
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Daisy Buchanan
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]

chap7_names = ["Nick Carraway", "Jay Gatsby", "Tom Buchanan", "Daisy Buchanan", "Jordan Baker", "George Wilson", "Myrtle Wilson"]
chap7_chapter_values = [
    # Nick Carraway's relationships
    [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [8, 0, 0, 8, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3],
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4]
    ],
    # Jay Gatsby's relationships
    [
        [8, 0, 0, 8, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4]
    ],
    # Tom Buchanan's relationships
    [
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5],
        [1, 0, 0, 9, 0, 3, 3, 3, 2, 1, 2, 1, 3, 10],
        [8, 0, 0, 9, 0, 7, 7, 7, 7, 8, 8, 1, 6, 1]
    ],
    # Daisy Buchanan's relationships
    [
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    # Jordan Baker's relationships
    [
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5],
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    [
    [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3],
    [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
    [1, 0, 0, 9, 0, 3, 3, 3, 2, 1, 2, 1, 3, 10],
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
],
# Myrtle Wilson's relationships
[
    [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4],
    [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 4, 0, 3, 4],
    [8, 0, 0, 9, 0, 7, 7, 7, 7, 8, 8, 1, 6, 1],
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
]


chap8_names = ["Nick Carraway", "Jay Gatsby", "George Wilson", "Daisy Buchanan", "Tom Buchanan", "Jordan Baker"]
chap8_chapter_values = [
    # Nick Carraway's relationships
    [
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jay Gatsby
        [9, 0, 0, 8, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        # Towards George Wilson
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3],
        # Towards Daisy Buchanan
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Tom Buchanan
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Jordan Baker
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7]
    ],
    # Jay Gatsby's relationships
    [
        # Towards Nick Carraway
        [9, 0, 0, 8, 1, 9, 9, 8, 8, 9, 8, 0, 7, 9],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards George Wilson
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        # Towards Daisy Buchanan
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        # Towards Tom Buchanan
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        # Towards Jordan Baker
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7]
    ],
    # George Wilson's relationships
    [
        # Towards Nick Carraway
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 3, 0, 2, 3],
        # Towards Jay Gatsby
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Daisy Buchanan
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Tom Buchanan
        [1, 0, 0, 9, 0, 3, 3, 3, 2, 1, 2, 1, 3, 10],
        # Towards Jordan Baker
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    # Daisy Buchanan's relationships
    [
        # Towards Nick Carraway
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Jay Gatsby
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        # Towards George Wilson
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Tom Buchanan
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jordan Baker
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6]
    ],
    # Tom Buchanan's relationships
    [
        # Towards Nick Carraway
        [4, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 4],
        # Towards Jay Gatsby
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        # Towards George Wilson
        [1, 0, 0, 9, 0, 3, 3, 3, 2, 1, 2, 1, 3, 10],
        # Towards Daisy Buchanan
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jordan Baker
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5]
    ],
    # Jordan Baker's relationships
    [
        # Towards Nick Carraway
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Jay Gatsby
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards George Wilson
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Daisy Buchanan
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Tom Buchanan
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
]



chap9_names = ["Nick Carraway", "Jay Gatsby", "Daisy Buchanan", "Tom Buchanan", "Jordan Baker", "Henry C. Gatz", "Meyer Wolfshiem", "Owl Eyes"]
chap9_chapter_values = [
    # Nick Carraway's relationships
    [
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jay Gatsby
        [10, 0, 0, 9, 1, 10, 10, 9, 9, 10, 9, 0, 8, 10],
        # Towards Daisy Buchanan
        [4, 0, 0, 6, 1, 6, 6, 6, 6, 6, 6, 0, 5, 6],
        # Towards Tom Buchanan
        [1, 0, 0, 9, 0, 3, 3, 3, 2, 1, 2, 1, 3, 10],
        # Towards Jordan Baker
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Henry C. Gatz
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Meyer Wolfshiem
        [6, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5],
        # Towards Owl Eyes
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7]
    ],
    # Jay Gatsby's relationships
    [
        # Towards Nick Carraway
        [10, 0, 0, 9, 1, 10, 10, 9, 9, 10, 9, 0, 8, 10],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Daisy Buchanan
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        # Towards Tom Buchanan
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        # Towards Jordan Baker
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Henry C. Gatz
        [9, 0, 0, 8, 1, 9, 9, 8, 9, 9, 9, 0, 8, 9],
        # Towards Meyer Wolfshiem
        [7, 0, 0, 1, 0, 7, 7, 7, 7, 7, 7, 0, 6, 7],
        # Towards Owl Eyes
        [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7]
    ],
    # Daisy Buchanan's relationships
    [
        # Towards Nick Carraway
        [4, 0, 0, 6, 1, 6, 6, 6, 6, 6, 6, 0, 5, 6],
        # Towards Jay Gatsby
        [10, 0, 0, 10, 1, 10, 10, 10, 10, 10, 10, 0, 9, 10],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Tom Buchanan
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Jordan Baker
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Towards Henry C. Gatz
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Meyer Wolfshiem
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Owl Eyes
        [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    # Tom Buchanan's relationships
    [
        # Towards Nick Carraway
        [1, 0, 0, 9, 0, 3, 3, 3, 2, 1, 2, 1, 3, 10],
        # Towards Jay Gatsby
        [1, 0, 0, 9, 0, 4, 4, 4, 2, 1, 2, 1, 3, 10],
        # Towards Daisy Buchanan
        [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
        # Self
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        # Towards Jordan Baker
        [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5],
        # Towards Henry C. Gatz
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Meyer Wolfshiem
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
        # Towards Owl Eyes
        [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3]
    ],
    # Jordan Baker's relationships
   [
    # Towards Nick Carraway
    [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
    # Towards Jay Gatsby
    [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
    # Towards Daisy Buchanan
    [6, 0, 0, 7, 1, 7, 7, 7, 7, 7, 6, 0, 5, 6],
    # Towards Tom Buchanan
    [5, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5],
    # Towards Henry C. Gatz
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Meyer Wolfshiem
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Owl Eyes
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Self
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
],
    [
    # Towards Nick Carraway
    [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
    # Towards Jay Gatsby
    [9, 0, 0, 8, 1, 9, 9, 8, 9, 9, 9, 0, 8, 9],
    # Towards Daisy Buchanan
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Tom Buchanan
    [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Jordan Baker
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Meyer Wolfshiem
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Owl Eyes
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Self
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
],
[
    # Towards Nick Carraway
    [6, 0, 0, 1, 0, 5, 5, 5, 5, 5, 5, 0, 4, 5],
    # Towards Jay Gatsby
    [7, 0, 0, 1, 0, 7, 7, 7, 7, 7, 7, 0, 6, 7],
    # Towards Daisy Buchanan
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Tom Buchanan
    [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Jordan Baker
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Henry C. Gatz
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Owl Eyes
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Self
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
],[
    # Towards Nick Carraway
    [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
    # Towards Jay Gatsby
    [7, 0, 0, 7, 1, 7, 7, 7, 7, 7, 7, 0, 6, 7],
    # Towards Daisy Buchanan
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Tom Buchanan
    [3, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Jordan Baker
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Henry C. Gatz
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Towards Meyer Wolfshiem
    [4, 0, 0, 1, 0, 4, 4, 4, 4, 4, 4, 0, 3, 3],
    # Self
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]
]

global chapter_names,relationships_data
chapter_names= []
relationships_data = []
def validate_chapter_data(names, chapter_values):
    # Check if lengths of names list and chapter_values list are the same
    if len(names) != len(chapter_values):
        return False

    # Check each sub-array in chapter_values
    for sub_array in chapter_values:
        if len(sub_array) != len(names):
            print("false not all ppl ")
            return False
        for value in sub_array:
            if len(value) != 14:
                print("false not 14 found")
                return False
    return True
#9
def get_dataF():
    for i in range(0,10):
        number = str(i)
        name_array = "chap" + number + "_names"
        data_array = "chap" + number + "_chapter_values"
        # Accessing dynamically named variables
        if name_array in globals():
            names = globals()[name_array]
            data = globals()[data_array]
            validate_chapter_data(names,data)
            chapter_names.append(names)
            relationships_data.append(data)

        else:
            print(f"{name_array} does not exist.")
    
    return chapter_names,relationships_data


def check_relationships_data(chapter_names, relationships_data):
    errors = []

    for chapter_idx, (names, relations) in enumerate(zip(chapter_names, relationships_data)):
        if len(names) != len(relations):
            errors.append(f"Chapter {chapter_idx + 1}: Mismatch between number of names ({len(names)}) and number of relationships ({len(relations)})")
            continue
        
        for char_idx, char_relations in enumerate(relations):
            if len(char_relations) != len(names):
                errors.append(f"Chapter {chapter_idx + 1}, Character {char_idx + 1}: Mismatch between number of names ({len(names)}) and number of relationships ({len(char_relations)})")
                continue
            
            for target_idx, relation in enumerate(char_relations):
                if not isinstance(relation, list) or len(relation) != 14 or any(not isinstance(emotion, int) for emotion in relation):
                    errors.append(f"Chapter {chapter_idx + 1}, Character {char_idx + 1}, Target {target_idx + 1}: Invalid relationship data (should be a list of 14 integers)")

    if errors:
        for error in errors:
            print(error)
    else:
        print("All relationship data is valid.")

def get_data_full_GG():
    Fchapter_names,Frelationships_data = get_dataF()
    check_relationships_data(Fchapter_names,Frelationships_data)
    return Fchapter_names,Frelationships_data


