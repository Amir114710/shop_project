from django.shortcuts import redirect



class LoginRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated == True:
            return redirect('home_app:home')
        return super(LoginRequirdMixins ,  self ).dispatch(request , *args , **kwargs)
class LogoutRequirdMixins:
    def dispatch(self , request , *args , **kwargs):
        if request.user.is_authenticated == False:
            return redirect('home_app:home')
        return super(LogoutRequirdMixins ,  self ).dispatch(request , *args , **kwargs)