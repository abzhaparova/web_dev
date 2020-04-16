from django.urls import path
from api.views import company_list, company_detail, vacancies_by_company, VacancyListAPIView, VacancyDetailAPIView, vacancies_top10
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies', company_list),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies', vacancies_by_company),
    path('vacancies/', VacancyListAPIView.as_view()),
    path('vacancies/<int:vacancy_id>/', VacancyDetailAPIView.as_view()),
    path('vacancies/top_ten', vacancies_top10),
]