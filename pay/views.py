import requests
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse


def index(request):
    if request.method == "POST":
        URL = 'https://kapi.kakao.com/v1/payment/ready'
        headers = {
            "Authorization": "KakaoAK" + "1d619e4e5edbca6428e10ae0609dd830",  # 변경불가
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",  # 변경불가
        }

        params = {
            "cid": "TC0ONETIME",  # 테스트용 코드
            "partner_order_id": "1001",  # 주문번호
            "partner_user_id": "german",  # 유저 아이디
            "item_name": "미라클레터 멤버쉽",  # 구매 물품 이름
            "quantity": "1",  # 구매 물품 수량
            "total_amount": "100",  # 구매 물품 가격
            "tax_free_amount": "0",  # 구매 물품 비과세
            "approval_url": "pay/approval.html",  # 결제 성공 시 이동할 url
            "cancel_url": reverse('news'),  # 결제 취소 시 이동할 url
            "fail_url": "pay/approval.html",  # 결제 실패 시 이동할 url
        }

        res = requests.post(URL, headers=headers, params=params)
        request.session['tid'] = res.json()['tid']  # 결제 승인시 사용할 tid를 세션에 저장
        next_url = res.json()['next_redirect_pc_url']  # 결제 페이지로 넘어갈 url을 저장
        return redirect(next_url)

    return render(request, 'pay/index.html')


# 승인 페이지
def complete(request):

    return render(request, 'pay/complete.html')