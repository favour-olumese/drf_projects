from .models import Book
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.response import Response
from books.serializers import BookSerializer


def serializer(serializer_class):
    """
    This allows the browsable API generate the form field for a function
    based view.

    This solution is omitted from the DRF documentation.
    Gotten from: https://stackoverflow.com/a/78421547/18145407
    """
    def decorator(api_view):
        api_view.cls.serializer_class = serializer_class
        api_view.view_class.serializer_class = serializer_class
        return api_view

    return decorator


@serializer(BookSerializer)
@api_view(['GET', 'POST'])
def book_list(request):
    """
    List all books or add a new book.
    """
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@serializer(BookSerializer)
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, pk):
    """
    Retrieve, update, or deleate a book.
    """
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)