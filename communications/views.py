from rest_framework.views import APIView
from rest_framework.response import Response

from communications.models import Suggestions


class SuggestionsView(APIView):
    def post(self, request):
        try:
            by = request.data['by']
            description = request.data['description']

            suggestion = Suggestions.objects.create(by = by, description= description)
            return Response({"success": "Your suggestion is droped successfully."})

        except:
            return Response({"error": "Seems like the fields are missing"})

