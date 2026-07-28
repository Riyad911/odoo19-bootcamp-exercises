# F1 — reports (Session 2 + 3 skills) — Bookshop


def remove_duplicate_isbn(books):
    seen_isbn = list()
    unique_books = list()
    for book in books:
        if book["isbn"] not in seen_isbn:
            seen_isbn.append(book["isbn"])
            unique_books.append(book)
    return unique_books

def count_by_genre(books):
    # TODO: {"kids": 2, "tech": 1, ...}
    report_count = dict()
    for book in books:
        genre = book.get("genre", "Unknown")
        report_count[genre] = report_count.get(genre, 0) + 1
    return report_count



def total_stock_value(books):
    # TODO: sum(stock * price)
    total = 0
    for book in books:
        total += book["stock"] * book["price"]
    return total

def average_price_by_genre(books):
    # TODO: {"kids": 30.0, "tech": 120.0, ...}
    report = {}

    for book in books:
        genre = book.get("genre", "Unknown")
        price = book.get("price", 0)

        if genre not in report:
            report[genre] = {"total": 0, "count": 0}

        report[genre]["total"] += price
        report[genre]["count"] += 1

    averages = {}

    for genre, data in report.items():
        averages[genre] = data["total"] / data["count"]

    return averages




def out_of_stock_titles(books):
    # TODO: list of titles where stock == 0
    out_of_books = list()
    for book in books:
        if book["stock"] == 0:
            out_of_books.append(book["title"])
    return out_of_books

def unique_authors(books):
    # TODO: list of author names, no duplicates
    unique_auth = list()
    for book in books:
        if book["author"] not in unique_auth:
            unique_auth.append(book["author"])
    return unique_auth
