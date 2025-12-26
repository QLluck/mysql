from flask import request


def paginate_query(query):
    """Simple pagination helper returning items and meta."""
    page = int(request.args.get("page", 1))
    page_size = min(int(request.args.get("page_size", 20)), 100)
    items = query.limit(page_size).offset((page - 1) * page_size).all()
    total = query.order_by(None).count()
    return items, {"page": page, "page_size": page_size, "total": total}

