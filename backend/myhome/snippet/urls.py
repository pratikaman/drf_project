from django.urls import path
from snippet.views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", api_root),
    path('snippets/<int:pk>/highlight/', SnippetHighlight.as_view(), name='snippet-highlight'),

    path('v1/snippets/', snippet_list, name='snippet-list-1'),
    path('v1/snippets/<int:pk>/', snippet_detail, name='snippet-detail-1'),

    path('v2/snippets/', snippet_list2, name='snippet-list-2'),
    path('v2/snippets/<int:pk>/', snippet_detail2, name='snippet-detail-2'),

    path('v3/snippets/', SnippetList.as_view(), name='snippet-list-3'),
    path('v3/snippets/<int:pk>', SnippetDetail.as_view(), name='snippet-detail-3'),

    path('v4/snippets/', SnippetListV2.as_view(), name='snippet-list-4'),
    path('v4/snippets/<int:pk>', SnippetDetailV2.as_view(), name='snippet-detail-4'),

    path('v5/snippets/', SnippetListV3.as_view(), name='snippet-list-5'),
    path('v5/snippets/<int:pk>', SnippetDetailV3.as_view(), name='snippet-detail-5'),

    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),

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