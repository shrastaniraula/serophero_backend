from rest_framework.response import Response
from rest_framework.views import APIView
from news.models import News
from reports.models import Report

from user.models import User


class ReportView(APIView):
    def post(self, request):
        try:
            reason = request.data['reason']
            by = request.data['by']
            report_type = request.data['type']

            reported_by = User.objects.get(id = by)

            if report_type == "user":
                report_user = request.data['user']
                reported_user_obj = User.objects.get(id = report_user)
                report = Report.objects.create( by= reported_by, reason= reason, user= reported_user_obj)
                

            elif report_type == "news":
                report_post = request.data['post']
                reported_post_obj = News.objects.get(id = report_post)
                report = Report.objects.create( by= reported_by, reason= reason, post= reported_post_obj)

        
            return Response({"success": "Report placed successfully"})
        except:
            return Response({"error": "There was an error in the process"})
