from core.db.mongo_db import lib
from schema.models import Book, Book_up
# import smtplib
# from configuration import MIMEMultipart,MIMEText


# Create a new book
def create_book(book: Book):
    lib.insert_one(book.dict())
    return {"message": "Book created successfully"}


# Get a book by ID
def get_all_data():
    books = lib.find({})
    details = []
    for book in books:
        detail = {'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
        details.append(detail)
    return {"details": details}


def get_book_id(id: int):
    books = lib.find({})
    details = []
    for book in books:
        if book['id'] == id:
            detail = {'id': book['id'], 'title': book['title'], 'author': book['author'], 'borrowed': book['borrowed']}
            details.append(detail)
    return {"details": details}


def update_book(book_id: int, book: Book_up):
    result = lib.update_one({"id": book_id}, {"$set": book.dict()})

    if result.modified_count > 0:
        return {"message": "Book updated successfully"}
    else:
        return {"error": "Book not found"}


# Delete a book
def delete_book(book_id: int):
    result = lib.delete_one({"id": book_id})

    if result.deleted_count > 0:
        return {"message": "Book deleted successfully"}
    else:
        return {"error": "Book not found"}


"""for mailing"""


# def send_email(recipient_email, subject, body):
#     sender_email = "your_email@example.com"
#
#     sender_password = "your_email_password"
#
#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = recipient_email
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))
#
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login(sender_email, sender_password)
#         server.send_message(message)
#
#
# def send_grouped_units_email(request: EmailRequest):
#     result = lib.aggregate(pipeline)
#     email_body = ""
#
#     for item in result:
#         category = item["_id"]
#         total_units = item["total_units"]
#         email_body += f"Category: {category}, Total Units: {total_units}\n"
#
#     send_email(request.recipient_email, request.subject, email_body)
#     return {"message": "Email sent successfully"}
