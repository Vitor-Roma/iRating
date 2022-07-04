from django.core.files import File
import urllib

result = urllib.urlretrieve(image_url) # image_url is a URL to an image

# self.photo is the ImageField

self.photo.save(
    os.path.basename(self.url),
    File(open(result[0], 'rb'))
    )

self.save()

class CachedImage(models.Model):
    url = models.CharField(max_length=255, unique=True)
    photo = models.ImageField(upload_to=photo_path, blank=True)

    def cache(self):
        """Store image locally if we have a URL"""

        if self.url and not self.photo:
            result = urllib.urlretrieve(self.url)
            self.photo.save(
                    os.path.basename(self.url),
                    File(open(result[0], 'rb'))
                    )
            self.save()