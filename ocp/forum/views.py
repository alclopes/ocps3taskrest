import json
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (TemplateView, View, ListView, DetailView)
from django.contrib import messages
from django.http import HttpResponse
from .models import Thread, Reply
from .forms import ReplyForm
from django.utils.translation import ugettext as _


class ForumFilter(ListView):
    #Configurando a quantidade de páginas por tela (pagination)
    paginate_by = 5
    template_name = 'forum/index.html'

    #Como definimos querysets não foi necessario definir o model desta classe,
    def get_queryset(self):
        queryset = Thread.objects.all()
        #/Importante: Quando usamos self.request.GET.get('order', '')
        # com GET.Get nos passamos no parametro um string vazio,
        # que será o default para o get se não retornar nada da consulta.
        # o que não ocorre se fizemos apenas: order = self.request.GET('order')
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'created':
            queryset = queryset.order_by('-created')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')
        #/Importante: Como esta view é acessada por duas URLs diferentes
        # a view deve identificar qual URL a acessou para tomar a acão respectiva
        # no caso uma URL encaminha parametros nomeados(Kwargs) e a outra não (Args)
        # abaixo verificamos se a Kwargs tem o nome "tag" se existir é porque foi a
        # URL refente a ordenação de tags.
        tag = self.kwargs.get('tag', '')
        if tag:
            # __icontains é um field-lookups da queryset para indicar maior ou igual a hoje
            # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups
            queryset = queryset.filter(tags__slug__icontains=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ForumFilter, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context


class ThreadView(DetailView):
    model = Thread
    template_name = 'forum/thread.html'

    # Incrementando no get do topico a contagem de visualizações
    # Esta eh uma forma simples mas permite que o incremento de mais de
    # uma vez pelo mesmo usuario, se for controlado pela sessão é mais confiável.
    def get(self, request, *args, **kwargs):
        response = super(ThreadView, self).get(request, *args, **kwargs)
        if self.request.user.is_authenticated: # //Important
            if self.object.author != self.request.user:
                self.object.views = self.object.views + 1
                self.object.save()
        return response

    # O detail já tem um get mais nos vamos oclocar mais informação nele
    def get_context_data(self, **kwargs):
        context = super(ThreadView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        context['form'] = ReplyForm(self.request.POST or None)
        return context

    # O detail não implementa post, mas precisamos incluir para encaminhar a resposta para
    # este topico.
    def post(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:  # //Important
            messages.error(self.request, _('To reply to the topic you must be logged in'))
            # Redirecionando a pagina para a URL atual, passando pelo get
            # não é necessario nenhum outro parametro pois todos estão no request atual.
            return redirect(self.request.path)
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        form = context['form']
        if form.is_valid():
            # vamos colocar commit=False pois ainda temos que preencher
            # outros valores do objeto reply antes de salvar.
            reply = form.save(commit=False)
            reply.thread = self.object
            reply.author = self.request.user
            reply.save()
            messages.success(
                self.request, _('Your answer was sended with success')
            )
            # Carregando o formulário em branco
            context['form'] = ReplyForm()
        # Redirecionando para a página atual enviando apenas o contexto
        # pois a pagina já possui o self.request e o seu próprio template
        return self.render_to_response(context)


# Set answer correct
class ReplyCorrectView(View):
    correct = True

    def get(self, request, pk):
        reply = get_object_or_404(Reply, pk=pk, thread__author=request.user)
        reply.correct = self.correct
        reply.save()
        message = _('Answer updated with success')
        if request.is_ajax():
            data = {'success': True, 'message': message}
            return HttpResponse(json.dumps(data), mimetype='application/json')
        else:
            messages.success(request, message)
            return redirect(reply.thread.get_absolute_url())


index = ForumFilter.as_view()
thread = ThreadView.as_view()
reply_correct = ReplyCorrectView.as_view()
reply_incorrect = ReplyCorrectView.as_view(correct=False)
