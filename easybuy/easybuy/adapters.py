from allauth.socialaccount.adapter import DefaultSocialAccountAdapter

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def save_user(self, request, sociallogin, form=None):
        user = super().save_user(request, sociallogin, form=form)
        
        if sociallogin.account.provider == 'google':
            extra_data = sociallogin.account.extra_data
            profile_image_url = extra_data.get('picture')
            
            if profile_image_url:
                user.profile.image = profile_image_url  # Access the Profile model's image field
                user.profile.save()
        
        return user
