from rest_framework import status
# from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import spaceship

statusCode = status.HTTP_400_BAD_REQUEST
RESPONSE = {
    'success': 'false',
    'status code': status.HTTP_400_BAD_REQUEST,
    'message': 'City and Planet Does not exist',
}


# Create your views here.
@api_view(['POST', ])
def AddSpaceship(request):
    if (spaceship.objects.filter(pk=request.data['id']).exists()):
        # e=spaceship.objects.filter(pk=request.data['id'])
        for i in spaceship.objects.filter(ship_id=request.data['id']):
            id = i.ship_id
            name = i.name
            model = i.model
            city = i.city
            planet = i.planet
            status = i.status
        print("entered already exists")
        # statusCode = status.HTTP_200_OK
        response = {
            'success': 'False',
            'statusCode': "312",
            'message': 'Spaceship already exists',
            'data': {
                'id': id,
                'name': name,
                'model': model,
                'city': city,
                'planet': planet,
                'status': status,
            }}
        print(response)
    else:
        try:
            print("first time")
            e = spaceship()
            e.ship_id = request.data['id']
            e.name = request.data['name']
            e.model = request.data['model']
            e.city = request.data['city']
            e.planet = request.data['planet']
            if 'status' in request.data.keys():
                e.status = request.data['status']
            e.save()
            response = {
                'success': 'True',
                'statusCode': "200",
                'message': 'Spaceship added Successfully',
            }
        except Exception as e:
            print(e)
            response = {
                'success': 'False',
                'statusCode': "301",
                'message': e,
            }
    return Response(response)
