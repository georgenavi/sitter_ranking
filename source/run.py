from source.config import INPUT_FILE, OUTPUT_FILE
from csv_reader import load_sitters
from csv_writer import save_sitters


def main(input_file: str = INPUT_FILE, output_file: str = OUTPUT_FILE) -> None:
    """Process sitter reviews and generate rankings."""
    print(f"Loading data from {input_file}...")
    sitters_map = load_sitters(input_file)

    if not sitters_map:
        print("No data to process. Exiting.")
        return

    print(f"Loaded {len(sitters_map)} sitters")

    print(f"Saving results to {output_file}...")
    save_sitters(list(sitters_map.values()), output_file)

    print("Done!")


if __name__ == "__main__":
    main()