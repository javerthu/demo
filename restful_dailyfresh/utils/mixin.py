from django.contrib.auth.decorators import login_required #进行登录验证django自带的user才可行，在本案例中就是重写了django的user表


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        # 调用父类的as_view
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)