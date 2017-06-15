from edc_visit_schedule.visit import Crf

crfs = (
    Crf(show_order=1, model='bcpp_clinic_subject.questionnaire'),
    Crf(show_order=2, model='bcpp_clinic_subject.viralloadtracking'),
    Crf(show_order=3, model='bcpp_clinic_subject.vlresult'))
