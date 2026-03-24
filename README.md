# Robo-Raksha
robo raksha is autonomous smart surveillance robot project
I built Robo Raksha as a prototype for my science fest to help solve a critical problem: many lives are lost during accidents because help cannot reach the area in time and cause of no human intervention.

Robo Raksha is an autonomous robot designed to patrol environments 24/7. When an emergency happens, it can safely drive into dangerous zones that might be too risky for humans. It uses its sensors to monitor the environment and streams live video so rescue workers can see exactly what is happening. It automatically sends out the exact GPS location and the intensity of the emergency, helping rescue teams respond safely, effectively, and on time.

Hardware Used:
Arduino UNO R3: The main "brain" of the robot that processes the sensor data.

ESP32: Handles the wireless connections.

OV2640 Camera: The "eyes" of the robot, providing a 24/7 live video stream.

GSM SIM800L: Sends text message (SMS) alerts to emergency contacts.

GPS NEO-6M: Pinpoints and shares the robot's accurate location.

Sensors: Flame, vibration, and sound sensors to detect different types of hazards.

Software & Code:
All microcontroller code was written in C/C++ using the Arduino IDE.

TinyGPS++ Library: Used to process the location data from the GPS module.

ESP32 WebCamera Code: Adapted from the example code to handle the live video streaming.
