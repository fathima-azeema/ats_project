from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q, Count
import json
from .models import Applicant
from .forms import ApplicantForm


class ApplicantListView(ListView):
    """
    List view for applicants with search and filter functionality.
    Includes dashboard statistics and chart data.
    """
    model = Applicant
    template_name = 'applicants/applicant_list.html'
    context_object_name = 'applicants'
    paginate_by = 10

    def get_queryset(self):
        """
        Override to handle search and status filtering.
        Search by name or position, filter by status.
        """
        queryset = super().get_queryset()
        
        # Get search query parameter
        search_query = self.request.GET.get('search', '').strip()
        
        # Get status filter parameter
        status_filter = self.request.GET.get('status', '').strip()
        
        # Apply search filter (search by name or position)
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | 
                Q(position__icontains=search_query)
            )
        
        # Apply status filter
        if status_filter:
            queryset = queryset.filter(status=status_filter)
        
        return queryset

    def get_context_data(self, **kwargs):
        """
        Add dashboard statistics and chart data to context.
        """
        context = super().get_context_data(**kwargs)
        
        # Get current search and filter values for template
        context['current_search'] = self.request.GET.get('search', '')
        context['current_status'] = self.request.GET.get('status', '')
        
        # Dashboard statistics (always show total counts)
        context['total_applicants'] = Applicant.objects.count()
        context['new_count'] = Applicant.objects.filter(status='New').count()
        context['shortlisted_count'] = Applicant.objects.filter(status='Shortlisted').count()
        context['rejected_count'] = Applicant.objects.filter(status='Rejected').count()
        context['hired_count'] = Applicant.objects.filter(status='Hired').count()
        
        # Chart data - Status counts for pie chart
        status_labels = ['New', 'Shortlisted', 'Rejected', 'Hired']
        status_counts = [
            context['new_count'],
            context['shortlisted_count'],
            context['rejected_count'],
            context['hired_count']
        ]
        # Bootstrap color scheme for status
        status_colors = ['#6c757d', '#0dcaf0', '#dc3545', '#198754']
        
        # Convert to JSON for JavaScript consumption
        context['status_labels_json'] = json.dumps(status_labels)
        context['status_counts_json'] = json.dumps(status_counts)
        context['status_colors_json'] = json.dumps(status_colors)
        
        # Chart data - Position counts for bar chart (top 10)
        position_counts = Applicant.objects.values('position').annotate(
            count=Count('id')
        ).order_by('-count')[:10]
        
        position_labels = [item['position'] for item in position_counts]
        position_counts_list = [item['count'] for item in position_counts]
        
        # Convert to JSON for JavaScript consumption
        context['position_labels_json'] = json.dumps(position_labels)
        context['position_counts_json'] = json.dumps(position_counts_list)
        
        return context


class ApplicantCreateView(SuccessMessageMixin, CreateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'applicants/applicant_form.html'
    success_url = reverse_lazy('applicant-list')
    success_message = "Applicant '%(name)s' was created successfully."


class ApplicantUpdateView(SuccessMessageMixin, UpdateView):
    model = Applicant
    form_class = ApplicantForm
    template_name = 'applicants/applicant_form.html'
    success_url = reverse_lazy('applicant-list')
    success_message = "Applicant '%(name)s' was updated successfully."


class ApplicantDeleteView(SuccessMessageMixin, DeleteView):
    model = Applicant
    template_name = 'applicants/applicant_confirm_delete.html'
    success_url = reverse_lazy('applicant-list')
    success_message = "Applicant was deleted successfully."
