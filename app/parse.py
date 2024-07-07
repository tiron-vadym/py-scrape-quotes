import output_csv_path


def main() -> None:
    quotes = output_csv_path.get_quotes()

    output_csv_path.write_quotes_to_csv(quotes)
    print("Quotes have been written")


if __name__ == "__main__":
    main()
