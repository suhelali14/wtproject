from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth

from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import Profile, Post, LikePost, FollowersCount,Usermode,Products,Recommendation,Cart,cartProduct
from itertools import chain
import random
# Create your views here.

@login_required(login_url='login')
def index(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))
    product = Products.objects.all()
    all = Products.objects.filter(price='150').values()
    # price = Products.objects.filter(price=type).values()
    product_cart=[]
    product_id=[]

    for users in product:
        product_id.append(users.id)

    for ids in product_id:
        prolist = Products.objects.filter(id=ids)
        product_cart.append(prolist)
    random.shuffle(product_cart)
    product_cart_list = list(chain(*product_cart))
    user_profile1 = Profile.objects.get(user=request.user)
    user_city=user_profile1.city
    return render(request, 'index.html', {'product': product_cart_list[:4],'user_profile': user_profile, 'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4],'user_city':user_city})


def signup(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        phone=request.POST.get('phone')
        birthdate=request.POST.get('birthdate')
        city=request.POST.get('city')
        zipcode=request.POST.get('zipcode')
        usermode=0
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                
                
                user_login = auth.authenticate(username=username, password=password1)
                auth.login(request, user_login)

                #create a Profile object for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, fullname=fullname,phone=phone,city=city,birthdate=birthdate,zipcode=zipcode,usermode=usermode)

                new_profile.save()
                
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('signup')
        
    else:
        return render(request, 'signup.html')
        
    

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'login.html')


@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

def about(request):
    return HttpResponse('Hello There')

def faq(request):
    return HttpResponse('Hello There')

def search(request):
    return HttpResponse('Hello There')





@login_required(login_url='login')
def services(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    products =Products.objects.all()

    user_following_list = []
    feed = []
    customers_list=[]
    
    user_following = FollowersCount.objects.filter(follower=request.user.username)
    customers=Usermode.objects.filter(user=request.user.username)
    
    for users in customers:
        customers_list.append(users.user)
    
    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))
   
    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []
    customers_all=[]
    
  
    for user in customers:
        user_list = Usermode.objects.filter(username=user.user)
        customers_all.append(user_list)
    
    

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)

    
    
    new_suggestions_list2 = [x for x in list(all_users) if (x not in list(customers_all))]
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    final_suggestions_list2 = [x for x in list(new_suggestions_list2) if ( x not in list(current_user))]
    
    random.shuffle(final_suggestions_list2)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list2:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))
    product = Products.objects.all()
    all = Products.objects.filter(price='150').values()
    # price = Products.objects.filter(price=type).values()
    product_cart=[]
    product_id=[]

    for users in product:
        product_id.append(users.id)

    for ids in product_id:
        prolist = Products.objects.filter(id=ids)
        product_cart.append(prolist)
    product_cart_list = list(chain(*product_cart))
    
    electronic=Cart.objects.values_list('electronic')[0]
    cloth=Cart.objects.values_list('cloth')[0]
    watches=Cart.objects.values_list('watches')[0]
    grocery=Cart.objects.values_list('grocery')[0]
    sports=Cart.objects.values_list('sports')[0]
    user_profile1 = Profile.objects.get(user=request.user)
    user_city=user_profile1.city
    
    return render(request, 'services.html', {'product': product_cart_list, 'products':products,'user_profile': user_profile, 'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4],'user_city':user_city})


@login_required(login_url='loginpr')
def profile(request, pk):
    user_object = User.objects.get(username=pk)
    user_profile = Profile.objects.get(user=user_object)
    user_posts = Post.objects.filter(user=pk)
    user_post_length = len(user_posts)

    follower = request.user.username
    user = pk

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'Unfollow'
    else:
        button_text = 'Follow'

    user_followers = len(FollowersCount.objects.filter(user=pk))
    user_following = len(FollowersCount.objects.filter(follower=pk))
    user_profile1 = Profile.objects.get(user=request.user)
    user_city=user_profile1.city
    user = User.objects.get(username=request.user.username)
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'user_posts': user_posts,
        'user_post_length': user_post_length,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
        'user_city':user_city,
        'user':user,
    }
    return render(request, 'profile.html', context)

   # return render(request, 'profile.html', {'user_profile': user_profile})

    
 

@login_required(login_url='login')
def search(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    product_cart=[]
    product_id=[]
    
    product = Products.objects.all()
    all = Products.objects.filter(price='150').values()
    # price = Products.objects.filter(price=type).values()
    product_cart=[]
    product_id=[]
    username_profile = []
    username_profile_list = []
    
    for users in product:
        product_id.append(users.id)

    for ids in product_id:
        prolist = Products.objects.filter(id=ids)
        product_cart.append(prolist)

    product_cart_list = list(chain(*product_cart))


    
    if request.method == 'POST':
        username = request.POST['username']
      
        username_object = User.objects.filter(username__icontains=username)
        category_list=[]
        product = Products.objects.all()
        all = Products.objects.filter(price='150').values()
        # price = Products.objects.filter(price=type).values()
        product_cart=[]
        product_id=[]
        username_profile = []
        username_profile_list = []

        search=Products.objects.filter(type__icontains=username)
        name_p=Products.objects.filter(name__icontains=username)
      
        user_profile1 = Profile.objects.get(user=request.user)
        city = request.POST['city']
        user_profile1.city = city
        user_profile1.save()
        for users in search:
            product_id.append(users.id)
        for users in name_p:
            product_id.append(users.id)    
                

        for ids  in product_id:
            prolist = Products.objects.filter(id=ids)
            
            product_cart.append(prolist)
        
       
        
        for users in product_id:
            cat_list = Products.objects.filter(type=users)
            category_list.append(cat_list)

        
        user_city = user_profile1.city
        final_cart=[]

        category_type_list=[]
        if username in category_type_list:
            
            category_type_list.append(username)
            
        product_cart_list = list(chain(*product_cart))
        category_type_list=list(chain(*category_list))
    return render(request, 'search.html', {'product_cart_list':product_cart_list,'user_profile': user_profile, 'category': category_type_list,'user_city':user_city})



def signuppr(request):
    if request.method=='POST':
        fullname=request.POST.get('fullname')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        phone=request.POST.get('phone')
        birthdate=request.POST.get('birthdate')
        city=request.POST.get('city')
        zipcode=request.POST.get('zipcode')
        usermode=1
        
        profileimg='https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg'
        code=request.POST.get('code')
        if code=='amigoo':
            if password1 == password2:
                if User.objects.filter(email=email).exists():
                    messages.info(request, 'Email Taken')
                    return redirect('signuppr')
                elif User.objects.filter(username=username).exists():
                    messages.info(request, 'Username Taken')
                    return redirect('signuppr')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                
                
                    user_login = auth.authenticate(username=username, password=password1)
                    auth.login(request, user_login)

                    #create a Profile object for the new user
                    user_model = User.objects.get(username=username)
                    new_profile = Profile.objects.create(user=user_model, id_user=user_model.id, fullname=fullname,phone=phone,city=city,birthdate=birthdate,zipcode=zipcode,usermode=usermode, profileimg= profileimg)
                    new_profile.save()

                    
                    return redirect('loginpr')
            else:
                messages.info(request, 'Password Not Matching')
                return redirect('signuppr')
        
    else:
        return render(request, 'signuppr.html')


def loginpr(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('provider')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')

    else:
        return render(request, 'loginpr.html')
    
@login_required(login_url='login')
def provider(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)

    user_following_list = []
    feed = []

    user_following = FollowersCount.objects.filter(follower=request.user.username)

    for users in user_following:
        user_following_list.append(users.user)

    for usernames in user_following_list:
        feed_lists = Post.objects.filter(user=usernames)
        feed.append(feed_lists)

    feed_list = list(chain(*feed))

    # user suggestion starts
    all_users = User.objects.all()
    user_following_all = []

    for user in user_following:
        user_list = User.objects.get(username=user.user)
        user_following_all.append(user_list)
    
    new_suggestions_list = [x for x in list(all_users) if (x not in list(user_following_all))]
    current_user = User.objects.filter(username=request.user.username)
    final_suggestions_list = [x for x in list(new_suggestions_list) if ( x not in list(current_user))]
    random.shuffle(final_suggestions_list)

    username_profile = []
    username_profile_list = []

    for users in final_suggestions_list:
        username_profile.append(users.id)

    for ids in username_profile:
        profile_lists = Profile.objects.filter(id_user=ids)
        username_profile_list.append(profile_lists)

    suggestions_username_profile_list = list(chain(*username_profile_list))
    user = request.user.username
    usertype=1
    new_usertype=Usermode.objects.create(user=user,usertype=usertype)
    new_usertype.save()
    
    return render(request, 'provider.html', {'user_profile': user_profile, 'posts':feed_list, 'suggestions_username_profile_list': suggestions_username_profile_list[:4]})


@login_required(login_url='login')
def upload(request):

    if request.method == 'POST':
        user = request.user.username
        product=request.POST['name']
        productimg = request.FILES.get('productimg')
        description = request.POST['caption']
        price=request.POST['price']
        name=request.POST['name']
        type=request.POST['type']
        
        location = request.POST['location']
        user_object = User.objects.get(username=request.user.username)
        user_profile = Profile.objects.get(user=user_object)
        phone=user_profile.phone
        
        new_product = Products.objects.create(user=user, productimg=productimg, description=description,price=price,type=type,name=name,location=location,phone=phone)
        new_product.save()

        return redirect('provider')
    else:
        return redirect('provider')

@login_required(login_url='login')
def upload_post(request):

    if request.method == 'POST':
        user = request.user.username
        image = request.FILES.get('image')
        caption = request.POST['caption']
        name=request.POST['name']
        new_post = Post.objects.create(user=user, image=image, caption=caption,name=name)
        new_post.save()

        return redirect('provider')
    else:
        return redirect('provider')


@login_required(login_url='login')
def follow(request):
    if request.method == 'POST':
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).first():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            return redirect('/profile/'+user)
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            new_follower.save()
            return redirect('/profile/'+user)
    else:
        return redirect('/')

@login_required(login_url='login')
def cart(request):
    user_object = User.objects.get(username=request.user.username)
    user_profile = Profile.objects.get(user=user_object)
    product_cart=[]
    product_id=[]
    
    product = Products.objects.all()
    all = Products.objects.filter(price='150').values()
    # price = Products.objects.filter(price=type).values()
    product_cart=[]
    product_id=[]
    username_profile = []
    username_profile_list = []

    for users in product:
        product_id.append(users.id)

    for ids in product_id:
        prolist = Products.objects.filter(id=ids)
        product_cart.append(prolist)

    product_cart_list = list(chain(*product_cart))


    
    if request.method == 'POST':
        username = request.POST['product_id']
       
        # product_name=request.POST['product_id']
        # new_add=Cart.objects.create(product_id=product_name)
        # new_add.save()
        username_object = User.objects.filter(username__icontains=username)
        category_list=[]
        product = Products.objects.all()
        all = Products.objects.filter(price='150').values()
        # price = Products.objects.filter(price=type).values()
        product_cart=[]
        product_id=[]
        username_profile = []
        username_profile_list = []

        search=Products.objects.filter(id__icontains=username)
        name_p=Products.objects.filter(type__icontains=username)

        name_p=Cart.objects.filter()
        for users in search:
            product_id.append(users.id)
        for users in name_p:
            product_id.append(users.id)    
                

        for ids in product_id:
            prolist = Products.objects.filter(id=ids)
            
            product_cart.append(prolist)
        
        product_cart_list = list(chain(*product_cart))
        
        for users in product_id:
            cat_list = Products.objects.filter(type=users)
            category_list.append(cat_list)
        

        category_type_list=list(chain(*category_list))
        if username in category_type_list:
            category_type_list=[]
            category_type_list.append(username)

        user = request.user.username
        user_cart=Cart.objects.filter(user=user).exists()

       
        electronic=Cart.objects.values_list('electronic')[0]
        cloth=Cart.objects.values_list('cloth')[0]
        watches=Cart.objects.values_list('watches')[0]
        grocery=Cart.objects.values_list('grocery')[0]
        sports=Cart.objects.values_list('sports')[0]
        electronic_=Cart.objects.all().values()
        for electronic in electronic:
            ele=electronic
        for cloth in cloth:
            clo=cloth
        for watches in watches:
            wat=watches
        for grocery in grocery:
            gro=grocery
        for sports in sports:
            spo=sports                
        

        if Cart.objects.filter(user=user).exists():
            if ele==0 or clo==0 or wat==0 or gro==0 or spo==0:

                for users in name_p:
                    ele=Products.objects.filter(id=username).values_list('type')[0]
                    if 'electronic' in ele:
                        electronic=electronic+1
                        Cart.objects.update(electronic=electronic)
                    if 'cloth' in ele:
                        cloth=cloth+1
                        Cart.objects.update(cloth=cloth)
                    if 'watches' in ele:
                        watches=watches+1
                        Cart.objects.update(watches=watches)
                    if 'grocery' in ele:
                        grocery=grocery+1
                        Cart.objects.update(grocery=grocery)
                    if 'sports' in ele:
                        sports=sports+1
                        Cart.objects.update(sports=sports)
            id_name=Products.objects.filter(id=username).values_list('user')[0]
            user_name=Products.objects.filter(id=username).values_list('id')[0]
            for id in id_name:
                id_name_in=id
            for id in user_name:
                user_name_in=id    
            add=cartProduct.objects.create(product_id=user_name_in,user=id_name_in)
            add.save()
        else:
            new_add=Cart.objects.create(user=user,electronic=0,cloth=0,watches=0,grocery=0,sports=0)
            new_add.save()
        
              
        cart_items=[]
        cart_item=cartProduct.objects.filter(user=username).values()
        for i in cart_item:
            cart_items.append(i)

        product_cart_list_cart = list(chain(*cart_items))
            
          
        
            
        
        # new_cart = Cart.objects.create()
        # new_cart.save()    
    return render(request, 'cart.html', {'cart_items':product_cart_list_cart,'elctronic':electronic,'product_cart_list':product_cart_list,'user_profile': user_profile, 'category': category_type_list},)

