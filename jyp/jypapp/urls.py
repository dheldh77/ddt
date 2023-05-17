from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import (
    DetailEmployee, ListPost, DetailPost, SearchPost,
    RecommandByJob, RecommandByViewLog, RecommandBySearchLog,
    RecommandByFollow
)


urlpatterns = [
    path('detail_employee/<str:emp_id>/', DetailEmployee.as_view()),
    path('list_post/', ListPost.as_view()),
    path('detail_post/<int:post_id>/', DetailPost.as_view()),
    path('search_post/', SearchPost.as_view()),
    path('recommand_by_job/', RecommandByJob.as_view()),
    path('recommand_by_view_log/', RecommandByViewLog.as_view()),
    path('recommand_by_search_log/', RecommandBySearchLog.as_view()),
    path('recommand_by_follow/', RecommandByFollow.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)