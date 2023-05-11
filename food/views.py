import csv
from django.shortcuts import render

from .models import food
from user_test.models import Member
from rest_framework import viewsets
from .serializers import foodSerializer
# Create your views here.
def index(request):

    return render(request, 'food/index.html')

def food_info_input(request):
    if request.method == "GET":
        return render(request, 'food/food_info_input.html')
    elif request.method == "POST":
        context = {}
        food_name = request.POST["food_name"]
        serving_size = request.POST["serving_size"]
        carbon = request.POST["carbon"]
        calories = request.POST["calories"]
        protein = request.POST["protein"]
        fat = request.POST["fat"]
        cholesterol = request.POST["cholesterol"]

        rs = food.objects.filter(food_name=food_name)
        if rs.exists():
            context['message'] = food_name + "가 중복됩니다."
            return render(request, 'food/food_info_input.html', context)

        else:
            food.objects.create(
                food_name=food_name, serving_size=serving_size, calories=calories,carbon=carbon,
                protein=protein, fat=fat, cholesterol=cholesterol)
            context['message'] = food_name + "입력완료."
            return render(request, 'food/food_info_input.html', context)
    return render(request, 'food_info_input.html')


def food_list(request):
    foods = food.objects.all().order_by('pk')

    return render(
        request,
        'food/food_list.html',
        {
            'foods': foods,
        }
    )

def food_input(request):
    if request.method == "GET":
        foods = food.objects.all().order_by('pk')
        return render(
            request,
            'food/food_input.html',
            {
            'foods': foods,
            }
        )

    elif request.method == "POST":
        context = {}

        food_name = request.POST.get('food_name')
        serving_size = request.POST.get('serving_size')

        list = request.POST.get('list')
        amount = request.POST.get('amount')
        calories = request.POST.get('calories')
        carbon = request.POST.get('carbon')
        protein = request.POST.get('protein')
        fat = request.POST.get('fat')
        cholesterol = request.POST.get('cholesterol')
        foods = food.objects.get(food_name=food_name)
        rate = int(serving_size)/int(foods.serving_size)

        if amount is '':
            context['list'] = str(food_name)+str(serving_size)+'g '
            context['amount'] = int(serving_size)
            context['calories'] = round(int(foods.calories)*rate,2)
            context['carbon'] = round(int(foods.carbon)*rate,2)
            context['protein'] = round(int(foods.protein)*rate,2)
            context['fat'] = round(int(foods.fat)*rate,2)
            context['cholesterol'] = round(int(foods.cholesterol)*rate,2)

        else:
            context['list'] = str(list)+str(food_name)+str(serving_size)+'g '
            context['amount'] = int(amount)+int(serving_size)
            context['calories'] = round(float(calories)+int(foods.calories)*rate,2)
            context['carbon'] = round(float(carbon)+int(foods.carbon)*rate,2)
            context['protein'] = round(float(protein)+int(foods.protein)*rate,2)
            context['fat'] = round(float(fat)+int(foods.fat)*rate,2)
            context['cholesterol'] = round(float(cholesterol)+int(foods.cholesterol)*rate,2)



        return render(request, 'food/food_input.html',context)
        # if rs.exists():

def feedback(request):
    if request.method == "GET":
        return render(request, 'food/feedback.html')

    elif request.method == "POST":
        context = {}

        used_calories = request.POST.get('used_calories')
        calories = request.POST.get('calories')
        id=request.POST.get('id')


        context['calories'] = calories


        context['feedback'] = ' '
        if used_calories is not None:
            members = Member.objects.get(member_id=id)

            if members.gender=='남자':
                base_calories= 66+13.7*int(members.weight)+(5*int(members.height))-(6.5*int(members.age))
                context['base_calories'] = base_calories

            else:
                base_calories=665 + 9.6 * int(members.weight) + (1.8 * int(members.height)) - (4.7 * int(members.age))
                context['base_calories'] = base_calories

            if members.purpose=='감량':
                recommend_calories=base_calories-500

            if members.purpose=='증량':
                recommend_calories=base_calories+500


            context['used_calories'] = used_calories
            if float(base_calories)+float(used_calories)>float(calories):
                less_calories=round(float(base_calories)+float(used_calories)-float(calories),2)
                potato_ea=round(less_calories/130,1)
                egg_ea = round(less_calories / 75, 1)
                chest_ea =round(less_calories / 115, 1)
                banana_ea =round(less_calories / 95, 1)
                context['feedback'] = '부족한 칼로리는'+str(less_calories) +'입니다'
                context['feedback1']=('감자'+str(potato_ea)+'개'+
                                      '삶은계란' + str(egg_ea) + '개' +
                                      '닭가슴살' + str(chest_ea) + '개' +
                                      '바나나' + str(banana_ea) + '개' +
                                      '로 영양분을 보충하세요')
            else:
                much_calories=float(calories)-float(base_calories) - float(used_calories)
                squat_m=round(much_calories/9.8)
                bike_m=round(much_calories/3.4)
                pushup_m = round(much_calories / 4.2)
                swim_m = round(much_calories / 17)
                run_m = round(much_calories / 9.4)
                context['feedback'] = '과다한 칼로리는' + str(much_calories) + 'cal입니다.'
                context['feedback1'] = ('스쿼트'+str(squat_m)+'분, '+
                                        '자전거타기'+str(bike_m)+'분, '+
                                        '팔굽혀펴기'+str(pushup_m)+'분, '+
                                        '수영'+str(swim_m)+'분, '+
                                        '조깅'+str(run_m)+'분, '+
                                        '으로칼로리를 소모할수 잇습니다.')


        return render(request, 'food/feedback.html',context)

class foodViewset(viewsets.ModelViewSet):
    queryset = food.objects.all()
    serializer_class = foodSerializer







def csvinput(request):
    if request.method == "GET":

        f = open('C:/Users/원승혁/mysite/food/전국통합식품영양성분정보(음식)표준데이터.csv', 'r',encoding='euc-kr')
        rdr = csv.reader(f)
        next(rdr)
        for line in rdr:
            for n in range(30):
                if line[n] == '':
                    line[n] = 0
            food.objects.create(

                food_name=str(line[1]), serving_size=int(100), calories=round(float(line[17])), carbon=round(float(line[19])),
                protein=round(float(line[20])), fat=round(float(line[22])), cholesterol=round(float(line[29])))

        f.close()

    return render(request, 'food/index.html')