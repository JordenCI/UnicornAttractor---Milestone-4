from django.shortcuts import render
from .graphs import BugBarChart, FeatureBarChart, BugPieChart

def graphs(request):
    """A view that displays the graphs page"""
    return render(request, "graphs.html", {'bug_bar_chart': BugBarChart, 'feature_bar_chart': FeatureBarChart, 'bug_pie_chart': BugPieChart})