import app.app as app
import camera.controller as camera


startedCamera = camera.start()

if not startedCamera:
    del camera

app()
