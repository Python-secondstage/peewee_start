from database import Thread

Thread.create(name="Keisuke", title="Title", body="Body")

thread01 = Thread(name="Mei", title="Title2", body="Body2")
thread01.save()

thread02 = Thread(name="Mio", title="Title3", body="Body3")
thread02.save()
