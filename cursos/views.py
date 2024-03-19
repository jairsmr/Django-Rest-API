from rest_framework import mixins, viewsets
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer


class CursosViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    # def get(self, request):
    #     cursos = Curso.objects.all()
    #     serializer = CursoSerializer(cursos, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = CursoSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class CursoAPIView(generics.ListAPIView):
#     queryset = Curso.objects.all()
#     serializer_class =CursoSerializer


class AvaliacoesViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    # def get(self, request):
    #     avaliacoes = Avaliacao.objects.all()
    #     serializer = AvaliacaoSerializer(avaliacoes, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request):
    #     serializer = AvaliacaoSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


# class AvalaiacaoAPIView(generics.ListAPIView):
#     queryset = Curso.objects.all()
#     serializer_class =AvaliacaoSerializer
