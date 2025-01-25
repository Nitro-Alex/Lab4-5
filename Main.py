from Func_implementation import create_db
from Home_window import *
from Class_implementaition import *

create_db()

ges1 = Ges()
home_window = HomeWindow(ges1)
home_window.mainloop()