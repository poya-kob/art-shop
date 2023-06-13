from rest_framework.response import Response
from rest_framework.views import APIView


class TempHome(APIView):
    def get(self, request):
        return Response(f'hi {request.user.mobile_number}') if request.user.is_authenticated else Response(
            'hello')
