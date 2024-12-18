chap1_names = ["Utterson", "Enfield", "Hyde"]
chap1_data = [
    [
        [0]*14,  # Utterson's feelings towards all
        [7, 0, 0, 1, 8, 8, 6, 6, 8, 8, 7, 4, 2, 4],  # Utterson's feelings towards Enfield
        [2, 0, 0, 7, 2, 2, 3, 3, 2, 2, 1, 6, 7, 8],  # Utterson's feelings towards Hyde
    ],
    [
        [7, 0, 0, 1, 8, 8, 6, 6, 8, 8, 7, 4, 2, 4],  # Enfield's feelings towards Utterson
        [0]*14,  # Enfield's feelings towards all
        [1, 0, 0, 6, 1, 1, 2, 2, 2, 1, 1, 5, 7, 8],  # Enfield's feelings towards Hyde
    ],
    [
        [2, 0, 0, 7, 2, 2, 3, 3, 2, 2, 1, 6, 7, 8],  # Hyde's feelings towards Utterson
        [1, 0, 0, 6, 1, 1, 2, 2, 2, 1, 1, 5, 7, 8],  # Hyde's feelings towards Enfield
        [0]*14,  # Hyde's feelings towards all
    ],
]


chap2_names = ["Utterson", "Jekyll", "Lanyon", "Hyde"]
chap2_data = [
    [
        [0]*14,  # Utterson's feelings towards all
        [5, 0, 0, 2, 5, 5, 6, 6, 7, 7, 8, 5, 5, 6],  # Utterson's feelings towards Jekyll
        [7, 0, 0, 1, 8, 8, 6, 6, 8, 8, 7, 4, 2, 5],  # Utterson's feelings towards Lanyon
        [1, 0, 0, 6, 1, 1, 3, 2, 2, 1, 1, 6, 8, 7],  # Utterson's feelings towards Hyde
    ],
    [
        [5, 0, 0, 2, 5, 5, 6, 6, 7, 7, 8, 5, 5, 6],  # Jekyll's feelings towards Utterson
        [0]*14,  # Utterson's feelings towards all
        [6, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 5, 3, 4],  # Jekyll's feelings towards Lanyon
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Jekyll's feelings towards Hyde
    ],
    [
        [7, 0, 0, 1, 8, 8, 6, 6, 8, 8, 7, 4, 2, 5],  # Lanyon's feelings towards Utterson
        [6, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 5, 3, 4],  # Lanyon's feelings towards Jekyll
        [0]*14,  # Utterson's feelings towards all
        [1, 0, 0, 2, 1, 1, 3, 3, 2, 1, 1, 6, 7, 7],  # Lanyon's feelings towards Hyde
    ],
    [
        [1, 0, 0, 6, 1, 1, 3, 2, 2, 1, 1, 6, 8, 7],  # Hyde's feelings towards Utterson
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Hyde's feelings towards Jekyll
        [1, 0, 0, 2, 1, 1, 3, 3, 2, 1, 1, 6, 7, 7],  # Hyde's feelings towards Lanyon
        [0]*14,  # Utterson's feelings towards all
    ],
]
chap3_names = ["Utterson", "Jekyll"]
chap3_data = [
    [
        [0]*14,  # Utterson's feelings towards all
        [6, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Utterson's feelings towards Jekyll
    ],
    [
        [6, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Jekyll's feelings towards Utterson
        [0]*14,  # Jekyll's feelings towards all
    ],
]

chap4_names = ["Utterson", "Hyde", "Sir Danvers Carew", "Inspector Newcomen"]
chap4_data = [
    [
        [0]*14,  # Utterson's feelings towards all
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 2, 1, 6, 8, 8],  # Utterson's feelings towards Hyde
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Utterson's feelings towards Sir Danvers Carew
        [6, 0, 0, 1, 5, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Utterson's feelings towards Inspector Newcomen
    ],
    [
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 2, 1, 6, 8, 8],  # Hyde's feelings towards Utterson
        [0]*14,  # Hyde's feelings towards all
        [1, 0, 0, 9, 1, 1, 3, 2, 2, 2, 1, 7, 9, 9],  # Hyde's feelings towards Sir Danvers Carew
        [2, 0, 0, 8, 2, 2, 4, 3, 3, 3, 2, 7, 8, 8],  # Hyde's feelings towards Inspector Newcomen
    ],
    [
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Sir Danvers Carew's feelings towards Utterson
        [1, 0, 0, 9, 1, 1, 3, 2, 2, 2, 1, 7, 9, 9],  # Sir Danvers Carew's feelings towards Hyde
        [0]*14,  # Sir Danvers Carew's feelings towards all
        [4, 0, 0, 1, 4, 5, 5, 6, 7, 6, 6, 3, 2, 3],  # Sir Danvers Carew's feelings towards Inspector Newcomen
    ],
    [
        [6, 0, 0, 1, 5, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Inspector Newcomen's feelings towards Utterson
        [2, 0, 0, 8, 2, 2, 4, 3, 3, 3, 2, 7, 8, 8],  # Inspector Newcomen's feelings towards Hyde
        [4, 0, 0, 1, 4, 5, 5, 6, 7, 6, 6, 3, 2, 3],  # Inspector Newcomen's feelings towards Sir Danvers Carew
        [0]*14,  # Inspector Newcomen's feelings towards all
    ],
]



chap5_names = ["Utterson", "Jekyll", "Hyde", "Poole", "Guest"]
chap5_data = [
    [
        [0]*14,  # Utterson's feelings towards all
        [7, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Utterson's feelings towards Jekyll
        [1, 0, 0, 7, 1, 1, 3, 2, 2, 1, 1, 6, 8, 8],  # Utterson's feelings towards Hyde
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Utterson's feelings towards Poole
        [6, 0, 0, 1, 6, 6, 7, 7, 8, 7, 7, 4, 2, 4],  # Utterson's feelings towards Guest
    ],
    [
        [7, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Jekyll's feelings towards Utterson
        [0]*14,  # Jekyll's feelings towards all
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Jekyll's feelings towards Hyde
        [6, 0, 0, 1, 6, 6, 7, 7, 8, 7, 7, 4, 3, 3],  # Jekyll's feelings towards Poole
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Jekyll's feelings towards Guest
    ],
    [
        [1, 0, 0, 7, 1, 1, 3, 2, 2, 1, 1, 6, 8, 8],  # Hyde's feelings towards Utterson
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Hyde's feelings towards Jekyll
        [0]*14,  # Hyde's feelings towards all
        [2, 0, 0, 7, 2, 2, 4, 3, 3, 2, 2, 7, 8, 8],  # Hyde's feelings towards Poole
        [3, 0, 0, 6, 3, 3, 5, 4, 4, 3, 3, 6, 7, 7],  # Hyde's feelings towards Guest
    ],
    [
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Poole's feelings towards Utterson
        [6, 0, 0, 1, 6, 6, 7, 7, 8, 7, 7, 4, 3, 3],  # Poole's feelings towards Jekyll
        [2, 0, 0, 7, 2, 2, 4, 3, 3, 2, 2, 7, 8, 8],  # Poole's feelings towards Hyde
        [0]*14,  # Poole's feelings towards all
        [4, 0, 0, 1, 4, 4, 6, 5, 5, 4, 4, 5, 6, 6],  # Poole's feelings towards Guest
    ],
    [
        [6, 0, 0, 1, 6, 6, 7, 7, 8, 7, 7, 4, 2, 4],  # Guest's feelings towards Utterson
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Guest's feelings towards Jekyll
        [3, 0, 0, 6, 3, 3, 5, 4, 4, 3, 3, 6, 7, 7],  # Guest's feelings towards Hyde
        [4, 0, 0, 1, 4, 4, 6, 5, 5, 4, 4, 5, 6, 6],  # Guest's feelings towards Poole
        [0]*14,  # Guest's feelings towards all
    ],
]

chap6_names = ["Utterson", "Jekyll", "Lanyon", "Hyde", "Poole"]
chap6_data = [
    [
        [0]*14,  # Utterson's feelings towards all
        [6, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Utterson's feelings towards Jekyll
        [7, 0, 0, 1, 8, 8, 6, 6, 8, 8, 7, 4, 2, 5],  # Utterson's feelings towards Lanyon
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 2, 1, 6, 8, 8],  # Utterson's feelings towards Hyde
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Utterson's feelings towards Poole
    ],
    [
        [6, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Jekyll's feelings towards Utterson
        [0]*14,  # Jekyll's feelings towards all
        [6, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 5, 3, 4],  # Jekyll's feelings towards Lanyon
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Jekyll's feelings towards Hyde
        [6, 0, 0, 1, 6, 6, 7, 7, 8, 7, 7, 4, 3, 3],  # Jekyll's feelings towards Poole
    ],
    [
        [7, 0, 0, 1, 8, 8, 6, 6, 8, 8, 7, 4, 2, 5],  # Lanyon's feelings towards Utterson
        [6, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 5, 3, 4],  # Lanyon's feelings towards Jekyll
        [0]*14,  # Lanyon's feelings towards all
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 1, 1, 6, 8, 8],  # Lanyon's feelings towards Hyde
        [4, 0, 0, 1, 4, 4, 6, 5, 5, 4, 4, 5, 6, 6],  # Lanyon's feelings towards Poole
    ],
    [
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 2, 1, 6, 8, 8],  # Hyde's feelings towards Utterson
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Hyde's feelings towards Jekyll
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 1, 1, 6, 8, 8],  # Hyde's feelings towards Lanyon
        [0]*14,  # Hyde's feelings towards all
        [2, 0, 0, 7, 2, 2, 4, 3, 3, 2, 2, 7, 8, 8],  # Hyde's feelings towards Poole
    ],
    [
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Poole's feelings towards Utterson
        [6, 0, 0, 1, 6, 6, 7, 7, 8, 7, 7, 4, 3, 3],  # Poole's feelings towards Jekyll
        [4, 0, 0, 1, 4, 4, 6, 5, 5, 4, 4, 5, 6, 6],  # Poole's feelings towards Lanyon
        [2, 0, 0, 7, 2, 2, 4, 3, 3, 2, 2, 7, 8, 8],  # Poole's feelings towards Hyde
        [0]*14,  # Poole's feelings towards all
    ],
]

chap7_names = ["Utterson", "Enfield", "Jekyll"]
chap7_data = [
    [
        [0]*14,  # Utterson's feelings towards all
        [7, 0, 0, 1, 8, 8, 6, 6, 8, 8, 7, 4, 2, 4],  # Utterson's feelings towards Enfield
        [6, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Utterson's feelings towards Jekyll
    ],
    [
        [7, 0, 0, 1, 8, 8, 6, 6, 8, 8, 7, 4, 2, 4],  # Enfield's feelings towards Utterson
        [0]*14,  # Enfield's feelings towards all
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Enfield's feelings towards Jekyll
    ],
    [
        [6, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Jekyll's feelings towards Utterson
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Jekyll's feelings towards Enfield
        [0]*14,  # Jekyll's feelings towards all
    ],
]

chap8_names = ["Utterson", "Poole", "Jekyll", "Hyde"]
chap8_data = [
    [
        [0]*14,  # Utterson's feelings towards all
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Utterson's feelings towards Poole
        [6, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Utterson's feelings towards Jekyll
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 2, 1, 6, 8, 8],  # Utterson's feelings towards Hyde
    ],
    [
        [5, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 4, 3, 3],  # Poole's feelings towards Utterson
        [0]*14,  # Poole's feelings towards all
        [6, 0, 0, 1, 6, 6, 7, 7, 8, 7, 7, 4, 3, 3],  # Poole's feelings towards Jekyll
        [2, 0, 0, 7, 2, 2, 4, 3, 3, 2, 2, 7, 8, 8],  # Poole's feelings towards Hyde
    ],
    [
        [6, 0, 0, 1, 7, 6, 6, 7, 8, 7, 7, 4, 2, 4],  # Jekyll's feelings towards Utterson
        [6, 0, 0, 1, 6, 6, 7, 7, 8, 7, 7, 4, 3, 3],  # Jekyll's feelings towards Poole
        [0]*14,  # Jekyll's feelings towards all
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Jekyll's feelings towards Hyde
    ],
    [
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 2, 1, 6, 8, 8],  # Hyde's feelings towards Utterson
        [2, 0, 0, 7, 2, 2, 4, 3, 3, 2, 2, 7, 8, 8],  # Hyde's feelings towards Poole
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Hyde's feelings towards Jekyll
        [0]*14,  # Hyde's feelings towards all
    ],
]
chap9_names = ["Lanyon", "Jekyll", "Hyde"]
chap9_data = [
    [
        [0]*14,  # Lanyon's feelings towards all
        [6, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 5, 3, 4],  # Lanyon's feelings towards Jekyll
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 2, 1, 6, 8, 8],  # Lanyon's feelings towards Hyde
    ],
    [
        [6, 0, 0, 1, 5, 5, 7, 7, 8, 7, 7, 5, 3, 4],  # Jekyll's feelings towards Lanyon
        [0]*14,  # Jekyll's feelings towards all
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Jekyll's feelings towards Hyde
    ],
    [
        [1, 0, 0, 8, 1, 1, 3, 2, 2, 2, 1, 6, 8, 8],  # Hyde's feelings towards Lanyon
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Hyde's feelings towards Jekyll
        [0]*14,  # Hyde's feelings towards all
    ],
]

chap10_names = ["Jekyll", "Hyde"]
chap10_data = [
    [
        [0]*14,  # Jekyll's feelings towards all
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Jekyll's feelings towards Hyde
    ],
    [
        [4, 0, 0, 1, 2, 2, 6, 5, 5, 5, 7, 7, 8, 8],  # Hyde's feelings towards Jekyll
        [0]*14,  # Hyde's feelings towards all
    ],
]


global start , end 
start = 1
end = 10
def collect_chapter_data_DJ_MH():
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