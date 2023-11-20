from flask import Flask, render_template, request

# pip install RPi.GPIO

# Initialization GPIO PINS

# ? ForWard_Pin1 = 18
# ? ForWard_Pin2 = 19

#! BackWard_Pin1 = 20
#! BackWard_Pin2 = 21

# todo Left_Right_Pin1 = 22
# todo Left_Right_Pin1 = 23


# GPIO.setmode(GPIO.BCM)

# ? GPIO.setup(ForWard_Pin1, GPIO.OUT)
# ? GPIO.setup(ForWard_Pin2, GPIO.OUT)

# ! GPIO.setup(BackWard_Pin1, GPIO.OUT)
# ! GPIO.setup(BackWard_Pin2, GPIO.OUT)

# todo GPIO.setup(Left_Right_Pin1, GPIO.OUT)
# todo GPIO.setup(Left_Right_Pin2, GPIO.OUT)

# todo Pwm_Left_Right_Pin1 = GPIO.PWM(Left_Right_Pin1,100)    // Determine PWM Frequency
# todo Pwm_Left_Right_Pin2 = GPIO.PWM(Left_Right_Pin2,100)    // Determine PWM Frequency

# ? Pwm_ForWard_Pin1 = GPIO.PWM(ForWard_Pin1,100)    // Determine PWM Frequency
# ? Pwm_ForWard_Pin2 = GPIO.PWM(ForWard_Pin2,100)    // Determine PWM Frequency

# ! Pwm_BackWard_Pin1 = GPIO.PWM(BackWard_Pin1,100)    // Determine PWM Frequency
# ! Pwm_BackWard_Pin1 = GPIO.PWM(BackWard_Pin2,100)    // Determine PWM Frequency


# todo duty_cycle = 50

# todo If The Value of duty_cycle is 0   --> output is Zero
# todo If The Value of duty_cycle is 100 --> output is Full

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


slider_value = 0


@app.route("/get_value", methods=["POST"])
def get_value():
    data = request.get_json()
    slider_value = data["value"]
    print("Slider value:", slider_value)  # Show The Speed Value Inside The Terminal
    return "", 204


@app.route("/ForWard")
def sendFront():
    print("ForWard")

    # ? Pwm_ForWard_Pin1.start(slider_value)
    # ? Pwm_ForWard_Pin2.start(0)

    #! Pwm_BackWard_Pin1.start(slider_value)
    #! Pwm_BackWard_Pin2.start(0)

    # todo Left_Right_Pin1.start(0)
    # todo Left_Right_Pin2.start(0)

    #  GPIO.output(ForWard_Pin1, GPIO.HIGH)
    #  GPIO.output(ForWard_Pin2, GPIO.LOW)

    #  GPIO.output(BackWard_Pin1, GPIO.HIGH)
    #  GPIO.output(BackWard_Pin2, GPIO.LOW)

    # GPIO.output(Left_Right_Pin1, GPIO.LOW)
    # GPIO.output(Left_Right_Pin2, GPIO.LOW)

    return "success"


@app.route("/BackWard")
def sendBack():
    print("BackWard")

    # ? Pwm_ForWard_Pin1.start(0)
    # ? Pwm_ForWard_Pin2.start(slider_value)

    #! Pwm_BackWard_Pin1.start(0)
    #! Pwm_BackWard_Pin2.start(slider_value)

    # todo Left_Right_Pin1.start(0)
    # todo Left_Right_Pin2.start(0)

    #  GPIO.output(ForWard_Pin1, GPIO.HIGH)
    #  GPIO.output(ForWard_Pin2, GPIO.LOW)

    #  GPIO.output(BackWard_Pin1, GPIO.HIGH)
    #  GPIO.output(BackWard_Pin2, GPIO.LOW)

    # GPIO.output(Left_Right_Pin1, GPIO.LOW)
    # GPIO.output(Left_Right_Pin2, GPIO.LOW)

    return "success"


@app.route("/Left")
def sendLeft():
    print("Left")

    # ? GPIO.output(ForWard_Pin1, GPIO.LOW)
    # ? GPIO.output(ForWard_Pin2, GPIO.LOW)

    #! GPIO.output(BackWard_Pin1, GPIO.LOW)
    #! GPIO.output(BackWard_Pin2, GPIO.LOW)

    # todo Pwm_Left_Right_Pin1.start(duty_cycle)
    # todo Pwm_Left_Right_Pin2.start(0)

    return "success"


@app.route("/Right")
def sendRight():
    print("Right")

    # ? GPIO.output(ForWard_Pin1, GPIO.LOW)
    # ? GPIO.output(ForWard_Pin2, GPIO.LOW)

    #! GPIO.output(BackWard_Pin2, GPIO.LOW)
    #! GPIO.output(BackWard_Pin1, GPIO.LOW)

    # todo Pwm_Left_Right_Pin1.start(0)
    # todo Pwm_Left_Right_Pin1.start(duty_cycle)

    return "success"


@app.route("/Stop")
def sendStop():
    print("Stop")

    # ? GPIO.output(ForWard_Pin1, GPIO.LOW)
    # ? GPIO.output(ForWard_Pin2, GPIO.LOW)

    #! GPIO.output(BackWard_Pin1, GPIO.LOW)
    #! GPIO.output(BackWard_Pin2, GPIO.LOW)

    # todo Pwm_Left_Right_Pin1.stop()
    # todo Pwm_Left_Right_Pin2.stop()

    return "success"


if __name__ == "__main__":
    # app.run(debug=True, port=80)
    app.run(host="0.0.0.0", port=9000)
