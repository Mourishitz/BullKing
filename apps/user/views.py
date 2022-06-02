from rest_framework import status
from apps.user.models import User
from rest_framework.response import Response
from apps.user.serializers import UserSerializer
from apps.core.views import generate_random_password
from rest_framework.viewsets import mixins, GenericViewSet


class Create(mixins.CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):

        data = request.data
        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            pass_word = generate_random_password()
            user = serializer.save()
            user.set_password(pass_word)
            user.username = user.email
            user.save()
            headers = self.get_success_headers(serializer.data)

            email_body = 'Olá '+user.first_name+' aqui está sua senha provisória \n'+str(pass_word)
            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Email Jobtime'}
            Util.send_email(data)

            return Response({
                'message': 'Usuário criado com sucesso!', 'user': serializer.data
            },
                status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Read(mixins.RetrieveModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'


class List(mixins.ListModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class Update(mixins.UpdateModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        super(Update, self).update(request, *args, **kwargs)
        user = self.get_object()

        if request.data.get('email'):
            user.username = user.email
            user.save()

        if request.data.get('password'):
            user.set_password(request.data.get('password'))
            user.save()

        serializer = UserSerializer(user)
        return Response(serializer.data)


class Delete(mixins.DestroyModelMixin, GenericViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'id'
