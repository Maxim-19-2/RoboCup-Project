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
	tts = ALProxy("ALTextToSpeech", IP, PORT)


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


	picount=0
	try:
		while True:
			if(tracker.isTargetLost()):           #remove efefctor to lower arm while searching
				tts.say("cant find the Ball!")
				tracker.setEffector("None")
				posture.goToPosture("StandInit", fractionMaxSpeed)
				motion.moveTo(0,0,(math.pi/3))
				picount+=1
			if(not tracker.isTargetLost()):	
				tracker.setEffector(effector)		# set effector to pint at ball
			if(picount=6):
				motion.moveTo(0,0,(-math.pi)) 		#turn robot back to orignal positon so he wont die because of the cables
				motion.moveTo(0,0,(-math.pi))
				picount=0
			time.sleep(0.5)
	except KeyboardInterrupt:
		print "..."
		print "Interrupted by user"
		print "Stopping..."

	# Stop tracker, go to posture Crouch.
	tts.say("Going to Sleep!")
	tracker.stopTracker()
	tracker.unregisterAllTargets()
	tracker.setEffector("None")
	posture.goToPosture("Crouch", fractionMaxSpeed)
	motion.rest()

	print "ALTracker stopped."


if __name__ == "__main__" :
	main()
