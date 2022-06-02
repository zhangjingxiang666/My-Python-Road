import Move
import ClickAndScroll
import threading

MoveThread=threading.Thread(target=Move.main)
ClickAndScrollThread=threading.Thread(target=ClickAndScroll.main)
MoveThread.start()
ClickAndScrollThread.start()
MoveThread.join()
ClickAndScrollThread.join()
