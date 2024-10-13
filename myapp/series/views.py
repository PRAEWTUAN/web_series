from django.shortcuts import render, redirect, get_object_or_404
from accounts.models import Series, Comment, Rating, WatchList
from accounts.forms import SeriesForm, CommentForm, RatingForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    series_list = Series.objects.all()  # Get all series
    return render(request, 'index.html', {'series_list': series_list})

def series_detail(request, id):
    series = get_object_or_404(Series, id=id)  # Get series by ID

    # Prepare forms
    comment_form = CommentForm()
    rating_form = RatingForm()

    # Get comments for this series
    comments = series.comments.all()  

    return render(request, 'series_detail.html', {
        'series': series,
        'comment_form': comment_form,
        'rating_form': rating_form,
        'comments': comments,
    })

def series_list(request, country=None):
    if country:
        series = Series.objects.filter(country__iexact=country)  # ใช้ __iexact เพื่อไม่ให้คำนึงถึงตัวพิมพ์ใหญ่หรือตัวพิมพ์เล็ก
    else:
        series = Series.objects.all()
    
    return render(request, 'series_list.html', {'series': series})

def recommended_series(request):
    # Get the top 10 series by average rating
    series_list = Series.objects.order_by('-average_rating')[:10]
    return render(request, 'recommended_series.html', {'series_list': series_list})

@login_required
def comments_view(request, series_id):
    series = get_object_or_404(Series, id=series_id)
    comments = series.comments.all()

    comment_form = CommentForm()  # สร้างฟอร์มให้พร้อม
    rating_form = RatingForm()  # สร้างฟอร์มให้พร้อม

    if request.method == "POST":
        comment_form = CommentForm(request.POST)  # สร้างฟอร์มจากข้อมูลที่ส่งเข้ามา
        rating_form = RatingForm(request.POST)  # สร้างฟอร์มจากข้อมูลที่ส่งเข้ามา

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.series = series
            comment.save()
            messages.success(request, 'ความคิดเห็นถูกส่งเรียบร้อยแล้ว!')
        
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.series = series
            rating.save()
            update_average_rating(series)  # อัปเดตคะแนนเฉลี่ย
            messages.success(request, 'คะแนนถูกส่งเรียบร้อยแล้ว!')

        return redirect('comments', series_id=series.id)

    return render(request, 'comments.html', {
        'series': series,
        'comments': comments,
        'comment_form': comment_form,
        'rating_form': rating_form,
    })

@login_required
def add_series(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        country = request.POST['country']
        cover_image = request.FILES.get('cover_image')

        series = Series.objects.create(
            title=title,
            description=description,
            country=country,
            cover_image_url=cover_image  # ตรวจสอบว่าฟิลด์นี้ใช้ URLField หรือไม่
        )
        messages.success(request, 'เพิ่มซีรีส์สำเร็จ')
        return redirect('home')
    
    return render(request, 'add_series.html')  # Add series page

@login_required
def edit_series(request, series_id):
    series = get_object_or_404(Series, id=series_id)  # ค้นหาซีรีส์จาก ID
    if request.method == 'POST':
        form = SeriesForm(request.POST, instance=series)  # ใช้ฟอร์มเดิมในการอัปเดต
        if form.is_valid():
            form.save()
            messages.success(request, 'แก้ไขซีรีส์สำเร็จ')
            return redirect('home')
    else:
        form = SeriesForm(instance=series)  # โหลดข้อมูลเก่าเข้าสู่ฟอร์ม

    return render(request, 'edit_series.html', {'form': form})  # แสดงฟอร์มแก้ไขซีรีส์

@login_required
def delete_series(request, series_id):
    series = get_object_or_404(Series, id=series_id)  # ค้นหาซีรีส์จาก ID
    if request.method == 'POST':
        series.delete()  # ลบซีรีส์
        messages.success(request, 'ลบซีรีส์สำเร็จ')
        return redirect('home')

    return render(request, 'confirm_delete.html', {'series': series})  # หน้าคอนเฟิร์มการลบซีรีส์

def update_average_rating(series):
    ratings = series.ratings.all()
    if ratings:
        average_rating = sum(rating.score for rating in ratings) / ratings.count()
        series.average_rating = average_rating
        series.save()

@login_required
def add_to_watchlist(request, series_id):
    series = Series.objects.get(id=series_id)
    watchlist, created = WatchList.objects.get_or_create(user=request.user)
    watchlist.series.add(series)
    return redirect('series_detail', id=series.id)  # เปลี่ยนจาก 'series_id' เป็น 'id'

@login_required
def remove_from_watchlist(request, series_id):
    watchlist = WatchList.objects.get(user=request.user)
    series = get_object_or_404(Series, id=series_id)
    watchlist.series.remove(series)
    return redirect('series_detail', id=series.id)  # เปลี่ยน 'series_id' เป็น 'id'

@login_required
def view_watchlist(request):
    watchlist, created = WatchList.objects.get_or_create(user=request.user)  # แก้ไขเป็น get_or_create
    return render(request, 'series/watchlist.html', {'watchlist': watchlist})
