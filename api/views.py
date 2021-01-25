from django.http import JsonResponse
from rest_framework import status
# from rest_framework.generics import RetrieveAPIView
from rest_framework.decorators import api_view

from api.models import spaceship, location

statusCode = status.HTTP_400_BAD_REQUEST
RESPONSE = {
    'success': 'false',
    'status code': status.HTTP_400_BAD_REQUEST,
    'message': 'City and Planet Does not exist',
}


# Create your views here.
@api_view(['POST', ])
def DelSpaceship(request):
    if (spaceship.objects.filter(pk=request.data['id']).exists()):
        for i in spaceship.objects.filter(ship_id=request.data['id']):
            location_id = i.loc.loc_id
        for i in location.objects.filter(loc_id=location_id):
            i.capacity += 1
            i.save()
        spaceship.objects.filter(pk=request.data['id']).delete()
        response = {
            'success': 'True',
            'statusCode': "200",
            'message': 'Spaceship Removed', }
    else:
        response = {
            'success': 'False',
            'statusCode': "306",
            'message': 'Spaceship Does not exists',
        }
    return JsonResponse(response)


@api_view(['POST', ])
def DelLocation(request):
    if (location.objects.filter(pk=request.data['id']).exists()):
        location.objects.filter(pk=request.data['id']).delete()
        response = {
            'success': 'True',
            'statusCode': "200",
            'message': 'Location Removed', }
    else:
        response = {
            'success': 'False',
            'statusCode': "305",
            'message': 'Location Does not exists',
        }
    return JsonResponse(response)


@api_view(['POST', ])
def UpdateStatus(request):
    if (spaceship.objects.filter(pk=request.data['id']).exists()):
        i = spaceship.objects.filter(ship_id=request.data['id'])[0]
        i.status = request.data['status']
        i.save()
        response = {
            'success': 'True',
            'statusCode': "200",
            'message': 'Spaceship Status Updated',
            'data': {
                'id': i.ship_id,
                'name': i.name,
                'model': i.model,
                'city': i.loc.city,
                'planet': i.loc.planet,
                'status': i.status,
            }}
    else:
        response = {
            'success': 'False',
            'statusCode': "306",
            'message': 'Spaceship Does not exists',
        }
    return JsonResponse(response)


@api_view(['POST', ])
def Travel(request):
    if (spaceship.objects.filter(pk=request.data['id']).exists()) and (
    location.objects.filter(loc_id=request.data['dest_id']).exists()):
        i = spaceship.objects.filter(ship_id=request.data['id'])[0]
        if i.status == 'operational' and i.loc.loc_id != request.data['dest_id']:
            k = location.objects.filter(loc_id=i.loc.loc_id)[0]
            k.capacity += 1
            j = location.objects.filter(loc_id=request.data['dest_id'])[0]
            if j.capacity > 0 and j.capacity <= 10:
                j.capacity -= 1
                j.save()
                i.loc = j
                i.save()
                k.save()
                response = {
                    'success': 'True',
                    'statusCode': "200",
                    'message': 'Spaceship succesfully travelled',
                }
            else:
                response = {
                    'success': 'False',
                    'statusCode': "308",
                    'message': 'Capacity of Destination port is insufficient',
                }
        else:
            response = {
                'success': 'False',
                'statusCode': "309",
                'message': 'Spaceship is not in Operational state or Destination port is same as Current port',
            }
    else:
        response = {
            'success': 'False',
            'statusCode': "306",
            'message': 'Spaceship or Destination Spaceport does not exists',
        }
    return JsonResponse(response)

@api_view(['POST', ])
def AddSpaceship(request):
    if (spaceship.objects.filter(pk=request.data['id']).exists()):
        # e=spaceship.objects.filter(pk=request.data['id'])
        for i in spaceship.objects.filter(ship_id=request.data['id']):
            id = i.ship_id
            name = i.name
            model = i.model
            city = i.loc.city
            planet = i.loc.planet
            status = i.status
        # print("entered already exists")
        # statusCode = status.HTTP_200_OK
        response = {
            'success': 'False',
            'statusCode': "304",
            'message': 'Spaceship already exists',
            'data': {
                'id': id,
                'name': name,
                'model': model,
                'city': city,
                'planet': planet,
                'status': status,
            }}
        #print(response)
    else:
        try:
            #print("first time")
            e = spaceship()
            e.ship_id = request.data['id']
            e.name = request.data['name']
            e.model = request.data['model']
            # print("number 1")
            if (location.objects.filter(city=request.data['city'], planet=request.data['planet']).exists()):
                for i in location.objects.filter(city=request.data['city'], planet=request.data['planet']):
                    if i.capacity > 0:
                        i.capacity -= 1
                        e.loc = i
                        i.save()
                    else:
                        response = {
                            'success': 'False',
                            'statusCode': "303",
                            'message': 'Spaceship location capacity is full',
                        }
                        return JsonResponse(response)
            else:
                list_loc_id = []
                l = location()
                for i in location.objects.all():
                    list_loc_id.append(i.loc_id)
                if list_loc_id == []:
                    l.loc_id = 1
                else:
                    l.loc_id = max(list_loc_id) + 1
                l.city = request.data['city']
                l.planet = request.data['planet']
                l.capacity -= 1
                e.loc = l
                l.save()
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
    # response = json.dumps(response)
    return JsonResponse(response)


@api_view(['POST', ])
def Addlocation(request):
    if (location.objects.filter(pk=request.data['id']).exists()):
        for i in location.objects.filter(loc_id=request.data['id']):
            id = i.loc_id
            city = i.city
            planet = i.planet
            capacity = i.capacity

        response = {
            'success': 'False',
            'statusCode': "302",
            'message': 'Location already exists',
            'data': {
                'id': id,
                'city': city,
                'planet': planet,
                'capacity': capacity,
            }}

    else:
        try:
            e = location()
            e.loc_id = request.data['id']
            e.city = request.data['city']
            e.planet = request.data['planet']
            e.save()
            response = {
                'success': 'True',
                'statusCode': "200",
                'message': 'Location added Successfully',
            }
            # print(response)
            #return JsonResponse(response)
        except Exception as e:
            print(e)
            response = {
                'success': 'False',
                'statusCode': "301",
                'message': e,
            }
    # print(response)
    return JsonResponse(response)
