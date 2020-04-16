from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer


# CRUD - For Company Model
# FUNCTION BASED VIEW BY API_VIEW FROM REST FRAMEWORK: COMPANY_LIST AND COMPANY_DETAIL
@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)    # companies_json = [c.to_json() for c in companies]
        return Response(serializer.data)                        # return JsonResponse(companies_json, safe=False)

    elif request.method == 'POST':
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():  # Validate data from client
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    # Delete selected object
    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})

