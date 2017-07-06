from edc_map.mapper import Mapper
from edc_map.site_mappers import site_mappers


class SubjectTestPlotMapper(Mapper):

    map_area = 'subject_test_community'
    map_code = '41'
    pair = 0
    landmarks = ()
    center_lat = -24.557709
    center_lon = 25.807963
    clinic_lat = -24.645541
    clinic_lon = 25.912407
    radius = 100.5
    location_boundary = ()
    intervention = True


site_mappers.register(SubjectTestPlotMapper)
