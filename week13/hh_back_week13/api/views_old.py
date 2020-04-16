import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Vacancy
from api.serializers import CompanySerializer, VacancySerializer


# CRUD - For Company Model

@csrf_exempt
def company_list(request):
    if request.method == 'GET':
        # companies = Company.objects.filter(name='')
        # companies = Company.objects.filter(name_contains='product')
        # companies = Company.objects.filter(name__startswith='')
        # companies = Company.objects.filter(name__endswith='')
        # companies = Company.objects.filter(name__exact='')

        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)    # companies_json = [c.to_json() for c in companies]
        return JsonResponse(serializer.data, safe=False)       # return JsonResponse(companies_json, safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)

        serializer = CompanySerializer(data=request_body)
        if serializer.is_valid():  # Validate data from client
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

@csrf_exempt
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer(company)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        request_body = json.loads(request.body)
        serializer = CompanySerializer(instance=company, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

    # Delete selected object
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'deleted': True})


# def vacancies_by_company(request, company_id):
#     try:
#         c = Company.objects.get(id=company_id)
#     except Company.DoesNotExist as e:
#         return JsonResponse({'error': str(e)})
#     vacancies = Vacancy.objects.filter(company=c)
#     json_vacancies = [v.to_json() for v in vacancies]
#     return JsonResponse(json_vacancies, safe=False)


@csrf_exempt
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        request_body = json.loads(request.body)

        serializer = VacancySerializer(data=request_body)
        if serializer.is_valid():  # Validate data from client
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        request_body = json.loads(request.body)

        serializer = VacancySerializer(instance=vacancy, data=request_body)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': serializer.errors})

    # Delete selected object
    elif request.method == 'DELETE':
        vacancy.delete()
        return JsonResponse({'deleted': True})

#
# def vacancy_ratings_by_salary(request):
#     vacancy_ratings = Vacancy.objects.order_by('-salary')[:10]
#     # vacancy_ratings = Vacancy.objects.filter(
#     # ratings_by_salary=Vacancy.objects.order_by('-salary')[9].salary)
#     vacancy_ratings_json = [vacancy.to_json() for vacancy in vacancy_ratings]
#     return JsonResponse(vacancy_ratings_json, safe=False)
