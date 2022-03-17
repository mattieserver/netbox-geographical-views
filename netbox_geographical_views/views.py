from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from django.views.generic import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.conf import settings
from django.http import QueryDict
from django.http import HttpResponseRedirect

from .forms import DeviceFilterForm
from .filters import DeviceFilterSet

import json

from dcim.models import Device, Cable, DeviceRole, DeviceType
from extras.models import Tag


class GeographicalHomeView(PermissionRequiredMixin, View):
    permission_required = ('dcim.view_site', 'dcim.view_device')

    """
    Show the home page
    """
    def get(self, request):
        self.queryset = Device.objects.all()

        return render(request, 'netbox_geographical_views/index.html' , {
            
            }
        )
