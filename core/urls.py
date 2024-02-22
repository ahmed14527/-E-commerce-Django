from django.urls import path, include
from rest_framework import routers
from .views import (
    ItemListView,
    ItemDetailView,
    OrderItemListView,
    OrderItemDetailView,
    OrderListView,
    OrderDetailView,
    AddressListView,
    AddressDetailView,
    PaymentListView,
    PaymentDetailView,
    CouponListView,
    CouponDetailView,
    RefundListView,
    RefundDetailView,
    ItemViewSet,
    OrderItemViewSet,
    OrderViewSet,
    AddressViewSet,
    PaymentViewSet,
    CouponViewSet,
    RefundViewSet
)

router = routers.DefaultRouter()
router.register(r'items', ItemViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'coupons', CouponViewSet)
router.register(r'refunds', RefundViewSet)

urlpatterns = [
    path('items/', ItemListView.as_view(), name='item-list'),
    path('items/<int:pk>/', ItemDetailView.as_view(), name='item-detail'),
    path('order-items/', OrderItemListView.as_view(), name='order-item-list'),
    path('order-items/<int:pk>/', OrderItemDetailView.as_view(), name='order-item-detail'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('addresses/', AddressListView.as_view(), name='address-list'),
    path('addresses/<int:pk>/', AddressDetailView.as_view(), name='address-detail'),
    path('payments/', PaymentListView.as_view(), name='payment-list'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('coupons/', CouponListView.as_view(), name='coupon-list'),
    path('coupons/<int:pk>/', CouponDetailView.as_view(), name='coupon-detail'),
    path('refunds/', RefundListView.as_view(), name='refund-list'),
    path('refunds/<int:pk>/', RefundDetailView.as_view(), name='refund-detail'),
    path('api/', include(router.urls)),
]