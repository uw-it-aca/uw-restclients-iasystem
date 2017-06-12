from restclients_core import models


class Evaluation(models.Model):
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

    def __str__(self):
        return "{%s: %d, %s: %s, %s: %s, %s: %s, %s: %s, %s: %s, %s: %s, %s: %0.6f}" % (
            "sln", self.section_sln,
            "eval_open_date", self.eval_open_date,
            "eval_close_date", self.eval_close_date,
            "eval_url", self.eval_url,
            "is_completed", self.is_completed,
            "report_url", self.eval_url,
            "report_available_date", self.report_available_date,
            "response_rate", self.response_rate)

    def is_online(self):
        return (self.delivery_method == "Online")

    def is_open(self):
        return (self.eval_status != "Closed")

    def json_data(self):
        return {
            "section_sln": self.section_sln,
            "eval_open_date": str(self.eval_open_date),
            "eval_close_date": str(self.eval_close_date),
            "eval_status": self.eval_status,
            "eval_url": self.eval_url,
            "report_url": self.report_url,
            "report_available_date": str(self.report_available_date),
            "response_rate": self.response_rate,
            "delivery_method": self.delivery_method,
            "is_completed": self.is_completed,
            "is_open": self.is_open(),
            "is_online": self.is_online()
        }
