import resrc.apk_re as apkre
import resrc.strfind as strfind
import logging
import oo.ooclass as ooclass
import oo.oosubclass as oosubclass

logging.basicConfig(filename='example.log', format='%(asctime)s:%(levelname)s:%(message)s', filemode='w', level=logging.DEBUG)

apkre.re_do()

strfind.main()

oo1 = oosubclass.oosubclass(1)
oo2 = ooclass.ooclass(1)
print ('check oo1 == oo2 ' + str( oo1 == oo2) )
