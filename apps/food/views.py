from .models import Food
from rest_framework import status
from .serializers import FoodSerializer
from rest_framework.response import Response
from rest_framework.viewsets import mixins, GenericViewSet


class Create(mixins.CreateModelMixin, GenericViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def create(self, request, *args, **kwargs):

        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            food = serializer.save()
            food.save()
            headers = self.get_success_headers(serializer.data)
            return Response({
                'message': 'Food Registered!', 'food': serializer.data
            },
                status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class List(mixins.ListModelMixin, GenericViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer


class Read(mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = 'name'

class Update(mixins.UpdateModelMixin, GenericViewSet):
    queryset = Food.objects.all()
    lookup_field = 'name'
    serializer_class = FoodSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        super(Update, self).update(request, *args, **kwargs)
        event = self.get_object()

        serializer = FoodSerializer(event)
        return Response(serializer.data)


class Delete(mixins.DestroyModelMixin, GenericViewSet):
    queryset = Food.objects.all()
    lookup_field = 'name'
    serializer_class = FoodSerializer