from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from news.models import News
from news.serializers import NewsSerializer
from user.models import User

class NewsView(APIView):
    def get(self, request):
        news = News.objects.filter(is_verified = True)
        news_data = []

        for each_news in news:
            serialized_data = NewsSerializer(each_news).data
            news_data.append(serialized_data)

        return Response({"news": news_data})
    
    # def post(self,request):
    #     user = request.data['author']
    #     news_heading = request.data['news_heading']
    #     news_description = request.data['news_description']
    #     news_image = request.FILES['news_image']

    #     author = User.objects.filter(id = user)

    #     news = News.objects.create( author = author, news_description = news_description, news_heading= news_heading, news_image= news_image)
    #     news.save()
    #     return Response({"success": "Successfully posted news"})


    def post(self, request):
        try:
            user_id = request.data['author']
            news_heading = request.data['news_heading']
            news_description = request.data['news_description']
            news_image = request.FILES['news_image']

            # Use get to directly retrieve the user, assuming the ID exists
            author = User.objects.get(id=user_id)

            # Alternatively, handle User.DoesNotExist exception if needed
            # author = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({"error": "User does not exist"}, status=400)
        except KeyError as e:
            return Response({"error": f"Missing required field: {str(e)}"}, status=400)

        # Create the News instance without using a serializer
        news = News.objects.create(
            author=author,
            news_heading=news_heading,
            news_description=news_description,
            news_image=news_image
        )

        return Response({"success": "Successfully posted news"})