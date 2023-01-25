"""Defines url pattern for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    # Page that shows all Topics.
    path('topics/', views.topics, name='topics'),
    # Detail Page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # Page for adding a new Topic
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding new Entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    # page for editing entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('sample/', views.sample, name='sample'),
]

