from The_Great_Gatsby_data import get_data_full_GG
from Comm_data import get_dataF
from full_data_odyssey import collect_chapter_data
from Alice_in_Wonderland import *
from Doctor_Jekyll_and_Mr_Hyde import *
from The_Metamorphosis import *
from The_Picture_of_Dorian_Gray import *
# Get data for The Great Gatsby
chap_data_gg, chap_names_gg = get_data_full_GG()
total_data_gg = chap_data_gg, chap_names_gg

# Get data for The Count of Monte Cristo
chap_data_CC, chap_names_CC = get_dataF()
total_data_CC = chap_data_CC, chap_names_CC

# Get data for The Odyssey
chap_data_O, chap_names_O = collect_chapter_data()  # Assuming this function should be used here
total_data_O = chap_data_O, chap_names_O

# Get data for The Odyssey
chap_data_O, chap_names_O = collect_chapter_data()  # Assuming this function should be used here
total_data_O = chap_data_O, chap_names_O

# Get data for The Picture of Dorian Gray
chap_data_PDG, chap_names_PDG = collect_chapter_data_PDG()  # Assuming this function should be used here
total_data_PDG = chap_data_PDG, chap_names_PDG

# Get data for The Picture of Dorian Gray
chap_data_M, chap_names_M = collect_chapter_data_M()  # Assuming this function should be used here
total_data_M = chap_data_M, chap_names_M

# Get data for The Strange Case of Dr. Jekyll and Mr. Hyde
chap_data_DJ_MH, chap_names_DJ_MH = collect_chapter_data_DJ_MH()  # Assuming this function should be used here
total_data_DJ_MH = chap_data_DJ_MH, chap_names_DJ_MH

# Get data for Alice's Adventures in Wonderland"
chap_data_AW, chap_names_AW = collect_chapter_data_AW()  # Assuming this function should be used here
total_data_AW = chap_data_AW, chap_names_AW

# Create library of books
Library_of_books = {
    "The Count of Monte Cristo": total_data_CC,
    "The Odyssey": total_data_O,
    "Alice's Adventures in Wonderland":total_data_AW,
    "The Strange Case of Dr. Jekyll and Mr. Hyde":total_data_DJ_MH,
    "The Metamorphosis" :total_data_M,
    "The Picture of Dorian Gray":total_data_PDG
}


def get_range_of_indices1(array1, array2, start, end):
    # Check if start and end indices are within the bounds of the arrays
    if start < 0 or end >= len(array1) or end >= len(array2):
        raise ValueError("Start or end index out of bounds")

    # Extract the elements within the specified range for both arrays
    sub_array1 = array1[start:end+1]
    sub_array2 = array2[start:end+1]

    return sub_array1, sub_array2


def get_range_of_indices(array1, array2, start, end):
    return array1[start:end], array2[start:end]

def get_book_names():
    keys = list(Library_of_books.keys())
    return keys

def get_dic_data():
    return Library_of_books


def get_data_for_all():
    all_book_names = []
    all_chapter_data = []
    all_relationships_data = []
    names = get_book_names()
    for book in names:
        all_book_names.append(book)
        chapter_data, relationships_data = Library_of_books[book]
        all_chapter_data.append(chapter_data)
        all_relationships_data.append(relationships_data)
    return all_book_names,all_chapter_data,all_relationships_data

all_book_names,all_chapter_data,all_relationships_data = get_data_for_all()
