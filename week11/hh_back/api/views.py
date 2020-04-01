from django.http.response import JsonResponse
from api.models import Company, Vacancy

def company_list(request):
    companies = Company.objects.all()
    companies_json = [company.to_json() for company in companies]  # creates new massiv
    return JsonResponse(companies_json, safe=False)

def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(company.to_json())

def vacancies_by_company(request, company_id):
    try:
        c = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    vacancies = Vacancy.objects.filter(company=c)
    json_vacancies = [v.to_json() for v in vacancies]
    return JsonResponse(json_vacancies, safe=False)

def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    vacancies_json = [vacancy.to_json() for vacancy in vacancies]
    return JsonResponse(vacancies_json, safe=False)

def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(vacancy.to_json())

def vacancy_ratings_by_salary(request):
    vacancy_ratings = Vacancy.objects.order_by('-salary')[:10]
    # vacancy_ratings = Vacancy.objects.filter(
    # ratings_by_salary=Vacancy.objects.order_by('-salary')[9].salary)
    vacancy_ratings_json = [vacancy.to_json() for vacancy in vacancy_ratings]
    return JsonResponse(vacancy_ratings_json, safe=False)

