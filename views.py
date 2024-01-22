from datetime import datetime


def parse_date(date_str):
    try:
        return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
    except ValueError:
        return datetime.strptime(date_str, '%d-%m-%Y')
    
def filter_comments(comments, search_author, at_from, at_to, like_from, like_to, reply_from, reply_to, search_text):
    filtered_comments = []

    for comment in comments:
        comment_at = parse_date(comment['at'])
        

        #checking the author condition if it is present in query string
        author_condition = not search_author or (search_author.lower() in comment['author'].lower())

        #checking the date condition if it is present in query string
        # If at_from is None or empty, set at_from_condition to True. Otherwise, check if comment_at is greater than or equal to at_from.

        at_from_condition = not at_from or comment_at >= parse_date(at_from)
        at_to_condition = not at_to or comment_at <= parse_date(at_to)

        # date_condition is True only if both at_from_condition and at_to_condition are True.
        date_condition = at_from_condition and at_to_condition
       
        like_from_condition = not like_from or comment['like'] >= int(like_from)
        like_to_condition = not like_to or comment['like'] <= int(like_to)
        like_condition = like_from_condition and like_to_condition

        reply_from_condition = not reply_from or comment['reply'] >= int(reply_from)
        reply_to_condition = not reply_to or comment['reply'] <= int(reply_to)
        reply_condition = reply_from_condition and reply_to_condition

        text_condition = not search_text or search_text.lower() in comment['text'].lower()


        if author_condition and date_condition and like_condition and reply_condition and text_condition:
            filtered_comments.append(comment)

    return filtered_comments
