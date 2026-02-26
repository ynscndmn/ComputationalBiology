

def find_motif_indices(sequence, motif):
    """
    Core Logic: Finds all 1-based starting positions of a motif in a DNA sequence.
    """
    indices = []
    
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i : i + len(motif)] == motif:
            indices.append(i + 1)
    return ' '.join(map(str, indices))

def run_sample():
    """Handles the predefined sample dataset."""
    sample_seq = "GATATATGCATATACTT"
    sample_motif = "ATAT"
    print(f"\n[SAMPLE DATA]")
    print(f"Sequence: {sample_seq}")
    print(f"Motif:    {sample_motif}")
    
    result = find_motif_indices(sample_seq, sample_motif)
    print(f"RESULT:   {result}")

def run_manual_input():
    """Handles user-provided input from the terminal."""
    print("\n[MANUAL INPUT MODE]")
    seq = input("Enter DNA sequence (s): ").strip().upper()
    motif = input("Enter motif to find (t): ").strip().upper()
    
    if seq and motif:
        result = find_motif_indices(seq, motif)
        print(f"\nRESULT: {result}")
    else:
        print("\n[ERROR] Inputs cannot be empty!")

def display_menu():
    """Prints the main menu options."""
    print("\n" + "="*35)
    print("      DNA MOTIF FINDER MENU")
    print("="*35)
    print("1. Run Sample Dataset")
    print("2. Enter Custom Data Manually")
    print("3. Exit")
    print("-" * 35)

def main():
    """Main program loop."""
    while True:
        display_menu()
        choice = input("Select an option (1-3): ").strip()

        if choice == "1":
            run_sample()
        elif choice == "2":
            run_manual_input()
        elif choice == "3":
            print("\nExiting... See you later!")
            break
        else:
            print("\n[INVALID] Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()