# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests
import time
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from show_newwords.models import NewWords, New_List, Stop_List, Coverate, RunTime, runInfo


# Create your views here.

def index(request):
    runtime = RunTime.objects.latest('id')
    info = runInfo.objects.first()
    print info.info
    return render(request, 'home.html',{'time':runtime.time,"info":info.info})

def show_new_words(request,num):
    print "woshi" + num
    new_words_list = NewWords.objects.all()
    page_con = "抱歉，数据为空，可能与上次程序运行一场有关，点击上方Run运行新的结果"
    return render(request, 'home.html', {"new_words_list":new_words_list,"page_con": page_con})

@csrf_protect
@csrf_exempt
def show_user_defined_num(request):
    if request.method == 'POST':
        user_defined_num = request.POST.get('num')
        runInfo.objects.filter(id = 1).update(info="程序正在运行中....")
        print user_defined_num
        try:
            import sys
            basepath = "C:/Users/huxw/Desktop/dictfound/dictfound.git"
            sys.path.append(str(basepath))
            path = "C:/Users/huxw/Desktop/dictfound/dictfound.git/solution_newdict_main.py"
            execfile(str(path))
            print "success"
            runInfo.objects.filter(id = 1).update(info="点击上方获取结果按钮查看最新结果")
            return HttpResponse("运行成功!")
        except:
            return HttpResponse("程序异常!")
    else:
        return render_to_response('home.html')




@csrf_protect
@csrf_exempt
def add_new(request):
    if request.method == 'POST':
        word_id = request.POST.get('word_id')
        wordObj = NewWords.objects.filter(id=word_id)
        wordObj.update(add_msg="已添加至新词库")
        nl = wordObj.first()
        word = nl.new_word
        counts = nl.counts
        type = nl.types
        # 添加到新词库
        New_List.objects.get_or_create(new_word=word,counts=counts,types=type)
        # 将该词从停用词库删除
        Stop_List.objects.filter(stop_word=word).delete()
        return HttpResponse('已添加至新词库')
    else:
        print "无效点击"

@csrf_protect
@csrf_exempt
def add_stop(request):
    if request.method == 'POST':
        word_id = request.POST.get('word_id')
        wordObj = NewWords.objects.filter(id=word_id)
        wordObj.update(add_msg="已添加至停用词库")
        nl = wordObj.first()
        word = nl.new_word
        # 添加到停用词库
        Stop_List.objects.get_or_create(stop_word=word)
        # 将该词从新词库删除
        New_List.objects.filter(new_word=word).delete()
        return HttpResponse('已添加至停用词库')
    else:
        print "无效点击"

@csrf_protect
@csrf_exempt
def go_new(request):
    new_words_list = New_List.objects.all()
    return render(request, 'new_word_lab.html', {"new_words_list": new_words_list})

@csrf_protect
@csrf_exempt
def go_stop(request):
    page_dic = {'page_content': None, 'page_count': None}
    if request.method == 'POST':
        page_num = request.POST.get('page', None)
        data_count = request.POST.get('count', None)
        print(page_num, data_count)
        page_end = int(page_num) * int(data_count)
        page_start = page_end - int(data_count)
        query_obj = Stop_List.objects.all()[page_start:page_end]
        print(query_obj)
        page_count = Stop_List.objects.count()
        print(page_count)
        page_cont_str = ''
        for i in query_obj:
            page_cont_str += '''
                <tr>
                
                <td>%d</td>
                <td>%s</td>
                <td><p class="text-success" id="msg_%d"+ >%s</p></td> 
                <td>
                    <button type="button" class="btn btn-primary btn-xs" onclick="delete_word(%d,'stop')">移出停用词库</button>
                </td>
                <td>
                    <button type="button" class="btn btn-danger btn-xs" onclick="stop_to_new(%d)">移至新词库</button>
                </td>
                
                </tr>
                ''' % (i.id, i.stop_word,i.id,i.add_msg,i.id,i.id)
        page_dic['page_content'] = page_cont_str
        page_dic['page_count'] = page_count
        return HttpResponse(json.dumps(page_dic))
    elif request.method == 'GET':
        page_count = Stop_List.objects.count()
        x, y = divmod(page_count, 12)
        if y:
            page_num = x + 1
        else:
            page_num = x
        return render(request, 'stop_word_lab.html', {'pagecount': page_num})  # 传递数据一共分多少页。

    # stop_words_list = Stop_List.objects.all()
    # return render(request, 'stop_word_lab.html', {"stop_words_list": stop_words_list})

@csrf_protect
@csrf_exempt
def delete_word(request):
    if request.method == 'POST':
        word_id = request.POST.get('word_id')
        type = request.POST.get('type')
        print type
        if type == "new":
            # 将该词从新词库删除
            New_List.objects.filter(id=word_id).delete()
            return HttpResponse('已将该词移除新词库')
        else:
            # 将该词从停用词库删除
            Stop_List.objects.filter(id=word_id).delete()
            return HttpResponse('已将该词移除停用词库')
    else:
        print "无效点击"

@csrf_protect
@csrf_exempt
def new_to_stop(request):
    if request.method == 'POST':
        word_id = request.POST.get('word_id')
        newObj = New_List.objects.filter(id=word_id)
        newObj.update(add_msg="已添加至停用词库")
        nl = newObj.first()
        word = nl.new_word
        # 从新词库删除
        New_List.objects.filter(new_word=word).delete()
        # 加入停用词库
        Stop_List.objects.get_or_create(stop_word=word)
        return HttpResponse('已添加至停用词库')

@csrf_protect
@csrf_exempt
def stop_to_new(request):
    if request.method == 'POST':
        word_id = request.POST.get('word_id')
        stopObj = Stop_List.objects.filter(id=word_id)
        stopObj.update(add_msg="已添加至新词库")
        nl = stopObj.first()
        word = nl.stop_word
        # 从停用词库删除
        Stop_List.objects.filter(stop_word=word).delete()
        # 加入新词库
        New_List.objects.get_or_create(new_word=word, counts=0)
        return HttpResponse('已添加至新词库')

def cover(word):
    url_ver = "http://dict.youdao.com/jsonapi?le=eng&q="+word
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36'}
    response = requests.get(url_ver, headers=headers, allow_redirects=False, timeout=5)
    res = response.text
    res = json.loads(res)
    return res

@csrf_protect
@csrf_exempt
def getCoverResult(request):
    if request.method == 'POST':
        newwords = New_List.objects.all()
        count = 0
        for newword in newwords:
            res = cover(newword.new_word)
            if "ce" in res:
                count += 1

        res = float(count) / float(newwords.__len__())
        t = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        Coverate.objects.create(
            time = t,
            coverate = res * 100
        )
        return HttpResponse("计算成功")
    else:
        print "无效点击"


@csrf_protect
@csrf_exempt
def getCoverAllResult(request):
    if request.method == 'POST':
        time = Coverate.objects.values("time")
        coverates = Coverate.objects.values("coverate")
        time_arry = []
        cover_array = []
        for i in time:
            time_arry.append(i['time'])
        for i in coverates:
            cover_array.append(i['coverate'])

        table_dic = {'time': None, 'coverate': None}
        table_dic['time'] = time_arry
        table_dic['coverate'] = cover_array

        # ajax_coverates = serializers.serialize("json", coverates)
        return HttpResponse(json.dumps(table_dic)) #返回json
    else:
        print "无效点击"