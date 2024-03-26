from rest_framework.response import Response
from rest_framework.views import APIView
from news.models import News
from reports.models import Report

from user.models import User


class ReportView(APIView):
    def post(self, request):
        user = request.user
        if user.is_authenticated:
            try:
                reason = request.data['reason']
                report_type = request.data['type']
                report_id = request.data['id']
                print(reason, report_id, report_type)


                if report_type == "user":
                    reported_user_obj = User.objects.get(id = report_id)
                    report = Report.objects.create( by= user, reason= reason, user= reported_user_obj)
                    

                elif report_type == "news":
                    print("in news")
                    reported_post_obj = News.objects.get(id = report_id)
                    report = Report.objects.create( by= user, reason= reason, post= reported_post_obj)

            
                return Response({"success": "Report placed successfully"})
            except:
                return Response({"error": "There was an error in the process"})
