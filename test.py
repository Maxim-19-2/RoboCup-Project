import time
import math
from naoqi import ALProxy

def main():
	IP = "10.0.7.101"
	PORT = 9559
	ballSize = 0.06
	effector = "RArm"

	print "Connecting to", IP, "with port", PORT

	motion = ALProxy("ALMotion", IP, PORT)
	posture = ALProxy("ALRobotPosture", IP, PORT)
	tracker = ALProxy("ALTracker", IP, PORT)
	navigation = ALProxy("ALNavigation",IP,PORT)

	# First, wake up.
	motion.wakeUp()

	fractionMaxSpeed = 0.8
	# Go to posture stand
	posture.goToPosture("StandInit", fractionMaxSpeed)

	# Add target to track.
	targetName = "RedBall"
	diameterOfBall = ballSize
	tracker.registerTarget(targetName, diameterOfBall)

	# set mode
	mode = "Head"
	tracker.setMode(mode)

	# set effector
	tracker.setEffector(effector)

	# Then, start tracker.
	tracker.track(targetName)

	print "ALTracker successfully started, now show a red ball to robot!"
	print "Use Ctrl+c to stop this script."


	if(not tracker.isTargetLost()):
		print "."		# set effector
		

	try:
		while True:
			if(tracker.isTargetLost()):
				posture.goToPosture("StandInit", fractionMaxSpeed)
				motion.moveTo(0,0,(math.pi/3))
			time.sleep(1)
	except KeyboardInterrupt:
		print "..."
		print "Interrupted by user"
		print "Stopping..."

	# Stop tracker, go to posture Sit.
	tracker.stopTracker()
	tracker.unregisterAllTargets()
	tracker.setEffector("None")
	posture.goToPosture("Crouch", fractionMaxSpeed)
	motion.rest()

	print "ALTracker stopped."


if __name__ == "__main__" :
	main()