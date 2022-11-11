from ckan.lib.base import BaseController, render

class TrafficLightController(BaseController):
    def render_reference_page(self):
        return render('ckanext/traffic_light/reference_page.html')