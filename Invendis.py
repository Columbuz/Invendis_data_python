import modbus_tk # type: ignore
import modbus_tk.defines as cst # type: ignore
from modbus_tk import modbus_tcp # type: ignore
import time

# Function to read the data from Modbus TCP
def read_modbus_tcp():
    try:
        # IP and port of the Modbus TCP server
        modbus_server_ip = '192.168.0.194'  # Replace with your Modbus server's IP
        modbus_server_port = 502            # Default Modbus TCP port

        # Create a Modbus TCP master
        master = modbus_tcp.TcpMaster(modbus_server_ip, modbus_server_port)
        master.set_timeout(5.0)
        master.set_verbose(True)

        # Modbus Slave ID, starting register, number of registers to read
        slave_id = 10
        start_register = 0
        num_of_registers = 120

        while True:
            # Send Modbus request and read data
            modbus_data = master.execute(slave_id, cst.READ_HOLDING_REGISTERS, start_register, num_of_registers)

            # Display the results continuously
            print("\nModbus Data (Reading Registers):\n")
            for i, value in enumerate(modbus_data):
                print(f"Start Register: {start_register + i + 1}    Value: {hex(value)}")

            print("\nModbus Read Successful!\n")
            time.sleep(2)  # Sleep for 2 seconds before the next read

    except modbus_tk.modbus.ModbusError as e:
        print(f"Modbus Error: {e}")
    except Exception as e:
        print(f"Connection Error: {e}")

# Call the function to start reading
if __name__ == "__main__":
    read_modbus_tcp()
