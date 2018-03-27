import time
import sensors
sensors.init()

while True:
    try:
        for chip in sensors.iter_detected_chips():
            print '%s' % (chip)
            for feature in chip:
                print '  %s: %.2f' % (feature.label, feature.get_value())
    finally:
        time.sleep(60)

sensors.cleanup()
