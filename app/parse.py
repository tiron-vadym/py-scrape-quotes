from app.output_csv_path import get_quotes, write_quotes_to_csv


def main() -> None:
    quotes = get_quotes()
    write_quotes_to_csv(quotes)
    print("Quotes have been written")


if __name__ == "__main__":
    main()
