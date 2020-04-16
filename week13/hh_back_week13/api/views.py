from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

# Token
# eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNTg3MDM0OTUxLCJlbWFpbCI6ImFkbWluQGdtYWlsLmNvbSJ9.GvuBOogYj49VsjyZT4GGh3NU5OQf6nSkuLfG_jEHw6U


# FUNCTION BASED VIEW BY API_VIEW FROM REST FRAMEWORK: COMPANY_LIST AND COMPANY_DETAIL
@api_view(['GET', 'POST'])
def company_list(request):
    if request.method == 'GET':
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True) # companies_json = [c.to_json() for c in companies]
        permission_classes = (IsAuthenticated,)
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

    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})

@api_view(['GET'])
def vacancies_by_company(request, company_id):
    try:
        companies = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        vacancies = companies.vacancies.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)


# CLASS BASED VIEW: SEPARATE HTTP METHODS
class VacancyListAPIView(APIView):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():  # Validate data from client
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VacancyDetailAPIView(APIView):
    def get_object(self, id):
        #gets inf from vacancy title using id and checks if it exists
        try:
            vacancy = Vacancy.objects.get(id=id)
        except Vacancy.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    def put(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, vacancy_id):
        vacancy = self.get_object(vacancy_id)
        vacancy.delete()
        return Response({'deleted': True})


@api_view(['GET'])
def vacancies_top10(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.order_by("-salary")[:10]
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

# class vacancies_top10APIView(APIView):
#     def get(self, request):
#         vacancy_ratings = Vacancy.objects.order_by('-salary')[:10]
#         serializer = VacancySerializer(vacancy_ratings, many=False)
#         return Response(serializer.data)


# class vacancies_top10APIView(generics.ListCreateAPIView):
#     queryset = Vacancy.objects.order_by('-salary')[:10]
#     serializer_class = VacancySerializer
