!/bin/bash

echo "=== INITIALIZING AGI ORGANISM ==="

if [ ! -d "venv" ]; then
    echo "[SETUP] Creating Python Virtual Environment..."
    python3 -m venv venv
fi

source venv/bin/activate

echo "[SETUP] Installing Python libs..."
pip install -q -r requirements.txt

echo "[BUILD] Compiling C++ Memory Core..."
if [ "$(uname)" == "Darwin" ]; then
    # MacOS
    g++ -shared -o memory_core.so -fPIC memory_core.cpp
    g++ -shared -o vision_core.so -fPIC vision_core.cpp
else
    g++ -shared -o memory_core.so -fPIC memory_core.cpp
    g++ -shared -o vision_core.so -fPIC vision_core.cpp
fi

echo "[START] Starting Node.js Sensory Network..."
if [ -f "network_sense.js" ]; then
    node network_sense.js &
    NODE_PID=$!
    echo "Node PID: $NODE_PID"
fi

echo "[START] AGI MAIN BRAIN LAUNCHING..."
python3 main.py

kill $NODE_PID
echo "=== SYSTEM SHUTDOWN ==="
