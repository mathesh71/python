def main():
    # ---- 1. TUPLE (immutable data - student IDs) ----
    student_ids = (101, 102, 103, 104)
    print("Student IDs (tuple):", student_ids)

    # ---- 2. LIST (ordered collection - student names) ----
    student_names = ["Alice", "Bob", "Charlie", "Diana"]
    print("Student Names (list):", student_names)

    # List operations
    student_names.append("Eve")
    print("After adding Eve:", student_names)
    student_names.remove("Bob")
    print("After removing Bob:", student_names)
    print("Slicing names [1:3]:", student_names[1:3])

    # ---- 3. DICTIONARY (key-value pairs - ID to Name) ----
    student_dict = dict(zip(student_ids, student_names))  # Combines tuple and list
    print("Student Dictionary (ID to Name):", student_dict)

    # Dictionary operations
    student_dict[105] = "Frank"  # Add new entry
    del student_dict[103]        # Remove entry by key
    print("Updated Dictionary:", student_dict)
    print("All IDs:", list(student_dict.keys()))
    print("All Names:", list(student_dict.values()))

    # ---- 4. SET (unique clubs students are in) ----
    club_a = {"Alice", "Diana", "Eve"}
    club_b = {"Charlie", "Eve", "Frank"}
    print("Club A members:", club_a)
    print("Club B members:", club_b)

    # Set operations
    print("Union (all students in any club):", club_a | club_b)
    print("Intersection (in both clubs):", club_a & club_b)
    print("Difference (in A not in B):", club_a - club_b)
    print("Symmetric Difference (exclusive members):", club_a ^ club_b)

    # Bonus: list comprehension
    capital_names = [name.upper() for name in student_names]
    print("Capitalized Names:", capital_names)

if __name__ == "__main__":
    main()
