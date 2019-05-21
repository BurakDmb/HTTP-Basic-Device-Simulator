## A simple physical sensor device simulator with using HTTP communication.

- Connects to a HTTP server
- If a get_temp request comes, then creates a random temperature result
- And sends the result with the "house/sensor_result" header back
- This simulator is running on a free tier amazon server(ec2-18-195-119-211.eu-central-1.compute.amazonaws.com) 
- And you can send HTTP POST requests to "house/sensor,get_temp" body to get a result
- Message Example: "house/sensor,get_temp"

- Usage:
    ~~~~
    git clone https://github.com/BurakDmb/HTTP-Basic-Device-Simulator.git
    cd HTTP-Basic_Device-Simulator
    python3 main.py
    ~~~~

- Also you can use this command to use this script in background
  ~~~~
  nohup python3 main.py &
  ~~~~
- And you can kill using:
  ~~~~
  ps -aux | grep main.py
  kill PID(the pid of main.py process)
  ~~~~