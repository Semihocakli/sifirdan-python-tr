from rest_framework import permissions

class IsYazarOrReadOnly(permissions.BasePermission):
    """
    Sadece yazarın blog yazısını düzenlemesine izin veren özel izin sınıfı.
    """

    def has_object_permission(self, request, view, obj):
        # GET, HEAD ya da OPTIONS istekleri için izin ver
        if request.method in permissions.SAFE_METHODS:
            return True

        # Yazı sahibi ile giriş yapmış kullanıcı aynı mı?
        return obj.yazar == request.user.username 