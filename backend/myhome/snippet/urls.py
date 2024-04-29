from django.urls import path
from snippet.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('v1/snippets/', snippet_list),
    path('v1/snippets/<int:pk>/', snippet_detail),

    path('v2/snippets/', snippet_list2),
    path('v2/snippets/<int:pk>/', snippet_detail2),

    path('v3/snippets/', SnippetList.as_view()),
    path('v3/snippets/<int:pk>', SnippetDetail.as_view()),

    path('v4/snippets/', SnippetListV2.as_view()),
    path('v4/snippets/<int:pk>', SnippetDetailV2.as_view()),

    path('v5/snippets/', SnippetListV3.as_view()),
    path('v5/snippets/<int:pk>', SnippetDetailV3.as_view()),

]


# using format_suffix_patterns to add suffix patterns to the URLs

# We can control the format of the response that we get back, either by using the Accept header:
# Accept:application/json
# Accept:text/html 

# http://127.0.0.1:8000/snp/v2/snippets/ # Request JSON
# http://127.0.0.1:8000/snp/v2/snippets/ # Request HTML

# or by appending a format suffix to the URL:
# http://127.0.0.1:8000/snp/v2/snippets.json # Request JSON
# http://127.0.0.1:8000/snp/v2/snippets.api # Request HTML


urlpatterns = format_suffix_patterns(urlpatterns)