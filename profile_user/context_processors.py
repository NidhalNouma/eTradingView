# context_processors.py

import environ
env = environ.Env()

def profile_context(request):
    coupon = {
        "code": env('COUPON_CODE'),
        "off": env('COUPON_OFF'),
    }

    return {
        'stripe_customer': getattr(request, 'stripe_customer', None),
        'user_profile': getattr(request, 'user_profile', None),
        'subscription': getattr(request, 'subscription', None),

        'subscription_period_end': getattr(request, 'subscription_period_end', None),
        'subscription_active': getattr(request, 'subscription_active', None),
        'subscription_status': getattr(request, 'subscription_status', None),

        'subscription_price_id': getattr(request, 'subscription_price_id', None),
        'subscription_plan': getattr(request, 'subscription_plan', None),
        'payment_methods': getattr(request, 'payment_methods', None),

        'has_subscription': getattr(request, 'has_subscription', False),
        'subscription_canceled': getattr(request, 'subscription_canceled', False),

        'notifications': getattr(request, 'notifications', False),
        'coupon': coupon,

        "stripe_public_key": env('STRIPE_API_PUBLIC_KEY'),
    }