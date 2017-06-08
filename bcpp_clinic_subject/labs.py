from edc_lab import AliquotType, LabProfile, ProcessingProfile, RequisitionPanel
from edc_lab.site_labs import site_labs

from .constants import RESEARCH_BLOOD_DRAW, VIRAL_LOAD


lab_profile = LabProfile('bcpp_clinic_subject')

pl = AliquotType('Plasma', 'PL', '36')
lab_profile.add_aliquot_type(pl)

bc = AliquotType('Buffy Coat', 'BC', '12')
lab_profile.add_aliquot_type(bc)

wb = AliquotType('Whole Blood', 'WB', '02')
wb.add_derivative(bc)
wb.add_derivative(pl)
lab_profile.add_aliquot_type(wb)

viral_load_panel = RequisitionPanel(VIRAL_LOAD, wb, abbreviation='VL')
viral_load_processing = ProcessingProfile('viral_load', wb)
viral_load_processing.add_process(pl, 3)
viral_load_processing.add_process(bc, 2)
viral_load_panel.processing_profile = viral_load_processing
lab_profile.add_processing_profile(viral_load_processing)
lab_profile.add_panel(viral_load_panel)

rdb_panel = RequisitionPanel(RESEARCH_BLOOD_DRAW, wb, abbreviation='RBD')
rdb_processing_profile = ProcessingProfile('rbd', wb)
rdb_processing_profile.add_process(pl, 4)
rdb_processing_profile.add_process(bc, 2)
rdb_panel.processing_profile = rdb_processing_profile
lab_profile.add_processing_profile(rdb_processing_profile)
lab_profile.add_panel(rdb_panel)

site_labs.register('bcpp_clinic_subject.subjectrequisition', lab_profile)
