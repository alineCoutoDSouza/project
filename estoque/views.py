from .models import Produto
from .serializers import ProdutoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def getProdutos(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def getProdutoById(request,pk):
    try:
        produto = Produto.objects.get(id=pk)
    except Produto.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == 'PUT':
        serializer = ProdutoSerializer(produto,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)