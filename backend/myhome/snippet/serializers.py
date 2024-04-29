from rest_framework import serializers
from snippet.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')


    def create(self, validated_data):
        """
        Create and return a new 'Snippet' instance, given the validated data.
        """
        return Snippet.objects.create(**validated_data)
    
    def update(self, instance, validated_data):

        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.title)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()

        return instance
    

# Run in shell for test

# from snippet.models import Snippet
# from snippet.serializers import SnippetSerializer
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# import io

# snippet = Snippet(code='foo = "bar"\n')
# snippet.save()

# snippet = Snippet(code='print("hello, world")\n')
# snippet.save()

# serializer = SnippetSerializer(snippet)
# serializer.data

# content = JSONRenderer().render(serializer.data)
# content

# stream = io.BytesIO(content)
# data = JSONParser().parse(stream)


# serializer = SnippetSerializer(data=data)
# serializer.is_valid()
# 
# serializer.validated_data
# 
# serializer.save()



# we can create the same serializer class using ModelSerializer class

# this is same as SnippetSerializer. this automatically create fields based on the model fields and the methods 'create' and 'update'
class SnippetSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = "__all__"


