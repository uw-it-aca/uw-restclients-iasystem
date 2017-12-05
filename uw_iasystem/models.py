from restclients_core import models


class Evaluation(models.Model):
    DOMAIN_SEA = 'uw'
    DOMAIN_BOT = 'uwb'
    DOMAIN_TAC = 'uwt'
    DOMAIN_EO_AP = 'uweo-ap'
    DOMAIN_EO_IELP = 'uweo-ielp'

    domain = models.CharField(max_length=16)
    section_sln = models.IntegerField()
    eval_open_date = models.DateTimeField()
    eval_close_date = models.DateTimeField()
    is_completed = models.NullBooleanField()
    eval_status = models.CharField(max_length=7)
    eval_url = models.URLField()
    report_url = models.URLField()
    report_available_date = models.DateTimeField()
    response_rate = models.FloatField()
    delivery_method = models.CharField(max_length=32)

    def __init__(self, *args, **kwargs):
        super(Evaluation, self).__init__(*args, **kwargs)
        self.instructor_ids = []

    def is_online(self):
        return (self.delivery_method == "Online")

    def is_open(self):
        return (self.eval_status != "Closed")

    def is_seattle(self):
        return self.domain == Evaluation.DOMAIN_SEA

    def is_bothell(self):
        return self.domain == Evaluation.DOMAIN_BOT

    def is_tacoma(self):
        return self.domain == Evaluation.DOMAIN_TAC

    def is_eo_ap(self):
        return self.domain == Evaluation.DOMAIN_EO_AP

    def is_eo_ielp(self):
        return self.domain == Evaluation.DOMAIN_EO_IELP

    def json_data(self):
        return {
            "domain": self.domain,
            "section_sln": self.section_sln,
            "eval_open_date": (str(self.eval_open_date)
                               if self.eval_open_date else None),
            "eval_close_date": (str(self.eval_close_date)
                                if self.eval_close_date else None),
            "eval_status": self.eval_status,
            "eval_url": self.eval_url,
            "report_url": self.report_url,
            "report_available_date": (str(self.report_available_date)
                                      if self.report_available_date else None),
            "response_rate": self.response_rate,
            "delivery_method": self.delivery_method,
            "is_completed": self.is_completed,
            "is_open": self.is_open(),
            "is_online": self.is_online()
        }

    def __str__(self):
        return str(self.json_data())
