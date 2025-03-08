import json
from .models.collection import CardCollection


def main() -> None:
    try:
        collection = CardCollection()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except json.JSONDecodeError:
        print("Error: Invalid JSON in data files")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
