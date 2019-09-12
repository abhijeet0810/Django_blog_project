from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
    path('new/', views.PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', views.PostUpdate.as_view(), name='post-update'),
    path('<int:pk>/delete/', views.PostDelete.as_view(), name='post-delete'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    # path('search/', views.search_titles, name='search_titles'),
]

# Create view (PostCreate) template name would be differnt from  List view and Detail view 
# (PostList PostDetail)
# the reason is that, it is going to share the template with the Update view
# So the template for both views are post_form.html