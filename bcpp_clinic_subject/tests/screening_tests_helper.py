from edc_constants.constants import YES, POS, NOT_APPLICABLE, FEMALE

from ..constants import ABLE_TO_PARTICIPATE
from ..models.subject_eligibility import SubjectEligibility
from edc_base.utils import get_utcnow


class ScreeningTestHelper:

    def make_eligibility(self, options=None):
        """Returns subject eligibilty.
        """
        if options:
            options = options
        else:
            options = dict(
                report_datetime=get_utcnow(),
                age_in_years=27,
                part_time_resident=YES,
                first_name='TEST',
                initials='TT',
                gender=FEMALE,
                has_identity=YES,
                hiv_status=POS,
                inability_to_participate=ABLE_TO_PARTICIPATE,
                citizen=YES,
                literacy=YES,
                guardian=NOT_APPLICABLE)
        return SubjectEligibility.objects.create(**options)
