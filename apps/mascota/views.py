from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from .models import Mascota

from .serializers import MascotaSerializer
from .serializers import MascotaVotoSerializer


class MascotaViewPost(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    serializer = MascotaSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MascotaViewList(generics.ListAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer


class MascotaViewUpdate(generics.UpdateAPIView):
    queryset = Mascota.objects.all()
    serializer_class = MascotaVotoSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        instance.votos = instance.votos + 1
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
