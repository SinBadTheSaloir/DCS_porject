import pg8000
from pg8000.exceptions import DatabaseError

from Library import *

# Define global variable for database credentials
code_password = "Christ_is_king25"



# Define the function to insert the layers into the database
def insert_layers():
    layers = [
        "Friendship", "Family", "Romantic Interest", "Enemies",
        "Political Alignment", "Employment Relationship", "Social Standing",
        "Trust", "Respect", "Communication",
        "Shared History", "Conflict History",
        "Shared Goals", "Conflict of Interest"
    ]
    
    try:
        # Connect to PostgreSQL
        conn = pg8000.connect(
            database="tensor_data",
            user="postgres",
            password=code_password,
            host="localhost",
            port=5432
        )
        cursor = conn.cursor()
        
        # Insert each layer into the Layers table
        for layer_name in layers:
            cursor.execute("""
                INSERT INTO Layers (layer_name)
                VALUES (%s) ON CONFLICT DO NOTHING;
            """, (layer_name,))
        
        # Commit the transaction
        conn.commit()
        
        # Close connection
        cursor.close()
        conn.close()
        print("Layers successfully inserted into the database.")
    except DatabaseError as e:
        print(f"Error inserting layers: {e}")

# Define the function to insert story data into the database
def insert_story_data(book_title, chapter_number, character_names, adjacency_matrix):
    layers = [
        "Friendship", "Family", "Romantic Interest", "Enemies",
        "Political Alignment", "Employment Relationship", "Social Standing",
        "Trust", "Respect", "Communication",
        "Shared History", "Conflict History",
        "Shared Goals", "Conflict of Interest"
    ]

    try:
        # Connect to PostgreSQL
        conn = pg8000.connect(
            database="tensor_data",
            user="postgres",
            password=code_password,
            host="localhost",
            port=5432
        )
        cursor = conn.cursor()
        
        # Insert book data into the Books table
        cursor.execute("""
            INSERT INTO Books (title)
            VALUES (%s) ON CONFLICT (title) DO NOTHING RETURNING book_id;
        """, (book_title,))
        result = cursor.fetchone()
        if result:
            book_id = result[0]
        else:
            cursor.execute("SELECT book_id FROM Books WHERE title = %s;", (book_title,))
            book_id = cursor.fetchone()[0]
        
        # Insert chapter data into the Chapters table
        cursor.execute("""
            INSERT INTO Chapters (book_id, chapter_number)
            VALUES (%s, %s) RETURNING chapter_id;
        """, (book_id, chapter_number))
        chapter_result = cursor.fetchone()
        chapter_id = chapter_result[0] if chapter_result else None
        
        # Insert character data into the Characters table and store character IDs
        character_ids = {}
        for name in character_names:
            cursor.execute("""
                INSERT INTO Characters (name, book_id)
                VALUES (%s, %s) ON CONFLICT (name, book_id) DO NOTHING RETURNING character_id;
            """, (name, book_id))
            char_result = cursor.fetchone()
            if char_result:
                character_ids[name] = char_result[0]
            else:
                cursor.execute("SELECT character_id FROM Characters WHERE name = %s AND book_id = %s;", (name, book_id))
                character_ids[name] = cursor.fetchone()[0]
        
        # Insert relationships into the Node_Interactions table
        for i, source_name in enumerate(character_names):
            for j, target_name in enumerate(character_names):
                if i != j:  # Skip self-relations
                    for layer_idx, relationship_strength in enumerate(adjacency_matrix[i][j]):
                        if relationship_strength > 0:
                            cursor.execute("""
                                INSERT INTO Node_Interactions (
                                    character_a_id, character_b_id, layer_id, chapter_id, relationship_strength
                                )
                                VALUES (%s, %s, %s, %s, %s);
                            """, (
                                character_ids[source_name],
                                character_ids[target_name],
                                layer_idx + 1,  # Layer ID (assuming layers table has pre-populated IDs 1-14)
                                chapter_id,
                                relationship_strength
                            ))
        
        # Commit the transaction
        conn.commit()
        
        # Close connection
        cursor.close()
        conn.close()
        print("Story data successfully inserted into the database.")
    except DatabaseError as e:
        print(f"Error inserting story data: {e}")




def insert_book_data(book_title, chapters_names, relationships_data):
    # Ensure layers are inserted before adding story data
    insert_layers()
    
    for chapter_number, (character_names, adjacency_matrix) in enumerate(zip(chapters_names, relationships_data), start=1):
        insert_story_data(book_title, chapter_number, character_names, adjacency_matrix)


    
all_book_names,all_chapter_data,all_relationships_data = get_data_for_all()
print(all_book_names)
print(len(all_chapter_data))
print(len(all_relationships_data))

def add_libary_to_data_base():
    all_book_names,all_chapter_data,all_relationships_data = get_data_for_all()

    for book_count in range(0,len(all_book_names)):
        book_title = all_book_names[book_count]
        chapters_names = all_chapter_data[book_count]
        relationships_data = all_relationships_data[book_count]
        insert_book_data(book_title, chapters_names, relationships_data)
        print("this one has been done",book_title)



add_libary_to_data_base()

#insert_book_data(book_title="The Great Gatsby", chapters_names=chapters_names, relationships_data=relationships_data)
 