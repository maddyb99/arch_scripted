import pyautogui
from PIL import Image, ImageFilter,ImageStat
def brightness( im_file ):
   im = im_file.convert('L')
   stat = ImageStat.Stat(im)
   return stat.rms[0]
myScreenshot = pyautogui.screenshot()
if brightness(myScreenshot)>100:
    img = Image.new('RGBA', myScreenshot.size, (0,0,0,50))
    # img.show()
    myScreenshot.paste(img,(0, 0),img)
    # myScreenshot.show()
blurImage = myScreenshot.filter(ImageFilter.GaussianBlur(5))
blurImage.save(r'/home/maddyb/Documents/PROJECTS/Scripts/kde-custom-lock/now.png')