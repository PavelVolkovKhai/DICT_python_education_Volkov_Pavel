FORMATTERS = [
    "plain",
    "bold",
    "italic",
    "header",
    "link",
    "inline-code",
    "ordered-list",
    "unordered-list",
    "new-line"
]


def show_help():
    print(
        "Available formatters: "
        "plain bold italic header link inline-code "
        "ordered-list unordered-list new-line"
    )
    print("Special commands: !help !done")


def read_list():
    while True:
        try:
            number_of_rows = int(input("Number of rows: > "))
        except ValueError:
            print("The number of rows should be greater than zero.")
            continue

        if number_of_rows <= 0:
            print("The number of rows should be greater than zero.")
            continue

        rows = []

        for i in range(number_of_rows):
            row = input(f"Row #{i + 1}: > ")
            rows.append(row)

        return rows


def save_markdown(markdown):
    with open("output.md", "w", encoding="utf-8") as file:
        file.write("\n".join(markdown))


def main():
    markdown = []

    while True:
        command = input("Choose a formatter: > ")

        if command == "!help":
            show_help()

        elif command == "!done":
            save_markdown(markdown)
            break

        elif command not in FORMATTERS:
            print("Unknown formatting type or command")
            continue

        elif command == "new-line":
            markdown.append("")

        elif command == "header":
            try:
                level = int(input("Level: > "))
            except ValueError:
                print("The level should be within the range of 1 to 6.")
                continue

            if not 1 <= level <= 6:
                print("The level should be within the range of 1 to 6.")
                continue

            text = input("Text: > ")
            markdown.append("#" * level + " " + text)

        elif command == "link":
            label = input("Label: > ")
            url = input("URL: > ")
            markdown.append(f"[{label}]({url})")

        elif command == "ordered-list":
            rows = read_list()
            for i, row in enumerate(rows, start=1):
                markdown.append(f"{i}. {row}")

        elif command == "unordered-list":
            rows = read_list()
            for row in rows:
                markdown.append(f"* {row}")

        else:
            text = input("Text: > ")

            if command == "plain":
                formatted_text = text
            elif command == "bold":
                formatted_text = f"**{text}**"
            elif command == "italic":
                formatted_text = f"*{text}*"
            elif command == "inline-code":
                formatted_text = f"`{text}`"
            else:
                continue

            markdown.append(formatted_text)

        print("\n".join(markdown))
        print()


if __name__ == "__main__":
    main()
