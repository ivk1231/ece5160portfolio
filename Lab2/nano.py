import serial
import time
import numpy as np
import matplotlib.pyplot as plt

SERIAL_PORT = '/dev/cu.usbserial-10' 
BAUD_RATE   = 115200
DURATION    = 8

def collect_data():
    timestamps = []
    p_acc = []
    p_gyr = []
    p_comp = []
    
    print(f"Connecting to {SERIAL_PORT}...")
    try:
        with serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1) as ser:
            ser.reset_input_buffer()
            print("Recording... Tilt the board!")
            start_time = time.time()
            while (time.time() - start_time) < DURATION:
                if ser.in_waiting:
                    try:
                        line = ser.readline().decode('utf-8').strip()
                        parts = line.split(',')
                        if len(parts) >= 4:
                            timestamps.append(float(parts[0]))
                            p_acc.append(float(parts[1]))
                            p_gyr.append(float(parts[2]))
                            p_comp.append(float(parts[3]))
                    except ValueError: continue 
    except Exception as e: return None, None, None, None
    return np.array(timestamps), np.array(p_acc), np.array(p_gyr), np.array(p_comp)

if __name__ == "__main__":
    t, acc, gyr, comp = collect_data()
    if t is not None:
        t_sec = (t - t[0]) / 1000.0
        plt.figure(figsize=(12, 6))
        
        plt.plot(t_sec, acc, label='Accelerometer (Noisy)', color='blue', alpha=0.3)
        plt.plot(t_sec, gyr, label='Gyro Only (Drifts)', color='green', linestyle='dashed', alpha=0.6)
        plt.plot(t_sec, comp, label='Complementary Filter (Fused)', color='red', linewidth=2.5)
        
        plt.title('Complementary Filter Performance')
        plt.xlabel('Time (s)')
        plt.ylabel('Angle (deg)')
        plt.legend()
        plt.grid(True)
        plt.show()