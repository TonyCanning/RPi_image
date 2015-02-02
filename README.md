# RPi_image
Program included on this image:
  - avconv is included for creating a timelapse video from images taken by raspistill (https://libav.org/avconv.html)


Code included has be written during my time at FabLab NerveCentre, Derry, NI. (Unless otherwise stated)

Included in this image:
<b>~/us_robot/ contains 3 python files</b>
  - ultrasonic.py returns a distance measurement and is written for the very commonly used HC-SR04 ultrasonic sensor.
  - motor_drive.py is a simple script to drive 2 DC motors from the pi.
Both of these files are present so that you can troubleshoot a complete wall avoiding robot.
The third file in this folder
  - wall_avoiding_robot.py is a complete script which, when run, defaults both motors to forward drive while the disctance measurement from the ultrasonic sensor remains above 10cm. If something is sensed closer than 10cm, one of the motors reverses, turning the robot away.
Of course, you can feel free to edit the file to change how close you want the robot to get to an object before it turns or to reduce or increase the interval between measurements (currently set at 0.5 seconds)

<b>~/time_lapse/ contains 2 python files</b>
  - time_lapse.py makes use of the offical Raspberry Pi camera (& Pi NoIR camera) in order to take a series of stills, which it will sequentially name, and assemble them into an mp4 short movie. 
  - create_movie.py is a copy of the time_lapse.py file but I have commented out the image capture code so that you can build a movie with any set of images. This is useful if you are using a relatively high number of images on a smaller micro SD card - the python script will continue to try to take pictures even if the card is full - this could leave you with no space to produce the mp4.
